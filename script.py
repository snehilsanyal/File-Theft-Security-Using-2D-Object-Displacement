import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_images(image_path1, image_path2):
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)
    return img1, img2

# Change path to the relative image paths!!
image_path1 = 'image1.jpg'
image_path2 = 'image2.jpg'

img1, img2 = load_images(image_path1, image_path2)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')
plt.show()

def apply_sobel_edge_detection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobelx, sobely)
    sobel_combined = np.uint8(sobel_combined)
    _, sobel_combined = cv2.threshold(sobel_combined, 50, 255, cv2.THRESH_BINARY)
    return sobel_combined

edges1 = apply_sobel_edge_detection(img1)
edges2 = apply_sobel_edge_detection(img2)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(edges1, cmap='gray')
plt.title('Edges Image 1')
plt.subplot(1, 2, 2)
plt.imshow(edges2, cmap='gray')
plt.title('Edges Image 2')
plt.show()

def find_paper_corners(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    kernel = np.ones((5, 5), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    large_contours = [c for c in contours if cv2.contourArea(c) > 5000]

    for contour in large_contours:
        epsilon = 0.05 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            return np.intp(approx)

    return None

corners1 = find_paper_corners(img1)
corners2 = find_paper_corners(img2)

if corners1 is None or corners2 is None:
    print("Failed to detect corners in one or both images.")
else:
    def plot_corners(img, corners, title):
        img_with_corners = img.copy()
        if corners is not None:
            for corner in corners:
                x, y = corner.ravel()
                cv2.circle(img_with_corners, (x, y), 10, (0, 0, 255), -1)
            cv2.polylines(img_with_corners, [corners], isClosed=True, color=(255, 0, 0), thickness=4)
        plt.imshow(cv2.cvtColor(img_with_corners, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis('off')

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plot_corners(img1, corners1, 'Image 1 Corners')
    plt.subplot(1, 2, 2)
    plot_corners(img2, corners2, 'Image 2 Corners')
    plt.show()

def draw_paper_outline(img, points, color=(0, 0, 255)):
    if points is None or len(points) != 4:
        print("Error: Invalid points for drawing paper outline.")
        return img
    img_with_paper = img.copy()
    pts = np.array(points, dtype=np.int32)
    cv2.polylines(img_with_paper, [pts], isClosed=True, color=color, thickness=3)
    return img_with_paper

img1_with_paper = draw_paper_outline(img1, corners1)
img2_with_paper = draw_paper_outline(img2, corners2)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img1_with_paper, cv2.COLOR_BGR2RGB))
plt.title('Image 1 with Paper Outline')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img2_with_paper, cv2.COLOR_BGR2RGB))
plt.title('Image 2 with Paper Outline')
plt.show()

def compute_transformation_matrix(pts1, pts2):
    if pts1 is None or pts2 is None:
        print("Error: Missing points for computing transformation matrix.")
        return None

    if len(pts1) == 4 and len(pts2) == 4:
        pts1 = np.array(pts1, dtype=np.float32).reshape(-1, 1, 2)
        pts2 = np.array(pts2, dtype=np.float32).reshape(-1, 1, 2)
        H, _ = cv2.findHomography(pts1, pts2, cv2.RANSAC)

        H_4x4 = np.eye(4)
        H_4x4[:3, :3] = H
        H_4x4[0, 3] = H[0, 2]
        H_4x4[1, 3] = H[1, 2]
        H_4x4[2, 3] = 0

        return np.round(H_4x4, 2)

H = compute_transformation_matrix(corners1, corners2)

if H is not None:
    print("4x4 Transformation Matrix:\n", H)
else:
    print("Transformation matrix computation failed.")

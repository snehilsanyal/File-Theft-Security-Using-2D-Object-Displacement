# 🕵🏻‍♂️📂 File Theft Security Using 2D Object Displacement
This repository contains the code and methodology for detecting 2D object transformations (translation and rotation) using two images. This approach is efficient, robust, and designed to work in real-time applications without the need for machine learning models.

## About
This project introduces a computationally efficient method for estimating the transformation matrix of 2D objects, such as documents or sheets of paper. The technique addresses challenges like image quality variations, partial occlusions, and significant transformations. Applications include object tracking, augmented reality, image registration, and document mishandling detection in office environments.

## Features
- **Homography Estimation**: Computes the geometric relationship between two images.
- **RANSAC Algorithm**: Removes outliers during feature matching for robust transformation estimation.
- **Feature Matching**: Efficient keypoint detection using ORB (Oriented FAST and Rotated BRIEF).
- **Edge Detection**: Employs Canny edge detection to enhance feature visibility.
- **Real-Time Capability**: Designed for dynamic environments with computational efficiency.

## Applications
- Document mishandling detection
- Augmented reality (AR) integration
- Robotics and industrial automation
- Image registration for medical imaging and remote sensing

## Methodology
The methodology involves the following steps:
1. **Preprocessing**:
   - Convert images to grayscale
   - Apply denoising and normalization
   - Perform edge detection
2. **Feature Extraction**:
   - Use ORB for detecting keypoints and descriptors
3. **Feature Matching**:
   - Match keypoints between images using FLANN-based matcher
4. **Transformation Estimation**:
   - Compute homography matrix
   - Use RANSAC to refine matches
5. **Transformation Measurement**:
   - Apply the transformation matrix to determine positional and orientation changes

## Tools and Libraries
- **OpenCV**: Core image processing (e.g., edge detection, feature extraction, homography computation)
- **NumPy**: Matrix operations for numerical accuracy
- **Matplotlib**: Visualization of intermediate and final results
- **Pillow**: Preprocessing tasks like resizing and format conversion

## Results
The system performs well in various scenarios:
1. **Single Paper Detection**: High precision in calculating rotation and translation.
2. **Overlapping Papers**: Effectively separates and calculates transformations for individual papers.
3. **Edge Overlapping Papers**: Handles tightly stacked configurations with advanced edge detection.
4. **No Change in Images**: Reports a unity transformation matrix when no displacement is detected.

## Limitations and Future Enhancements
- Struggles with textured or colored papers and non-planar transformations.
- Future work includes adding depth-sensing capabilities and optimizing for high-resolution images.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/snehilsanyal/File-Theft-Security-Using-2D-Object-Displacement.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. #TODO

## Examples
- **Input**: Two images (reference and target)
- **Output**: Transformation matrix indicating rotation and translation

## References
1. Xie, Y., Shen, J., & Wu, C. (2019). Robust object tracking using affine transformation.
2. Jo, B.-W., Lee, Y.S., Jo, J.H., & Khan, R.M.A. (2018). Computer vision-based displacement measurements.

For more details, refer to the [conference paper](https://github.com/Kartik8Dwivedi/File-Theft-Security).

## Maintainers
- [Snehil Sanyal](https://github.com/snehilsanyal)
- [Kartik Dwivedi](https://github.com/kartik8dwivedi)

## Contribution
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

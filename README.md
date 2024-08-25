Face Detection System Using Python
==================================

This project is a face detection system developed using Python. It utilizes the `haarcascades` frontal face XML file for face detection and the `face_recognition` library for recognizing faces. The system can detect and recognize faces in images provided in the test directory, based on training images stored in a structured folder format.

Table of Contents
-----------------

-   [Prerequisites](#prerequisites)
-   [Installation](#installation)
-   [Project Structure](#project-structure)
-   [Usage](#usage)
-   [Contributing](#contributing)
-   [License](#license)

## Prerequisites
-------------

Before running the project, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

Additionally, you'll need to install the following Python libraries:

-   `opencv-python` (cv2)
-   `face_recognition`
-   `os` (This is part of the Python standard library and doesn't need separate installation)

## Installation
------------

To install the required dependencies, run the following command in your terminal or command prompt:

```
pip install opencv-python face_recognition
```
## Project Structure
-----------------

The project repository contains the following structure:
```
.
├── FaceDetectionUsingOpenCv.py  # Main Python script to run the face detection
├── haarcascades                # Directory containing Haar cascade files
│   └── haarcascade_frontalface_default.xml
├── training_images             # Directory containing training images
│   ├── Person1
│   │   ├── image1.jpg
│   │   └── image2.jpg
│   └── Person2
│       ├── image1.jpg
│       └── image2.jpg
└── test                        # Directory containing test images
    ├── test_image1.jpg
    └── test_image2.jpg`
```

### Description of Folders and Files

-   **FaceDetectionUsingOpenCv.py**: The main script to execute for face detection and recognition.
-   **haarcascades**: Contains the Haar cascade XML file used for detecting faces.
-   **training_images**: Contains subfolders named after each person. Each subfolder should contain multiple images of that person for training the model.
-   **test**: Contains the images to be tested for face detection and recognition.

## Usage
-----

To use the face detection system, follow these steps:

1.  **Prepare Training Images**:

    -   In the `training_images` directory, create a subfolder for each person you want to recognize. Name the folder with the person's name.
    -   Upload multiple images of the person into their respective folder.
2.  **Prepare Test Images**:

    -   Place the images you want to test in the `test` directory.
3.  **Update the Script**:

    -   Open `FaceDetectionUsingOpenCv.py`.
    -   On **line 45**, ensure the filename mentioned for the test file corresponds to the file you want to test. For example:
    `test_image_path = 'test/test_image1.jpg'`

4.  **Run the Script**:

    -   Run the script using Python:
    `python FaceDetectionUsingOpenCv.py`

    -   A window will open displaying the test image with rectangles marking all detected faces. The recognized faces will be labeled with the respective names.

## Contributing
------------

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License
-------

This project is licensed under the MIT License. See the LICENSE file for details.

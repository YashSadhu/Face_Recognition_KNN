# Face Recognition Using Machine Learning

This project is a real-time facial recognition system built using OpenCV and the K-Nearest Neighbors (KNN) algorithm. The system can detect and recognize faces from a pre-trained dataset of labeled facial images.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Generating Training Data](#generating-training-data)
  - [Building the Face Classifier](#building-the-face-classifier)
  - [Testing on Raspberry Pi](#testing-on-raspberry-pi)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Facial recognition is an important application of computer vision and machine learning techniques. This project explores the use of the OpenCV library and the KNN algorithm to build a real-time facial recognition system. The system follows a three-step process:

1. **Face Detection:** Detect faces in the input video stream using Haar feature-based cascade classifiers.
2. **Data Preparation:** Generate a training dataset by capturing and labeling facial images.
3. **Face Classification:** Train a KNN model on the dataset to classify and recognize faces in real-time.

## Requirements
- Python 3.x
- OpenCV
- NumPy
- Raspberry Pi (optional, for testing on a different platform)
- PuTTY (for accessing Raspberry Pi from a laptop)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/face-recognition-project.git
    ```
2. Install the required Python packages:
    ```bash
    pip install opencv-python numpy
    ```

## Usage
### Generating Training Data
1. Run the `face_data.py` script:
    ```bash
    python face_data.py
    ```
2. Enter the name of the person whose face data you want to register.
3. Wait for the script to capture multiple face images. Press 'q' to stop and save the registered face and name.

### Building the Face Classifier
1. Run the `face_recognition.py` script:
    ```bash
    python face_recognition.py
    ```
2. The script will load the pre-trained dataset, build the KNN face classifier, and start the real-time face recognition process.
3. The camera feed will be displayed, and recognized faces will be marked with bounding boxes and names.
4. Press 'q' to exit the script.

### Testing on Raspberry Pi
1. Connect the Raspberry Pi to your laptop using an Ethernet cable.
2. Install PuTTY on your laptop and use it to access the Raspberry Pi remotely.
3. Copy the project files to the Raspberry Pi using a USB drive or by cloning the repository on the Pi.
4. Follow the steps for Generating Training Data and Building the Face Classifier on the Raspberry Pi.
5. Observe the real-time face recognition output on the Raspberry Pi's display or through the remote desktop connection.

## Results
The face recognition system successfully detects and recognizes faces in real-time video streams. The detected faces are marked with bounding boxes, and the recognized individuals' names are displayed. The system has been tested and works on both a laptop and a Raspberry Pi.

## Contributing
We value contributions by:  Gaurav Ahuja, Dibyam Jalan, Yashkumar Sadhu, Mahendra Choudhary and Akshat Soni

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


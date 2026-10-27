# Real-Time Object Detection and Tracking

## Project Overview

This project implements real-time object detection and tracking using a webcam or a saved video file. It uses a pretrained YOLO11n model to detect objects and ByteTrack to track detected objects across consecutive video frames.

The application displays bounding boxes, object labels, and tracking IDs in a window using OpenCV.

## Features

- Live webcam input.
- Saved video input, including compatible `.mov` and `.mp4` files.
- Pretrained YOLO11n object detection.
- Bounding boxes and object labels.
- Object tracking using ByteTrack.
- Tracking IDs displayed with detections.
- Proportional display resizing to avoid image distortion.
- Press `Q` to exit the video window.

## Technologies Used

- Python
- OpenCV
- Ultralytics YOLO11n
- ByteTrack
- NumPy

## Requirements

- Python
- A webcam for live camera input, or a compatible video file.
- An internet connection for the initial YOLO model download, if the model is not already available locally.

## Installation

1. Clone or download this project.
2. Create and activate a Python virtual environment.
3. Install the required packages:

```bash
pip install ultralytics opencv-python numpy
```

4. Ensure that `main.py` and the pretrained `yolo11n.pt` model are available in the project directory.

## How to Run

### Live Webcam

Run:

```bash
python main.py
```

The application opens the default webcam and displays detected and tracked objects.

### Saved Video

Place your video file in the project directory, then run:

```bash
python main.py --source "test_video.mov"
```

Replace `test_video.mov` with your actual video filename or provide the full path to a video file.

## How It Works

1. OpenCV captures frames from the webcam or video file.
2. YOLO11n detects objects in each frame.
3. ByteTrack associates detections across frames and assigns tracking IDs.
4. The application draws bounding boxes, class labels, and tracking IDs.
5. OpenCV displays the annotated frames.

## Project Structure

```text
CodeAlpha_ObjectDetectionTracking/
├── main.py
├── yolo11n.pt
├── README.md
└── venv/
```

The virtual environment folder (`venv/`) and model weights do not need to be uploaded to a public repository if the setup instructions explain how to install dependencies and obtain the model.

## Internship Task

CodeAlpha Virtual Artificial Intelligence Internship

**Task 4:** Object Detection and Tracking

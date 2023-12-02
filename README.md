
# Automated Surveillance System using YOLOv8n

This repository contains code that utilizes YOLOv8n model for object detection in a surveillance system. The system is designed to detect people in a camera feed and send an alarm message to a Telegram chat or group at specific times, providing a 24/7 surveillance solution.

## Overview

The Python code provided here implements an automated surveillance system that performs the following:

- Uses the YOLOv8n model to detect objects in a camera feed.
- Specifically identifies and highlights persons within the frame.
- Calculates the frames per second (FPS) for real-time monitoring.
- Intended to trigger an alarm message on a Telegram chat or group when a person is detected.

## Requirements

To run this project, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- Ultralytics (`ultralytics`)

## Usage

1. Clone this repository to your local machine.
2. Install the necessary dependencies.
3. Download the `yolov8n.pt` file containing the YOLOv8n model weights.
4. Run the `main.py` script.

```bash
python main.py

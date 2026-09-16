# 🎧 Hand Gesture Based Volume Control

A real-time computer vision mini project that allows users to control computer volume using hand gestures.

## 🚀 Features

- Real-time hand detection
- Touch-free volume control
- Thumb and index finger gesture detection
- Volume Up and Volume Down using hand movement
- Real-time camera feed
- MediaPipe hand tracking

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI
- Computer Vision

## ⚙️ How It Works

The project uses the webcam to detect hand landmarks using MediaPipe.

The distance between the **thumb** and **index finger** is calculated.

- 🖐️ Distance greater than 150 → Volume Up
- 🤏 Distance less than 50 → Volume Down

PyAutoGUI sends volume control commands to the computer.

## 📦 Installation

Install the required libraries:

```bash
pip install opencv-python mediapipe numpy pyautogui

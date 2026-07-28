# 🔥 AI-Based Autonomous Fire Fighting Robot

An AI-powered autonomous fire fighting robot that detects fire in real time using a YOLOv8 model running on a Raspberry Pi. Once fire is detected, the Raspberry Pi communicates with an ESP32 over UART. The ESP32 controls the robot's movement and activates a water pump to extinguish the fire automatically.

---

## 📌 Project Overview

This project combines Artificial Intelligence, Computer Vision, Embedded Systems, and Robotics to build an autonomous fire fighting robot capable of detecting and suppressing fire with minimal human intervention.

---

## 🚀 Features

- Real-time fire detection using YOLOv8
- Raspberry Pi camera support
- AI inference on Raspberry Pi
- UART communication between Raspberry Pi and ESP32
- Autonomous robot movement
- Automatic water pump activation
- Modular software architecture
- Easy to customize and extend

---

## 🛠 Hardware Used

- Raspberry Pi 4
- ESP32 Development Board
- Raspberry Pi Camera Module
- L298N Motor Driver
- DC Motors
- Relay Module
- Water Pump
- Li-ion Battery
- Chassis
- Connecting Wires

---

## 💻 Software Used

- Python 3
- Arduino IDE
- OpenCV
- Ultralytics YOLOv8
- PyTorch
- PySerial

---

## 📂 Folder Structure

```
AI-Fire-Fighting-Robot
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── raspberry_pi/
│   ├── main.py
│   ├── fire_detection.py
│   ├── yolo_detect.py
│   ├── camera.py
│   ├── uart.py
│   └── models/
│       └── best.pt
│
├── esp32/
│   └── esp32_robot.ino
│
├── docs/
├── images/
├── videos/
└── datasets/
```

---

## ⚙ System Architecture

Camera
↓

Raspberry Pi

↓

YOLOv8 Fire Detection

↓

UART Communication

↓

ESP32

↓

Motor Driver + Water Pump

↓

Fire Extinguished

---

## 🔄 Working

1. Camera continuously captures images.
2. YOLOv8 detects fire.
3. Raspberry Pi sends command to ESP32 through UART.
4. ESP32 moves robot toward fire.
5. Relay turns ON water pump.
6. Fire is extinguished.
7. Robot returns to monitoring mode.

---

## 📥 Installation

Clone repository

```bash
git clone https://github.com/yourusername/AI-Fire-Fighting-Robot.git
```

Install Python packages

```bash
pip install -r requirements.txt
```

Upload ESP32 code using Arduino IDE.

Copy the YOLO model into

```
raspberry_pi/models/
```

---

## ▶ Run

```bash
cd raspberry_pi
python main.py
```

---

## 📊 Results

- Accurate fire detection
- Fast response
- Automatic fire suppression
- Reliable UART communication

---

## 📈 Future Scope

- Thermal camera integration
- GSM alerts
- Mobile application
- Cloud monitoring
- GPS navigation
- Obstacle avoidance

---

## 👨‍💻 Team Members

- Shivam Kumar
- Team Members

---

## 📚 References

- YOLOv8 Documentation
- Raspberry Pi Documentation
- ESP32 Documentation
- OpenCV Documentation

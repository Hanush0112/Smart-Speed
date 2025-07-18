# 🚗 Smart Speed – Intelligent Speed Limit Compliance System

**Smart Speed** is a real-time embedded AI project that helps reduce road accidents by automatically detecting speed limit signs using computer vision and adjusting a vehicle's motor speed accordingly using Arduino Uno. Built using **Raspberry Pi**, **Pi Camera**, and **Arduino**, this system enhances road safety through automation and edge AI.

📌 IEEE Published Research | 🔍 Raspberry Pi + Arduino Uno | ⚙️ Computer Vision + Embedded Systems

---

## 🎯 Objective

To prevent overspeeding and reduce accidents by:
- Detecting speed limit signs using a Pi camera
- Interpreting the sign using a trained computer vision model
- Sending appropriate speed commands to the Arduino to limit the vehicle’s speed

---

## 🧠 How It Works

1. **Image Capture**: Pi Camera captures frames in real time.
2. **Speed Sign Detection**: A trained model (YOLO or CNN) detects and classifies speed limit signs (e.g., 30, 50, 60).
3. **Speed Control Command**: Raspberry Pi sends the detected limit to Arduino Uno via serial communication.
4. **Motor Adjustment**: Arduino adjusts the motor speed accordingly using PWM signals.

---

## 🧾 Installation & Setup

### 🔹 On Raspberry Pi

1. **Install dependencies**
```bash
sudo apt update
pip install opencv-python numpy serial
```
2. **Clone the repo**
```bash
git clone https://github.com/Hanush0112/Smart-Speed.git
cd Smart-Speed
```
3. **Run the detection script**
```bash
python detect_speed_limit.py
```
## 🔹 On Arduino
Open motor_control.ino in Arduino IDE

Upload to Arduino Uno via USB

Connect motor driver and power source

---

## 🧪 Technologies Used

| Component        | Purpose                                      |
|------------------|----------------------------------------------|
| Raspberry Pi     | Edge computing, image processing             |
| Arduino Uno      | Motor control based on detected speed        |
| Pi Camera        | Real-time video frame capturing              |
| OpenCV           | Image preprocessing and contour detection    |
| Custom CNN / YOLO| Speed limit recognition model                |
| Python           | Raspberry Pi control and processing script   |
| C++ / Arduino IDE| Arduino motor and PWM control                |
| Serial Communication | Raspberry Pi ↔ Arduino data transfer     |

---

## ⚙️ Hardware Requirements

- Raspberry Pi 3/4
- Pi Camera module
- Arduino Uno
- L298N Motor Driver
- 4 DC Motors + Wheels
- Jumper wires + Breadboard
- Power supply (battery)

## 🔮 Future Improvements
Add GPS + location-based dynamic speed limits

Include traffic light & obstacle detection

Optimize model for faster inference (using TensorRT or Edge TPU)

Solar-powered and weather-resistant hardware casing

# raspberry_pi_speed_detector.py

import cv2
import pickle
import serial
import time
import numpy as np

# Load trained model
with open('trained.p', 'rb') as f:
    model = pickle.load(f)

# Initialize serial communication with Arduino
arduino = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

cap = cv2.VideoCapture(0)
IMG_SIZE = 32

def preprocess_image(img):
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img / 255.0
    return img.reshape(1, IMG_SIZE, IMG_SIZE, 1)

# Define the speed class mapping
speed_classes = {0: 20, 1: 30, 2: 40, 3: 50, 4: 60, 5: 70, 6: 80, 7: 90, 8: 100}

print("🚦 Smart Speed Detection Started...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    try:
        processed = preprocess_image(frame)
        prediction = model.predict(processed)
        class_index = np.argmax(prediction)
        confidence = np.max(prediction)

        if confidence > 0.8:
            detected_speed = speed_classes.get(class_index, 0)
            print(f"Detected Speed Limit: {detected_speed} km/h")
            arduino.write((str(detected_speed) + '\n').encode())
            time.sleep(2)

    except Exception as e:
        print(f"Detection Error: {e}")

    cv2.imshow("Smart Speed", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()

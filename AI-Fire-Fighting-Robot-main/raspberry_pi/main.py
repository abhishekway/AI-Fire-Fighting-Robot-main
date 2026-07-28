from ultralytics import YOLO
import cv2
import serial
import time

# Load YOLO model
model = YOLO("models/best.pt")

# UART Configuration
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)

# Camera
cap = cv2.VideoCapture(0)

print("AI Fire Fighting Robot Started...")

while True:

    ret, frame = cap.read()

    if not ret:
        continue

    results = model(frame)

    fire_detected = False

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])

            # Fire class assumed to be class 0
            if cls == 0:
                fire_detected = True

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, "Fire", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 0, 255),
                            2)

    if fire_detected:
        print("Fire Detected")
        ser.write(b'F\n')
    else:
        ser.write(b'N\n')

    cv2.imshow("Fire Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
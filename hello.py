import cv2
import csv
from datetime import datetime
import os


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("INFO: Press 'O' to confirm attendance, 'Q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            "Press O to mark attendance",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow("Attendance System", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('o'):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")

        file_exists = os.path.isfile("attendance.csv")

        with open("attendance.csv", "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["Date", "Time"])
            writer.writerow([date, time])

        print("Attendance marked")
        break

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

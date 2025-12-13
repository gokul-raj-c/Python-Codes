import cv2
import numpy as np

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Face detection
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # Draw face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # ---------- T-ZONE EXTRACTION ----------
        tz_x1 = int(x + 0.25 * w)
        tz_y1 = int(y + 0.15 * h)
        tz_x2 = int(x + 0.75 * w)
        tz_y2 = int(y + 0.65 * h)

        t_zone = gray[tz_y1:tz_y2, tz_x1:tz_x2]

        cv2.rectangle(frame, (tz_x1, tz_y1), (tz_x2, tz_y2), (0, 255, 0), 2)

        # ---------- PREPROCESS ----------
        blur = cv2.GaussianBlur(t_zone, (5, 5), 0)
        _, thresh = cv2.threshold(
            blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        # ---------- CONTOUR DETECTION ----------
        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 150:   # remove noise
                x1, y1, w1, h1 = cv2.boundingRect(cnt)

                cv2.rectangle(
                    frame,
                    (tz_x1 + x1, tz_y1 + y1),
                    (tz_x1 + x1 + w1, tz_y1 + y1 + h1),
                    (0, 0, 255),
                    1
                )

    cv2.imshow("T-Zone + Contour Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

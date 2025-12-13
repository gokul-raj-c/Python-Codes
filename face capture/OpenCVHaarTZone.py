import cv2

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # Face box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # ---------- T-ZONE ----------
        tz_x1 = int(x + 0.25 * w)
        tz_y1 = int(y + 0.15 * h)
        tz_x2 = int(x + 0.75 * w)
        tz_y2 = int(y + 0.65 * h)

        cv2.rectangle(
            frame,
            (tz_x1, tz_y1),
            (tz_x2, tz_y2),
            (0, 255, 0),
            2
        )

    cv2.imshow("OpenCV + Haar + T-Zone", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

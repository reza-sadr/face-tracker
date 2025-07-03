import cv2

# Use OpenCV's built-in Haar cascade for face detection
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red square

        # Add instruction text at the bottom left of the window
        text = "Press Esc to exit..."
        font = cv2.FONT_HERSHEY_PLAIN  # Sans-serif font
        font_scale = 2.0  # Larger font size
        thickness = 3     # Increased thickness
        color = (255, 255, 255)
        margin = 10
        text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
        text_x = margin
        text_y = frame.shape[0] - margin
        cv2.putText(frame, text, (text_x, text_y), font, font_scale, color, thickness, cv2.LINE_AA)

        cv2.imshow("Face Tracker", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q") or key == 27:  # 27 is the Esc key
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

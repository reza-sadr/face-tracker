import cv2

# Use OpenCV's built-in Haar cascade for face detection
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
FACE_MODES = ("normal", "blur", "negative", "grayscale")


def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
    face_mode_index = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60)
        )

        face_mode = FACE_MODES[face_mode_index]

        for (x, y, w, h) in faces:
            if face_mode != "normal":
                face_roi = frame[y : y + h, x : x + w]

            if face_mode == "blur":
                # Use an odd kernel that scales with face size for a consistent blur effect.
                kernel = max(15, ((min(w, h) // 3) | 1))
                blurred_face = cv2.GaussianBlur(face_roi, (kernel, kernel), 0)
                frame[y : y + h, x : x + w] = blurred_face
            elif face_mode == "negative":
                frame[y : y + h, x : x + w] = cv2.bitwise_not(face_roi)
            elif face_mode == "grayscale":
                grayscale_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
                frame[y : y + h, x : x + w] = cv2.cvtColor(
                    grayscale_face, cv2.COLOR_GRAY2BGR
                )

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red square

        # Add instruction text at the bottom left of the window
        text = f"Mode: {face_mode} | Space: next mode | Esc/q: exit"
        font = cv2.FONT_HERSHEY_PLAIN  # Sans-serif font
        font_scale = 2.0  # Larger font size
        thickness = 3  # Increased thickness
        color = (255, 255, 255)
        margin = 10
        text_x = margin
        text_y = frame.shape[0] - margin
        cv2.putText(
            frame,
            text,
            (text_x, text_y),
            font,
            font_scale,
            color,
            thickness,
            cv2.LINE_AA,
        )

        cv2.imshow("Face Tracker", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord(" "):
            face_mode_index = (face_mode_index + 1) % len(FACE_MODES)
        elif key == ord("q") or key == 27:  # 27 is the Esc key
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

import cv2
from deepface import DeepFace

def capture_image_from_webcam(filename="captured.jpg"):
    cap = cv2.VideoCapture(0)
    captured = False

    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imshow("Press SPACE to capture", frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):  # SPACE to capture
            cv2.imwrite(filename, frame)
            captured = True
            break

    cap.release()
    cv2.destroyAllWindows()
    return filename if captured else None

def detect_emotion(image_path="captured.jpg"):
    result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
    return result[0]['dominant_emotion']

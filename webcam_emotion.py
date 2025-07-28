import cv2
from deepface import DeepFace

# 1. Open webcam
cap = cv2.VideoCapture(0)
print("🎥 Press SPACE to capture your face")

while True:
    ret, frame = cap.read()
    cv2.imshow("Press SPACE to capture", frame)

    key = cv2.waitKey(1)
    if key == 32:  # SPACE key to capture
        cv2.imwrite("captured.jpg", frame)
        print("✅ Image captured as 'captured.jpg'")
        break

cap.release()
cv2.destroyAllWindows()

# 2. Analyze emotion using DeepFace
try:
    result = DeepFace.analyze(img_path="captured.jpg", actions=['emotion'])
    emotion = result[0]['dominant_emotion']
    print(f"🧠 Detected Emotion: {emotion}")
except Exception as e:
    print(f"❌ Error: {e}")

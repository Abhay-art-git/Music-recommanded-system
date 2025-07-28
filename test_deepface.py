from deepface import DeepFace

result = DeepFace.analyze(img_path="test.jpg", actions=['emotion'])
print("Dominant Emotion:", result[0]['dominant_emotion'])

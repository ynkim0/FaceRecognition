from itertools import combinations
import face_recognition
import os

db_path = "C:/Users/remoAI/Downloads/data/base1"
face_encodings = []
images_path = []
not_detected_images = []
for image_path in [db_path + "/" + image for image in os.listdir(db_path)]:
    image = face_recognition.load_image_file(image_path)
    temp = face_recognition.face_encodings(image)[0]
    if len(temp) > 0:
        face_encodings.append(temp)
        images_path.append(image_path)
    else:
        not_detected_images.append(image_path)

with open('result.txt','w') as f:
    for image1_index, image2_index in combinations(range(0, len(face_encodings), 1), 2):
        result = face_recognition.compare_faces([face_encodings[image1_index]], face_encodings[image2_index])
        if result[0]:
            f.write(images_path[image1_index] + " " + images_path[image2_index] + "\n")
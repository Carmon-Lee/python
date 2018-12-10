import face_recognition as fr

image=fr.load_image_file('lena.jpeg')
image_unknown=fr.load_image_file('lena_unknown.jpeg')

encoding=fr.face_encodings(image)[0]
encoding_unknown=fr.face_encodings(image_unknown)[0]

results=fr.compare_faces([encoding],encoding_unknown)
print(results)
# face_loc=face_recognition.face_locations(image)
# print(face_loc)


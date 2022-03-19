import cv2
import face_recognition
import os
import pickle
Images_Names = os.listdir("images")
print(Images_Names)
Names=[]
Encode=[]
for images in Images_Names:
    img=face_recognition.load_image_file('images/'+images)
    encode_image=face_recognition.face_encodings(img)[0]
    Encode.append(encode_image)
    Names.append(images.split('.')[0])


print(Names)
print(Encode)
with open('Train.pkl','wb') as f:
    pickle.dump(Names,f)
    pickle.dump(Encode,f)


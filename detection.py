import cv2
from brilho import *

input('pode começar? ')

cv2.namedWindow('a') # sim vai ficar uma puta janela aberta com a imagem da sua câmera
video = cv2.VideoCapture(0)  # arrumar a câmera
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cont_frame = 0
brilho_baixo = False

while True:
    ok, frame = video.read()
    cont_frame += 1                                    # Configuração para detectar rostos
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(cinza, 1.2, 5)

    if cont_frame % 30 == 0:   # Checar os rostos de 30 em 30 frames
        print(cont_frame)
        if type(faces) is tuple:  # Se não houverem rostos
            if brilho_baixo == False:
                print('Diminuindo brilho')  # Se não houver rostos, ele baixa o brilho
                diminuir()                  # (se estiver baixo, fodase)
                brilho_baixo = True
        else:                              
            if brilho_baixo == True:
                print('Aumentando brilho')        # Se houverem rostos, aumentar o brilho
                aumentar()                        # (se já estiver alto, fodase)
                brilho_baixo = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)
    cv2.imshow('a', frame)                                          # Mostrar a janela da câmera
    key = cv2.waitKey(20)
    if key == 27:
        break
    
cv2.destroyWindow('a')
video.release()

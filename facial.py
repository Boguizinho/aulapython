import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
reconhecimento_rosto = mp.solutions.face_detection

desenho = mp.solutions.drawing_utils
reconhedor_rosto = reconhecimento_rosto.FaceDetection()

while webcam.isOpened():
    validação, frame = webcam.read()
    if not validação:
        break
    imagem = frame
    lista_rostos = reconhedor_rosto.process(imagem)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            desenho.draw_detection(imagem, rosto)

    cv2.imshow("Rostos na sua Webcam", imagem)
    if cv2.waitKey(5) == 27:
        break
webcam.release()
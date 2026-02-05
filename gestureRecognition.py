#Instalar e importar las librerias
import numpy as np
import handDetector as hand
import time
import cv2
import serial #pip install pyserial
 
#Abrir una cámara para capturar video
cap = cv2.VideoCapture(0)
 
detector = hand.handDetector() #Crear un objeto para encontar puntos de referencia de la mano

serialConnection = serial.Serial("COM5",115200)

while True:

    ret, img = cap.read() # Captura frame por frame

    if ret:
    
        img = detector.findHands(img) # Buscar mano/s en la imagen
        
        lmList, bbox = detector.findPosition(img) #Devuelve los puntos de referencia y el recuadro que encierra la mano
        
        
        if len(lmList) != 0: #Verificar si hay mano
            print("Mano detectada")
            print("Lista de puntos:", lmList)
    
            fingers = detector.fingersUp()
            print("Dedos detectados:", fingers)

            #Reconocimiento de gestos de la mano
            

            serialConnection.write((str(fingers[0])+','+str(fingers[1])+','+str(fingers[2])+
                                    ','+str(fingers[3])+','+str(fingers[4])+'\n').encode())


     
        
        cv2.imshow("Image", img) #Mostrar imagen
        
    if cv2.waitKey(10) == ord('q'): #Presionar la letra q del teclado para cerrar
        break
serialConnection.close()   
cap.release() #Liberar camara
cv2.destroyAllWindows() #Destruir o cerrar las ventanas

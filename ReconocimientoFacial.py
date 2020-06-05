import cv2
import os
from tkinter import *

def iniciar():
	dataPath = './data' #Cambia a la ruta donde hayas almacenado Data
	imagePaths = os.listdir(dataPath)
	print('imagePaths=',imagePaths)

	#face_recognizer = cv2.face.EigenFaceRecognizer_create()
	#face_recognizer = cv2.face.FisherFaceRecognizer_create()
	face_recognizer = cv2.face.LBPHFaceRecognizer_create()

	# Leyendo el modelo
	#face_recognizer.read('modeloEigenFace.xml')
	#face_recognizer.read('modeloFisherFace.xml')
	face_recognizer.read('modeloLBPHFace.xml')

	#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
	cap = cv2.VideoCapture('dani.mp4')

	faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

	while True:
		ret,frame = cap.read()
		if ret == False: break
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		auxFrame = gray.copy()

		faces = faceClassif.detectMultiScale(gray,1.3,5)

		for (x,y,w,h) in faces:
			rostro = auxFrame[y:y+h,x:x+w]
			rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
			result = face_recognizer.predict(rostro)

			cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
			'''
			# EigenFaces
			if result[1] < 5700:
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			else:
				cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
			
			# FisherFace
			if result[1] < 500:
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			else:
				cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
			'''
			# LBPHFace
			if result[1] < 70:
				cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			else:
				cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
			
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
        		break
	cap.release()
	cv2.destroyAllWindows()


class Ventana:
	window = Tk()
	window.geometry('800x600')
	window.title("Reconocimiento facial")
	# Etiquetas
	etiqueta_video = Label(window, text="Video")
	etiqueta_video.grid(column=0,row=0)
	# Etiqueta de estado
	etiqueta_estado = Label(window, text="Estado: En pausa")
	etiqueta_estado.grid(column=0,row=1)
	# Botones
	btn_comenzar = Button(window, text="Comenzar",command=iniciar)
	btn_stop = Button(window, text="Detener")
	btn_comenzar.grid(column=0, row=2)
	btn_stop.grid(column=2, row=2)
	window.mainloop()

if __name__=="__main__":
	ventana_principal = Ventana()

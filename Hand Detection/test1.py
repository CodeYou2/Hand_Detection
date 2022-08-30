from tkinter import *
from tkinter import messagebox 
import cv2
import mediapipe as mp
import time

root=Tk()
root.geometry("400x300")
Label(root,text="VOLUME CONTROL USING HANDTRACKING",font=("Bauhaus 93",10,'italic')).grid(row=0,column=2)
desc_user=Label(root,text="""A demfffff
bbbbbbbb
hjjjbjj
buubb""",font=("Times New Roman",10))
desc_user.grid(row=1,column=1)

def show():
    msg=messagebox.askyesno("alert","Are you sure about it?")
    if msg == True:
        cap= cv2.VideoCapture(0)

        mpHands = mp.solutions.hands
        hands = mpHands.Hands(False)
        mpDraw = mp.solutions.drawing_utils

        cTime = 0
        pTime = 0

        while True:
            success, img = cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)
            #print(results.multi_hand_landmarks)

            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        #print(id,lm)
                        h, w, c = img.shape
                        cx, cy = int(lm.x*w), int (lm.y*h)
                        print (id, cx, cy)

                        if id==4:
                            cv2.circle(img, (cx,cy),15, (255,0,255), cv2.FILLED)

                    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime

            cv2.putText(img, str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)


            cv2.imshow("Image", img)
            cv2.waitKey(1)

Button(root,text="Next>",command=show).grid(row=5,column=2,padx=10,pady=100)
Button(root,text="Exit",command=root.destroy).grid(row=5,column=1,padx=10,pady=100)

root.mainloop()
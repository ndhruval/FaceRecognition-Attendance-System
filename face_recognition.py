from cProfile import label
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import cv2
import mysql.connector
import os
import numpy as np
import PIL 


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1630x890+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",33,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1630,height=45)

        #Background Image
        img4=Image.open(r"Images/210888.jpg")
        img4=img4.resize((1630,890),PIL.Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=50,width=1630,height=890)

        img_top=Image.open(r"D:\Face-Recognition-Attendance-System-main\Images\face.jpg")
        img_top=img_top.resize((680,750),PIL.Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=20,y=70,width=680,height=750)

        img_bottom=Image.open(r"D:\Face-Recognition-Attendance-System-main\Images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_bottom=img_bottom.resize((980,750),PIL.Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=70,width=980,height=750)

        #Button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="lightblue")
        b1_1.place(x=385,y=665,width=200,height=40)

    def mark_attendance(self,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            mydata=f.readlines()
            name_list=[]
            for line in mydata:
                entry=line.split((","))
                name_list.append(entry[0])
            if((r not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                date1=now.strftime("%d/%m/%Y")
                time2=now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{time2},{date1},Present")


    #*********Face Recognition**********

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="Admin1",password="Admin@1",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                # my_cursor.execute("select Student_id from student where Student_id="+str(id))
                # i=my_cursor.fetchone()
                # i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    #cv2.putText(img,f"Student Id:{i}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(r,n,d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face:",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,y]
            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognizer",img)

            if cv2.waitKey(1)==13:
                break
                video_cap.release()
                cv2.destroyAllWindows()

    



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()

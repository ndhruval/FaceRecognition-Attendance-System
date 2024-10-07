from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x890+0+0")
        self.root.title("Face Recognition System")

        img4=Image.open(r"D:\Mini project\Images\facial-recognition.jpg")
        img4=img4.resize((1530,890),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=890)

        title_lbl=Label(bg_img,text="TRAINING DATA SET",font=("times new roman",33,"bold"),bg="lightblue",fg="red")
        title_lbl.place(x=0,y=0,width=1630,height=45)

        # img_top=Image.open(r"D:\Mini project\Images\face_recog.png")
        # img_top=img_top.resize((1630,325),Image.ANTIALIAS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top)

        # f_lbl=Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=70,y=55,width=1400,height=505)

        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=480,y=780,width=630,height=60)
        
        # img_bottom=Image.open(r"D:\Mini project\Images\Facial-Recognition-Attendance-system.jpg")
        # img_bottom=img_bottom.resize((1630,325),Image.ANTIALIAS)
        # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        # f_lbl=Label(self.root,image=self.photoimg_bottom)
        # f_lbl.place(x=70,y=440,width=1400,height=325)

    def train_classifier(self):
        data_directory=("Data")
        path=[os.path.join(data_directory,file) for file in os.listdir(data_directory)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')
            imageNu=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNu)
            ids.append(id)
            cv2.imshow("Train",imageNu)
            cv2.waitKey(1)==13
        ids=np.array(ids)
    
    #**********Train the classifier and save***********
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!!")
        






if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
    

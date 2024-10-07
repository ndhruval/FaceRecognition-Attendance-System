from email.mime import image
from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import title
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
import os
import PIL 


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x890+0+0")
        self.root.title("Face Recognition System")
        # First Image
        img=Image.open(r"D:\Face-Recognition-Attendance-System-main\Images\face_header_sd.jpg")
        img=img.resize((500,130),PIL.Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #Second Image
        img2=Image.open(r"D:\Face-Recognition-Attendance-System-main\Images\Face-recognition2.jpg")
        img2=img2.resize((500,130),PIL.Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=600,height=130)

        #Third Image
        img3=Image.open(r"D:\Face-Recognition-Attendance-System-main\Images\face_header_sd.jpg")
        img3=img3.resize((500,130),PIL.Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=600,height=130)


        # background Image
        img4=Image.open(r"D:\Face-Recognition-Attendance-System-main\Images\210888.jpg")
        img4=img4.resize((1530,890),PIL.Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=790)
        
        # Title
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #Student Button
        img5=Image.open(r"D:\Face-Recognition-Attendance-System-main\Images\face.jpg")
        img5=img5.resize((500,200),PIL.Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.face_recognizer,cursor="hand2")
        b1.place(x=100,y=90,width=220,height=200)

        b1_1=Button(bg_img,text="Face Recognition",command=self.face_recognizer,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=100,y=260,width=220,height=30)

        #Details section
        img6=Image.open(r"D:\Face-Recognition-Attendance-System-main\Images\student-information.png")
        img6=img6.resize((250,170),PIL.Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6) 

        b1=Button(bg_img,image=self.photoimg6,command=self.student_details,cursor="hand2")
        b1.place(x=1250,y=90,width=220,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=1250,y=270,width=220,height=30)

        #Attendance Section
        # img7=Image.open(r"D:\Mini project\Images\attendance-speech-bubble-vector-24175572.jpg")
        # img7=img7.resize((270,200),Image.ANTIALIAS)
        # self.photoimg7=ImageTk.PhotoImage(img7)  

        # b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        # b1.place(x=1200,y=90,width=220,height=200)

        # b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        # b1_1.place(x=1200,y=260,width=220,height=30)

        #Train Face 
        # img8=Image.open(r"D:\Mini project\Images\Attendance.jpg")
        # img8=img8.resize((500,200),Image.ANTIALIAS)
        # self.photoimg8=ImageTk.PhotoImage(img8)

        # b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        # b1.place(x=1200,y=90,width=220,height=200)

        # b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        # b1_1.place(x=1200,y=200,width=220,height=30)

        #Train
        img9=Image.open(r"D:\Face-Recognition-Attendance-System-main\Images\20104094.jpg")
        img9=img9.resize((500,230),PIL.Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,command=self.train_data,cursor="hand2")
        b1.place(x=650,y=90,width=220,height=230)

        b1_1=Button(bg_img,text="Train",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        b1_1.place(x=650,y=300,width=220,height=30)
        #......>>>>
        # img11=Image.open(r"D:\Mini project\Images\240-2407002_customer-helpdesk-call-center-icon-vector.png")
        # img11=img11.resize((200,210),Image.ANTIALIAS)
        # self.photoimg11=ImageTk.PhotoImage(img11)

        # b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        # b1.place(x=930,y=350,width=220,height=200)

        # b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        # b1_1.place(x=930,y=540,width=220,height=30)


        # ********Function Buttons************
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app1=Train(self.new_window)

    def face_recognizer(self):
        self.new_window=Toplevel(self.root)
        self.app1=Face_Recognition(self.new_window)




        





if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

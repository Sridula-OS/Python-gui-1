import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from fractions import Fraction

class FirstPage:
    

    def __init__(self,window):
        self.window=window
        self.window.geometry('1166x718')
        self.window.state('zoomed')


        #========background image======
        self.bg_frame= Image.open(r"C:\Users\ossri\Downloads\backgroundpic.jpg")
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        #=========frame============
        self.lgn_frame = Frame(self.window, bg='#040405', width='650', height=500)
        self.lgn_frame.place(x=700 , y=100)

        self.txt = 'WELCOME'
        self.heading = Label(self.lgn_frame , text=self.txt, font=('yu gothic ui', 25, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=200, y=1, width=200, height=100)

        #=========another image=========
        self.side_image= Image.open(r"C:\Users\ossri\Downloads\sideimage1.png")
        self.resize_image = self.side_image.resize((300,300))
        photo = ImageTk.PhotoImage(self.resize_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5,y=100)

        #===========text explanation========
        self.txt='NAME:Nikitha Rodrigues'          
        self.heading = Label(self.lgn_frame , text=self.txt, font=('yu gothic ui',12, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=362, y=125, width=200, height=22)

        self.txt='USN:RVCE23BCY056'          
        self.heading = Label(self.lgn_frame , text=self.txt, font=('yu gothic ui',12, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=350, y=160, width=200, height=15)

        self.txt='NAME:Sridula O S  '          
        self.heading = Label(self.lgn_frame , text=self.txt, font=('yu gothic ui',12, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=342, y=225, width=200, height=15)

        self.txt=' USN:RVCE23BCY057'          
        self.heading = Label(self.lgn_frame , text=self.txt, font=('yu gothic ui',12, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=350, y=255, width=200, height=15)

        self.txt='Welcome to our Python GUI'          
        self.heading = Label(self.lgn_frame , text=self.txt, font=('yu gothic ui',12, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=337, y=320, width=220, height=15)

        self.txt='Click on continue to get started'          
        self.heading = Label(self.lgn_frame , text=self.txt, font=('yu gothic ui',12, 'bold'), bg='#040405', fg='white')
        self.heading.place(x=324, y=360, width=250, height=24)

        #================button creation============
        self.btn=Button(self.lgn_frame, text='CONTINUE',command=self.open_second_page,  font=('yu gothic ui',12, 'bold'),cursor='hand2',bg='blue')
        self.btn.place(x=400, y=400)


    def open_first_page(self):
        FirstPage(self.window)
        
    
    def open_second_page(self):

        
        self.lgn_frame1 = Frame(self.window, bg='#040405', width='650', height=500)
        self.lgn_frame1.place(x=700 , y=100)

        self.label=Label(self.lgn_frame1, text='PROGRAM TO CALCULATE GOLDEN RATIO',font=('yu gothic ui',20, 'bold'), bg='#040405', fg='white' )
        self.label.place(x=47, y=1, width=550, height=60)

        self.label=Label(self.lgn_frame1, text='Enter any two numbers from 1 to 100.\nThe maximum difference between the numbers should be 30.',font=('yu gothic ui',12, 'bold'), bg='#040405', fg='white' )
        self.label.place(x=25, y=75, width=600, height=40)
        
        self.label=Label(self.lgn_frame1, text='The program will generate those many values of golden ratio.',font=('yu gothic ui',12, 'bold'), bg='#040405', fg='white' )
        self.label.place(x=25, y=125, width=600, height=40)

        #===============first user input==========================
        self.entry_var10 = StringVar()  # Variable to store user input
        
        self.e=Entry(self.lgn_frame1, textvariable=self.entry_var10, font=('yu gothic ui',20, 'bold'),width=50, bg='grey' )
        self.e.place(x=35, y=180)


        #================ second user input==============================
        self.entry_var = StringVar()  # Variable to store user input
        
        self.e=Entry(self.lgn_frame1, textvariable=self.entry_var, font=('yu gothic ui',20, 'bold'),width=50, bg='grey' )
        self.e.place(x=35, y=260)

        #======================= information button============================
        self.info_button=Button(self.lgn_frame1, text='NOTE',font=('yu gothic ui',12, 'bold'), command=self.open_fourth_page,cursor='hand2',bg='blue')
        self.info_button.place(x=220, y=320, width=220, height=60)

        self.info_button.bind("<Enter>", self.on_enter)
        self.info_button.bind("<Leave>", self.on_leave)

        
        
        back_button=Button(self.lgn_frame1, text='Back to first page',font=('yu gothic ui',12, 'bold'), command=self.open_first_page,cursor='hand2',bg='blue')
        back_button.place(x=100, y=390, width=220, height=60)

        front_button=Button(self.lgn_frame1, text='Go to next page',font=('yu gothic ui',12, 'bold'),command=self.open_third_page, cursor='hand2',bg='blue')
        front_button.place(x=350, y=390, width=220, height=60)

    def open_third_page(self):
        user_input1 = self.entry_var10.get()
        user_input1=int(user_input1)
        user_input2 = self.entry_var.get()
        user_input2=int(user_input2)

        l=[0,1]
        for i in range(0,user_input2):
            l.append(l[i]+l[i+1])
            

        gratio= [l[i]/l[i-1] for i in range(2,len(l))]

        for j in range(0,len(gratio)):
            gratio[j]=float("{:.1f}".format(gratio[j]))

         
        self.lgn_frame2 = Frame(self.window, bg='#040405', width='650', height=500)
        self.lgn_frame2.place(x=700 , y=100)

        self.label=Label(self.lgn_frame2, text='OUTPUT',font=('yu gothic ui',20, 'bold'), bg='#040405', fg='white' )
        self.label.place(x=47, y=1, width=550, height=60)

        #=============== fibonacci sequence==============
        self.label=Label(self.lgn_frame2, text="The fibonacci sequence is:" ,font=('yu gothic ui',20, 'bold'), bg='#040405', fg='white' )
        self.label.place(x=20, y=60, width=350, height=35)
        

        self.label=Label(self.lgn_frame2, text=l[user_input1:user_input1 + 5] ,font=('yu gothic ui',9, 'bold'), bg='#040405', fg='#FFEB3B' )
        self.label.place(x=10, y=100, width=650, height=16)
        self.label=Label(self.lgn_frame2, text=l[user_input1+5:user_input1 + 10] ,font=('yu gothic ui',9, 'bold'), bg='#040405', fg='#FFEB3B' )
        self.label.place(x=10, y=120, width=650, height=16)
        self.label=Label(self.lgn_frame2, text=l[user_input1+10:user_input1 + 15] ,font=('yu gothic ui',9, 'bold'), bg='#040405', fg='#FFEB3B' )
        self.label.place(x=10, y=140, width=650, height=16)
        self.label=Label(self.lgn_frame2, text=l[user_input1+15:user_input1 + 20] ,font=('yu gothic ui',9, 'bold'), bg='#040405', fg='#FFEB3B' )
        self.label.place(x=10, y=160, width=650, height=16)
        self.label=Label(self.lgn_frame2, text=l[user_input1+20:user_input1 + 25] ,font=('yu gothic ui',8, 'bold'), bg='#040405', fg='#FFEB3B' )
        self.label.place(x=10, y=180, width=650, height=16)
        self.label=Label(self.lgn_frame2, text=l[user_input1+25:user_input1 + 31] ,font=('yu gothic ui',7, 'bold'), bg='#040405', fg='#FFEB3B' )
        self.label.place(x=10, y=200, width=650, height=16)

        #=============== golden ratio====================
        self.label=Label(self.lgn_frame2, text="The golden ratio is:" ,font=('yu gothic ui',20, 'bold'), bg='#040405', fg='white' )
        self.label.place(x=8, y=240, width=289, height=35)

        self.label=Label(self.lgn_frame2, text=gratio[user_input1: user_input1+15] ,font=('yu gothic ui',15, 'bold'), bg='#040405', fg='#FFEB3B' )
        self.label.place(x=10, y=300, width=650, height=25)
        self.label=Label(self.lgn_frame2, text=gratio[user_input1+15: user_input1+31] ,font=('yu gothic ui',15, 'bold'), bg='#040405', fg='#FFEB3B' )
        self.label.place(x=10, y=340, width=650, height=25)
        

        back_button=Button(self.lgn_frame2, text='Back to second page',font=('yu gothic ui',12, 'bold'), command=self.open_second_page, cursor='hand2',bg='blue')
        back_button.place(x=100, y=400, width=220, height=60)

    def open_fourth_page(self):

        self.lgn_frame1 = Frame(self.window, bg='#040405', width='700', height=500)
        self.lgn_frame1.place(x=700 , y=100)

        self.label=Label(self.lgn_frame1, text='Golden Ratio is the ratio of \n consecutive Fibonacci numbers.\n The approximate value of golden \n ratio is 1.618033\nIts mathematical representation is:',font=('yu gothic ui',16, 'bold'), bg='#040405', fg='yellow' , justify='left')
        self.label.place(x=145,y=65, width=550, height=150)

        self.label=Label(self.lgn_frame1, text=' a+b/a = a/b\n\nThe relationship between the two\nquantities a and b is such that\nthe ratio of a and b to a is\nequal to the ratio of a to b',font=('yu gothic ui',16, 'bold'), bg='#040405', fg='yellow' )
        self.label.place(x=135, y=250, width=570, height=175)

        back_button=Button(self.lgn_frame1, text='Back to second page',font=('yu gothic ui',12, 'bold'), command=self.open_second_page, cursor='hand2',bg='blue')
        back_button.place(x=50, y=400, width=220, height=60)

        #=========another image=========
        self.side_image2= Image.open(r"C:\Users\ossri\Downloads\golden ratio pic.png")
        self.resize_image = self.side_image2.resize((250,250))
        photo = ImageTk.PhotoImage(self.resize_image)
        self.side_image_label2 = Label(self.lgn_frame1, image=photo, bg='#040405')
        self.side_image_label2.image = photo
        self.side_image_label2.place(x=0,y=25)


    def on_enter(self, event):
        # Change button background color when the mouse enters
        self.info_button.config(bg='yellow')

    def on_leave(self, event):
        # Change button background color when the mouse leaves
        self.info_button.config(bg='blue')

    
        

def page():
    window=Tk()
    FirstPage(window)
    window.mainloop()
    
if(__name__=='__main__'):
    page()

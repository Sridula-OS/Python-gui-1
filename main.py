import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

class FirstPage:
    

    def __init__(self,window):
        self.window=window
        self.window.geometry('1166x718')
        self.window.state('zoomed')


        #========background image======
        self.bg_frame= Image.open(r"C:\Users\HP\Pictures\Saved Pictures\backgroundpic.jpg")
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
        self.side_image= Image.open(r"C:\Users\HP\Pictures\Saved Pictures\sideimage1.png")
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

        self.label=Label(self.lgn_frame1, text='Enter a number from 1 to 10.',font=('yu gothic ui',12, 'bold'), bg='#040405', fg='white' )
        self.label.place(x=25, y=75, width=600, height=40)
        
        self.label=Label(self.lgn_frame1, text='The program will generate those many values of golden ratio.',font=('yu gothic ui',12, 'bold'), bg='#040405', fg='white' )
        self.label.place(x=25, y=125, width=600, height=40)

        
        self.entry_var = StringVar()  # Variable to store user input
        
        self.e=Entry(self.lgn_frame1, textvariable=self.entry_var, font=('yu gothic ui',20, 'bold'),width=50, bg='grey' )
        self.e.place(x=35, y=200)

        
        
        back_button=Button(self.lgn_frame1, text='Back to first page',font=('yu gothic ui',12, 'bold'), command=self.open_first_page,cursor='hand2',bg='blue')
        back_button.place(x=100, y=350, width=220, height=60)

        front_button=Button(self.lgn_frame1, text='Go to next page',font=('yu gothic ui',12, 'bold'),command=self.open_third_page, cursor='hand2',bg='blue')
        front_button.place(x=350, y=350, width=220, height=60)

    def open_third_page(self):
        user_input = self.entry_var.get()
        user_input=int(user_input)

        l=[0,1]
        for i in range(0,user_input):
            l.append(l[i]+l[i+1])
            

        gratio= [l[i]/l[i-1] for i in range(2,len(l))]

         
        self.lgn_frame2 = Frame(self.window, bg='#040405', width='650', height=500)
        self.lgn_frame2.place(x=700 , y=100)

        self.label=Label(self.lgn_frame2, text='OUTPUT',font=('yu gothic ui',20, 'bold'), bg='#040405', fg='white' )
        self.label.place(x=47, y=1, width=550, height=60)
        self.label=Label(self.lgn_frame2, text="The fibonacci sequence is:" ,font=('yu gothic ui',20, 'bold'), bg='#040405', fg='white' )
        self.label.place(x=20, y=100, width=350, height=35)

        self.label=Label(self.lgn_frame2, text=l ,font=('yu gothic ui',17, 'bold'), bg='#040405', fg='#FFEB3B' )
        self.label.place(x=10, y=140, width=400, height=22)


        self.label=Label(self.lgn_frame2, text="The golden ratio is:" ,font=('yu gothic ui',20, 'bold'), bg='#040405', fg='white' )
        self.label.place(x=8, y=225, width=289, height=35)

        self.label=Label(self.lgn_frame2, text=gratio[0:7] ,font=('yu gothic ui',15, 'bold'), bg='#040405', fg='#FFEB3B' )
        self.label.place(x=10, y=260, width=650, height=25)
        self.label=Label(self.lgn_frame2, text=gratio[7:10] ,font=('yu gothic ui',15, 'bold'), bg='#040405', fg='#FFEB3B' )
        self.label.place(x=10, y=300, width=650, height=25)

        back_button=Button(self.lgn_frame2, text='Back to second page',font=('yu gothic ui',12, 'bold'), command=self.open_second_page, cursor='hand2',bg='blue')
        back_button.place(x=100, y=380, width=220, height=60)


    
        

def page():
    window=Tk()
    FirstPage(window)
    window.mainloop()
    
if(__name__=='__main__'):
    page()

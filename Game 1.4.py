# coding=utf8
"""
Kod: Cognitive madness
2018-05-10
Adam King & Lucas Niklasson
"""
import tkinter as tk               
from tkinter import font as tkfont
import os
import sys

#Organiserar frames
class FrameSwitch(tk.Tk):

    def __init__(self):        
        tk.Tk.__init__(self)
    
    
        #Best�mmmer titelfonten p� varje frame
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        #skapar grunden f�r varje frame
        container = tk.Frame(self)
        container.pack()
        self.frames = {}
        
        # lagrar alla frames pa varandra
        # nar vi vill att en frame ska vara synlig
        # lyfter vi den over alla andra
        for F in (Menu, Dead, BegAdv, Quit, Que1, Que2, Que3, Que4, Que5, Que6, Que7):
            frame_scene = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[frame_scene] = frame
            


            #tillverkar frames i samma storlek
            #Vilket g�r att den som �r l�ngst upp �r synlig endast
            frame.grid(column=0,row=0, sticky="wens")

        self.show_frame("Menu")
        #lyfter fram frames
    def show_frame(self, frame_scene):
        #Nar klassen/framen anropas lyfts den fram
        frame = self.frames[frame_scene]
        frame.tkraise()


################################################################################


#Ger val om man vill avsluta eller borja sitt adventure
class Menu(tk.Frame):
    """Huvudmeny"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="Welcome to: Mad cognition, bruh!", font=controller.title_font, bg="black" , fg="yellow")
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Start The Game",bg="yellow", padx=10, pady=10,
                           #Lambda: h�nvisar till frame_name i listan i klass frameswith.
                           #sedan tar controller.show_frame �ver i den egna metoden
                           #och tar fram den �nskade framen i detta fall "BegAdv"
                            command=lambda: controller.show_frame("BegAdv"))
        button2 = tk.Button(self, text="Quit The Game", bg="yellow", padx=10,pady=10,
                            command=lambda:controller.show_frame("Quit"))
        button1.pack()
        button2.pack()
        
        

        

class Dead(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="Suddenly you are hit in the back with an axe. GAME OVER", 
                         font=controller.title_font, bg="black", fg="yellow",)
        label2 = tk.Label(self, text="Somebody whispers in you ear: It's never too late to give up",
                          font=controller.title_font, bg="black", fg="yellow")
        label.pack(side="top", fill="x", pady=10)
        label2 .pack(side="top", fill="x", pady=10)
        
        
        button1 = tk.Button(self, text="Menu", bg="yellow", 
                            command=lambda: controller.show_frame("Menu"))
        button1.pack(side="bottom",ipadx=100, ipady=50)
        
    
        

#Borjar spelet genom att skicka en vidare till spelets f�rsta scenario
class BegAdv(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="You wake up in a desolate mansion. ",
                         font=controller.title_font, fg="yellow", bg="black")
        label2 = tk.Label(self, text="You have been kidnapped by mad cognitive scientists. ", 
                          font=controller.title_font, fg="yellow", bg="black")
        label3 = tk.Label(self, text="They challenge you to answer their five riddles. Or die trying. ",
                          font=controller.title_font, fg="yellow", bg="black")
        label.pack(fill="x", pady=10)
        label2.pack(fill="x", pady=10)
        label3.pack(fill="x", pady=10)
        
        button = tk.Button(self, padx=20,pady=20, text="Begin", bg="red",
                           command=lambda: controller.show_frame("Que1"))
        button.pack(side="bottom",ipadx=100, ipady=50)
        
        
        
#Ska avsluta programmet men funkar ej
class Quit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="There is no quitting. Only Death...", font=controller.title_font,
                         bg="black", fg="yellow")
        label.pack(side="top", fill="x", pady=10)
        #st�nger programmet/framesen
        button = tk.Button(self, text="Quit", bg="purple",
                           command=parent.destroy)
        
        


      
        
        
        
################################################################################        
 
        

#Spelets forsta scenario
#�rver tk.Frame
class Que1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        #skriver text o anv�nder sig av fontmallen fr�n frameswitch klassen
        label = tk.Label(self, text="The first riddle reads:", 
                         font=controller.title_font, bg="black", fg="yellow")
        label2 = tk.Label(self, text="What is the PFC short for?", 
                             font=controller.title_font, bg="black", fg="yellow") 
        #Packar de tv� texterna
        label.pack(side="top", fill="x", pady=10)
        label2.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Prefrontal Cortex", bg="yellow", 
                            command=lambda: controller.show_frame("Que2"))#progression
        button2 = tk.Button(self, text="Personal Force calculator", bg="yellow", 
                            command=lambda: controller.show_frame("Dead")) # failstate
        button3 = tk.Button(self, text="Potassium Field controller", bg="yellow", 
                            command=lambda: controller.show_frame("Dead")) # failstate     
        #packar de 3 knapparna och fyller dem med ipadx & ipady
        button1.pack(side="bottom",ipadx=116, ipady=50)
        button2.pack(side="bottom",ipadx=100, ipady=50)    
        button3.pack(side="bottom",ipadx=100, ipady=50)
        
#Spelets andra scenario
class Que2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="One of the scientists mutters a new question: What is GABA?", 
                         font=controller.title_font, bg="black", fg="yellow",)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="A neurotransmitter", 
                            bg="yellow",command=lambda: controller.show_frame("Que3"))#progression
        button2 = tk.Button(self, text="A new kind of smartdrug", 
                            bg="yellow",command=lambda: controller.show_frame("Dead")) #Failstate
        button3 = tk.Button(self, text="A protein", bg="yellow", 
                            command=lambda: controller.show_frame("Dead"))#failstate
        button4 = tk.Button(self, text="A somatotopic map", bg="yellow", 
                            command=lambda: controller.show_frame("Dead"))#failstate        
        button1.pack(side="bottom",ipadx=107, ipady=50)
        button2.pack(side="bottom",ipadx=100, ipady=50)
        button3.pack(side="bottom",ipadx=112, ipady=50)
        button4.pack(side="bottom",ipadx=100, ipady=50)
        
#Spelets tredje scenario
class Que3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="The scientists looks away!", 
                         font=controller.title_font, bg="black", fg="yellow",)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Wait until next question", bg="yellow",
                            command=lambda: controller.show_frame("Que4"))#progression
        button2 = tk.Button(self, text="Attack!", bg="yellow",
                            command=lambda: controller.show_frame("Dead"))#failstate
        button3 = tk.Button(self, text="Ask to have a question repeated!", bg="yellow", 
                            command=lambda: controller.show_frame("Dead"))#failstate        
        button1.pack(side="bottom",ipadx=100, ipady=50)
        button2.pack(side="bottom",ipadx=120, ipady=50)
        button3.pack(side="bottom",ipadx=100, ipady=50)
         

      
#Spelets fjarde scenario    
class Que4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="After the long wait you get a new question: Where is fusiform gyrus?", 
                         font=controller.title_font, bg="black", fg="yellow",)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="The temporallobe", bg="yellow",
                            command=lambda: controller.show_frame("Que5"))#progression
        button2 = tk.Button(self, text="The parietallobe", bg="yellow", 
                            command=lambda: controller.show_frame("Dead"))#failstate
        button3 = tk.Button(self, text="The brainstem", bg="yellow", 
                            command=lambda: controller.show_frame("Dead"))#failstate
        button4 = tk.Button(self, text="The frontal lobe", bg="yellow",
                            command=lambda: controller.show_frame("Dead"))#failstate      
        button1.pack(side="bottom",ipadx=100, ipady=50)
        button2.pack(side="bottom",ipadx=100, ipady=50)
        button3.pack(side="bottom",ipadx=100, ipady=50)
        button4.pack(side="bottom",ipadx=100, ipady=50)
        

#Spelets femte scenario
class Que5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="To what kind of system belongs Pulvinar?", 
                         font=controller.title_font, bg="black", fg="yellow",)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="The sight", bg="yellow", 
                            command=lambda: controller.show_frame("Que6"))#progression
        button2 = tk.Button(self, text="Your hearing", bg="yellow",
                            command=lambda: controller.show_frame("Dead"))#failstate
        button3 = tk.Button(self, text="The touch", bg="yellow",
                            command=lambda: controller.show_frame("Dead"))#failstate
        button4 = tk.Button(self, text="The smell", bg="yellow",
                            command=lambda: controller.show_frame("Dead"))#failstate         
        button1.pack(side="bottom",ipadx=100, ipady=50)
        button2.pack(side="bottom",ipadx=100, ipady=50)
        button3.pack(side="bottom",ipadx=100, ipady=50)
        button4.pack(side="bottom",ipadx=100, ipady=50)


#Spelets sjatte scenario   
class Que6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="The last question..from the years 63-83 a team won hockey-VM 17 times, what team?", 
                         font=controller.title_font, bg="black", fg="yellow")
        label.pack(side="top", fill="x", pady=10)
        
        button1 = tk.Button(self, text="China", bg="yellow",
                                command=lambda: controller.show_frame("Dead"))#failstate
        button2 = tk.Button(self, text="Sweden", bg="yellow",
                            command=lambda: controller.show_frame("Dead"))#failstate  
        button3 = tk.Button(self, text="The Soviet union", bg="yellow",
                                command=lambda: controller.show_frame("Que7"))#progression
        button4 = tk.Button(self, text="USA", bg="yellow",
                                command=lambda: controller.show_frame("Dead"))#failstate
        button1.pack(side="bottom",ipadx=100, ipady=50)
        button2.pack(side="bottom",ipadx=100, ipady=50)
        button3.pack(side="bottom",ipadx=85, ipady=50)
        button4.pack(side="bottom",ipadx=100, ipady=50)        
    

################################################################################

#Spelets sjunde scenario
class Que7(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        label = tk.Label(self, text="You made your way out, congrats on being alive!", 
                        font=controller.title_font, bg="black", fg="yellow")
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Menu", bg="yellow",
                            command=lambda: controller.show_frame("Menu"))#Tar tillbaka anv�ndaren till huvudmenyn
        button2 = tk.Button(self, text="Ask for constructive criticism", bg="yellow",
                            command=lambda: controller.show_frame("Dead"))#failstate (lade till denna f�r att det �r sjukt roligt)     
        button1.pack(side="bottom",ipadx=125, ipady=50)
        button2.pack(side="bottom",ipadx=100, ipady=50)


################################################################################
if __name__ == "__main__": 
    app = FrameSwitch()
    app.mainloop()   

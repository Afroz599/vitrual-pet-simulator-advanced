from random import randint
from PIL import Image,ImageTk
import tkinter as tk
import pyttsx3
import speech_recognition as sr
root=tk.Tk()
engine=pyttsx3.init()
root.title('https://Petsimulator.in')
t0=tk.Label(root,text='Feed, play, and train your puppy to keep it happy and healthy.',font=('Arial',12,'italic'),fg='brown').pack(fill='x')
root.geometry('500x700')
root.configure(borderwidth=10)
img=Image.open(r"C:\Users\Asus\Downloads\HD-wallpaper-cute-dog-for-cute-white-puupy-puupy-dog-pet-animal-removebg-preview.png")
img=img.resize((200,250))
photo=ImageTk.PhotoImage(img)
label_img=tk.Label(root,image=photo)
label_img.image=photo
label_img.pack()
l2=tk.Label(root,text='Name your pet',font=('Arial',10)).pack(padx=2,pady=3)
e1=tk.Entry(root)
e1.pack(padx=2,pady=3)
def name():
    engine.setProperty('rate',350) 
    l3=tk.Label(root,text=f'{e1.get()}  is ready for taming',font=('Arial',10)).pack(pady=2)
    engine.say('bowwww,bowwwww')
    engine.runAndWait()
btn=tk.Button(root,text='set name',font=('Arial',8),command=name,cursor='hand2').pack(pady=3)
def talk():
    l3=tk.Label(root,text='say something...',font=('Arial',8)).pack()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        text=text.lower()
        if text=='name':
            engine.say(f'woow iam {e1.get()}wowwow')
            engine.runAndWait()
        elif text=='food':
            engine.say(f'wowwfff woffwoff')
            engine.runAndWait()
        elif text=='bark':
            engine.say('woffff what iam supposed to')
            engine.runAndWait()
        else:
            engine.say('wowwwwwwwwwwwwww')
            engine.runAndWait()
    except sr.UnknownValueError:
        l4=tk.Label(root,text=f'{e1.get()} cannot hear you').pack()
    except sr.RequestError:
        l5=tk.Label(root,text=f'{e1.get()} is busy now').pack()    
btn4=tk.Button(root,text=f'Talk with {e1.get()}',command=talk,cursor='hand2').pack(pady=2)
def food():
    k=randint(1,100)
    if k%2==0:
        l5=tk.Label(root,text=f'{e1.get()} stomach is full',font=('Arial',10,'bold'),fg='green').pack(pady=3)
        engine.say('woof woff')
    else:
        l6=tk.Label(root,text=f'you are feeding {e1.get()}',font=('Arial',10,'bold'),fg='green').pack(pady=3)
        engine.say('woooaaaah')
def game():
    k=randint(1,100)
    if k%2==0:
        l7=tk.Label(root,text=f'{e1.get()} is playing with you',font=('Arial',10,'bold'),fg='blue').pack(pady=3)
        engine.say('WOOF WOOF WOOO')
    else:
        l8=tk.Label(root,text=f'{e1.get()} is tired',font=('Arial',10,'bold'),fg='blue').pack(pady=3)
        engine.say('Wooo...Zzz...')    
def end():
    exit()
def submit1():
    food()
def submit2():
    game()
def submit3():
    end()
btn3=tk.Button(root,text='Feed',command=submit1,cursor='hand2').pack(side='left')
btn4=tk.Button(root,text='Play',command=submit2,cursor='hand2').pack(side='left')
btn5=tk.Button(root,text='Exit',command=submit3,cursor='hand2').pack(side='left')
root.mainloop()

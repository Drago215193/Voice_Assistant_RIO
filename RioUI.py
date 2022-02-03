from cProfile import label
from cmath import exp
import imghdr
from logging import root
from tkinter import *
from PIL import ImageTk,Image

root= Tk()

root.title('rio')
root.geometry('1040x600')

img = ImageTk.PhotoImage(Image.open('D:\\git rio\\Voice_Assistant_RIO\\eve.jpg'))
panel = Label(root, image=img)
panel.pack(side='right', fill='both', expand='no')

userText = StringVar()

userText.set('Your Virtual Assistant')
userFrame = LabelFrame(root, text='RIO', font=('Railways', 30, 'bold'))
userFrame.pack(fill='both', expand='yes')

top= Message(userFrame, textvariable=userText, bg='black', fg='white')
top.config(font=("Century Gothic", 25, 'bold'))
top.pack(side='top', fill='both', expand='yes')

btn = Button(root, text='Run', font=('railways', 15, 'bold'),bg='red', fg='white').pack(fill='x', expand='no')
btn2 = Button(root, text='Close', font=('railways', 15,'bold'), bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')

root.mainloop()


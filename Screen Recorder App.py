from tkinter import *
import pyscreenrec
from PIL import Image


root =Tk()
root.geometry("500x300") # kobr l fenetre
root.title("Screen Recorder By Hamza") #name de la fenetre
root.config(bg = "#2B2B2C") # colore de bagraound
root.resizable(False, False) # means que je peut modifier les diametre de la fenetre

def start_rec():
    file = Filename.get()
    rec.start_recording(str(file+".mp4"),5)

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()

rec = pyscreenrec.ScreenRecorder()
# mettre l'icone
icone = PhotoImage (file = r"D:\python\Screen Recorder\img\rec.png")
root.iconphoto(False, icone)

#entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=19, font="arial 15")
entry.place(x = 150, y = 100)
Filename.set("New Record")

#botton
img = Image.open('D:\python\Screen Recorder\img\start-button.png')
img = img.resize((50, 50))
img.save('start1.png')
btn = PhotoImage(file= "start1.png")
start = Button(root, image=btn, bd=0, bg="#2B2B2C", command=start_rec)
start.place(x = 225, y = 30)

imgstpause = Image.open('D:\python\Screen Recorder\img\stop.png')
imgstpause = imgstpause.resize((50, 50))
imgstpause.save('stop1.png')
imspause = PhotoImage(file= "stop1.png")
pause = Button(root, image=imspause, bd=0, bg="#2B2B2C", command=pause_rec)
pause.place(x = 325, y = 150)

imgs = Image.open('D:\python\Screen Recorder\img\pause.png')
imgs = imgs.resize((50, 50))
imgs.save('pause1.png')
imgresum = PhotoImage(file= "pause1.png")
resume = Button(root, image=imgresum, bd=0, bg="#2B2B2C", command=resume_rec)
resume.place(x = 225, y = 150)

imgstop = Image.open('D:\python\Screen Recorder\img\star.png')
imgstop = imgstop.resize((50, 50))
imgstop.save('star1.png')
imgpstop = PhotoImage(file= "star1.png")
stop = Button(root, image=imgpstop, bd=0, bg="#2B2B2C", command=stop_rec)
stop.place(x = 125, y = 150)

root.mainloop()
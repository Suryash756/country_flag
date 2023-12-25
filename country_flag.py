from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title("COUNTRY_FLAGS")
root.geometry("600x600")
root.configure(background="#6dd5ed")

head = Label(root,text="COUNTRY_IMAGE",fg="#734b6d",bg="#6dd5ed")
head.place(rely=0.1,relx=0.5,anchor = CENTER)

inp = Entry(root)


img = Label(root,fg="#734b6d",bg="#6dd5ed")

america = ImageTk.PhotoImage(Image.open("America.jpg"))
australia = ImageTk.PhotoImage(Image.open("Australia.png"))
india = ImageTk.PhotoImage(Image.open("India.jpg"))
japan = ImageTk.PhotoImage(Image.open("Japan.jpg"))
china = ImageTk.PhotoImage(Image.open("china.jpg"))

dict = {"america":america,"autralia":australia,"india":india,"japan":japan,"china":china}

def fun():
    inp_val = inp.get()
    try:
        img["image"]=dict[inp_val]
    except:
        messagebox.showinfo("problem","looks country is not available in our dictonary or try writting country name in lowercase")

btn = Button(root,text="enter",command=fun)
inp.place(rely=0.2,relx=0.5,anchor=CENTER)
btn.place(rely=0.2,relx=0.7,anchor=CENTER)
img.place(rely=0.5,relx=0.5,anchor=CENTER)
    


root.mainloop()
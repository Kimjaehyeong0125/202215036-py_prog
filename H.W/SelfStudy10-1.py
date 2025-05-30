from tkinter import*
window=Tk()

image_files = ["C:\\Users\\dktm9\\Downloads\\gif\\rabbit.gif"
               ,"C:\\Users\\dktm9\\Downloads\\gif\\kitkat.gif"]


photos = [PhotoImage(file=img) for img in image_files]


for photo in photos:
    lb1=Label(window,image=photo)
    lb1.pack(side=LEFT)


window.mainloop()
from tkinter import *
from time import *

# 파일명 리스트
fnameList = ["yogurt.gif", "gingerbread.gif", "honey.gif",
             "icecream.gif", "jellybean.gif", "kitkat.gif",
             "lollipop.gif", "marshmallow.gif", "nougat.gif"]

# 각 파일에 대응되는 한글 이름 리스트
titleList = ["yogurt.gif", "gingerbread.gif", "honey.gif",
             "icecream.gif", "jellybean.gif", "kitkat.gif",
             "lollipop.gif", "marshmallow.gif", "nougat.gif"]

photoList = [None] * 9
num = 0

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0

    photo = PhotoImage(file="C:\\Users\\dktm9\\Downloads\\gif\\" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    nameLabel.config(text=titleList[num])  # 한글 이름 표시

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8

    photo = PhotoImage(file="C:\\Users\\dktm9\\Downloads\\gif\\" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    nameLabel.config(text=titleList[num])  # 한글 이름 표시

window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음>>", command=clickNext)

photo = PhotoImage(file="C:\\Users\\dktm9\\Downloads\\gif\\" + fnameList[0])
pLabel = Label(window, image=photo)

# 시작 시 첫 번째 항목의 이름 출력
nameLabel = Label(window, text=titleList[0], font=("Arial", 12))

btnPrev.place(x=250, y=10)
nameLabel.place(x=320, y=15)
btnNext.place(x=400, y=10)
pLabel.place(x=15, y=50)

window.mainloop()

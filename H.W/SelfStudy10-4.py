from tkinter import *
from tkinter import messagebox

def shiftEvent(event):
    # Shift 눌렸을 때만 다음 키 입력을 기다림
    window.bind("<Key>", arrowOnly)

def arrowOnly(event):
    arrows = {
        "Up": "위쪽 화살표",
        "Down": "아래쪽 화살표",
        "Left": "왼쪽 화살표",
        "Right": "오른쪽 화살표"
    }
    if event.keysym in arrows:
        messagebox.showinfo("키보드 이벤트", f"눌린 키: {arrows[event.keysym]}")
    # 다시 일반 키로 복귀
    window.bind("<Key>", keyEvent)

def keyEvent(event):
    pass  # 일반 키 눌림은 무시

window = Tk()
window.bind("<Shift_L>", shiftEvent)
window.bind("<Key>", keyEvent)
window.mainloop()

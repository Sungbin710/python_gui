from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")

# 아이디, 비밀번호와 같이 한줄에 입력받을 정보 (Enter 불가능)
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1: 첫번째 라인, 0: 0번째 column 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
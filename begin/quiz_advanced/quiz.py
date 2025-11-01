from tkinter import *
question = {'1 + 1' : [1,2,3,4],
                '2 + 2' : [2,3,4,8],
                '3 + 4' : [1,3,7,9]}
ans = [2,4,7]
mark = 0

def start_quiz():
    start_button.forget() # giau nut Start
    next_button.pack() #hien thi button Next
    next_question()

def next_question():
    global mark
    if mark < len(question):
        check_ans()
        user_ans.set('None')

        c_question = list(question.keys())[mark]
        clear_frame()
        Label(f1,text=f'Question : {c_question}',padx=15,font ='calibre 15 bold').pack(anchor=NW)
        for option in question[c_question]:
            Radiobutton(f1,text=option,variable=user_ans,value=option,padx=25).pack(anchor=NW)
        mark += 1
    else:
        next_button.forget()
        check_ans()
        clear_frame()
        output = f'Your score is {user_score.get()} out of {len(question)}'
        Label(f1,text = output, font='calibre 25 bold').pack()
        Label(f1,text='Thank you for playing',
                font = 'calibre 20 bold').pack()
def check_ans():
    #lay cau hoi tu user da chon tu StringVar
    try:
        temp_ans = int(user_ans.get())
    except ValueError:
        return
    #kiem tra dieu kien
    if temp_ans == ans[mark -1]:
        user_score.set(user_score.get() + 1)
def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("QUIZ APP CUA DUC DEP ZAI")
    root.geometry("850x520")
    root.minsize(800, 400)

    user_ans = StringVar()
    user_ans.set("None")
    user_score = IntVar()
    user_score.set(0)

    Label(root,text="QUIZ GAME",
        font = 'calibre 40 bold',
        relief=SUNKEN, background="cyan",
        padx=10, pady=9).pack()
        
    Label(root,text='',
        font= 'calibre 10 bold').pack()
    start_button = Button(root,text='Start Quiz',
                        command = start_quiz,
                        font = 'calibre 14 bold')
    
    start_button.pack()

    f1 = Frame(root)
    f1.pack(side='top',fill='x')
    next_button = Button(root,text= 'Next Button',
                        command= next_question,
                        font = 'calibre 20 bold')
    root.mainloop()
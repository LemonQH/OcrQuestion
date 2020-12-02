import tkinter as tk
from tkinter import filedialog,messagebox,ttk
from QuestionClass import Question
import os

question=Question([],"")

def get_files():
    files = filedialog.askopenfilenames(filetypes=[("image", "*.bmp"),("image", "*.png"),("image", "*.jpg"),])
    question.file_paths=files

    if files:
        for file in files:
            text1.insert(tk.END, file + '\n')
            text1.update()
    else:
        print('')
def set_result_path():
    result_path=filedialog.askdirectory()
    question.result_path=result_path
    text2.insert(tk.END,result_path)

def search_question_files():
    question.start_ocr()
    os.system('start '+question.result_path)




root=tk.Tk()
root.title(" youdao ocr question test")
frm = tk.Frame(root)
frm.grid(padx='50', pady='50')

btn_get_file = tk.Button(frm, text='选择题目图片', command=get_files)
btn_get_file.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
text1 = tk.Text(frm, width='40', height='10')
text1.grid(row=0, column=1)
btn_get_result_path=tk.Button(frm,text='选择搜索结果路径',command=set_result_path)
btn_get_result_path.grid(row=1,column=0)
text2=tk.Text(frm,width='40', height='2')
text2.grid(row=1,column=1)



btn_sure=tk.Button(frm,text="搜题",command=search_question_files)
btn_sure.grid(row=4,column=1)

root.mainloop()
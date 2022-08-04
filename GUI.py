import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from functools import partial
from merge import merge_multiple_cocos
from preprocess import PreProcess
from tkinter.messagebox import askokcancel, showinfo, showerror

dict_coco: dict = {}
list_coco: list = []
list_out: list = []
counter: list = []

window = tk.Tk()

window.title("Coco Toolkit")

tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Merge Multiple')
tabControl.add(tab2, text='Train Test Val Split')

e1 = Entry(tab1, width=50, borderwidth=5)
e2 = Entry(tab1, width=50, borderwidth=5)
e3 = Entry(tab1, width=50, borderwidth=5)
e4 = Entry(tab1, width=10, borderwidth=5)
e5 = Entry(tab2, width=50, borderwidth=5)
e6 = Entry(tab2, width=50, borderwidth=5)
e7 = Entry(tab2, width=50, borderwidth=5)
e8 = Entry(tab2, width=10, borderwidth=5)
e9 = Entry(tab2, width=10, borderwidth=5)

e4.insert(0, "100000")

e1.grid(row=1, column=0)
e2.grid(row=4, column=0)
e3.grid(row=8, column=0)
e4.grid(row=9, column=0)
e5.grid(row=1, column=0)
e6.grid(row=4, column=0)
e7.grid(row=8, column=0)
e8.grid(row=9, column=0)
e9.grid(row=9, column=1)


def directory(entry, tp):
    # get a directory path by user
    if tp == 0:
        filepath = filedialog.askdirectory()
        answer = askokcancel(title='Confirm Selected File', message=filepath)
        if answer:
            entry.insert(0, string=filepath)
            dict_coco["image"] = filepath
    if tp == 1:
        filepath = filedialog.askopenfilename()
        answer = askokcancel(title='Confirm Selected File', message=filepath)
        if answer:
            entry.insert(0, string=filepath)
            dict_coco["json"] = filepath
    if tp == 2:
        if len(entry.get()) != 0:
            list_out.append(entry.get())
        else:
            filepath = filedialog.askdirectory()
            entry.insert(0, string=filepath)
            list_out.append(filepath)


def iter_dir(coco_dict):
    counter.append(0)
    if len(e1.get()) != 0 and len(e2.get()) != 0 or len(e5.get()) != 0 and len(e6.get()) != 0:
        if coco_dict:
            list_coco.append([coco_dict["json"], coco_dict["image"]])
            del coco_dict["json"]
            del coco_dict["image"]
            e1.delete(0, END)
            e2.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            showinfo(title="Information", message="Dataset is ready")
        else:
            if len(e2.get()) != 0:
                list_coco.append([e2.get(), e1.get()])
                e1.delete(0, END)
                e2.delete(0, END)
                showinfo(title="Information", message="Dataset is ready")
            else:
                list_coco.append([e6.get(), e5.get()])
                e5.delete(0, END)
                e6.delete(0, END)
                showinfo(title="Information", message="Dataset is ready")

    else:
        showerror(title="Error", message="Please copy path datasets or choose your directory with"
                                         " clicking image path and json path buttons")


def clear(list_c):
    list_c.clear()


label = Label(tab1, text="Choose image folder directory or enter it", fg="black", font="Castellar")
label.grid(row=0)
label = Label(tab1, text="")
label.grid(row=2)
label = Label(tab1, text="Choose coco json file directory or enter it", fg="black", font="Castellar")
label.grid(row=3)
label = Label(tab1, text="")
label = Label(tab2, text="Choose image folder directory or enter it", fg="black", font="Castellar")
label.grid(row=0)
label = Label(tab2, text="")
label.grid(row=2)
label = Label(tab2, text="Choose coco json file directory or enter it", fg="black", font="Castellar")
label.grid(row=3)
label = Label(tab1, text="")
label.grid(row=5)
label = Label(tab1, text="")
label.grid(row=6)
label = Label(tab2, text="")
label.grid(row=5)
label = Label(tab2, text="")
label.grid(row=6)
label = Label(tab1, text="Choose output directory or enter it", fg="black", font="Castellar")
label.grid(row=7)
label = Label(tab2, text="Choose output directory or enter it", fg="black", font="Castellar")
label.grid(row=7)
label = Label(tab1, text="Enter max id", fg="black", font="Castellar")
label.grid(row=9, column=0, sticky=tk.W)
label = Label(tab2, text="Test Percent %", fg="black", font="Castellar")
label.grid(row=9, column=0, sticky=tk.W)
label = Label(tab2, text="Val Percent %", fg="black", font="Castellar")
label.grid(row=9, column=0, sticky=tk.E)

cb = BooleanVar()
button1 = Checkbutton(tab1, text="Visualizer", variable=cb, onvalue=True, offvalue=False, height=2, width=10)
button1.grid(row=9, column=0, sticky=tk.E)

button_img_pth = Button(tab1, text="Image Path", fg="black", bg="white", command=partial(directory, e1, 0))
button_img_pth.grid(row=1, column=1)
button_json_pth = Button(tab1, text="Json Path", fg="black", bg="white", command=partial(directory, e2, 1))
button_json_pth.grid(row=4, column=1)
button_img_pth2 = Button(tab2, text="Image Path", fg="black", bg="white", command=partial(directory, e5, 0))
button_img_pth2.grid(row=1, column=1)
button_json_pth2 = Button(tab2, text="Json Path", fg="black", bg="white", command=partial(directory, e6, 1))
button_json_pth2.grid(row=4, column=1)
button_out_pth = Button(tab1, text="Output Path", fg="black", bg="white", command=partial(directory, e3, 2))
button_out_pth.grid(row=8, column=1)
button_out_pth2 = Button(tab2, text="Output Path", fg="black", bg="white", command=partial(directory, e7, 2))
button_out_pth2.grid(row=8, column=1)
button_insert_data = Button(tab1, text="Insert Dataset", fg="black", bg="white", command=partial(iter_dir, dict_coco))
button_insert_data.grid(row=5, column=0)
button_insert_data2 = Button(tab2, text="Insert Dataset", fg="black", bg="white", command=partial(iter_dir, dict_coco))
button_insert_data2.grid(row=5, column=0)
button_merge = Button(tab1, text="Merge", fg="black", bg="white",
                      command=lambda: [merge_multiple_cocos(list_coco, merge_path=list_out[0], first_id=int(e4.get()),
                                                           visualizer=cb.get()), clear(list_c=list_coco)])
button_split = Button(tab2, text="Split", fg="black", bg="white",
                      command=lambda: [PreProcess(PreProcess.reader(list_coco[0][0])).train_test_validation_split(
                          image_path=list_coco[0][1], test_percent=int(e8.get()), validation_percent=int(e9.get()),
                          out_path=list_out[0]), clear(list_coco)])

button_merge.grid(row=10, column=0)
button_split.grid(row=10, column=0)

tabControl.pack(expand=1, fill="both")

window.mainloop()

print(list_coco)
#SPDX-License-Identifier: MIT
# Created by masataka.eth
import os
import tkinter as tk
from tkinter import scrolledtext 
from datetime import datetime
import copy
import json

root = tk.Tk()
root.title('Make Metadata JsonFile')
root.geometry("500x650")
root.resizable(width=False, height=False)

# global --------------------------------------
attribute_cnt = 0
trait_type_list = []
value_list = []

# Function ------------------------------------ 
def close_window():
    root.destroy()

def chgradio():
    try:
        if radiovar.get() == 2:
            rdo3_txt["state"] = "normal"
        else:
            rdo3_txt["state"] = "disable"
    except:
        var_output.set("Exception error occurred!")

def AddAttribute():
    global attribute_cnt
    try:
        if txt_4_0.get() == "" or txt_4_1.get() == "":
            var_output.set("Both inputs are required!")
            return
        attribute_cnt += 1

        trait_type_list.append(txt_4_0.get())
        value_list.append(txt_4_1.get())

        text_area.delete("1.0","end")
        for num in range(len(trait_type_list)):
            text_area.insert(tk.END,trait_type_list[num] + "," + value_list[num] + "\n")

    except:
        var_output.set("Exception error occurred!")

def DeleteAttribute():
    global attribute_cnt
    try:
        if attribute_cnt <= 0:
            var_output.set("There are no items to delete.")
            return
        attribute_cnt -= 1

        del trait_type_list[len(trait_type_list) -1]        
        del value_list[len(value_list) -1]

        text_area.delete("1.0","end")
        for num in range(len(trait_type_list)):
            text_area.insert(tk.END,trait_type_list[num] + "," + value_list[num] + "\n")

    except:
        var_output.set("Exception error occurred!")

def Validate():
    if txt_0_0.get() == "" or txt_0_1.get() == "" or txt_1_0.get() == ""  or txt_3_0.get() =="":
        return False
    if int(txt_0_0.get()) >= int(txt_0_1.get()):
        return False
    

def ExeOutput():
    try:
        if Validate() == False:
            var_output.set("Please review the input data!")
            return

        fromint = int(txt_0_0.get())
        toint = int(txt_0_1.get())
        dict = {}
        dict2 = {}
        attlist = []

        # extensin fix
        extension = ""
        if radiovar.get() == 0:
            extension = ".png"
        elif radiovar.get() == 1:
            extension = ".gif"
        else:
            extension = "." + rdo3_txt.get()

        # make newFolder
        new_dir_path = './' + datetime.now().strftime('%Y%m%d%H%M%S')
        os.mkdir(new_dir_path)

        # from - to make json
        for num in range(fromint,toint+1):
            dict["name"] = txt_1_0.get() + "#" + str(num)
            dict["description"] = txt_2_0.get()

            #dict["image"] = txt_3_0.get() + str(num) + extension
            dict["image"] = txt_3_0.get() + "2209_gold_photographer" + extension

            # attribute
            if attribute_cnt > 0:
                attlist.clear()
                for idx in range(attribute_cnt):
                    dict2["trait_type"] = trait_type_list[idx]
                    dict2["value"] = value_list[idx]
                    attlist.append(copy.deepcopy(dict2))
                    dict2.clear
                dict["attributes"] = attlist
            
            # json file output
            outputpath = new_dir_path + '/' + str(num) + '.json'
            json_file = open(outputpath, mode='w',encoding='utf-8')
            json.dump(dict, json_file, indent=2, ensure_ascii=False)
            json_file.close()

            # If there are line breaks in the description, fix them appropriately!
            print(outputpath + " gnenerate.")

        var_output.set("Success Complete!")
    except:
        var_output.set("Exception error occurred!")

# Control -----------------------------------
# 1.No From and To
label_0_0 = tk.Label(root,text="#", font=("Yu Gothic", "10"))
label_0_1 = tk.Label(root,text="From", font=("Yu Gothic", "10"))
txt_0_0 = tk.Entry(width=8)
label_0_2 = tk.Label(root,text="To", font=("Yu Gothic", "10"))
txt_0_1 = tk.Entry(width=8)

#2.name
label_1_0 = tk.Label(root,text="name", font=("Yu Gothic", "10"))
txt_1_0 = tk.Entry(width=60,)

#3.description
label_2_0 = tk.Label(root,text="description", font=("Yu Gothic", "10"))
txt_2_0 = tk.Entry(width=60,)

#4.image
label_3_0 = tk.Label(root,text="image path", font=("Yu Gothic", "10"))
txt_3_0 = tk.Entry(width=60,)

#5. extension
radiovar = tk.IntVar()
radiovar.set(0) # default:value=0
rdo1 = tk.Radiobutton(root, value=0,variable=radiovar,command=chgradio,text='png')
rdo2 = tk.Radiobutton(root, value=1,variable=radiovar,command=chgradio,text='gif')
rdo3 = tk.Radiobutton(root, value=2,variable=radiovar,command=chgradio,text='other >')
rdo3_txt = tk.Entry(width=20,state="disable")

#6.attributes
label_4_0 = tk.Label(root,text="attributes", font=("Yu Gothic", "10"))
label_4_1 = tk.Label(root,text="trait_type", font=("Yu Gothic", "10"))
txt_4_0 = tk.Entry(width=40,)
label_4_2 = tk.Label(root,text="value", font=("Yu Gothic", "10"))
txt_4_1 = tk.Entry(width=40,)

btn_add = tk.Button(root, text='add',width = 5,bg = "White",command=AddAttribute)
btn_delete = tk.Button(root, text='delete',width = 5,bg = "White",command=DeleteAttribute)

text_area = scrolledtext.ScrolledText(root,wrap = tk.WORD,width = 30,height = 8,) 

# Go buttom!
btn_go = tk.Button(root, text='Make Now!',
width = 50,
height = 2,
bg = "White",
command=ExeOutput,
# state="disable"
)
var_output= tk.StringVar()
var_output.set("")
label_output = tk.Label(root, textvariable = var_output, font=("Yu Gothic", "12"),foreground='red')

# Close buttom
btn_close = tk.Button(root, text='Close',
width = 20,
height = 2,
bg = "White",
command = close_window
)

#parts design -----------------------------
start = 20
# 1.No From and To
label_0_0.place(x=20, y=start)
label_0_1.place(x=70, y=start)
txt_0_0.place(x=120, y=start)
label_0_2.place(x=190, y=start)
txt_0_1.place(x=220, y=start)
#2.name
label_1_0.place(x=20, y=start + 40)
txt_1_0.place(x=120, y=start + 40)
#3.description
label_2_0.place(x=20, y=start + 80)
txt_2_0.place(x=120, y=start + 80)
#4.image
label_3_0.place(x=20, y=start + 120)
txt_3_0.place(x=120, y=start + 120)

#5.extension
rdo1.place(x=120, y=start + 160)
rdo2.place(x=200, y=start + 160)
rdo3.place(x=280, y=start + 160)
rdo3_txt.place(x=350, y=start + 160)

#6.attributes
label_4_0.place(x=20, y=start + 200)
label_4_1.place(x=40, y=start + 240)
txt_4_0.place(x=120, y=start + 240)
label_4_2.place(x=40, y=start + 280)
txt_4_1.place(x=120, y=start + 280)

btn_add.place(x=120, y=start + 320)
btn_delete.place(x=220, y=start + 320)

text_area.place(x=120, y=start + 360)

# Go buttom!
btn_go.place(x=20, y=start + 500)
label_output.place(x=20, y=start + 580)
btn_close.place(x=325, y=580)

root.mainloop()
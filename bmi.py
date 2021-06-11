import os
from tkinter import *
import PIL.Image
import PIL.ImageTk
import pymongo
from tkinter.ttk import Combobox

client = pymongo.MongoClient("mongodb://localhost:27017")

mydb = client["BMI"]
mycol = mydb["bmi_details"]  # Creating a collection
dict={}


def id_number():
    id_number = str(id_num_enter.get())
    return id_number


def user_name():
    username = str(username_enter.get())
    return username


# def gender():
#     gender = str(v0.get())
#     return gender


def call_all():
    id_num = id_number()
    usernam = user_name()
    # gender = gender()
    height = get_height()
    weight = get_weight()
    # bmi = calBmi(BMI)

    mydict = {"id number": id_num, "username": usernam, "height": height, "weight": weight}
    print(mydict)

        # {"bmi": "bmi"}

    mycol.insert_one(mydict)


window= Tk()
# adding a widget label
lbl = Label(window, text="CALCULATE YOUR BMI ", fg='black', font=("Lucida Grande", 16))
lbl.place(x=300, y=56)
lbl.config(bg='#90EE90')

# adding an id_label
id_num_label = Label(window, text="Id Number", fg='black', font=("Lucida Grande", 12))
id_num_label.place(x=7, y=120)
id_num_label.config(bg='#90EE90')


# Adding an id  entry
id_num_enter = Entry(window, text="id number", bd=5, width=50)
id_num_enter.place(x=90, y=120)

# adding a username_label
username_label = Label(window, text="Full Name", fg='black', font=("Lucida Grande", 12))
username_label.place(x=7, y=170)
username_label.config(bg='#90EE90')


# Adding an username  entry
username_enter = Entry(window, text="Full name", bd=5, width=50)
username_enter.place(x=90, y=170)

# adding a height_label
height_label = Label(window, text="height", fg='black', font=("Lucida Grande", 12))
height_label.place(x=27, y=300)
height_label.config(bg='#90EE90')

# Adding an height  entry
height_enter = Entry(window, text="height", bd=5, width=50)
height_enter.place(x=80, y=300)

# adding a weight_label
weight_label = Label(window, text="weight", fg='black', font=("Lucida Grande", 12))
weight_label.place(x=25, y=350)
weight_label.config(bg='#90EE90')

# Adding an weight  entry
weight_enter = Entry(window, text="weight", bd=5, width=50)
weight_enter.place(x=80, y=350)

# text entry to display the BMI label
bmi_label = Label(window, text="Your BMI", fg='black', font=("lucida Grande", 12))
bmi_label.place(x=10, y=435)
bmi_label.config(bg='#107C10')

# text entry to display the BMI
bmi_dispaly = Entry(window, text="", bd=5, width=50)
bmi_dispaly.place(x=80, y=435)

# to display comment after BMI has been diplayed
txtfld = Text(window, width=35, height=20)
txtfld.place(x=410, y=115)
txtfld.config(bg='#808080')

# to display store info in a database
txtfld_db = Text(window, width=35, height=10)
txtfld_db.place(x=410, y=297)
txtfld_db.config(bg='#808080')


# get height
def get_height():
    try:
        height = float(height_enter.get())
        return height
        if height==0:
            raise ValueError(height)
    except ValueError:
       print(height, "you cannot enter a zero")



# get weight
def get_weight():
    try:
        weight = float(weight_enter.get())
        return weight
        if weight==0:
            raise ValueError(weight)
    except ValueError:
        print(weight, "you cannot enter a zero")


# Function to execute the statement
def calBmi(x):
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        BMI = weight / (height ** 2)
        bmi_dispaly.delete(0, 'end')
        bmi_dispaly.insert(END, BMI)
        txtfld.insert(END, bmi_comment(BMI))
        result = query_db_all()
        print(result)
        txtfld_db.insert(END, str(result) )
        return BMI
        if BMI==0:
            raise ValueError(BMI)
    except ValueError:
             print(BMI, "bmi cannot be equal to zero")
    except ZeroDivisionError:
        print("you can not divide by zero")

def query_db_all():
    res= mycol.find_one()
    return res

def bmi_comment(calc_bmi):
    txtfld.delete('1.0', 'end')
    if calc_bmi <= 18.4:
        comment = "You are underweight."
    elif calc_bmi <= 24.9:
        comment = "You are healthy."
    elif calc_bmi <= 29.9:
        comment = "You are over weight."
    elif calc_bmi <= 34.9:
        comment = "You are severely over weight."
    elif calc_bmi <= 39.9:
        comment = "You are obese."
    else:
        comment = "You are severely obese."
    return comment

# def insert_in_DB():
#      current_doc = list(users_data.find({}, sort=[('_id', pymongo.DESCENDING)]).limit(3))
#      data = dict(current_doc[0])
#      user_name = data["Username"]

     # users_data.update_one({"Username": user_name}, {"$set": {"BMI": BMI}})

v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text="MALE", variable=v0, value=1)
r2 = Radiobutton(window, text="FEMALE", variable=v0, value=2)
r3 = Radiobutton(window, text="OTHERS", variable=v0, value=3)
r1.place(x=100, y=250)
r2.place(x=180, y=250)
r3.place(x=260, y=250)
r1.config(bg='#107C10')
r2.config(bg='#107C10')
r3.config(bg='#107C10')


# this is the button label
btn = Button(window, text="Calculate", fg='black')
btn.bind('<Button-1>', calBmi)
btn.place(x=170, y=400)
btn.config(bg='#90EE90')

window.title('BMI CALCULATOR')

logo = PIL.Image.open('C:\\Users\\waruj\\Desktop\\best image 2.jpg')
logo = PIL.ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

window.resizable(width=False, height=False)
window.geometry("700x550+300+150")
window.configure(bg='#107C10')
window.mainloop()








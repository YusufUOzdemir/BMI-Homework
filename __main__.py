import tkinter
from tkinter import *

window=tkinter.Tk()
window.title("BMI Homework")

window.minsize(width=300, height=300)
label=tkinter.Label(text="BMI Calculator")
label.pack()
height_label=Label(text="Enter your height")
height_label.pack()
height=tkinter.Entry()
height.config(width=10)
height.pack()
weight_label=Label(text="Enter your weight")
weight_label.pack()
weight=tkinter.Entry()
weight.config(width=10)
weight.pack()
result_label=tkinter.Label(text="Your BMI score")
except_label=tkinter.Label(text="Make sure yourself enter values correctly")
def bc():
    try:
        h = int(height.get()) / 100
        w = int(weight.get())
        bmi = w / (h ** 2)
        result_text = f"BMI: {bmi:.2f}\n"
        if bmi<19.9:
            result_text+="You are underweight"
        elif 20<=bmi<24.9:
            result_text+="You are normalweight"
        elif 25<=bmi<29.9:
            result_text+="You are overweight"
        elif bmi>=30:
            result_text+="You are obese"
            result_label.config(text=result_text)
    except ValueError:
        except_label.pack()
result_label.pack()
calculate_button=tkinter.Button(text="Calculate your BMI",command=bc)
calculate_button.pack()
tkinter.mainloop()
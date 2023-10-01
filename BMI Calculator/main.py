from tkinter import *
root=Tk()
root.title("BMI CALCULATOR")
root.configure(bg="Grey")
#root.iconbitmap(r'favicon.ico')
def bmi(): 
	ans = float(txt.get())/(float (txt_2.get())*float(txt_2.get()))
	Label_2.config(text=ans)
	if(ans<18.5):
		Label_3.config(text="UNDERWEIGHT")
	elif(ans<24.9):
		Label_3.config(text="NORMAL WEIGHT")
	else:
		Label_3.config(text="OVER WEIGHT")
Label_1=Label(root, text="WEIGHT(in KGs): ").pack()
txt=Entry(root, text="")
txt.pack()
Label_1=Label(root, text="HEIGHT(in Metres): ").pack()
txt_2=Entry(root, text="")
txt_2.pack()
butt=Button(root, text="CALCULATE",bg="Silver",command=bmi).pack()
Label_2=Label(root, text="RESULT:")
Label_2.pack()
Label_3=Label(root, text="CATEGORY")
Label_3.pack()
root.mainloop()
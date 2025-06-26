from tkinter import *

def createSlider(txt,n) :
    label= Label(root, text= txt, 
                 font=("Helvetica", 18, "bold"), 
                 bg="#001C20", fg="white")
    label.grid(row=n, column=0, padx=15, pady=10)

    value = DoubleVar()
    slider= Scale(root, from_=0.0, to=10.0, resolution= 0.1,
                  orient = HORIZONTAL, length=400,
                  font=("Arial", 16, "bold"),
                  troughcolor="#03C0DE", bg="#001C20", fg="#FFFFFF",
                  variable=value)
    slider.grid(row=n, column=1, padx=15, pady=10)

    return value

def prt():
    print(f"Kp= {Kp.get()}, Ki= {Ki.get()}, Kd= {Kd.get()}")

root = Tk()
root.title("Constant Value Selector for PID")
root.geometry("720x480")
root.configure(bg="#001C20")

Kp = createSlider("Kp Value: ",0)
Ki = createSlider("Ki Value: ",1)
Kd = createSlider("Kd Value: ",2)

Button(root, text="Set Value", command=prt).grid(row=3, column=1, padx=15, pady=10)

root.mainloop()

"""
Chương trình giám sát và điều khiển hoạt động của smart farm trong môi trường nhà kính
"""

from serial import Serial
import time
import tkinter


def quit():
    global SmartFarm_01
    ser.write(bytes('L', 'UTF-8'))
    SmartFarm_01.destroy() # đóng cổng giao diện

def set_button1_state(): # nút kích mở đèn || có thể chuyển sang ứng dụng khác 
        varLabel.set("LED ON ")
        ser.write(bytes('H', 'UTF-8'))

def set_button2_state():
        varLabel.set("LED OFF")
        ser.write(bytes('L', 'UTF-8'))

ser = Serial('COM5', baudrate=9600)
print("Reset Arduino")
time.sleep(3)
ser.write(bytes('L', 'UTF-8'))

SmartFarm_01 = tkinter.Tk()
SmartFarm_01.minsize(600,600)
SmartFarm_01.geometry("600x600")
SmartFarm_01.title("HQ Smart Farm")
label3 = tkinter.Label(text = 'Building Python GUI to interface an arduino,'
                      '\n and control an LED',font=("Courier", 12,'bold')).pack()
tkTop.counter = 0
b = tkTop.counter

varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack()

varLabel2 = tkinter.IntVar()
tkLabel2 = tkinter.Label(textvariable=varLabel2, )
tkLabel2.pack()

button1 = tkinter.IntVar()
button1state = tkinter.Button(tkTop,text="ON",command=set_button1_state,height = 4,fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button1state.pack(side='top', ipadx=10, padx=10, pady=15)

button2 = tkinter.IntVar()
button2state = tkinter.Button(tkTop,
    text="OFF",
    command=set_button2_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5
)
button2state.pack(side='top', ipadx=10, padx=10, pady=15)

tkButtonQuit = tkinter.Button(
    tkTop,
    text="Quit",
    command=quit,
    height = 4,
    fg = "black",
    width = 8,
    bg = 'yellow',
    bd = 5
)
tkButtonQuit.pack(side='top', ipadx=10, padx=10, pady=15)

tkinter.mainloop()
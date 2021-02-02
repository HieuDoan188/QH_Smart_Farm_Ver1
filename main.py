"""
Chương trình giám sát và điều khiển hoạt động của smart farm trong môi trường nhà kính
"""

from serial import Serial
import time
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql


# connect tới DB - mySQL
mypass = ""
mydatabase = "SmartFarm"

con = pymysql.connect(host = "localhost", user = "root", port = 3308, password = mypass, database = mydatabase)
cur = con.cursor() 

# thay đổi sang port đang chạy - từ từ xài
# device = '/dev/tty.usbmodem1411' 
# try:
#   print "Trying...",device 
#   arduino = serial.Serial(device, 9600) 
# except: 
#   print "Failed to connect on",device    

# arduino = Serial.Serial("COM5", baudrate = 9600)
# try: 
#   data = arduino.readline()  #read the data from the arduino
#   pieces = data.split("\t")  #split the data by the tab
#   #Here we are going to insert the data into the Database
#   try:
#     cur.execute("INSERT INTO house1 (TEMP) VALUES (%s)", (pieces[0]))
#     con.commit() #commit the insert
#     cur.close()  #close the cursor
#   except MySQLdb.IntegrityError:
#     print "failed to insert data"
#   finally:
#     cursor.close()  #close just incase it failed
# except:
#   print "Failed to get data from Arduino!"

arduino = Serial("COM5", baudrate = 9600)
data = arduino.readline()  #read the data from the arduino
#Here we are going to insert the data into the Database
cur.execute("INSERT INTO house1 (TEMP) VALUES (%s);" %data)
con.commit() #commit the insert
cur.close()  #close the cursor

# hàm sử dụng để truyền tín hiệu về arduino
def quit():
    global SmartFarm_01
    ser.write(bytes('L', 'UTF-8'))
    SmartFarm_01.destroy() # đóng cổng giao diện

def set_buttonLED_ON(): # nút kích mở đèn || có thể chuyển sang ứng dụng khác 
    varLabel.set("LED ON ")
    ser.write(bytes('H', 'UTF-8'))

def set_buttonLED_OFF():
    varLabel.set("LED OFF")
    ser.write(bytes('L', 'UTF-8'))

# mở cổng com và kết nối UART với arduino
# ser = Serial('COM5', baudrate=9600)
print("Reset Arduino")
time.sleep(3)
arduino.write(bytes('L', 'UTF-8')) # mặc định kết nối là đèn tắt

# khởi tạo giao diện
SmartFarm_01 = Tk()
SmartFarm_01.minsize(600,600)
SmartFarm_01.geometry("600x600")
SmartFarm_01.title("HQ Smart Farm")
label3 = Label(text = 'CHƯƠNG TRÌNH QUẢN LÝ NÔNG VỤ',font=("Courier", 10,'bold')).pack()

# on/ off đèn 
varLabel = IntVar() # khởi tạo label dạng Int
tkLabel = Label(textvariable=varLabel,)
tkLabel.pack()

button1 = IntVar()
button1state = Button(SmartFarm_01,text="ON",command=set_buttonLED_ON,height = 4,fg = "black",
    width = 8,bd = 5,activebackground='green')
button1state.pack(side='left', ipadx=0, padx=10, pady=15)

button2 = IntVar()
button2state = Button(SmartFarm_01,text="OFF",command=set_buttonLED_OFF,height = 4,fg = "black",
    width = 8,bd = 5)
button2state.pack(side='left', ipadx=10, padx=10, pady=15)

tkButtonQuit = Button(SmartFarm_01,text="Quit",command=quit,height = 4,fg = "black",width = 8,
    bg = 'yellow',bd = 5)
tkButtonQuit.pack(side='bottom', ipadx=10, padx=10, pady=15)

mainloop()
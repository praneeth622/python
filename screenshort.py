import tkinter as tk
import pyautogui

root= tk.Tk()

size1 = tk.Canvas(root, width = 300, height =300)
size1.pack()

def takesnap():

      screenshot = pyautogui.screenshot()
      screenshot.save(r'F:\\Srinivas\\Documents\\Praneeth\\Python Files\\Python\\trail.png')

Button1 = tk.Button(text='Take snapshort', command=takesnap , bg='green', fg='orange', font=10 )
size1.create_window(150, 150, window=Button1)

root.mainloop()


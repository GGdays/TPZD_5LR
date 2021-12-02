from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import numpy as np
import math

global path_image

image_display_size = 400, 250

def on_click():
    global path_image
    path_image = filedialog.askopenfilename()
    load_image = Image.open(path_image)
    load_image.thumbnail(image_display_size, Image.ANTIALIAS)
    np_load_image = np.asarray(load_image)
    np_load_image = Image.fromarray(np.uint8(np_load_image))
    render = ImageTk.PhotoImage(np_load_image)
    img = Label(app, image=render)
    img.image = render
    img.place(x=20, y=50)

def encrypt_data_into_image():
    global path_image
    data = txt.get(1.0, "end-1c")
    img = cv2.imread(path_image)
    data = [format(ord(i), '08b') for i in data]
    _, width, _ = img.shape
    PixReq = len(data) * 3

    RowReq = PixReq/width
    RowReq = math.ceil(RowReq)

    count = 0
    charCount = 0
    for i in range(RowReq + 1):
        while(count < width and charCount < len(data)):
            char = data[charCount]
            charCount += 1
            for index_k, k in enumerate(char):
                if((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                    img[i][count][index_k % 3] -= 1
                if(index_k % 3 == 2):
                    count += 1
                if(index_k == 7):
                    if(charCount*3 < PixReq and img[i][count][2] % 2 == 1):
                        img[i][count][2] -= 1
                    if(charCount*3 >= PixReq and img[i][count][2] % 2 == 0):
                        img[i][count][2] -= 1
                    count += 1
        count = 0
    cv2.imwrite("encryptedImg.png", img)
    success_label = Label(app, text="Encryption completed successfully.",
                bg='lightsteelblue', font=("Times New Roman", 14))
    success_label.place(x=200, y=400)

app = Tk()
app.configure(background='darkslategray')
app.title("Encryption - LR4 _ Bondarenko Stephanie")
app.geometry('600x500')
on_click_button = Button(app, text="СHOOSE IMG", bg='white', fg='black', command=on_click)
on_click_button.place(x=250, y=10)
txt = Text(app, wrap=WORD, width=30)
txt.place(x=340, y=55, height=165)

encrypt_button = Button(app, text="ENCODE", bg='white', fg='black', command=encrypt_data_into_image)
encrypt_button.place(x=435, y=230)
app.mainloop()
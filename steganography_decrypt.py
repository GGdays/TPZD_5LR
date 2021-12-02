import cv2
from tkinter import filedialog, Tk, Button, Label
from PIL import Image, ImageTk
import numpy as np

image_display_size = 500, 350


def decrypt():
    load = Image.open("./encryptedImg.png")
    load.thumbnail(image_display_size, Image.ANTIALIAS)
    load = np.asarray(load)
    load = Image.fromarray(np.uint8(load))
    render = ImageTk.PhotoImage(load)
    img = Label(app, image=render)
    img.image = render
    img.place(x=100, y=50)

    img = cv2.imread("./encryptedImg.png")
    data = []
    stop = False
    for index_i, i in enumerate(img):
        i.tolist()
        for index_j, j in enumerate(i):
            if((index_j) % 3 == 2):
                data.append(bin(j[0])[-1])
                data.append(bin(j[1])[-1])
                if(bin(j[2])[-1] == '1'):
                    stop = True
                    break
            else:
                data.append(bin(j[0])[-1])
                data.append(bin(j[1])[-1])
                data.append(bin(j[2])[-1])
        if(stop):
            break

    message = []
    for i in range(int((len(data)+1)/8)):
        message.append(data[i*8:(i*8+8)])
    message = [chr(int(''.join(i), 2)) for i in message]
    message = ''.join(message)
    message_label = Label(app, text=message, bg='lightsteelblue', font=("Times New Roman", 14))
    message_label.place(x=30, y=400)

app = Tk()
app.configure(background='darkslategray')
app.title("Decryption - LR4 _ Bondarenko Stephanie")
app.geometry('600x600')
main_button = Button(app, text="DECRYPT IMG", bg='white', fg='black', command=decrypt)
main_button.place(x=250, y=10)
app.mainloop()
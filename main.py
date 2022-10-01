from tkinter import *
import tkinter.font as font
import cv2



def video_player():
    cap = cv2.VideoCapture("test_vid.mp4")
    while (cap.isOpened()):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (256, 256))
        cv2.imshow("frame",frame)
        if cv2.waitKey(25) == 27:
            break    
    

window = Tk(className="Space frontier")

window.geometry("700x800")
window.configure(bg="#0f0a1f")
window.resizable(False, False)

my_font = font.Font(family='Overstrike')

button = Button(window, text="Show video №1", command= video_player, bg= "#27076e", fg= "#e3c8dd",
 activebackground="#e35117", activeforeground="#2b0370", font=my_font, height= 3, width= 17 )

button_two = Button(window, text="Show video №2", command= video_player, bg= "#27076e", fg= "#e3c8dd",
 activebackground="#e35117", activeforeground="#2b0370", font=my_font, height= 3, width= 17 )

button.place(relx=0.5, rely=0.6, anchor=CENTER)
button_two.place(relx=0.5, rely=0.72, anchor=CENTER)

window.mainloop()

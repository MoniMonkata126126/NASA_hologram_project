from tkinter import *
import tkinter.font as font
import cv2
#from pyramid_editor import make_pyramid_video

def video_player():
    cap = cv2.VideoCapture("Solar Flare Explanations.mp4")
    while (cap.isOpened()):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (600, 600))
        cv2.imshow("frame",frame)
        if cv2.waitKey(25) == 27:
            break    
        
def api_video_player():
    #make_pyramid_video()
    cap = cv2.VideoCapture("Latest Solar Flare.mp4")
    while (cap.isOpened()):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (600, 600))
        cv2.imshow("frame",frame)
        if cv2.waitKey(25) == 27:
            break    
    

window = Tk(className="Space frontier")

window.geometry("700x800")
window.configure(bg="#0f0a1f")
window.resizable(False, False)

my_font = font.Font(family='Overstrike')

my_label = Label(window, text = 'Hologram Visualization of the Solar Flare', bg= "#27076e", fg= "#e3c8dd", font=my_font, height= 5, width= 35)
my_label.pack(side = TOP)

button = Button(window, text="Show Solar Flare", command= video_player, bg= "#27076e", fg= "#e3c8dd",
 activebackground="#15e5e8", activeforeground="#090124", font=my_font, height= 3, width= 17 )

button_two = Button(window, text="Latest Solar Flare", command= api_video_player, bg= "#27076e", fg= "#e3c8dd",
 activebackground="#15e5e8", activeforeground="#090124", font=my_font, height= 3, width= 17 )

button.place(relx=0.5, rely=0.6, anchor=CENTER)
button_two.place(relx=0.5, rely=0.72, anchor=CENTER)

window.mainloop()
# Use the Tkinter library to create GUI
from Tkinter import *
#Set up a GUI called window.


#What the button does
def start():
    pass


window = Tk()
window.title("WorldMap")
canvas = Canvas(width = 700, height = 350, bg = 'black')
canvas.pack(expand = YES, fill = BOTH)
gif1 = PhotoImage(file = 'worldmap3.gif')
canvas.create_image(80, 20, image = gif1, anchor = NW)

root = Tk()
frame = Frame(root)
frame.pack()

startbutton = Button(frame, text="Start", fg="green")
startbutton.pack(side = TOP )
quitbutton = Button(frame, text="Quit", fg="red")
quitbutton.pack(side = BOTTOM )
item1button = Button(frame, text="Item1", fg="black")
item1button.pack(side = BOTTOM )
item2button = Button(frame, text="Item2", fg="black")
item2button.pack(side = BOTTOM )
item3button =  Button(frame, text="Item3", fg="black")
item3button.pack(side = BOTTOM )




mainloop()

Items=['item1','item2','item3','item4','item5']

def linearSearch(item?,Items):
    Found = False
    position = 0
    while position<lens(Items) and not found:
        if Items[position] == myitem:
            found  = True
         position = position +1
         return found

if __name__=="__main__":
     = ("item1","item2","item3","item4","item5")
    
        
        























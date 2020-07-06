# Python program to illustrate a stop watch  
#importing the required libraries  
import tkinter as Tkinter  
from datetime import datetime 
import time
counter = 0
running = False

def counter_label(label):  
    def count():  
        if running:  
            global counter  
            
            # To manage the intial delay.  
            if counter==0:              
                time.sleep(1)
                display="GO"
            else: 
                tt = datetime.fromtimestamp(counter) 
                string = tt.strftime("%M:%S") 
                display=string  
    
            label['text']=display   #
            label.after(1000, count)   
            counter += 1
    
    # Triggering the start of the counter.  
    count()       
    
# start function of the stopwatch  
def Start(label):  
    global running  
    running=True
    counter_label(label)  
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
    
# Stop function of the stopwatch  
def Stop():  
    global running  
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
    
# Reset function of the stopwatch  
def Reset(label):  
    global counter  
    counter=0
    
    # If rest is pressed after pressing stop.  
    if running==False:        
        reset['state']='disabled'
        label['text']='Welcome!'
    
    # If reset is pressed while the stopwatch is running.  
    else:                 
        label['text']='GET READY!'
    
root = Tkinter.Tk()  
root.title("Stopwatch")  
    
# Fixing the window size. 
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown)) 
root.minsize(width=300, height=70)  

#Deal with the design
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")  
label.pack()  
f = Tkinter.Frame(root) 
start = Tkinter.Button(f, background="yellow", text='Start', fg="green", font="Times 16", width=6, command=lambda:Start(label))  
stop = Tkinter.Button(f, background="grey", text='Stop',fg="red", font="Times 16", width=6,state='disabled', command=Stop)  
reset = Tkinter.Button(f, background="green", text='Reset',fg="blue", font="Times 16",width=6, state='disabled', command=lambda:Reset(label))  
f.pack(anchor = 'center',pady=5) 
start.pack(side="left")  
stop.pack(side ="left")  
reset.pack(side="left")  
root.mainloop() 
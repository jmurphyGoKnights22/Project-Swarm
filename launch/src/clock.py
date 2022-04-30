# TKinter Clock To Keep Track Of How Long Search Takes
# Python program to illustrate a stop watch
# using Tkinter
#importing the required libraries
import tkinter as Tkinter
from datetime import datetime
import time
import threading

counter = 0
running = False
def counter_label(label):
    def count():
        if running:
            global counter
   
            # To manage the initial delay.
            if counter==0:            
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%M:%S")
                display=string
   
            label['text']=display   # Or label.config(text=display)
   
            # label.after(arg1, arg2) delays by 
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the 
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count) 
            counter += 1
   
    # Triggering the start of the counter.
    count()     
   
# start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)

   
# Stop function of the stopwatch
def Stop():
    global running
    running = False
   
# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=66600
   
    # If rest is pressed after pressing stop.
    if running==False:      
        label['text']='Welcome!'
   
    # If reset is pressed while the stopwatch is running.
    else:               
        label['text']='Starting...'


def Detect_Object():
    time.sleep(15)
    Stop()
    #label['text']='Ladies and Gentlemen, we got him.'


# Test Object Detection Function To 

root = Tkinter.Tk()
root.title("Swarm Search Timer")
   
# Fixing the window size.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
f = Tkinter.Frame(root)
f.pack(anchor = 'center',pady=5)

# Create 2 threads to navigate and detect objects simultaneously        
object_detection_thread = threading.Thread(target=Detect_Object)

# Start the threads
object_detection_thread.start()

Start(label) 
root.mainloop()


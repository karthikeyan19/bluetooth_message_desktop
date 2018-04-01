# This project requires PyBluez
from tkinter import *
import bluetooth
from tkinter import messagebox

#Look for all Bluetooth devices
#the computer knows about.
print( "Searching for devices...")
#Create an array with all the MAC
#addresses of the detected devices
nearby_devices = bluetooth.discover_devices()
#Run through all the devices found and list their name
num = 0
print ("Select your device by entering its coresponding number...")
for i in nearby_devices:
	num+=1
	print (num , ": " , bluetooth.lookup_name( i ))

#Allow the user to select their Arduino
#bluetooth module. They must have paired
#it before hand.
selection = int(input("> "))-1
print ("You have selected", bluetooth.lookup_name(nearby_devices[selection]))
bd_addr = nearby_devices[selection]

port = 1

#Create the GUI
class Application(Frame):

#Create a connection to the socket for Bluetooth
#communication
    sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    def disconnect(self):
    	#Close socket connection to device
        self.sock.close()
        messagebox.showinfo("Device Status","Disconnected")
        
    def getvalue(self):
        return mystring.get()    

    def client_exit(self):
        exit()
    def send(self):
        msg = self.getvalue()
        if msg == '':
               messagebox.showerror('Error','Message is empty')
        print(msg)
        try:
                self.sock.send(msg)
        except:
                messagebox.showerror('Error in Sending','Error in sending Message')
    def createWidgets(self):
        Label(self,text="Enter the Message").grid(row=0,column=2,padx=5,pady=5)  #label
        Entry(self,textvariable = mystring).grid(row=0, column=3) #entry textbox

        send = Button(self, text="send", command=self.send,justify=CENTER).grid(row=1, column=2,columnspan=2,padx=5,pady=5) #button
        disconnectButton = Button(self, text="Disconnect", command=self.disconnect).grid(row=0, column=0, sticky=W,padx=5,pady=5,columnspan=2) #button
        disconnectButton = Button(self, text="connect", command=self.connect).grid(row=1, column=0, sticky=W,padx=5,pady=5,columnspan=2) #button
        QuitButton = Button(self, text="QUIT", command=self.client_exit).grid(row=2, column=0, sticky=W,padx=5,pady=5,columnspan=2) #button
    def connect(self):
        try:
                self.sock.connect((bd_addr, port))
                messagebox.showinfo("Device Status","Connected")
        except:
                messagebox.showerror('Error in Sending','Error in sending Message')
               
    def __init__(self, master=None):
    	#Connect to the bluetooth device
    	#and initialize the GUI
        Frame.__init__(self, master)
        self.pack()
        self.grid()
        self.createWidgets()
        self.connect()
        
#Begin the GUI processing
root = Tk()
mystring=StringVar()
app = Application(master=root)
root.geometry("400x200")
root.title('Bluetooth Communication')
app.mainloop()
root.destroy()

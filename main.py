import os
import numpy
from vsm import createVSM, loadVSM, processQuery
from tkinter import *


map = {}
qmap= {}
doc = {}

if os.path.isfile("vsm.txt"):
    map, idf = loadVSM()
else:
    map,idf = createVSM()



def srch():
    result.delete('1.0', END)
    query = txtbar.get()
    if(txtbar.get() != ""):
        cos,x = processQuery(query, map, idf)
        if  x == 1:
            a = numpy.argsort(cos)

            x =0;
            for i in range(49,-1,-1):
                if cos[a[i]] > 0.05:
                    result.insert(END, str(a[i]+1) + " - " + str(cos[a[i]]) + "\n")
                    #print(str(a[i]+1) + " - " + str(cos[a[i]]))
                    x = x+1
            result.insert(END, str(x))
            result.insert(END, " Documents Retrieved")
            #print(str(x) + " Documents Retrieved")

        else:
            result.insert(END, "No Document Found")

root = Tk()
label1 = Label(root, text="Vector Space Model\n", width=500,font="18",bg="black",fg= "white")
label1.pack(side=TOP)
txtbar = Entry(root, width=30)
txtbar.pack()
root.title("VSM")
root.geometry("500x400")
root.configure(background="black")
label2 = Label(root, bg="black")
label2.pack()
btn = Button(root, text="Search", bg="red", fg="white", command=srch,width= 15)
btn.pack()
label3 = Label(root, bg="black")
label3.pack()
label3 = Label(root, bg="black",fg= "white",text="Result",font="18")
label3.pack(side=LEFT)
result = Text(root, width=50, height=50)
result.pack(side=BOTTOM)
root.mainloop()






#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import calender

n= int(input("Enter the year"))
text = calender.calender(n)
root = Tk()
root.geometry("550x600")
root.title("CALENDER")
label1 = Label(root,text="CALENDER",bg ='dark gray', font=("consolas",28,'bold'))
label1.grid(row=1,column=1)
root.config(background="white")
l1=Label(root,text=text,font=("consolas",10,'bold'))
l1.grid(row=2,column=1,padx=10)
root.mainloop()




# In[ ]:





# In[ ]:





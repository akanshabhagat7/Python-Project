#!/usr/bin/env python
# coding: utf-8

# # Final Project : GUI weather update using tkinter and python
# 
# ## Name - Akansha Bhagat

# In[7]:


import requests
from tkinter import *
from PIL import Image, ImageTk
import datetime as dt


# In[8]:


def weather():
    city = city_listbox.get()
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=83831e36a113e46a28adca59c21ceabc".format(city)
    #https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=83831e36a113e46a28adca59c21ceabc
    res = requests.get(url)
    output = res.json()
    
    weather_status = output['weather'][0]['description']
    temprature = output['main']['temp']
    pressure = output['main']['pressure']
    humidity = output['main']['humidity']
    wind_speed = output['wind']['speed']
    visibility = output['visibility']
    
    weather_status_label.configure(text="Weather Status : "+ weather_status)
    temprature_label.configure(text="Temprature : "+ str(temprature)+" °C")
    pressure_label.configure(text="Pressure : "+ str(pressure))
    humidity_label.configure(text="Humidity : "+ str(humidity)+" %")
    wind_speed_label.configure(text="Wind Speed : "+ str(wind_speed))
    visibility_label.configure(text="Visibility : "+ str(visibility)+" Km")


# In[9]:


window = Tk()
window.title("Weather Update")
window.geometry("600x450")
#window.configure(bg='lightpink')

date = dt.datetime.now()
label = Label(window, text=f"{date:%B %d, %Y}", font="Calibri, 10")
label.grid(pady=20)

#bg = PhotoImage(file = "image7.png")
#label1 = Label(window, image = bg)
#label1.place(x=0, y=0)


city_name_list = ["Lucknow","Delhi","Bangalore","Pune","Mumbai","Hyderabad","Chennai","Nagpur","Maharashtra","Bengaluru","Kolkata","Surat","Jaipur","Surat","Agra","Nashik","Indore"]

city_listbox = StringVar(window)
city_listbox.set("Select the City")
option = OptionMenu(window,city_listbox,*city_name_list)
option.grid(row=2,column=2,padx=150,pady=10)

b1 = Button(window,text="Check Weather",width=15,command=weather)
b1.grid(row=5,column=2,padx=150)

weather_status_label = Label(window,font=("times",15,"bold"))
weather_status_label.grid(row=10,column=2)

temprature_label = Label(window,font=("times",15,"bold"))
temprature_label.grid(row=12,column=2)

pressure_label = Label(window,font=("times",15,"bold"))
pressure_label.grid(row=14,column=2)

humidity_label = Label(window,font=("times",15,"bold"))
humidity_label.grid(row=16,column=2)

wind_speed_label = Label(window,font=("times",15,"bold"))
wind_speed_label.grid(row=18,column=2)

visibility_label = Label(window,font=("times",15,"bold"))
visibility_label.grid(row=20,column=2)

window.mainloop()


# In[ ]:


"""

How to use the project - 
click on "Select the City" button 
select the city of your choice from drop dowm list
click on "Check weather"
The output about the weather update of the city will be displayed.

"""


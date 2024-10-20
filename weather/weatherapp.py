
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim 
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root =Tk()
icon_image=PhotoImage(file="cloudy.png")
root.iconphoto(False,icon_image)
root.title("weather app")
root.geometry("900x500+200+100")
root.resizable(False,False)

def getweather():
    try:
        city=textfeild.get()

        geolocator = Nominatim(user_agent="geoapiExercise")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        Current_time=local_time.strftime("%I :%M %p")
        clock.config(text=Current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b4834fea774e9a80e918996f47dab300"


        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,",""FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("weather app","invalid entry!!")
    

#search box
search_image=PhotoImage(file="bar.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)

textfeild=tk.Entry(root,justify="center",width=20,font=("poppins",24,"bold"),bg="#404040",border=0,fg="white")
textfeild.place(x=50,y=40)
textfeild.focus()

search_icon=PhotoImage(file="Copy of search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=400,y=34)

#logo
logo_image=PhotoImage(file="Copy of logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#bottom box
Frame_image=PhotoImage(file="image for weather.png")
Frame_myimage=Label(image=Frame_image)
Frame_myimage.pack(padx=6,pady=6,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
Label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label1.place(x=120,y=400)
Label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label2.place(x=250,y=400)
Label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label3.place(x=430,y=400)
Label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#1ab5ef")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()
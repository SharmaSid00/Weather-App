from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title("Icon")
root.iconbitmap('C:/Users/Sudhanshu/PycharmProjects/GUI/tulips___copy_Tev_icon.ico')
root.geometry('220x60')

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=C8084FF6-DB74-4852-95AB-7FB9537856F7
#Create Function
def ziplookup():
    try:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipcode.get() +"&distance=25&API_KEY=C8084FF6-DB74-4852-95AB-7FB9537856F7")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']
        if category == "Good":
            weather_color = '#0C0'
        elif category == 'Moderate':
            weather_color = '#FFFF00'
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = '#FF9900'
        elif category  == 'Unhealthy':
            weather_color = '#FF0000'
        elif category == 'Very Unhealthy':
            weather_color = '#990066'
        elif category == 'Hazardous':
            weather_color = '#660000'
        root.configure(background=weather_color)
        my_Label = Label(root, text=city + "Air Quality " + str(quality) + " " + category, font=('Helvetica', 10),background=weather_color)
        my_Label.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error...."

zipcode=Entry(root)
zipcode.grid(row=0,column=0,stick=W+E+S+N)
zip_btn= Button(root,text='SUBMIT CODE',background='red',command=ziplookup).grid(row=0,column=1,stick=W+E+S+N)

root.mainloop()
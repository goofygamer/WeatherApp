import tkinter as tk
import requests
import time

API_KEY = "8ebd807426f3e2547b479fa7f4048257"
def getWeather(canvas):
    city = textfield.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    #outputted in Kelvin
    temperature = int(json_data['main']['temp'] - 273.15)
    min_temperature = int(json_data['main']['temp_min'] - 273.15)
    max_temperature = int(json_data['main']['temp_min'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info =  condition + "\n" + str(temperature) + "°C"
    final_data = "\n" + "Max Temperature: " + str(max_temperature)\
         + "\n" + "Min Temperature: " + str(min_temperature)\
         + "\n" + " Pressure: " + str(pressure)\
         + "\n" + "Humidity: " + str(humidity)\
         + "\n" + "Wind Speed: " + str(wind)\
         + "\n" + "Sunrise: " + sunrise\
         + "\n" + "Sunset: " + sunset
    
    label1.config(text = final_info)
    label2.config(text = final_data)





canvas = tk.Tk()
canvas.title("Weather App")
canvas.geometry("1000x700")

f = ("Bell MT", 15, "bold")
t = ("Bell MT", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = t)
label2.pack()

canvas.mainloop()


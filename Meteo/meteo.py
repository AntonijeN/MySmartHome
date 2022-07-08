

import requests
import xmltodict
import random as rd


url = "https://vrijeme.hr/hrvatska_n.xml"

response = requests.get(url)

data = xmltodict.parse(response.content)


class Podaci:
    def __init__(self, temperature, moisture, air_pressure):
        self.temperature = temperature
        self.moisture = moisture
        self.air_pressure = air_pressure

    
    def get_temperature(self, city_index):

        city = data["Hrvatska"]["Grad"][city_index]["GradIme"]
        temp = data["Hrvatska"]["Grad"][city_index]["Podatci"]["Temp"]

        print(f"Temperatura zraka za grad {city} je {temp} °C ")

      
    def get_moisture(self, city_index):

        city =data["Hrvatska"]["Grad"][city_index]["GradIme"]
        moisture = data["Hrvatska"]["Grad"][city_index]["Podatci"]["Vlaga"]

        print(f"Relativna vlažnost zraka za grad {city} je {moisture} % ")


    def get_air_pressure(self, city_index):

        city = data["Hrvatska"]["Grad"][city_index]["GradIme"] 
        air_pressure = data["Hrvatska"]["Grad"][city_index]["Podatci"]["Tlak"]

        print(f"Tlak zraka za grad {city} je {air_pressure} hPA ")


    def get_random_temperature(self):
        random_temperature = round(rd.uniform(12.5, 32.5), 2)
        print(f"Temperatura zraka je: {random_temperature} °C")
        return random_temperature

    def get_random_moisture(self):
        random_moisture = rd.randint(0, 99)
        print(f"Relativna vlažnost zraka je: {random_moisture} %")
        return random_moisture

    def get_random_air_pressure(self):
        random_air_pressure = round(rd.uniform(780, 1100), 2)
        print(f"Tlak zraka je: {random_air_pressure} hPA")
        return random_air_pressure

    def clothes_icon_show(self, random_temperature):
        if random_temperature < 22:
            print("Kratki rukavi")
        elif (random_temperature <= 22) and (random_temperature >= 12):
            print ("Lagana jakna")
        elif (random_temperature >= 0) and (random_temperature < 12):
            print("Zimska jakna")
        else:
            print("Kapa, šal i zimska jakna")


podaci = Podaci(18, 29, 1020)

podaci.get_random_temperature()
podaci.get_random_moisture()
podaci.get_random_air_pressure()
podaci.get_temperature(2)
podaci.get_moisture(2)
podaci.get_air_pressure(2)

podaci.clothes_icon_show(rd.randint(0,40))
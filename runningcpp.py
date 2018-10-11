import subprocess
import os
import requests 

#take same vin but dist + 1
response = requests.get("http://localhost:3000/api/services/1/1/1")
res = response.content
dat = res.decode("utf-8") 
print(dat)
array = dat.split(",")
str = array[3]
print(str)
array = str.split(":")
str = array[1]
print(str)
array = str.split(",")
z = array[0]
z = z[1]
print(z)
#z= int(z)
command = ("C:\Users\imj\Source\Repos\win_trial\Debug\win_trial.exe " + z)
print(command)
p = subprocess.call(command.split())
c = "3"
print("\n")
print("m")
print(p)
print("m")
response = requests.post("http://localhost:3000/api/services/1/1/1/" + c)
import os
import subprocess


for f_name in os.listdir('./'):
     if f_name.endswith('.jpg'):
         print(f_name)
         command = "convert " + f_name + " -resize 500x500\! " + "versa_300x300" + f_name
         subprocess.call(command, shell=True)


import os
import subprocess


count = 1
finish_flag = False
timestamplist = []
timestampdic = {}
for f_name in os.listdir('./input/'):
     if f_name.endswith('.png'):
         path = "./input/" + f_name
         print(path)
         timestamp  = os.path.getmtime(path)
         timestamplist.append(timestamp)
         timestampdic[timestamp] = path


print(timestamplist)
timestamplist.sort()
print("SORTED")

print(timestamplist)
print(timestampdic)

for x in timestamplist:
  filename = timestampdic[x]
  print(filename)
  source = filename
  dest = "./output/" + str(count) + ".png"
  os.rename(source, dest)  
  count = count + 1
  
finish_flag = True
if finish_flag:
  finish_flag = False
  subprocess.call("apngasm ./complete/output.png ./output/*.png 3 4", shell=True)
  finish_flag = True

if finish_flag:
  finish_flag = False
  subprocess.call("rm ./output/*.png", shell=True)
  finish_flag = True

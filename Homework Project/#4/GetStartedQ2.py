import os
import csv

mylist = os.listdir("crop_part1")
print(mylist)
with open("my_list.txt", "w") as file:
    for item in mylist:
        file.write("%s\n" % item)

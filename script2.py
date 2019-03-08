#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import csv
import io

filne = "output.txt"
list_final = []


with open(filne,'r+') as f:
    data = f.readlines()
    for i,line in enumerate(data):
        if line.startswith("નામ :") and data[i+1] != "\n":
            list_temp = []
            list_temp.append(line)
            i+=1
            list_temp.append(data[i])
            i+=1
            list_temp.append(data[i])
            i+=1
            if(data[i].startswith("ંજી") or data[i].startswith("ંજદાન") or data[i].startswith("જી\n") or data[i].startswith("જી") or data[i].startswith("ંજાજી")):
                i+=1
                list_temp.append(data[i])
            else:
                list_temp.append(data[i])
            i+=1
            list_temp.append(data[i])

      
            if (list_temp[1] == 'િપતાનુ\n' or list_temp[1] == 'પિતનુ\n' or list_temp[1]=='માતાનુ\n' or list_temp[1]=="સંબંધીનુ\n") and list_temp[2].startswith("ં નામ"):
                list_temp[1] = list_temp[1].strip("\n") + list_temp[2].strip("\n")
                list_temp[2] = list_temp[3]
                field_splitter  = list_temp[4].split("જાિત")
                list_temp[3] = field_splitter[0]
                list_temp[4] = field_splitter[1]
            elif (list_temp[1].startswith('િપતાનુ') or list_temp[1] == 'પિતનુ\n' or list_temp[1]=='માતાનુ' or list_temp[1]=="સંબંધીનુ\n") and ((list_temp[2].startswith("ંજાજી") or list_temp[2].startswith("ંજદાન"))):
                list_temp[1] = list_temp[1].strip("\n") + data[i-6]
                list_temp[2]=list_temp[3]
                field_splitter  = list_temp[4].split("જાિત")
                list_temp[3] = field_splitter[0]
                list_temp[4] = field_splitter[1]
            elif (list_temp[1].startswith('િપતાનુ') or list_temp[1] == 'પિતનુ\n' or list_temp[1]=='માતાનુ' or list_temp[1]=="સંબંધીનુ\n") and (list_temp[2].startswith("ંજદાન") or list_temp[2].startswith("ંજાજી") or list_temp[2].startswith("જાજી") or list_temp[2].startswith("જાજી\n") or list_temp[2].startswith("ંજદાન")):
                list_temp[1] = list_temp[1].strip("\n") + data[i-6]
                field_splitter  = list_temp[4].split("જાિત")
                list_temp[3] = field_splitter[0]
                list_temp[4] = field_splitter[1]
            
            elif (list_temp[1] == 'િપતાનુ\n' or list_temp[1] == 'પિતનુ\n'or list_temp[1]=='માતાનુ' or list_temp[1]=="સંબંધીનુ\n") and not list_temp[2].startswith("ં નામ") and not list_temp[2].startswith("ંજદાન"):
                list_temp[1] = list_temp[1].strip("\n") + data[i-6]
                field_splitter  = list_temp[3].split("જાિત")
                list_temp[3] = field_splitter[0]
                list_temp[4] = field_splitter[1]
   
            elif list_temp[1].startswith("ં નામ :"):
                list_temp[1]=list_temp[2].strip("\n")+list_temp[1].strip("\n")
                field_splitter  = list_temp[4].split("જાિત")
                list_temp[2] = list_temp[3]
                list_temp[3] = field_splitter[0]
                list_temp[4] = field_splitter[1]
            
            else:
                pass

            list_final.append(list_temp) 

import codecs
fout=codecs.open('final.csv','wb','utf-8')
fout.write("Name," + "Father's/Husband's Name," + "House Number," + "Age," + "Gender\n")
for i in list_final:
    for ind,j in enumerate(i):
        if(ind==0):
            j=j.strip("નામ :")
        elif(ind==1):
            j=j.strip("'િપતાનુ").strip("પિતનુ").strip("માતાનુ").strip("સંબંધીનુ").strip("નામ :")
        elif(ind==2):
            j=j.strip("ઘર નંબર : ")
        elif(ind==3):
            j=j.strip("ઉંમર : ")
        elif(ind==4):
            j=j.strip(" : ")
        fout.write(j.strip("\n"))
        fout.write(",")
    fout.write("\n")
fout.close()

r = csv.reader(open('final.csv')) # Here your csv file
lines = list(r)

for i in range(len(lines)):
    if lines[i][4] == 'પુ(cid:302)ષ':
        lines[i][4] = 'પુરુષ'

    elif lines[i][4] == '(cid:280)ી':
        lines[i][4] = 'સ્ત્રી'

writer = csv.writer(open('final.csv', 'w'))
writer.writerows(lines)
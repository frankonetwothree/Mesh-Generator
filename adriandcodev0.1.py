#!/usr/bin/env python3
import json
import yaml


mylist = ["apple", "banana", "cherry", "moocow", "peanuts", "george", "Mo","adrian"]
meshdict = {}

#take the length of the list in this case 8 and create two counters
listlen=len(mylist)
counter=0
counter2=0
#for loop to append dictionary, with i as the dictionary key

for i in mylist:
    counter=counter2
    counter2=counter2+1
    if counter < listlen -1:
        meshdict[i]=[]
    while counter < listlen:
#while counter is less then the list length, and I doesnt equal mylist (IE two tunnels are not the same)
        #if i != mylist[counter]:
        tunneldict = {  "dest_host" : mylist[counter],"source_IP" :"", "dest_ip" :"","tunnel_id" :"" }
        meshdict[i].append(tunneldict)
        counter=counter+1

iprange = "192.168.1."
current_ip = 1


for site in meshdict:
    for endpoint in meshdict[site]:
        #print("tunnel:" + site + " to "+ endpoint)
        #print("tunnel addressing: " + site + ": "+ iprange + str(current_ip)+"/30")

        endpoint['source_IP']=iprange + str(current_ip)+"/30"
        current_ip =current_ip+1
        endpoint['dest_ip']=iprange + str(current_ip)+"/30"
        current_ip =current_ip+4






#print("printing in JSON, so that its easier to read")



output=json.dumps(meshdict, indent =4)
#print(output)
#print("printing in YAML, so that its easier to read")

output=yaml.dump(meshdict)
print(output)

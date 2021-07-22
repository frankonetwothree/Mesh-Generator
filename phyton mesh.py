#!/usr/bin/env python3
import json
import yaml

listcount= 10
siteName= "MT"
mylist=[]
i=1
while i <= listcount:
    mylist.append(siteName+str(i))
    i=i+1
    print(mylist)
#mylist = ["apple", "banana", "cherry", "moocow", "peanuts", "george", "Mo","adrian"]
meshdict = {}


listlen=len(mylist)
counter=0
counter2=0
for i in mylist:
    counter=counter2
    counter2=counter2+1
    if counter < listlen -1:
        meshdict[i]=[]
    while counter < listlen:
        if i != mylist[counter]:
            tunneldict = {  "dest_host" : mylist[counter],"source_IP" :"", "dest_ip" :"","tunnel_id" :"" }
            meshdict[i].append(tunneldict)
        counter=counter+1

iprange = "192.168.1."
current_ip = 1


for site in meshdict:
    for endpoint in meshdict[site]:
        endpoint['source_IP']=iprange + str(current_ip)+"/30"
        current_ip =current_ip+1
        endpoint['dest_ip']=iprange + str(current_ip)+"/30"
        current_ip =current_ip+4

#print("printing in JSON, so that its easier to read")




#output the config
for site in meshdict:

        for tunnel in meshdict[site]:
            print("to file router " +site )
            print("set interface ....." + tunnel['source_IP'])
            print("to file router " +tunnel['dest_host'] )
            print("set interface ....." + tunnel['dest_ip'])


output=json.dumps(meshdict, indent =4)
print(output)
#print("printing in YAML, so that its easier to read")

output=yaml.dump(meshdict)
print(output)

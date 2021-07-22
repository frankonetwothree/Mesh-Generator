#!/usr/bin/env python3
import yaml
mylist = ["mt1", "mt2", "mt3", "mt4","mt5"]
meshdict = {}

iprange = "192.168.1."
current_ip = 1
tunnel_int="st0"



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
                #output=yaml.dump(meshdict)
                #print(output)
                meshdict[i].append(mylist[counter])
            counter=counter+1
#tunneldict=meshdict
#for site in tunneldict:
#    for endpoint in tunneldict[site]

#print(meshdict)
for site in meshdict:
    tunnel_range=3350
    for endpoint in meshdict[site]:
        print("tunnel:" + site + " to "+ endpoint)
        print("config for " +site)
        #print("set interfaces st0 unit " + str(tunnel_range) + " family inet address ", end="")
        #print(iprange + str(current_ip)+"/30")
        print("set interfaces st0 unit " + str(tunnel_range) + " description " + '"IPSEC to ' +endpoint + '"')
        #print("set interfaces st0 unit " + str(tunnel_range) + " point-to-point")
        #print("set interfaces st0 unit " + str(tunnel_range) + " family inet mtu 1900")
        #print("tunnel addressing: " + site + ": "+ iprange + str(current_ip)+"/30")
        current_ip =current_ip+1
        print("config for " +endpoint)
        #print("set interfaces st0 unit " + str(tunnel_range) + " family inet address ", end="")
        #print(iprange + str(current_ip)+"/30")
        print("set interfaces st0 unit " + str(tunnel_range) + " description " + '"IPSEC to ' +site + '"')
        #print("set interfaces st0 unit " + str(tunnel_range) + " point-to-point")
        #print("set interfaces st0 unit " + str(tunnel_range) + " family inet mtu 1900")
        tunnel_range=tunnel_range+1
        #print("tunnel addressing: " + endpoint + ": "+ iprange + str(current_ip)+"/30")
    current_ip =current_ip+3
    print()

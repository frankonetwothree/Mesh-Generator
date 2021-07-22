#!/usr/bin/env python3
import itertools
import json
import yaml
iprange = "192.168.1."
current_ip = 1

num_sites = 4
sites=[[iter+1 for iter in range(num_sites)],[iter+1 for iter in range(num_sites)],[iter+1 for iter in range(num_sites)]],[iter+1 for iter in range(num_sites)]]
b = list(itertools.product(*sites))
print(b)
#c_dict= dict(zip(b,b))

#for site in b:
#    for endpoint in b[site]:
#        print("tunnel:" + site + " to "+ endpoint)
#        print("tunnel addressing: " + site + ": "+ iprange + str(current_ip)+"/30")
#        current_ip =current_ip+1
#current_ip =current_ip+3



#print(b)

#output=json.dumps(b, indent=4)
#print(output)

output=yaml.dump(b)
print(output)

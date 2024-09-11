#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

node_list_spine = {"inf-spine1":"configs/spine1.conf" ,"inf-spine2":"configs/spine2.conf","inf-spine3":"configs/spine3.conf" ,"inf-spine4":"configs/spine4.conf"}

node_list_superspine = {"inf-cspine1":"configs/cspine1.conf" ,"inf-cspine2":"configs/cspine2.conf","inf-cspine3":"configs/cspine3.conf" ,"inf-cspine4":"configs/cspine4.conf"}

node_list_leaf = {"inf-leaf1":"configs/leaf1.conf" ,"inf-leaf2":"configs/leaf2.conf","inf-leaf3":"configs/leaf3.conf" ,"inf-leaf4":"configs/leaf4.conf", "inf-leaf5":"configs/leaf5.conf", "inf-leaf6":"configs/leaf6.conf", "inf-leaf7":"configs/leaf7.conf", "inf-leaf8":"configs/leaf8.conf"}

node_list_router = {"inf-router1":"configs/router1.conf" }


all_nodes = dict(node_list_spine)
all_nodes.update(node_list_superspine)
all_nodes.update(node_list_leaf)
all_nodes.update(node_list_router)


srl_username = "admin"
srl_password = "NokiaSrl1!"
device_type = "nokia_srl"


for (node,config) in all_nodes.items():
    
    device =  {
    "device_type": device_type,
    "host": node,
    "username": srl_username,
    "password": srl_password,
    }
    cfg_file = config
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_config_from_file(cfg_file)
        output += net_connect.commit()
        #output += net_connect.save_config()

    print()
    
    # uncomment this next line to get full output
    #print(output)
    
    # print only the "commit" part 
    print('\n'.join(output.splitlines()[-13:]))
    
    print()

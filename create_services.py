#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

node_list_service_lag_terminated_in_GRT = {"inf-leaf1":"configs/services/lag terminated in GRT/leaf1.conf" ,"inf-leaf2":"configs/services/lag terminated in GRT/leaf2.conf","inf-leaf3":"configs/services/lag terminated in GRT/leaf3.conf" ,"inf-leaf4":"configs/services/lag terminated in GRT/leaf4.conf", "inf-leaf5":"configs/services/lag terminated in GRT/leaf5.conf" ,"inf-leaf6":"configs/services/lag terminated in GRT/leaf6.conf","inf-leaf7":"configs/services/lag terminated in GRT/leaf7.conf" ,"inf-leaf8":"configs/services/lag terminated in GRT/leaf8.conf"}

node_list_service_lag_terminated_in_macvrf = {"inf-leaf1":"configs/services/lag terminated in mac-vrf/leaf1.conf" ,"inf-leaf2":"configs/services/lag terminated in mac-vrf/leaf2.conf","inf-leaf3":"configs/services/lag terminated in mac-vrf/leaf3.conf" ,"inf-leaf4":"configs/services/lag terminated in mac-vrf/leaf4.conf", "inf-leaf5":"configs/services/lag terminated in mac-vrf/leaf5.conf" ,"inf-leaf6":"configs/services/lag terminated in mac-vrf/leaf6.conf", "inf-leaf7":"configs/services/lag terminated in mac-vrf/leaf7.conf" ,"inf-leaf8":"configs/services/lag terminated in mac-vrf/leaf8.conf"}

node_list_service_lag_terminated_in_macvrf_and_ipvrf = {"inf-leaf1":"configs/services/lag terminated in mac-vrf and ip-vrf/leaf1.conf" ,"inf-leaf2":"configs/services/lag terminated in mac-vrf and ip-vrf/leaf2.conf","inf-leaf3":"configs/services/lag terminated in mac-vrf and ip-vrf/leaf3.conf" ,"inf-leaf4":"configs/services/lag terminated in mac-vrf and ip-vrf/leaf4.conf", "inf-leaf5":"configs/services/lag terminated in mac-vrf and ip-vrf/leaf5.conf" , "inf-leaf6":"configs/services/lag terminated in mac-vrf and ip-vrf/leaf6.conf","inf-leaf7":"configs/services/lag terminated in mac-vrf and ip-vrf/leaf7.conf" ,"inf-leaf8":"configs/services/lag terminated in mac-vrf and ip-vrf/leaf8.conf"}

node_list_service_multihomed_bridged_port_in_GRT = {"inf-leaf1":"configs/services/multihomed bridged port in GRT/leaf1.conf" ,"inf-leaf2":"configs/services/multihomed bridged port in GRT/leaf2.conf","inf-leaf3":"configs/services/multihomed bridged port in GRT/leaf3.conf" ,"inf-leaf4":"configs/services/multihomed bridged port in GRT/leaf4.conf", "inf-leaf5":"configs/services/multihomed bridged port in GRT/leaf5.conf" ,"inf-leaf6":"configs/services/multihomed bridged port in GRT/leaf6.conf","inf-leaf7":"configs/services/multihomed bridged port in GRT/leaf7.conf" ,"inf-leaf8":"configs/services/multihomed bridged port in GRT/leaf8.conf"}

node_list_service_multihomed_routed_port_in_GRT = {"inf-leaf1":"configs/services/multihomed routed port in GRT/leaf1.conf" ,"inf-leaf2":"configs/services/multihomed routed port in GRT/leaf2.conf","inf-leaf3":"configs/services/multihomed routed port in GRT/leaf3.conf" ,"inf-leaf4":"configs/services/multihomed routed port in GRT/leaf4.conf", "inf-leaf5":"configs/services/multihomed routed port in GRT/leaf5.conf" ,"inf-leaf6":"configs/services/multihomed routed port in GRT/leaf6.conf","inf-leaf7":"configs/services/multihomed routed port in GRT/leaf7.conf" ,"inf-leaf8":"configs/services/multihomed routed port in GRT/leaf8.conf"}




srl_username = "admin"
srl_password = "NokiaSrl1!"
device_type = "nokia_srl"

def service_config(service_dict, service_name):
    print ("############### ", service_name, " ###############")
    
    for (node,config) in service_dict.items():

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
        print('\n'.join(output.splitlines()[-5:]))

        print()

service_config(node_list_service_lag_terminated_in_GRT, "service_lag_terminated_in_GRT")
service_config(node_list_service_lag_terminated_in_macvrf, "service_lag_terminated_in_macvrf")
service_config(node_list_service_lag_terminated_in_macvrf_and_ipvrf, "service_lag_terminated_in_macvrf_and_ipvrf")
service_config(node_list_service_multihomed_bridged_port_in_GRT, "service_multihomed_bridged_port_in_GRT")
service_config(node_list_service_multihomed_routed_port_in_GRT, "service_multihomed_routed_port_in_GRT")
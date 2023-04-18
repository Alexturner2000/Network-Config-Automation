import sys
from netmiko import ConnectHandler
from getpass import getpass


with open('devices.txt', 'r') as file:
    devices = file.readlines()

# Prompt user for username and password
username = input("Enter the username: ")
password = getpass("Enter the password: ")


for device_line in devices:
    device_info = device_line.strip().split(',')
    device_type = device_info[0]
    ip_address = device_info[1]

    # Define device dictionary based on read and input data
    device = {
        'device_type': device_type,
        'ip': ip_address,
        'username': username,
        'password': password,
    }

    try:
        # Connect to the device
        net_connect = ConnectHandler(**device)
        print("Connected to device:", ip_address)

        # Send commands and retrieve output
        commands = ["show interfaces", "show interfaces description"]
        for command in commands:
            output = net_connect.send_command(command)
            print("Output of command", command, ":\n", output)

        # Close the SSH session
        net_connect.disconnect()

    except Exception as e:
        print("Error connecting to device", ip_address + ":", str(e))
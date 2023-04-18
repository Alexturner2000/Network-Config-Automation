import pandas as pd
from netmiko import ConnectHandler
from getpass import getpass

def extract_device_data(df):
    """Extract device data from a DataFrame and return as lists"""
    ip_addresses = []
    device_types = []

    for index in range(0, len(df)):
        ip_address = df.iloc[index, 0]  # Extract data from column A at current row
        device_type = df.iloc[index, 1]  # Extract data from column B at current row
        ip_addresses.append(ip_address)  # Append to ip_addresses list
        device_types.append(device_type)  # Append to device_types list

    return ip_addresses, device_types

def connect_to_device(device_type, ip_address, username, password):
    """Function to connect to a device and perform operations"""
    try:
        device = {
            "device_type": device_type,
            "ip": ip_address,
            "username": username,
            "password": password,
        }

        connection = ConnectHandler(**device)
        print(f"Successfully connected to {ip_address} ({device_type})")
        # Perform operations on the device here
        # ...
        connection.disconnect()  # Disconnect from the device
        print(f"Disconnected from {ip_address} ({device_type})")
    except Exception as e:
        print(f"Failed to connect to {ip_address} ({device_type}): {e}")

def main():
    # Read data from the spreadsheet
    df = pd.read_excel("devices.xlsx")

    # Extract data from all rows except the first row
    ip_addresses, device_types = extract_device_data(df.iloc[1:, :])

    # Prompt user for username and password
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Connect to devices
    for i in range(len(ip_addresses)):
        connect_to_device(device_types[i], ip_addresses[i], username, password)

if __name__ == "__main__":
    main()

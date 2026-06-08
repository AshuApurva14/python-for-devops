#!/usr/bin/env python3

""" Format and Print Coonection Info 
"""


ip_address = input("IP Address: ")
hostname = input("Hostname: ")
port_text = input("Port: ")
output_format = input("format: ").lower()

if not port_text.isdigit():
    print("Invalid Port")
else: 
    port = (port_text)

if output_format == "plain":
    print(f"{ip_address}")
    print(f"{hostname}")
    print(f"{port}")
elif output_format == "csv":
    print(f"The IP Address is: {ip_address}, Hostname: {hostname} and Port: {port}")

elif output_format == "url":
   print(f"https://{hostname}:{port}")

elif output_format == "json":
    conn_info = '{"IP Address": "{ip_address}}'
    print(f"{conn_info}")

else:
    print("Unknown Format")

    
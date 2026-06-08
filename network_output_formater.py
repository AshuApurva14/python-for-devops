#!/usr/bin/env python3


ip_address = input("IP Address: ")
hostname = input("Hostname: ")
port = input("Port: ")
output_format = input("format: ")

if output_format == "plain":
    print(f"{ip_address}")
    print(f"{hostname}")
    print(f"{port}")
elif output_format == "csv":
    print(f"The IP Address is: {ip_address}, Hostname: {hostname} and Port: {port}")

elif output_format == "url":
   print(f"https://{hostname}:{port}")

else:
    print("Unknown Format")

    
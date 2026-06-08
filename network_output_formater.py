#!/usr/bin/env python3


ip_address = input("IP Address: ")
hostname = input("Hostname: ")
port = input("Port: ")
output_format = input("format: ")

if output_format == "plain" or "PLAIN" or "Plain":
    print(f"{ip_address}")
    print(f"{hostname}")
    print(f"{port}")
elif output_format == "csv" or "CSV" or "Csv":
    print(f"The IP Address is: {ip_address}, Hostname: {hostname} and Port: {port}")

elif output_format == "url" or "URL" or "Url":
   print(f"https://{hostname}:{port}")

else:
    print("Unknown Format")

    
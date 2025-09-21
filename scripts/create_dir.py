#!/usr/bin/env python

import os

root_path = "/workspaces/python-for-devops/daily_challenge"  # Change this to your target directory
file_name= "challenge.md"
os.makedirs(root_path, exist_ok=True)

file_path = os.path.join(output_directory, output_filename)

for i in range(1, 31):
    dir_name = f"D"
    dir_path = os.path.join(root_path, dir_name)
    os.makedirs(dir_path, exist_ok=True)
    print(f"Created directory: {dir_path}")

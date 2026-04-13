#!/bin/bash

set -eou pipeline

# Install uv binary
echo -e "Installing UV package manager....\n"

install_status=$(curl -LsSf https://astral.sh/uv/install.sh | sh)
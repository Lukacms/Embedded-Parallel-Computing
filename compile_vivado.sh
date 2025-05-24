#!/bin/bash

# Take a .cal file as input
if [ $# -eq 0 ]; then
    echo "usage: $0 <network-name>"
    exit 1
fi

# Make sure a network name is provided
if [ -z "$1" ]; then
    echo "Network name not provided!"
    exit 1
fi

# Target folder will be the name of the .cal file without the extension, 
TARGET_FOLDER="out"

# Network name without namespaces (split by dots and get last part)
NETWORK_NAME="${1##*.}"
echo "Network name: $NETWORK_NAME"

# Path to Vivado / Vitis
# Change if not running on sekhmet
source /opt/xilinx/Vitis/2020.2/settings64.sh
source /opt/xilinx/Vivado/2020.2/settings64.sh
export XILINX_XRT="/opt/xilinx/xrt"

# Run streamblocks on it (first pass, multicore)
SRC_FILES=$(find src/ -type f -name "*.cal" | tr '\n' ':')
./streamblocks-platforms/streamblocks multicore \
    --set partitioning=on \
    --source-path "$SRC_FILES" \
    --target-path "$TARGET_FOLDER" \
    "$1"
# Check if streamblocks was successful
if [ $? -ne 0 ]; then
    echo "Streamblocks failed (multicore)!"
    exit 1
fi

# Run streamblocks on it (second pass, vivado)
./streamblocks-platforms/streamblocks vivado-hls \
    --set partitioning=on \
    --source-path "$SRC_FILES" \
    --target-path "$TARGET_FOLDER" \
    "$1"

# Check if streamblocks was successful
if [ $? -ne 0 ]; then
    echo "Streamblocks failed (vivado)!"
    exit 1
fi

# Check if the target folder was created
if [ ! -d "$TARGET_FOLDER" ]; then
    echo "Target folder was not created!"
    exit 1
fi

# Copy everything from ~/lib to target_folder/lib
PATCHED_LIB_PATH="./lib_patch/lib/"
TARGET_LIB_PATH="$TARGET_FOLDER/lib"
mkdir -p "$TARGET_LIB_PATH"
cp -r "$PATCHED_LIB_PATH"* "$TARGET_LIB_PATH"

# Create a build folder
mkdir -p "$TARGET_FOLDER/build"

# Set minimum cmake ver
find . -type f -not -name "*.sh" -not -path '*/\.*' | while read -r file; do
  if grep -q 'cmake_minimum_required(VERSION 3.10)' "$file"; then
    sed -i 's/cmake_minimum_required(VERSION 3\.10)/cmake_minimum_required(VERSION 3.0)/g' "$file"
    echo "Modified cmake version for: $file"
  fi
done

# Cmake (silence all warnings)
cd "$TARGET_FOLDER/build" 
cmake -DCMAKE_CXX_FLAGS="-w" .. -DHLS_CLOCK_PERIOD=3.3 -DFPGA_NAME=xcu200-fsgd2104-2-e -DPLATFORM=xilinx_u200_xdma_201830_2 -DUSE_VITIS=on -DCMAKE_BUILD_TYPE=Debug
# Build
cmake --build . --target "${NETWORK_NAME}_kernel_xclbin"

# Check if the build was successful
if [ $? -ne 0 ]; then
    echo "Build failed!"
    exit 1
fi

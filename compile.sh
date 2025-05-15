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

# Run streamblocks on it
SRC_FILES=$(find src/ -type f -name "*.cal" | tr '\n' ':')
./streamblocks-platforms/streamblocks multicore \
    --source-path "$SRC_FILES" \
    --target-path "$TARGET_FOLDER" \
    "$1"

# Check if streamblocks was successful
if [ $? -ne 0 ]; then
    echo "Streamblocks failed!"
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

# Cmake (silence all warnings)
cd "$TARGET_FOLDER/build" 
cmake -DCMAKE_CXX_FLAGS="-w" ..
# Build
cmake --build .

# Check if the build was successful
if [ $? -ne 0 ]; then
    echo "Build failed!"
    exit 1
fi
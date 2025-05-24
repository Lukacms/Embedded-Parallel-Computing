# Embedded-Parallel-Computing

## Prerequisites

- Java 11
- Maven
- Vivado/Vitis 2019.2

Make sure submodules are initialized and updated:

```bash
git submodule update --init --recursive
```

Compile streamblocks-tycho and streamblocks-platforms:

```bash
cd streamblocks-tycho
mvn -DskipTests install
cd ../streamblocks-platforms
mvn install
cd ..
```

### Note

If using Vivado/Vitis 2020.2, you should switch to the branch `vivado_2020_2_hlsmath` for streamblocks-platforms.
Otherwise the produced Verilog files won't be readable by Vivado/Vitis.

Newer versions may not be supported.

## Build and run a dataflow program

### Software compile

The `compile.sh` script is used to directly compile a dataflow program into an executable binary.

```bash
./compile.sh qrd.Top
```

The first argument is the top network of the dataflow program to compile. Here, for this example, it is the `Top` network, 
in the `qrd` namespace.
The script will compile the program and generate the output in the `out` directory, with the binary being located at `out/bin/Top`.

### Software run

```bash
./out/bin/Top
```

If a file is used by the dataflow program, the path for it should be given to the program with the `--i` flag:

```bash
./out/bin/Top --i=path/to/input/file
```

The syntax with the `=` is required, otherwise the program will not recognize the input file.

### Hardware compile

The `compile_hardware.sh` script is used to compile a dataflow program into Verilog files.

```bash
./compile_vivado.sh qrd.Top
```

This will automatically generate the Verilog files, as well as a host binary to run them.

#### Note

Compiling into a bitstream (the last part) takes about 4-6 hours. For faster compilation, modify the `compile_vivado.sh` script
to use software emulation.
Add the `-DTARGET=hw_emu` flag when creating CMake files in the `compile_vivado.sh` script like so:

```bash
# Cmake (silence all warnings)
cd "$TARGET_FOLDER/build" 
cmake -DCMAKE_CXX_FLAGS="-w" .. -DHLS_CLOCK_PERIOD=3.3 -DFPGA_NAME=xcu200-fsgd2104-2-e -DPLATFORM=xilinx_u200_xdma_201830_2 -DUSE_VITIS=on -DCMAKE_BUILD_TYPE=Debug -DTARGET=hw_emu
```

(notice the `-DTARGET=hw_emu` flag at the end).

### Hardware run

The host binary will be located in the `./out/bin` directory, with the name of the Top network. (in the same example, it will be `./out/bin/Top`). The verilog files will be located in the `./out/bin/xclbin` directory.

The host will look for the verilog files under the `./xclbin` directory, so it is necessary to go inside `./out/bin` first, and then run the host binary:

```bash
cd out/bin
XILINX_XRT=/opt/xilinx/xrt ./Top
```
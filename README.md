# Embedded-Parallel-Computing

## Prerequisites

- Java 11
- Maven

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

## Build

```bash
./compile.sh qrd.Top
```

## Run

```bash
./out/bin/Top
```
#!/usr/bin/env python3
import os, sys


def readFile(filename):
    with open(filename, "rb") as f:
        return f.read().decode("utf-8")


def writeFile(filename, data):
    with open(filename, "wb") as f:
        f.write(data.encode("utf-8"))


sourceFile = sys.argv[1]
code = readFile(sourceFile)

code = code.replace(
    "\t\tChunkInfo.PartitionIndex = -1;\n\t\tfor (int32 BlockIndex = FirstBlockIndex; BlockIndex <= LastBlockIndex; ++BlockIndex)",
    "\t\tChunkInfo.PartitionIndex = -1;\n\t\tfor (size_t BlockIndex = FirstBlockIndex; BlockIndex <= LastBlockIndex; ++BlockIndex)"
)

writeFile(sourceFile, code)

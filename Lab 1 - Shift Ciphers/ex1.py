#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out

#Lim Boon Han Melvin 1005288
import sys
import argparse
import string

def encrypt(char,key):
    if char in string.printable:
        #account for overflow
        output = (string.printable.index(char) + key) % len(string.printable)

    return string.printable[output]

def decrypt(text,key):
    return encrypt(text,-key)


def doStuff(filein, fileout, key, mode):
    # open file handles to both files
    fin = open(filein, mode="r", encoding="utf-8", newline="\n")  # read mode
    fout = open(fileout, mode="w", encoding="utf-8", newline="\n")  # write mode
    c = fin.read()  # read in file into c as a str
    # and write to fileout

    if (key < 1 or key >= len(string.printable)):
        print(f"key must be between 1 and {len(string.printable) - 1 }")
        return 0

    # PROTIP: pythonic way
        # do stuff
    if mode.upper() == "E": 
        output = "".join([encrypt(char,key) for char in c])
        mode = "Encryption"

    elif mode.upper() == "D": 
        output = "".join([decrypt(char,key) for char in c])
        mode = "Decryption"

    else: 
        print("Wrong value : e to encrypt, d to decrypt")
        return 0

    fout.write(output)

    # close all file streams
    fin.close()
    fout.close()

    # file will be closed automatically when interpreter reaches end of the block
    print(f"{mode} completed with key = {key}")

# our main function
if __name__ == "__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="filein", help="input file")
    parser.add_argument("-o", dest="fileout", help="output file")
    parser.add_argument("-k", help = "value to shift characters by")
    parser.add_argument("-m", help = "e to encrypt, d to decrypt")

    # parse our arguments
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout
    key = int(args.k)
    mode = args.m

    doStuff(filein, fileout,key,mode)
#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out

#Lim Boon Han Melvin 1005288
import sys
import argparse

def encrypt(byte,key):
    output = (byte+key) % 256

    return output

def decrypt(byte,key):
    return encrypt(byte,-key)

def doStuff(filein, fileout, key, mode):
    # open file handles to both files
    fin = open(filein, mode="rb")  #read binary
    fout = open(fileout, mode="wb")  # write binary
    c = bytearray(fin.read())  

    if (key < 0 or key > 255):
        print("key must be between 0 and 255")
        return 0

    # PROTIP: pythonic way
        # do stuff
    if mode.upper() == "E": 
        output = bytearray([encrypt(byte,key) for byte in c])
        mode = "Encryption"

    elif mode.upper() == "D": 
        output = bytearray([decrypt(char,key) for char in c])
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
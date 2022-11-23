#!/usr/bin/env python3
# SUTD 50.042 FCS Lab 1
# Simple file read in/out

#Lim Boon Han Melvin 1005288
import sys
import argparse

def decrypt(byte,key):
    output = (byte-key)%256

    return output

def doStuff(filein, fileout, key):
    
    fin = open(filein, mode="rb")  #read binary
    fout = open(fileout, mode="wb")  # write binary
    c = bytearray(fin.read())  

    output = bytearray([decrypt(char,key) for char in c])
    mode = "Decryption"

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

    # parse our arguments
    args = parser.parse_args()
    filein = args.filein
    fileout = args.fileout

    for key in range(256):
        fileout2 = fileout+ str(key) + ".png"
        doStuff(filein, fileout2,key)
        fileout2 = fileout
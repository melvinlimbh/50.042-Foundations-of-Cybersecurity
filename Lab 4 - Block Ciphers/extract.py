#!/usr/bin/env python3
# ECB plaintext extraction skeleton file for 50.042 FCS

import argparse
from collections import Counter

def getInfo(headerfile):
    with open(headerfile, mode="rb") as fin:
        header = fin.read()

    #print(header)
    return header

def extract(infile,outfile,headerfile):
    """
    ECB encrypts same block to same values 
    --> try using frequency analysis
    """
    header = getInfo(headerfile)
    #print(header)
    encrypted_texts = []

    with open(infile,"rb") as fin:
        # start reading from 1 position after header
        a = fin.seek(len(header)+1)
        #print(a)
        while(True):
            bytes_read = fin.read(8)
            if bytes_read == b"": break 
            encrypted_texts.append(bytes_read)
            
        block_frequency = Counter(encrypted_texts)
        #print(block_frequency)

        frequency = -1
        for block, count in block_frequency.items():
            if count > frequency:
                most_frequent_block = block
                frequency = count

        """
        decrypt based on frequency
        most comon = b"11111111"
        others = b"00000000"
        """
        decrypted = []
        for chunks in encrypted_texts:
            if chunks == most_frequent_block: decrypted.append(b'0'*8)
            else: decrypted.append(b'1'*8)

        decrypted_text = "".join([encoded_block.decode() for encoded_block in decrypted])
        decrypted_text = decrypted_text.encode() # encode it to be bytes-like
        #print(decrypted_text)

        with open(outfile,'wb') as fout:  # write in binary so that image can be produced
            fout.write(header) # include to ensure correct format
            fout.write(b'\n')
            fout.write(decrypted_text)

        fin.close()
        fout.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Extract PBM pattern.')
    parser.add_argument('-i', dest='infile',help='input file, PBM encrypted format')
    parser.add_argument('-o', dest='outfile',help='output PBM file')
    parser.add_argument('-hh', dest='headerfile',help='known header file')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    headerfile=args.headerfile

    print('Read from: %s'%infile)
    print('Read header file from: %s'%headerfile)
    print('Write to: %s'%outfile)

    #getInfo(headerfile)
    success = extract(infile,outfile,headerfile)
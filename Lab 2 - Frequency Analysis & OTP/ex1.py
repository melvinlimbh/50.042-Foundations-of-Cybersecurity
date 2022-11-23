import sys
import argparse

def doStuff(filein, fileout):
    
    fin = open(filein, mode="r", encoding="utf-8", newline="\n")
    fout = open(fileout, mode="w", encoding="utf-8", newline="\n")
    c = fin.read() 
        
    # do stuff
    #used a website for frequency analysis and obtained the mapping of values, put in a dictionary
    #https://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.htmlhttps://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.html
        
    ls1 = ['U','J','Y','Q','E','D','I','X','H','B','T',	'W','C',
    'S','O','K','M','V','F','R','L','A','N','Z','P','G']
    
    ls2 = ['E','T','I','A','O','N','S','H','R','L','D','G','M','C','Y',
    'U','W','F','P','B','V','K','X','J','Q','Z']

    for i in range(len(ls2)): c = c.replace(ls1[i],ls2[i].lower())
    
        # and write to fileout
    fout.write(c)
        
    fin.close()
    fout.close()
    print(c)

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

    doStuff(filein, fileout)


'''
Created on 31.10.2016

@author: Timo
'''
import argparse
import json

def process_input(args):
    if args.add_commas: sep = None
    outFile = open(args.output_json,"w",encoding=args.encoding)
    for line in open(args.input_sources,encoding=args.encoding):
        line = line.strip()
        tkns = line.split(None,2)
        outLine = process_source(args,tkns)

        outFile.write(line + "\n")
    outFile.close() 
    
def process_source(args,line):
     return line
def main():
    process_input()
    
if __name__ == '__main__':
    pass
print("Starting...")
# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
# here we use argeparse.ArgumentParser to define the command line inputs
import sys
import argparse


parser = argparse.ArgumentParser(description= "convert sam to bed")
parser.add_argument('-i', help='sam file input')
parser.add_argument('-o', help='bed file output', default = 'default.bed')

args=parser.parse_args()

if args.o == 'default.bed':     
    args.o=(str(args.i).rsplit(".",1)[0]+".bed")    
  
if args.i == args.o:
    raise ValueError('Your input and output files appear to be identical')
if str(args.i).rsplit(".",1)[1] != "sam":
    raise Exception('Are you sure this is a sam file?')    
#command line parameters for the sam file and bed file 
# read in the file 
samfile = open(args.i, 'r')



output = open(args.o, 'w')

#iterate over the lines 

count_unmapped = 0
count_no_strand = 0

for line in samfile:
    
    if line.startswith('@'):
        continue   
    else:
        #split line into strings
        splitline = (line.split('\t'))
        #unmapped reads can't go into the bed file
        if splitline[2] == '*':
            count_unmapped += 1
            continue
        else:
            chrom = splitline[2]
            gene_name = splitline[0]
            #SAM is 1-based and bed is 0 based
            start = int(splitline[3])-1
            readlength = len(splitline[9])
            stop = start + readlength
            # we check the strand and make sure the stop and start are sequential 
            #the end position is calculated from the length of the read 
            thestrand = "."
            if 'XS:A:-' in line:
                thestrand = '-'  
            elif 'XS:A:+' in line:
                thestrand = '+'     
    #format the string for the bed file line        
    bed_line =  '%(chrom)s\t%(start)i\t%(stop)i\t%(gene_name)s\t.\t%(thestrand)s\n' % locals()                 
    output.write(bed_line)      
    
samfile.close()
output.close()    
#ignore headers 
#split the line up
#assign each flag to a variable
#create missing variables
#order the variable and print to output
#order: chr, start, stop, read_name, empty, strand
    
    
    



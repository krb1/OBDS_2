# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
# here we use argeparse.ArgumentParser to define the command line inputs
import sys
import argparse


parser = argparse.ArgumentParser(description= "convert sam to bed")
parser.add_argument('-i', help='sam file input')
parser.add_argument('-o', help='bed file output', default=(str(args.i).rsplit(".",1)[0]+".bed"))
print(args.o)
args=parser.parse_args()

if args.i == args.o :
    raise ValueError('Your input and output files appear to be identical')
if str(args.i).rsplit(".",1)[1] != "sam":
    raise Exception('Are you sure this is a sam file?')    
#command line parameters for the sam file and bed file 
# read in the file 
samfile = open(args.i, 'r')



output = open(args.o, 'w')

#iterate over the lines 
for line in samfile:
    if line.startswith('@'):
        continue 
    elif 'XS:A:' not in line:
        continue
    
    else:
        #split line into strings
        splitline = (line.split('\t'))
        #unmapped reads can't go into the bed file
        if splitline[2] == '*':
            continue
        else:
              
            chrom = splitline[2]
            
            gene_name = splitline[0]
            # we check the strand and make sure the stop and start are sequential 
            #the end position is calculated from the length of the read 
            thestrand = '0'
            #SAM is 1-based and bam is 0 based
            Samfilestart = int(splitline[3])-1
            readlength = len(splitline[9])
            if 'XS:A:-' in line:
                thestrand = '-'
                #here we make the start in sam into stop in bed as it's reverse strand
                stop = Samfilestart
                start = stop - readlength
                
            elif 'XS:A:+' in line:
                thestrand = '+'
                start = Samfilestart
                stop = start + readlength
            else: 
               print("cannot find strand in this line")
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
    
    
    



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:22:29 2019

@author: bullk
"""

import pysam
import sys
import argparse

parser = argparse.ArgumentParser(description= "convert bam to bed")
parser.add_argument('-bamfile', help='bam file input')
parser.add_argument('-bedfile', help='bed file output', default = 'default.bed')
args=parser.parse_args()

if args.bedfile == 'default.bed':     
    args.bedfile=(str(args.bamfile).rsplit(".",1)[0]+".bed")   
    
if str(args.bamfile).rsplit(".",1)[1] != "bam":
    raise Exception('Are you sure this is a bam file?')       
else:
    pass

output = open(args.bedfile, 'w')
count_unmapped = 0
samfile = pysam.AlignmentFile(args.bamfile, "rb")
for read in samfile.fetch():
    if read.is_unmapped == True:
        count_unmapped += 1
        continue  
    #this will be fetch eventually
    else:
        chrom = read.reference_name
        start = read.reference_start
        stop = read.reference_end
        name = read.query_name
        if read.is_reverse == True:
            strand = "-"
        else:
            strand = "+"   
    
        bed_line = '{}\t{}\t{}\t{}\t.\t{}\n' .format(chrom, start, stop, name, strand) 
        output.write(bed_line)
print(count_unmapped)   
samfile.close()
output.close()
#I made this comment later
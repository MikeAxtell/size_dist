#!/usr/bin/env python3

#### Imports

import pysam
import argparse
import os
import sys

##### Functions .. one for bam files, other for fastq files

def fastq (file):
    sizes = {}
    tally = 0
    with pysam.FastxFile(file) as fh:
        for entry in fh:
            tally += 1
            sz = len(entry.sequence)
            if not sz in sizes:
                sizes[sz] = 1
            else:
                sizes[sz] += 1
    for sz in sorted(sizes):
        frac = sizes[sz] / tally
        print("{}\t{}\t{}\t{}".format(file, sz, sizes[sz], frac))

def bam (file, args):
    sizes = {}
    tally = 0
    fail = 0
    samfile = pysam.AlignmentFile(file, "rb")
    for read in samfile.fetch(until_eof=True):
        # exclusions
        if (args.includeSupplementary is False) and (read.is_supplementary is True):
            continue
        if (args.includeSecondary is False) and (read.is_secondary is True):
            continue
        if (args.includeDuplicate is False) and (read.is_duplicate is True):
            continue
        if (args.excludeUnmapped is True) and (read.is_unmapped is True):
            continue
        sz1 = read.query_length
        if sz1 > 0:
            tally += 1
            if not sz1 in sizes:
                sizes[sz1] = 1
            else:
                sizes[sz1] += 1
        else:
            # seq not stored, try the cigar string to infer length
            sz2 = read.infer_query_length()
            if sz2 is not None:
                tally += 1
                if not sz2 in sizes:
                    sizes[sz2] = 1
                else:
                    sizes[sz2] += 1
            else:
                fail += 1
    for sz in sorted(sizes):
        frac = sizes[sz] / tally
        print("{}\t{}\t{}\t{}".format(file, sz, sizes[sz], frac))

###### Argument parsing / help message / version

parser = argparse.ArgumentParser(prog='size_dist.py')
parser.add_argument("-s", "--includeSupplementary", action="store_true",
                    help="Include supplementary alignments (bam)")
parser.add_argument("-d", "--includeDuplicate", action="store_true",
                    help="Include duplicate alignments (bam)")
parser.add_argument("-c", "--includeSecondary", action="store_true",
                    help="Include secondary alignments (bam)")
parser.add_argument("-u", "--excludeUnmapped", action="store_true",
                    help="Exclude unmapped reads (bam)")
parser.add_argument("-v", "--version", action="version",
                    version='%(prog)s 1.0')
parser.add_argument("files", nargs='+',
                    help="One or more .bam or .fastq files")
args = parser.parse_args()


##### Print header for output
print("File\tSize\tFrequency\tFraction")

###### Script control .. go through each file.
for file in args.files:
    filebase, extension = os.path.splitext(file)
    if extension == '.bam' :
        bam(file, args)
    elif extension == '.fastq' :
        fastq(file)
    else :
        sys.stderr.write("File {} skipped; not bam or fastq\n".format(file))

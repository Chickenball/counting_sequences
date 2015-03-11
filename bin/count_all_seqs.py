#!/usr/bin/env python

import sys
import seq_utils
#import glob
import fnmatch
import os

if len(sys.argv) != 2:
	print "Please input exactly 2 agruments"

def count_all_seqs(filename):
	input_file = open(filename)
	seq_count = seq_utils.count_seqs(input_file)
	print seq_count,"in", os.path.basename(filename)

#for filename in glob.iglob(sys.argv[1] + '*.fasta'):
#    count_all_seqs(filename)

for filename in sorted(os.listdir(sys.argv[1])):
	path = os.path.join(sys.argv[1], filename)
	if fnmatch.fnmatch(path, '*.fasta'):
		count_all_seqs(path)


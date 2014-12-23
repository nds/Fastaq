import argparse
from fastaq import tasks

def run(description):
    parser = argparse.ArgumentParser(
        description = 'Trims any Ns off each sequence in a fasta/q file. Does nothing to gaps in the middle, just trims the ends',
        usage = 'fastaq trim_Ns_at_end <fasta/q in> <fasta/q out>')
    parser.add_argument('infile', help='Name of input fasta/q file')
    parser.add_argument('outfile', help='Name of output fasta/q file')
    options = parser.parse_args()
    tasks.trim_Ns_at_end(options.infile, options.outfile)

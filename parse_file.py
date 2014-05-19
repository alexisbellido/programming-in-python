#!/usr/bin/env python

"""
Parse a file and write output to another.

"""


from optparse import OptionParser
import re
from collections import OrderedDict


parser = OptionParser()

parser.add_option("-i", "--input", dest="input_filepath", help="input filepath")
parser.add_option("-o", "--output", dest="output_filepath", help="output filepath")

(options, args) = parser.parse_args()

#print options
#print args

input_filepath = options.input_filepath
output_filepath = options.output_filepath

lines = {}
pattern_key = re.compile(r'ednKey="(.*?)"')
pattern_value = re.compile(r'ednvalue="(.*?)"')

with open(input_filepath, 'r') as input_file:
    for line in input_file:
        line = line.strip()
        key = pattern_key.search(line)
        value = pattern_value.search(line)
        if (key and value):
            lines[key.group(1)] = value.group(1)

ordered_lines = OrderedDict(sorted(lines.items(), key = lambda t: int(t[0])))

with open(output_filepath, 'w') as output_file:
    for line in ordered_lines.items():
        #output_file.write('%s,%s\n' % (line[0], line[1]))
        output_file.write("{0} => __( '{1}', 'ev' ),\n".format(line[0], line[1]))

print "Completed" 

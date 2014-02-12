#!/usr/bin/env python

"""
Compare two files.

"""


from optparse import OptionParser


parser = OptionParser()

parser.add_option("-b", "--bad", dest="bad_filepath", help="bad filepath")
parser.add_option("-g", "--good", dest="good_filepath", help="good filepath")
parser.add_option("-o", "--output", dest="output_filepath", help="output filepath")


(options, args) = parser.parse_args()

#print options
#print args

bad_filepath = options.bad_filepath
good_filepath = options.good_filepath
output_filepath = options.output_filepath

good_emails = []

with open(good_filepath, 'r') as good_file:
    for line in good_file:
        good_emails.append(line.strip())

print "good emails", good_emails

output_file = open(output_filepath, 'w')

with open(bad_filepath, 'r') as bad_file:
    for line in bad_file:
        bad_email = line.strip()
        if bad_email not in good_emails:
            print "remove this: ", bad_email
            output_file.write(line)

output_file.close()

print "..."
print "Complete"

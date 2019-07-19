#!/usr/bin/env python3

import re
import numpy
import argparse

# original function copied from http://thereefuge.com/threads/reverse-engineering-a-hydra-26-hd.15524/
# Converted from (node)JS
# JS original https://github.com/chriswhong/ai-hydra-time-offset/blob/master/time-offset.js

# const getChecksum = (json) => {
#   // convert json to xml and get only the colors element
#   const colorsXml = js2xmlparser.parse('ramp', json.ramp)
#     .match(/(<colors>.+?<\/colors>)/gms)[0] #global, multiline, dotall
#     .replace(/(\r\n|\n|\r|\s+)/gm,"");

#   let checksum = 0;

#   if (colorsXml.length === 0) return k;

#   for (var i = 0; i < colorsXml.length; i += 1) {
#       const charCode = colorsXml.charCodeAt(i);
#       checksum = ((checksum << 5) - checksum) + charCode;
#       checksum = checksum & 4294967295;
#   }
#   if (checksum < 0) checksum = ~checksum;
#   return checksum;
# };


parser = argparse.ArgumentParser(description="Calculate an AIP schedule checksum and print it out.")
parser.add_argument("--schedule", "-s", help="The AIP schedule file to calculate the checksum for.")
args = parser.parse_args()

aip_file_handler = open(args.schedule,"r")
aip_file = aip_file_handler.read()
aip_file_handler.close()

results = re.search(r"(<colors>.+?<\/colors>)", aip_file, flags=re.MULTILINE|re.DOTALL)
results_group = results.group(1) # There shouldn't be more than one match so we only grab the first
results_text = re.sub(r"(\r\n|\n|\r|\s+)", "", results_group, flags=re.MULTILINE)

checksum = numpy.int32(0)

for char in results_text:
    charCode = ord(char)
    #print("{} = {}".format(char, charCode))
    checksum = numpy.int32(((numpy.left_shift(checksum, 5) - checksum) + charCode))
    #print(checksum)
    checksum = numpy.int32(numpy.bitwise_and(checksum, 4294967295))
    #print(checksum)

if checksum < 0:
    checksum = numpy.int32((numpy.invert(checksum)))

print(checksum)

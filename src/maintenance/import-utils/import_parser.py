#!/usr/bin/env python

import re
import sys
import os.path
from os import path

params = sys.argv.copy()

if len(params) == 1:
  gettrace = getattr(sys, 'gettrace', None)
  if gettrace:
    params.append('./downloads/random.quotes.cbridge.utf8.converted')

args_nbr = len(params)
assert (args_nbr > 1), "Missing filename parameter!!!"

def process_line(hfp, rfp, line):
  m = re.search("^\"(.*)\"\s+\-\s+(.*)$", line)
  if m:
    hfp.write("%s|%s\n" %(m.group(1), m.group(2)))
    # print(m.group(1))
    # print(m.group(2))
    # exit(0)
    rtn = True
  else:
    rfp.write(line)
    rtn = False
  return rtn

def process_file(fn):
  cnt = 0
  hfn = fn + '.handled'
  with open(hfn, "w") as handled:
    rfn = fn + '.rejected'
    with open(rfn, "w") as rejected:
      with open(fn) as inp:
        line = inp.readline()
        while line:
          cnt +=1
          if (cnt % 500) == 0:
            print('processed %d lines' % cnt)
          process_line(handled, rejected, line)
          line = inp.readline()
  return cnt

for i in range(1, args_nbr):
  fn = params[i]
  if path.exists(fn):
    lines = process_file(fn)
    print('processed %d lines' % lines)
  else:
    sys.stderr.write("File not found: %s !!\n" % fn)

# with open(filepath) as fp:
#    line = fp.readline()
#    cnt = 1
#    while line:
#        print("Line {}: {}".format(cnt, line.strip()))
#        line = fp.readline()
#        cnt += 1

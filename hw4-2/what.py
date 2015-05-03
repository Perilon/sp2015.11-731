import os
os.chdir("/home/andrew/sp2015.11-731/hw4-2")
import utils

parse_file = "/home/andrew/sp2015.11-731/hw4-2/data/dev+test.parses"
infile = "/home/andrew/sp2015.11-731/hw4-2/data/sample20-2.input"

def get_feature_list(infile, parse_file, gold=None, parse_features=False):
  parses = utils.read_dep_trees(parse_file)
  with open(infile) as f:
    for n, line in enumerate(f):
      if not line.strip(): continue
      print parses

get_feature_list(infile, parse_file)

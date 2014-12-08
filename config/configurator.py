import re

class Configurator():
  def __init__(self, filename):
    cfgFile = open(filename, "r")
    cfg = cfgFile.read()
    cfgFile.close()
    
    self.configs = []
    
    self.parse(cfg)
    
  def parse(self, cfg):
    print "Parsing Config!"
    lines = re.findall("\{(.*)\}", cfg, re.X | re.M)
    if(lines):
      print "Match 1"
      print lines[0]
    for line in lines:
      entry = {}
      print "Created Blank Entry"
      strings = re.findall(r"'(\w+)': '(\w+)';", line, re.X)
      if(strings):
        print "Match 2"
      for string in strings:
        print "Attempting Match 2"
        match = re.match("'(.*)': '(.*)';", item, re.X)
        print "Match 3"
        if(match):
          print "Matched Sucessfully"
          isInt = re.match("\d+", match.group(2), re.X)
          if(isInt):
            print "Found Integer Value:"
            identifier = match.group(1)
            value = match.group(2)
            entry[identifier] = int(value)
          else:
            print "Found String Value"
            identifier = match.group(1)
            value = match.group(2)
            entry[identifier] = value
          self.configs.append(entry)
        else:
          print "Did Not Match!"
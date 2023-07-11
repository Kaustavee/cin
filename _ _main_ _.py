import sys 
from .import which
args = argv[1:]
for arg in args :
    path = which(arg)
    print(path if not None else f"{arg} Not found")
import pip

def install(package, version=False):
    if version is False:
        pip.main(['install', package])
    else:
        pip.main(['install', package+"=="+version])



d = {}
with open("dependencies.txt") as f:
    for line in f:
       (key, val) = line.split()
       d[key] = val

modules = d

for m in modules.keys():
    try:
        __import__(m)
    except ImportError:
        print("Cannot import %s" % m)
        print("Installing...")
        if d[m] != "new":
            install(m)
        else:
            install(m, d[m])

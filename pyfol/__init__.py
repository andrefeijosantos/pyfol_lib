import os, sys

def pf_help():
    os.system("start pyfol/assets/home.html")

def clearCache():
    file = open("pyfol/assets/cache.txt", "w")
    file.write("")

print("PyFOL Prover included - version 1.0")
print("Call function \"pf_help()\" to access documentation.\n")

found = False
fin = open("pyfol/assets/cache.txt", "r")
for line in fin:
    if line.removesuffix("\n") == sys.argv[0]:
        found = True
        break

if not found: 
    pf_help()
    app = open("pyfol/assets/cache.txt", "a")
    app.write(sys.argv[0]+"\n")


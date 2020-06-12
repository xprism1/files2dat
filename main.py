'''
files2dat v1.3 by xprism 2020

main.py: Main program
'''

print("  /*********************************/")
print(" /  files2dat v1.3 by xprism 2020  /")
print("/*********************************/")
print("WARNING: Do not put the python scripts or the datfile inside the folder with files you want to add. Quit the program now and move them out if so.")

# Getting user information
# For testing: path = gold/ and datfilename = DSJ.dat
path = str(input("Enter the path to the folder containing files (and files only), e.g. C:\\roms: "))
datfilename = str(input("Enter the path to the datfile, e.g. C:\\datfile.dat: "))
datfileoutput = str(input("Enter the path to the output file, e.g. C:\\datfile_modified.dat: "))

global_entries = str(input("Do you want to batch add entries for all the files? E.g. status = 'verified'. [y/n]: "))
add_more = True
glo = {}
if global_entries == "y":
    while(add_more == True):
        key = str(input("Enter the entry key, e.g. if you want to have status = 'verified', enter status: "))
        value = str(input("Enter the entry value, e.g. if you want to have status = 'verified', enter verified (without the quotes): "))
        cont = str(input("Continue adding entries? [y/n]: "))
        glo[key] = value
        if cont == 'n':
            add_more = False

sort = str(input("Do you want to sort the datfile by set name? i.e. sort by the name in <game> [y/n]: "))
if sort == "y":
    sortedname = str(input("Enter the filename for the sorted datfile: "))

# Reading datfile
from bs4 import BeautifulSoup
datfile = open(datfilename, "r")
xml_data = datfile.read()
soup = BeautifulSoup(xml_data, 'lxml')
        
from getfileinfo import fileinfo
print("Getting file info...")
info = fileinfo(path)


print("Adding information to datfile...")
from pathlib import Path
from add2dat import add_set
from add2dat import add_rom
for i in range(len(info)):
    # Removing file extension from <game name=' '> and <description> (only name='' has file extension)
    x = info[i].get('name')
    filename = Path(x)
    filename_wo_ext = str(filename.with_suffix(''))
    
    add_set(datfilename, soup, filename_wo_ext, filename_wo_ext)
    add_rom(datfilename, soup, filename_wo_ext, info[i], glo)
print("Datfile modified successfully.")

from lxml import etree

# Resetting the already existing indentation, allowing the output to generate its own indentation correctly
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(datfilename, parser)

# Reformat datfile so the newly added entries aren't all squished together
with open(datfileoutput, "wb") as f:
    tree.write(f, pretty_print=True)

# Remove <html>, </html>, <body>, </body>
from striphtmltags import strip_tags
strip_tags(datfileoutput)

# Reformat datfile to use indentation level of a typical datfile
from xmlformatter import process
process(datfileoutput, 2, ['xml'])

# Removing empty lines from above output
with open(datfileoutput, 'r+') as fd:
    lines = fd.readlines()
    fd.seek(0)
    fd.writelines(line for line in lines if line.strip())
    fd.truncate()

# Removes the non-pretty printed, modified original file
import os
os.remove(datfilename)

# Sorts by set name
import sys
import subprocess
if sort == "y":
    # Detects if platform is windows or linux, then runs xmlsort.py in python2
    if sys.platform == 'win32':
        python2_command = ["C:\\Python27\\python.exe", "xmlsort.py", datfileoutput, sortedname, "-x", "header"]
    if sys.platform == 'linux':
        python2_command = ["python2", "xmlsort.py", datfileoutput, sortedname, "-x", "header"]
    process = subprocess.Popen(python2_command, stdout=subprocess.PIPE)
    output, error = process.communicate()
      
# Adds <!DOCTYPE> and <?xml version> to start of output file
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

# Removes first line from datfileoutput (<?xml version>)
with open(datfileoutput, 'r') as fin:
    data = fin.read().splitlines(True)
with open(datfileoutput, 'w') as fout:
    fout.writelines(data[1:])

line_prepender(datfileoutput, '<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd">')
line_prepender(datfileoutput, '<?xml version="1.0"?>')
if sort == "y":
    line_prepender(sortedname, '<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd">')
    line_prepender(sortedname, '<?xml version="1.0"?>')
print("Datfile prettified successfully.")

if sort == "y":
    print("Output file (unsorted): " + datfileoutput)
    print("Output file (sorted): " + sortedname)
else:
    print("Output file: " + datfileoutput)

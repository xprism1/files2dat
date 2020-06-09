from bs4 import BeautifulSoup

def add_set(datfile, soup, game_name, description): # adds a new entry: <game name = "pokemon"> <description = "pokemon"> </description> </game>
    name = soup.new_tag("game")
    name.attrs["name"] = game_name
    desc = soup.new_tag("description")
    desc.string = description
    soup.game.insert_after(name)
    game = soup.find("game", {"name": game_name})
    game.append(desc)
    
    datfile_added = str(soup)
    with open(datfile, "w+") as f:
        f.write(datfile_added) # writes modifications to datfile
    
def add_rom(datfile, soup, game_name, dict, glo): # adds a new entry under <game name = "pokemon">: <rom crc="123" size="123> </rom>
    rom = soup.new_tag("rom")
    rom.attrs["name"] = dict["name"]
    rom.attrs["size"] = dict["size"]
    rom.attrs["crc"] = dict["crc32"]
    rom.attrs["md5"] = dict["md5"]
    rom.attrs["sha1"] = dict["sha1"]
    
    # Batch added entries
    if len(glo) != 0:
        keys = []
        for i in glo.keys():
            keys.append(i)
        for i in keys:
            rom.attrs[i] = glo[i]
        
    game = soup.find("game", {"name": game_name})
    game.append(rom)
    
    datfile_added = str(soup)
    with open(datfile, "w+") as f:
        f.write(datfile_added) # writes modifications to datfile

# Getting user information
print("files2dat v1.1 by xprism")
print("WARNING: Do not put the python scripts or the datfile inside the folder with files you want to add. Quit the program now and move them out if so.")
path = str(input("Enter the path to the folder containing files (and files only), e.g. C:\\Users: "))
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

datfile = open(datfilename, "r")
xml_data = datfile.read()
soup = BeautifulSoup(xml_data, 'lxml')
        
from getfileinfo import fileinfo # import fileinfo function from getfileinfo.py
print("Getting file info...")
info = fileinfo(path)


print("Adding information to datfile...")
from pathlib import Path
for i in range(len(info)):
    # Removing file extension from <game name=' '> and <description> (only name='' has file extension)
    x = info[i].get('name')
    filename = Path(x)
    filename_wo_ext = str(filename.with_suffix(''))
    
    add_set(datfilename, soup, filename_wo_ext, filename_wo_ext)
    add_rom(datfilename, soup, filename_wo_ext, info[i], glo)

print("Datfile modified successfully.")

from lxml import etree

# Resetting the already existing indentation, allowing the output to generate it's own indentation correctly
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(datfilename, parser)

# Reformat datfile
with open(datfileoutput, "wb") as f:
    tree.write(f, pretty_print=True)
    
print("Datfile prettified successfully.")

# Adds <?xml version> and <!DOCTYPE> to start of output file
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
        
line_prepender(datfileoutput, '<!DOCTYPE datafile PUBLIC "-//Logiqx//DTD ROM Management Datafile//EN" "http://www.logiqx.com/Dats/datafile.dtd">')
line_prepender(datfileoutput, '<?xml version="1.0"?>')

print("Output file: " + datfileoutput)
print("Please open the datfile in a text editor manually, and remove <html>, <body> (at the start of the file) as well as </body>, </html> (at the end of the file).")

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
print("files2dat v1.0 by xprism")
path = str(input("Enter the path to the folder containing files (and files only), e.g. C:\\Users. Please replace each backslash with 2 backslashes! "))
datfilename = str(input("Enter the path to the datfile, e.g. C:\\datfile.dat. Please replace each backslash with 2 backslashes! "))

global_entries = str(input("Do you want to batch add entries for all the files? E.g. status = 'verified'. [y/n] "))
add_more = True
glo = {}
if global_entries == "y":
    while(add_more == True):
        key = str(input("Enter the entry key, e.g. in status = 'verified', status is the key and 'verified' is the value. "))
        value = str(input("Enter the entry value, e.g. in status = 'verified', status is the key and 'verified' is the value. "))
        cont = str(input("Continue adding entries? [y/n] "))
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
print("Please open the datfile in a text editor manually, and remove <html> (at the start of the file) as well as </html> (at the end of the file).")

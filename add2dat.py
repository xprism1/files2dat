'''
files2dat v1.2 by xprism 2020

add2dat.py: Adds information to datfile
'''

# Add a new entry: <game name = "pokemon"> <description = "pokemon"> </description> </game>
def add_set(datfile, soup, game_name, description):
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

# Add a new entry under <game name>: <rom crc="123" size="123> </rom>
def add_rom(datfile, soup, game_name, dict, glo):
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

'''
Code to test add_set and add_rom:
    
add_set("DSJ.dat", soup, "Pokemon - Gold Version 1997 (v3.01) (USA, Europe)", "Pokemon - Gold Version 1997 (v3.01) (USA, Europe)")
dict = {'name': 'Poke', 'size': '123', 'crc': '123ab'}
add_rom("DSJ.dat", soup, "Pokemon - Gold Version 1997 (v3.01) (USA, Europe)", dict)
'''
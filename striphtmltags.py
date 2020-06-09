'''
files2dat v1.2 by xprism 2020

striphtmltags.py: Strips <html>, </html>, <body> and </body> tags out of datfile
'''

def strip_tags(datfile):
    with open(datfile,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if "<html>" not in line:
                f.write(line)
        f.truncate()
        
    with open(datfile,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if "</html>" not in line:
                f.write(line)
        f.truncate()
        
    with open(datfile,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if "<body>" not in line:
                f.write(line)
        f.truncate()
        
    with open(datfile,"r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if "</body>" not in line:
                f.write(line)
        f.truncate()
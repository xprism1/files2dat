import os
def size(filename):
    st = os.stat(filename)
    return st.st_size

import binascii
def crc32(filename):
    buf = open(filename,'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf

import hashlib
def md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def sha1(filename):
    # BUF_SIZE is totally arbitrary, change for your app!
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def fileinfo(path):
    list_of_files = os.listdir(path)
    dir = []
    for i in list_of_files:
        path_to_file = os.path.join(path,i)
        size_output = size(path_to_file)
        crc32_output = crc32(path_to_file)
        md5_output = md5(path_to_file)
        sha1_output = sha1(path_to_file)
        dir.append({'size': size_output, 'name': i, 'crc32': crc32_output, 'md5': md5_output, 'sha1': sha1_output})
    return dir
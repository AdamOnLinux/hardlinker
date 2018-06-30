#!/usr/bin/env python3
import os, hashlib

### DIRECTORY OF IMAGES
dir = "./network_share"

### IMAGE EXTENTIONS
image_exts = ("jpg", "jpeg", "png", "tiff", "gif")

### INITALIZE
image_hashes = {}
image_sizes = {}
total_size = 0
total_files = 0
total_duplicates = 0

### HUMAN READABLE SIZES
def size_format(b):
    if b < 1000:
              return '%i' % b + 'B'
    elif 1000 <= b < 1000000:
        return '%.1f' % float(b/1000) + 'KB'
    elif 1000000 <= b < 1000000000:
        return '%.1f' % float(b/1000000) + 'MB'
    elif 1000000000 <= b < 1000000000000:
        return '%.1f' % float(b/1000000000) + 'GB'

### SCAN DIRECTORY RECURSIVELY 
### GATHER IMAGE PATH AND FILE SIZE
for root, dir, files in os.walk(dir, topdown=False):
   for name in files:
       full_path = os.path.join(root, name)
       # check for image extenions       
       if full_path.lower().endswith(image_exts): 
           file_size = os.path.getsize(full_path)
           total_files += 1
           # append file to array with size as key           
           if file_size in image_sizes: 
               image_sizes[file_size] = image_sizes[file_size] + "|" + full_path
           else:
               image_sizes[file_size] = full_path

### LOOP THROUGH IMAGE SIZE ARRAY
### CREATE ARRAY WITH UNIQUE CHECKSUM KEY
for size,file_path in image_sizes.items():
    
    if len(file_path.split('|')) > 1:
        for file_path_split in file_path.split('|'):
            # create md5 checksum for images
            file_hash = hashlib.md5(open(file_path_split, 'rb').read()).hexdigest()
            if file_hash in image_hashes:
                image_hashes[file_hash] = image_hashes[file_hash] + "|" + file_path_split
            else:
                image_hashes[file_hash] = file_path_split

## LOOP IMAGES WITH SAME CHECKSUM
## REMOVE DUPLICATES THAT SHARE SAME INODE
## LEAVE THE PRIMARY FILE AND HARD LINK REMOVED FILES TO PRIMARY
for image_hash,file_path in image_hashes.items():
    files = file_path.split('|')
    if len(files) > 1:
        x = 0
        for file in files:
            # inode of primary file
            primary_inode = os.stat(files[0]).st_ino
            # inode of duplicate file
            current_inode = os.stat(files[x]).st_ino
            # keep primary and delete files with duplicate inodes 
            if x != 0 and primary_inode != current_inode: 
                    if os.path.isfile(file) and os.path.isfile(files[0]):
                        os.remove(file)
                        os.link(files[0], file)
                        total_duplicates += 1
                        total_size += os.path.getsize(file)
                        # print each duplicate file removed and where it was hardlinked 
                        print("removed ({}) -> hardlink ({})".format(file,files[0]))                    
            x += 1

### PRINT RESULTS
if total_size == 0:
    print("No duplicate images found.")
else:
    total_size = size_format(total_size)
    print("\nImages found: {}\nDuplicates removed: {}\nSpace removed: {}\n".format(total_files, total_duplicates, total_size))
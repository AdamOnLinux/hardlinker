# Hardlink Duplicate Photos.

### Problem: 
You have a folder that has a ton of duplicate photos that are scattered all of the place!

### Solution:
I created a python script that will delete all your duplicate photos but leave the filenames and directories in place pointing to one copy of the photo, which is all you need.

![Screenshot](https://i.imgur.com/zsjNMDJ.png)

### How does it work?
1. Find all images that are the same size.

2. Create a checksum of those images to tell which are duplicates regardless of the filename.

3. Delete all duplicates images and hardlink the duplicate files to the one original file.

### FAQ

1. What the hell is a hardlink? **A hard link is merely an additional name for an existing file on your computer.**

2. What if I edit a photo and reupload? **The newly uploaded photo would be unique and not a duplicate.**

3. Can I remove the "original file" and not break the hardlink files? **Yes, saying the original file is just an easier way to explain. It actually links to an inode on the disk where the data is stored for the photo.**

4. Can I run this multiple times? **Yes, Script will find all duplicates and hardlink to original file every time it runs.**

5. Is there any limits or things you would do differently with update? **I would use inotify utility to run a script on any new file or modifcation. That way we would have no duplicates in real time.**

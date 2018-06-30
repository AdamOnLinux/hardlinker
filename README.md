# Hard Link Duplicate Photos.

### Problem: 
You have a folder that has a ton of duplicate photos that are scattered all over the place!

### Solution:
I created a python script that will delete all your duplicate photos but leave the filenames and directories as is, using the magic of hard links.

![Screenshot](https://i.imgur.com/zsjNMDJ.png)

### How does it work?
1. Find all images that are the same size.

2. Create a checksum of those images to find which are duplicates regardless of the filename.

3. Delete all duplicate images and hardlink the duplicate files to the original file.

### FAQ

1. What the hell is a hardlink? **A hard link is merely an additional name for an existing file on your computer.**

2. What if I edit a photo and reupload? **The newly uploaded photo would be unique and not a duplicate.**

3. Can I remove the "original file" or remove hard link files and not break things? **Yes, the "original file" is just an easier way to explain. It actually links to data on the disk where the photo is stored, not a file.**

4. Can I run this multiple times? **Yes, the script will find all duplicates and hardlink to original file every time it runs.**

5. Anything you would do differently? **I would use the linux inotify utility to run a script when any new file or modifcation is detected. That would remove duplicates in real time.**

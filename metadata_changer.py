import os
import sys
import eyed3
argLength = len(sys.argv)
if argLength == 3:
    arg = sys.argv[1]
    path = sys.argv[2]
else:
    print("metadata_changer.py [MODE] /path/to/directory")
    print("Modes:general, album")
    print("General - Adds metadata from file name in a form (Artist - Name) to .mp3 file")
    print("Album - Same as General, but also adds Album name from current folder name")
    exit(1)

if path[-1] == "/":
    path = path[:-1]

files = os.listdir(path)

for name in files:
    if name.endswith(".mp3"):
        print(os.path.join(path, name))
        audiofile = eyed3.load(os.path.join(path, name)) 
        removeMp3 = name.split(".mp3")
        nameSeparated = removeMp3[0].split(" - ", 1)
        audiofile.tag.artist =  nameSeparated[0]
        if arg == "album":
            audiofile.tag.album = os.path.basename(path)
        audiofile.tag.title = nameSeparated[1]
        audiofile.tag.save(version=eyed3.id3.ID3_DEFAULT_VERSION,encoding='utf-8')
        exit

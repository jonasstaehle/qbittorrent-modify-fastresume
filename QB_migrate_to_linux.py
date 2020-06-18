import os
import bencode
import re

for file in os.listdir():
    if file.endswith(".fastresume"):
        file_path_name = os.path.join(tor_dir, file)
        torrent = bencode.bread(file_path_name)
        save_path_orig = (torrent['save_path'])
        
        save_path_new = re.sub("find", "replace", save_path_orig)
        torrent['save_path']=save_path_new
        torrent['qBt-savePath']=save_path_new
        bencode.bwrite(torrent, file_path_name)
        print(torrent['save_path'])

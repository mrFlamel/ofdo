import requests
import platform
import os
import stat
import sys

def kontrolli_uuendusi(praegune_versioon, sihtkaust):
    try:
        r = requests.get("https://api.github.com/repos/mrflamel/ofdo/releases/latest")
        release_data = r.json()
        
        if release_data["tag_name"] != praegune_versioon:
            print("Laen alla uue versiooni " + release_data["tag_name"] + " praeguse " + praegune_versioon + " asemel...")
            if platform.system() == "Linux":
                filename = "ofdo-" + release_data["tag_name"] + "-linux"
            elif platform.system() == "Darwin":
                filename = "ofdo-" + release_data["tag_name"] + "-macos"
            elif platform.system() == "Windows":
                filename = "ofdo-" + release_data["tag_name"] + "-win.exe"
            
            uus_versioon = requests.get("https://github.com/mrflamel/ofdo/releases/latest/download/" + filename)
            with open(sihtkaust / filename, mode="wb") as file:
                file.write(uus_versioon.content)
                
            mode = os.stat(sihtkaust / filename).st_mode
            mode |= (mode & 0o444) >> 2
            os.chmod(sihtkaust / filename, mode)
            
            print('Uus fail nimega "' + filename + '" on salvestatud!')
            sys.exit()
            
        
    except requests.ConnectionError:
        return
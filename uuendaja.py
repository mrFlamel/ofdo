from requests import get, ConnectionError
import platform
import os
import sys
from tqdm import tqdm

def kontrolli_uuendusi(praegune_versioon, sihtkaust):
    try:
        r = get("https://api.github.com/repos/mrflamel/ofdo/releases/latest")
        release_data = r.json()
        
        if release_data["tag_name"] != praegune_versioon:
            print("UUS VERSIOON " + release_data["tag_name"] + " ON SAADAVAL!")

            # MUUDATUSTE NIMEKIRI
            muudatused = release_data["body"]
            if platform.system() == "Linux" or platform.system() == "Darwin":
                print("\n" + muudatused.replace("\r\n", "\n") + "\n")

            print("Laen alla uue versiooni " + release_data["tag_name"] + " praeguse " + praegune_versioon + " asemel...")
            if platform.system() == "Linux":
                filename = "ofdo-" + release_data["tag_name"] + "-linux"
            elif platform.system() == "Darwin":
                filename = "ofdo-" + release_data["tag_name"] + "-macos"
            
            if os.path.isfile(sihtkaust / filename):
                print('Fail "' + filename + '" on juba alla laetud!')
                sys.exit()
            
            uus_versioon = get("https://github.com/mrflamel/ofdo/releases/latest/download/" + filename, stream=True)
            total_size = int(uus_versioon.headers.get("content-length", 0))
            block_size = 1024
            with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
                with open(sihtkaust / filename, "wb") as file:
                    for data in uus_versioon.iter_content(block_size):
                        progress_bar.update(len(data))
                        file.write(data)
            if total_size != 0 and progress_bar.n != total_size:
                raise RuntimeError("Faili allalaadimine ebaõnnestus :(")
                
            mode = os.stat(sihtkaust / filename).st_mode
            mode |= (mode & 0o444) >> 2
            os.chmod(sihtkaust / filename, mode)
            
            print('Uus fail nimega "' + filename + '" on salvestatud!')
            sys.exit()
            
        
    except ConnectionError:
        return
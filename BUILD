/usr/bin/python3 -m venv venv

pyinstaller --onefile  ofdo.py kirjakohad.py laulud.py pühad.py slaidigeneraatorid.py --add-data=piibel.xml:. --add-data=laulud:laulud --copy-metadata odfdo --collect-all odfdo --hidden-import=odfdo.templates --add-data="07122025 Jumalateenistus originaal.odp":.

Vajalikud packagid:
pyinstaller
odfdo
python-dateutil

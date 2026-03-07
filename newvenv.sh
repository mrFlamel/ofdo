rm -rf venv

/usr/bin/python3 -m venv venv

source venv/bin/activate

pip install odfdo pyinstaller python-dateutil requests charset-normalizer==2.1.0

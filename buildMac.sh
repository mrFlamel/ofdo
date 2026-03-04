quickemu --vm ~/QUICKEMU/macos-big-sur.conf

ssh -p 22220 mycomputer@localhost "
cd ~/Desktop
mkdir KRAAM
exit
"

scp -P 22220 ofdo.spec ofdo.py kirjakohad.py laulud.py piibel.xml pyhad.py slaidigeneraatorid.py "07122025 Jumalateenistus originaal.odp" mycomputer@localhost:~/Desktop/KRAAM
scp -P 22220 -r laulud mycomputer@localhost:~/Desktop/KRAAM

ssh -p 22220 mycomputer@localhost "
cd ~/Desktop/KRAAM
/Library/Frameworks/Python.framework/Versions/3.12/bin/pyinstaller ofdo.spec
exit
"
scp -P 22220 mycomputer@localhost:~/Desktop/KRAAM/dist/ofdo ./dist/ofdoMAC

ssh -p 22220 -t mycomputer@localhost "
cd ~/Desktop
rm -rf KRAAM
sudo shutdown -h now
"

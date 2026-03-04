source venv/bin/activate

printf '\n\n\nLINUX:\n'
pyinstaller ofdo.spec

printf '\n\n\nWINDOWS:\n'
wine ~/.wine/drive_c/users/jakob-luhamets/AppData/Local/Programs/Python/Python312/Scripts/pyinstaller.exe ofdo.spec

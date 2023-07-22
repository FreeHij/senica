@echo off
pip install pyinstaller
echo put server.py in the same directory as compile script and the press any button
pause
curl -LO http://185.87.192.150/favicon.ico
pyinstaller -F -i favicon.ico server.py
del favicon.ico
cd dist
move /-Y server.exe ..
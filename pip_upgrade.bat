@echo off
set current_dir=%~dp0

:: 升级 pip
"%current_dir%\Python-3.12.4\python.exe" -m pip install --upgrade pip

:: 安装 requests
"%current_dir%\Python-3.12.4\python.exe" -m pip install requests

:: 安装 pyinstaller
"%current_dir%\Python-3.12.4\python.exe" -m pip install pyinstaller

:: 安装 beautifulsoup4
"%current_dir%\Python-3.12.4\python.exe" -m pip install beautifulsoup4

:: 安装 tkinterdnd2
"%current_dir%\Python-3.12.4\python.exe" -m pip install tkinterdnd2

:: 安装 qrcode
"%current_dir%\Python-3.12.4\python.exe" -m pip install qrcode[pil]

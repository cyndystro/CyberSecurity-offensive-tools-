@echo off

pip install numpy
pip install pandas
pip install matplotlib
pip install time
pip install keyboard

start slither.yeah.py
timeout /t 600
taskkill /im python.exe /f
python chart_generator.py
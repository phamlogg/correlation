import os
import sys

pip = os.system('python -m pip --version')

if pip != 0:
	os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')
	os.system('python get-pip.py')

try:
	os.system('pip install pipreqs')
except:
	print('Error!')

filepath = os.path.abspath('correlation-main')

try:
	req = os.system(f'pipreqs --encoding utf-8')
except Exception as e:
	print(e)
	
if req == 0:
	try:
		os.system('pip install -r requirements.txt')
	except FileNotFoundError:
		print('requirements.txt not found!')

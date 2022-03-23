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


req = os.system('pipreqs .')

if req == 0:
	try:
		os.system('pip install -r requirements.txt')
	except FileNotFoundError:
		print('requirements.txt not found!')


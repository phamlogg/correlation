import os
import platform

if platform.system() == 'Windows':
    os.system(f'python3 \Users\*\*\correlation\correlation.py \Users\*\*\correlation\Data.xlsx')
else:
    os.system(f'python3 /Users/*/*/correlation/correlation.py /Users/*/*/correlation/Data.xlsx')
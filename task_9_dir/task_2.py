# Task 2
# The sys module.
#  The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change it from within Python?
#  If so, does it affect where Python looks for module files? Run some interactive tests to find it out.
import sys
import os
print(sys.path)
print("__________________________________")
print(os.environ)

print("__________________________________")
print(os.environ['PYTHONPATH'].split(os.pathsep))
# os.environ['PYTHONPATH'].update('C:\\PYTHON\\BEETROOT\\Beetroot_Homeworks;C:\PYTHON\BEETROOT\Lesson9_addpath;C:\\Program Files\\JetBrains\\PyCharm 2021.3.2\\plugins\\python\\helpers\\pycharm_matplotlib_backend;C:\\Program Files\\JetBrains\\PyCharm 2021.3.2\\plugins\\python\\helpers\\pycharm_display;C:\\Program Files\\JetBrains\\PyCharm 2021.3.2\\plugins\\python\\helpers\\third_party\\thriftpy;C:\\Program Files\\JetBrains\\PyCharm 2021.3.2\\plugins\\python\\helpers\\pydev')
# my attempt to make changes through updating dictionary values with key: PYTHONPATH
print("__________________________________")

print(os.environ.get('PYTHONPATH', '').split(os.pathsep))
#set PYTHONPATH=C:\\PYTHON\pythonproject
sys.path.insert(1,'C:\PYTHON\pythonproject')  # change sys.path by affecting on the list.
print(sys.path)
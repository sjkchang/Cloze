import os
print('__file__', __file__)
print('dirname', os.path.dirname(__file__))
print('abspath', os.path.abspath(os.path.dirname(__name__)))

basedir = os.path.abspath(os.path.dirname(__name__))

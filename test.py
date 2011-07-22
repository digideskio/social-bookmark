import os.path

print os.path.abspath(__file__)

print os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')


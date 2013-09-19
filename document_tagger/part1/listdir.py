import os


path = './'
dirs = os.listdir(path)

for file in dirs:
    if not file.endswith('swp') and not file.endswith('pyc'):
        #print file
        print os.path.join(path, file)
    

import os
try: 
    os.system('wget https://www.robots.ox.ac.uk/~vgg/data/flowers/17/17flowers.tgz')
except: 
    os.system('apt-get install wget')

os.system('tar -xvzf 17flowers.tgz')

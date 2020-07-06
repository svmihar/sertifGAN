import os

os.system('drive add_remote "models/default/"')
os.system('drive add_remote "results/default/"')
os.system('mv results/default/* results/uda')

import os


command = '''stylegan2_pytorch --data images/ \
    --batch-size 3 \
    --gradient-accumulate-every 5 \
    --network-capacity 16'''
os.system(command)

import os


command = '''stylegan2_pytorch --data images/ \
    --batch-size 1 \
    --image-size 512 \
    --gradient-accumulate-every 5 \
    --attn-layers 1 \
    --network-capacity 16'''
os.system(command)

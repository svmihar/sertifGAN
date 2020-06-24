import os


command = """stylegan2_pytorch --data images/ \
    --batch-size 11 \
    --gradient-accumulate-every 1 \
    --cl-reg \
    --attn-layers 1 \
    --network-capacity 20"""
os.system(command)

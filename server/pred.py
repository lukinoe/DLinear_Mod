import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


from models.DLinear_Merge_Seq2Seq_Timeenc_M  import Model
import torch
import numpy as np 

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__



device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

d = dotdict()
d.seq_len = 500
d.pred_len = 100
individual = False
channels = 5

model = Model(d)
model.to(device)

model.load_state_dict(torch.load("C:/Users/lukas/OneDrive - Johannes Kepler Universität Linz/Projekte/DLinear/checkpoints/best/checkpoint.pth", map_location=torch.device(device)))

print("number of parameters:", sum(p.numel() for p in model.parameters()))

y_hat = model(torch.randn(1, 500, 5).to(device), torch.randn(1, 100, 5).to(device))

print(y_hat.detach().numpy())
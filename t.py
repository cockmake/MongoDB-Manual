import torch
t = torch.randn((3, 4, 4))
print(t[None].shape)
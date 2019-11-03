import torch
import torch.nn as nn
#import torch.nn.functional as F

class EMLLoss(nn.Module):
    def __init__(self):
        super(EMLLoss, self).__init__()
        self.eps = 1e-6

    def KL_loss(self, input, target):
        input = input / input.sum() 
        target = target / target.sum()
        loss = (target * torch.log(target/(input+self.eps) + self.eps)).sum()
        return loss 

    def CC_loss(self, input, target):
        input = (input - input.mean()) / input.std()  
        target = (target - target.mean()) / target.std()
        loss = (input * target).sum() / (torch.sqrt((input*input).sum() * (target * target).sum()))
        loss = 1 - loss
        return loss

    def NSS_loss(self, input, target):
        ref = (target - target.mean()) / target.std()
        input = (input - input.mean()) / input.std()
        loss = (ref*target - input*target).sum() / target.sum()
        return loss 

    def forward(self, input, fixs, target):
        kl_loss = self.KL_loss(input, target)
        cc_loss = self.CC_loss(input, target)
        nss_loss = self.NSS_loss(input, fixs)
        return kl_loss + cc_loss + nss_loss

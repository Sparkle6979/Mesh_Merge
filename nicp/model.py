import torch

class NICPmodel():
    def __init__(self,num_points):
        self.parameter = torch.autograd.Variable(torch.zeros(num_points,3),requires_grad=True)

    def predit(self,points,mean = False):
        if mean is False:
            params = self.parameter
        else:
            params = self.parameter.mean(0).reshape(1,-1)
        points = torch.tensor(points)
        return params + points
        
    def params(self):
        return self.parameter
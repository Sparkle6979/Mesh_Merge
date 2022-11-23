import torch

"""
params: train parameters
input: [n,3] mesh vertices info
edges: [m,2] the connected relationship
mask: [k,] the mask of input vertices
gt: [n,3] gt mesh vertices
"""
def train(nicp_model,params,input,edges,mask,gt,optimizer):

    
    edges = torch.tensor(edges)
    id0,id1 = edges.unbind(1)
    rid0 = id0.detach().numpy()
    rid1 = id1.detach().numpy()
    
    
    for iter in range(params['iters']):
        input = torch.tensor(input)
        output = nicp_model.predit(input)
        delta = output[mask] - torch.from_numpy(gt)
        delta = (delta ** 2).sum(-1)
        
        # loss_data = GMRobustError(delta,radius,True).mean()
        loss_data = params['data_weight']*delta.mean()
        loss_param = params['param_weight']*(nicp_model.params()**2).sum(-1).mean()

        
        v00,v01 = input[rid0],input[rid1]
        v10,v11 = output[rid0],output[rid1]

        loss_edge = ((v00 - v01).norm(dim=1, p=2) - (v10 - v11).norm(dim=1, p=2)) ** 2.0
        loss_edge = params['edge_weight']*loss_edge.mean()

        loss_k = (((v00-v01) - (v10-v11)).norm(dim=1, p=2)) ** 2.0
        loss_k = params['k_weight']*loss_k.mean()
        

        loss = loss_data + loss_param + loss_edge + loss_k
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # if not iter % ep_iter:
        #     print('iter(%d)\t, : loss_sum: %.4f, loss_data: %.4f, loss_param: %.4fm, loss_edge: %.4f, loss_k: %.4f'%(iter,loss.item(),loss_data.item(),loss_param.item(),loss_edge.item(),loss_k.item()))

    return 'success'
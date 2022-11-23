import torch
import torch.nn as nn
import numpy as np

import trimesh

"mesh : Trimesh mesh obj"
def getedge(mesh,vertices):
    edges = mesh.edges_unique
    return [edge for edge in edges if (edge[0] in vertices and edge[1] in vertices)]


"""
mesh: Trimesh mesh obj
vertices: [m,] mesh vertices
"""
def get_connections(mesh,vertices):
    edges = torch.tensor(np.array(getedge(mesh,vertices)))
    id0,id1 = edges.unbind(1)
    id0 = id0.detach().numpy()
    id1 = id1.detach().numpy()

    rid0 = [vertices.index(id) for id in id0]
    rid1 = [vertices.index(id) for id in id1]
    return list(zip(rid0,rid1))



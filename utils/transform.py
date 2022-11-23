import numpy as np

###################################################################################################
# align source mesh to target mesh
# min ||target - (s*source*R + t)||^2
# input: source, shape = [N,3], source mesh to be aligned
# 		 target, shape = [N,3], target mesh
#		 scale, if True, consider scaling factor for alignment; if False, scale will be set to 1
# output: R, shape = [3,3], rotation matrix
#		  t, shape = [1,3], translation vector
# 		  s, scaling factor
###################################################################################################
def align_source_to_target(source,target,scale = False):

	tar = target.copy()
	sou = source.copy()
	center_tar = tar - np.mean(tar,0) # centralized target mesh
	center_sou = sou - np.mean(sou,0) # centralized source mesh

	W = np.matmul(center_tar.transpose(),center_sou)
	U,S,V = np.linalg.svd(W)
	R = np.matmul(np.matmul(V.transpose(),np.diag([1,1,np.linalg.det(np.matmul(V.transpose(),U.transpose()))])),U.transpose()) # calculate rotation matrix (exclude mirror symmetry)

	if scale:
		R_sou = np.matmul(center_sou,R)
		s = np.sum(R_sou*center_tar)/np.sum(R_sou*R_sou)
	else:
		s = 1

	t = np.mean(tar,0) - s*np.matmul(np.expand_dims(np.mean(sou,0),0),R)

	return R,t,s




def apply_transform(vertices,R,t,scale = 1.0):	
    pcl = [(v.reshape(1,-1).dot(scale).dot(R) + t).flatten() for v in vertices]
    return pcl

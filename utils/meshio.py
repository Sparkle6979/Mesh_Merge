import numpy as np

def write_uv_obj(name,vs,vts,tris,fts,mtl_file,mtl_name):
    with open(name, 'w') as ff:
        ff.write('mtllib %s\n'%mtl_file)
        for v in vs:
            ff.write('v %.6f %.6f %.6f\n'%(v[0],v[1],v[2]))
        ff.write('usemtl %s\n'%mtl_name)
        for v in vts:
            ff.write('vt %.6f %.6f\n'%(v[0],v[1]))
        ff.write('s off\n')
        for fv,ft in zip(tris,fts):            
            ff.write('f %d/%d %d/%d %d/%d\n'%(fv[0]+1,ft[0]+1,fv[1]+1,ft[1]+1,fv[2]+1,ft[2]+1))



def load_obj(name):
    vs = []
    vts = []
    tris = []
    fts = []
    with open(name, 'r') as ff:
        lines = ff.read().split('\n')
        for l in lines:
            if len(l) > 4:
                if l[:2] == 'v ':
                    vs.append(np.array([float(v) for v in l[2:].split()]))
                if l[:2] == 'vt':
                    vts.append(np.array([float(v) for v in l[3:].split()]))
                if l[:2] == 'f ':
                    for fs in l[2:].split():
                        fs = [int(f)-1 for f in fs.split('/')]
                        tris.append(fs[0])
                        fts.append(fs[1])
    vs = np.stack(vs)
    vts = np.stack(vts)
    tris = np.array(tris).reshape(-1, 3)
    fts = np.array(fts).reshape(-1, 3)
    return vs, vts, tris, fts
    

def write_uv_obj(name,vs,vts,tris,fts,mtl_file,mtl_name):
    with open(name, 'w') as ff:
        ff.write('mtllib %s\n'%mtl_file)
        for v in vs:
            ff.write('v %.6f %.6f %.6f\n'%(v[0],v[1],v[2]))
        ff.write('usemtl %s\n'%mtl_name)
        for v in vts:
            ff.write('vt %.6f %.6f\n'%(v[0],v[1]))
        ff.write('s off\n')
        for fv,ft in zip(tris,fts):            
            ff.write('f %d/%d %d/%d %d/%d\n'%(fv[0]+1,ft[0]+1,fv[1]+1,ft[1]+1,fv[2]+1,ft[2]+1))
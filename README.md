# Mesh_Merge
## Dependencies
- numpy
- pytorch
- trimesh
- openmesh

---

## Rigid Transform Part:

### Target： 将 headmesh 与 bodymesh 空间上初步 align

1. 需要 headmesh 与 bodymesh 头部关键点的位置先验信息，如 双眼、鼻子、耳朵等，详见 keypoint_info.md
2. utils/transform.py 下的 align_source_to_target 方法 求解 R,t,scale，详见方法注释

---

## Non-Rigid Transform Part:

### Target：  bodymesh 脖子部分进行非刚性变换，使之更贴合 headmesh 的脖子

1. 需要 bodymesh 脖子部分（仅脖子） 及 脖子与部分上半身 vertices 的 indicate 作为先验信息  (blender)
2. 优化 bodymesh 脖子部分 vertices 的 offset，部分参数说明：
    - **data_weight**：mesh的vertices间距离的loss权重
    - param_weight：offset 参数的 L2正则化 loss权重
    - edge_weight：mesh edge变化前后距离的loss权重
    - **k_weight**：mesh edge变化前后方向的loss权重（平滑过渡）
3. 网络定义 nicp/model.py，训练部分 nicp/train.py

## Others：
**具体流程及操作详见 TEST.py**
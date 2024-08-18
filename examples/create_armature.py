import bpy
from mathutils import *

import numpy as np

C = bpy.context
D = bpy.data
O = bpy.ops







skeleton_tree = {
    'node_names': ['pelvis', 'torso', 'head', 'right_upper_arm', 'right_lower_arm', 'right_hand', 'sword', 'left_upper_arm', 'left_lower_arm', 'shield', 'left_hand', 'right_thigh', 'right_shin', 'right_foot', 'left_thigh', 'left_shin', 'left_foot'],
    'parent_indices': {
        'arr': np.array([-1,  0,  1,  1,  3,  4,  5,  1,  7,  8,  8,  0, 11, 12,  0, 14, 15]), 
        'context': {'dtype': 'int64'}
        },
    'local_translation': {
        'arr': np.array([[ 0.  ,  0.  ,  1.  ],
                        [ 0.  ,  0.  ,  0.24],
                        [ 0.  ,  0.  ,  0.22],
                        [-0.02, -0.18,  0.24],
                        [ 0.  ,  0.  , -0.27],
                        [ 0.  ,  0.  , -0.26],
                        [ 0.74,  0.  ,  0.  ],
                        [-0.02,  0.18,  0.24],
                        [ 0.  ,  0.  , -0.27],
                        [ 0.  ,  0.07, -0.12],
                        [ 0.  ,  0.  , -0.26],
                        [ 0.  , -0.08,  0.  ],
                        [ 0.  ,  0.  , -0.42],
                        [ 0.  ,  0.  , -0.41],
                        [ 0.  ,  0.08,  0.  ],
                        [ 0.  ,  0.  , -0.42],
                        [ 0.  ,  0.  , -0.41]], dtype=np.float32), 
        'context': {'dtype': 'float32'}
        },
    }


node_names = skeleton_tree["node_names"]
parent_indices = skeleton_tree["parent_indices"]["arr"]
local_translation = skeleton_tree["local_translation"]["arr"]






armature = D.objects.get("Armature")


# delete the existing armature, if any
if armature:
    O.object.mode_set(mode="OBJECT")

    armature.select_set(True)
    O.object.delete()


O.object.armature_add(enter_editmode=False, align="WORLD", scale=(1, 1, 1))

armature = C.active_object


print(armature.data)

armature.data.show_names = True



O.object.mode_set(mode="EDIT")
edit_bones = armature.data.edit_bones

# reconfigure root bone
root = edit_bones[0]
root.name = "root"
root.tail = Vector([1, 0, 0])

n_bones = len(node_names)

# create all bones
for name in node_names:
    edit_bones.new(name)
    
for i, name in enumerate(node_names):
    parent_idx = parent_indices[i]
    
    bone = edit_bones.get(name)
    
    if parent_idx == -1:
        bone.tail = Vector(local_translation[i])
        bone.parent = root
        continue
    
    parent_bone_name = node_names[parent_idx]
    parent_bone = edit_bones.get(parent_bone_name)
    
    bone.head = parent_bone.tail
    bone.tail = bone.head + Vector(local_translation[i])
    bone.parent = parent_bone


bpy.ops.object.mode_set(mode="OBJECT")    


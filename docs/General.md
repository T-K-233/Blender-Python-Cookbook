

# General Cookbook

## Get an object from the current scene

```python
cube = D.objects["Cube"]
```

Get currently selected object

```python
cube = C.active_object
```

## Rename object

```python
cube.data.name = "armature"
```


## Set Location of the object

```python
# set cube to be at x = 1 meter, y = 2 meter
cube.location = [1, 2, 0]

# move cube up by 1 meter
cube.location.z += 1

print(cube.location.x, cube.location.y, cube.location.z)
# 1.0 2.0 1.0
```

## Set Local Rotation of the object

### Mode of Rotation

Mode of rotation is one of the following:

- `QUATERNION`, in (w, x, y, z) format
- `XYZ`
- `XZY`
- `YXZ`
- `YZX`
- `ZXY`
- `AXIS_ANGLE`

### Euler angle mode

```python
cube.rotation_mode = "XYX"

# set rotation in x to 1 radian
cube.rotation_euler.x = 1

print(cube.rotation_euler)
# <Euler (x=1.0000, y=-0.0000, z=0.0000), order='XYZ'>
```

### Quaternion mode

```python
cube.rotation_mode = "QUATERNION"

cube.rotation_quaternion.w = 2

print(cube.rotation_quaternion)
# <Quaternion (w=2.0000, x=0.9998, y=0.0000, z=0.0000)>

print(cube.rotation_quaternion.to_euler())
# <Euler (x=0.9271, y=-0.0000, z=0.0000), order='XYZ'>
```

### Axis Angle mode

```python

cube.rotate_axis



```


### Convert between Rotation Modes

Use the following methods

`.to_quaternion()`

`.to_euler()`

`.to_matrix()`


> Note:
> 
> The rotation between each mode is isolated. 

example

```python
cube.rotation_mode = "QUATERNION"

cube.rotation_quaternion.w = 2

print(cube.rotation_quaternion.to_euler())
# <Euler (x=0.9271, y=-0.0000, z=0.0000), order='XYZ'>
print(cube.rotation_euler)
# <Euler (x=1.0000, y=-0.0000, z=0.0000), order='XYZ'>
```



## Update the scene

Sometimes, the scene in the viewport will not get updated after changing object parameters by script. Do this to force an update.

```python
bpy.context.view_layer.update()
```


# Change Mode

```python
# enter object mode (the default mode)
bpy.ops.object.mode_set(mode="OBJECT", toggle=False)

# enter edit mode
bpy.ops.object.mode_set(mode="EDIT", toggle=False)

# enter pose mode
bpy.ops.object.mode_set(mode="POSE", toggle=False)
```




## Create Armature


```python
bpy.ops.object.armature_add(enter_editmode=False, align="WORLD", scale=(1, 1, 1))

# get the newly created armature object
armature = bpy.context.active_object
```


```python


bpy.ops.object.armature_add(enter_editmode=False, align="WORLD", scale=(1, 1, 1))

armature = bpy.context.active_object #get the armature object

bpy.ops.object.mode_set(mode="EDIT", toggle=False)

armature.data.name = "armature"

bones = armature.data.edit_bones

# rename root bone
bones[0].name = "root"

bone = bones.new("BoneName")
bone.head = (0, 1, 1) # if the head and tail are the same, the bone is deleted
bone.tail = (0, 1, 2)    # upon returning to object mode

bone.parent = bones[0]

#eb = ebs.new("BoneName")
#eb.head = (-10, 1, 1) # if the head and tail are the same, the bone is deleted
#eb.tail = (0, 1, 2)    # upon returning to object mode



bpy.ops.object.mode_set(mode="OBJECT", toggle=False)
```







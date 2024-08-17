

# General Cookbook

## Get an object from the current scene

```python
cube = D.objects["Cube"]
```

## Set Location of the object

```python
cube = D.objects["Cube"]

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
cube = D.objects["Cube"]

cube.rotation_mode = "XYX"

# set rotation in x to 1 radian
cube.rotation_euler.x = 1

print(cube.rotation_euler)
# <Euler (x=1.0000, y=-0.0000, z=0.0000), order='XYZ'>
```

### Quaternion mode

```python
cube = D.objects["Cube"]

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


## Create Armature






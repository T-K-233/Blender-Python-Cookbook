
# Animation Cookbook

## Quick Example

```python


class AnimateCubeOperator(bpy.types.Operator):
    # handle containing information for Blender to register this operator
    bl_idname = "object.animate_cube"       # Unique identifier for the operator
    bl_label = "Animate Cube Operator"      # Display name in the interface
    
    # animation variables
    _timer = None
    _time_interval = 1. / 30.
    _last_update_t = 0
    cube = None

    def execute(self, context):
        # Add a timer to the window manager and register the modal handler
        wm = context.window_manager
        self._timer = wm.event_timer_add(self._time_interval, window=context.window)
        wm.modal_handler_add(self)
        
        # initialize the variable
        self._last_update_t = time.time()
        
        # find the reference to the cube by name
        # the name should correspond to the object name on the right panel, under "Scene Collection"    
        self.cube = bpy.data.objects["Cube"]
        self.cube.rotation_mode = "XYZ"

        print("Animation started.")
        return {"RUNNING_MODAL"}
    
    def modal(self, context, event):
        if event.type == "ESC":
            print("\"ESC\" is pressed.")
            return self.cancel(context)
            
        # this will eval true every Timer delay seconds
        if event.type == "TIMER":
            current_t = time.time()
            dt = current_t - self._last_update_t
            self._last_update_t = current_t
            
            if self.cube:
                # set a new location
                self.cube.location.x = 2 * math.sin(current_t)
                self.cube.location.y = 2 * math.cos(current_t)

                # increament is also possible
                self.cube.rotation_euler.z += dt

                # update the change
                bpy.context.view_layer.update()

            print(f"Animation update: {current_t:.3f} - {self.cube.rotation_euler.z}")
        return {"PASS_THROUGH"}
        
    def cancel(self, context):
        # Remove the timer
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
        
        # reset the state of the cube
        self.cube.location = [0, 0, 0]
        self.cube.rotation_mode = "QUATERNION"
        self.cube.rotation_quaternion = [1, 0, 0, 0]
        
        print("Animation stopped.")
        return {"CANCELLED"}

if __name__ == "__main__":
    # register the operator
    bpy.utils.register_class(AnimateCubeOperator)

    # start the operator
    bpy.ops.object.animate_cube()

```


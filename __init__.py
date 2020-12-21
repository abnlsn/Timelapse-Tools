bl_info = {
    "name": "Timelapse Tools",
    "author": "AB3D",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > UI > Tools > Timelapse Tools",
    "description": "Tools for recording awesome timelapses",
    "warning": "",
    "doc_url": "https://bit.ly/ab3dchannel",
    "category": "Timelapse Tools"
}

import bpy
import mathutils, math

from bpy.props import BoolProperty, FloatProperty

class CUSTOM_OT_OpenNewWindow(bpy.types.Operator):
    """Open a new window"""
    bl_label = "New Window"
    bl_idname = "timelapse_tools.new_window"
    
    def execute(self, context):
        
        render = bpy.context.scene.render
        
        bpy.ops.render.view_show("INVOKE_DEFAULT")
        
        screen = context.window_manager.windows[1].screen
        area = screen.areas[0]
        area.type = "VIEW_3D"
        area.spaces[0].show_region_ui = True
        
        return {"FINISHED"}

class TimelapseToolValues(bpy.types.PropertyGroup):
    is_running: BoolProperty(default = False)
    rotation_amount: FloatProperty(default = 20, name="Degrees of Rotation")
    second_break: FloatProperty(default = 2, name="Wait Seconds")
    
bpy.utils.register_class(TimelapseToolValues)
    
bpy.types.Scene.timelapse_tools = bpy.props.PointerProperty(type=TimelapseToolValues)


class CUSTOM_OT_TimelapseModal(bpy.types.Operator):
    bl_idname = "timelapse_tools.start_turntable"
    bl_label = "Start Turntable"
    
    def modal (self, context, event):
        if event.type == 'TIMER' and context.scene.timelapse_tools.is_running:
            v_loc = context.space_data.region_3d.view_location
            v_rot = context.space_data.region_3d.view_rotation
            
            v_loc.x = 0
            v_loc.y = 0
            v_loc.z = 0
            
            rotation = mathutils.Euler((0.0, 0.0, math.radians(context.scene.timelapse_tools.rotation_amount)), "XYZ")
            v_rot.rotate(rotation)
        elif context.scene.timelapse_tools.is_running == False:
            self.cancel(context)
            return {'CANCELLED'}
            
        return {'PASS_THROUGH'}
            
    def invoke(self, context, event):
        wm = context.window_manager
        context.scene.timelapse_tools.is_running = True

        self._timer = wm.event_timer_add(context.scene.timelapse_tools.second_break, window=context.window)
        
        wm.modal_handler_add(self)
        return {"RUNNING_MODAL"}
    
    def cancel(self, context):
        wm = context.window_manager
        
        wm.event_timer_remove(self._timer)
        
    
    
class CUSTOM_OT_StopTimelapseModal(bpy.types.Operator):
    bl_idname = "timelapse_tools.stop_turntable"
    bl_label = "Cancel Turntable"
    
    def execute(self, context):
        context.scene.timelapse_tools.is_running = False
        return {'FINISHED'}
    

### Drawing
    
    
class CUSTOM_PT_TimelapsePanel(bpy.types.Panel):
    bl_label = "Timelapse Tools"
    bl_space_type = "VIEW_3D"
    bl_category = "Tool"
    bl_region_type = "UI"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.prop(context.scene.timelapse_tools, "rotation_amount")
        row = layout.row()
        row.prop(context.scene.timelapse_tools, "second_break")
        row = layout.row()
        row = layout.row()
        row.operator("timelapse_tools.new_window")
        row = layout.row()
        row.operator("timelapse_tools.start_turntable", icon="PLAY")
        row = layout.row()
        row.operator("timelapse_tools.stop_turntable", icon="X")
        
        
classes = (CUSTOM_OT_OpenNewWindow, CUSTOM_PT_TimelapsePanel, CUSTOM_OT_TimelapseModal, CUSTOM_OT_StopTimelapseModal)
        


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()        
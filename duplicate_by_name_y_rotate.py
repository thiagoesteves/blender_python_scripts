"""
-----------------------------------------------------------------------------
@copyright 2020 Thiago Esteves
@doc Duplicate object by name and rotate in Y axis

@author Thiago Cesar Calori Esteves <thiago.calori@gmail.com>

@blender_version 2.8
-----------------------------------------------------------------------------
"""

import bpy
import random
import math

def duplicate_by_name_rotate(NAME, Y_DEGREES, COPIES):
    # Get Object
    obj = bpy.context.scene.objects[NAME]
    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')
    # Make the cube the active object
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    # Duplicate Selected
    for X in range(COPIES):
        bpy.ops.object.duplicate()
        # Get New Object and Rotate
        for obj in bpy.context.selected_objects:
            obj.rotation_euler.y += math.radians(Y_DEGREES)

duplicate_by_name_rotate("Cube", 10, 35)
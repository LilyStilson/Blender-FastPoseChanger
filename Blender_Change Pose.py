#====================== BEGIN GPL LICENSE BLOCK ======================
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
#======================= END GPL LICENSE BLOCK ========================

# <pep8 compliant>

bl_info = {
    "name": "Armature Pose",
    "version": (1, 0),
    "author": "Deneb",
    "blender": (2, 6, 0),
    "description": "Fast switch between Pose and Rest armature positions",
    "category": "Rigging"
}

import bpy

class VIEW3D_posePosition(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Armature Pose"
    #bl_options = {'DEFAULT_SHOWN'}
    
    def draw (self, context):
        layout = self.layout
        space = context.space_data
        
        row = layout.row()
        row.template_ID(context.scene.objects, "active")
            
        pose = layout.row()
        pose.prop(bpy.context.active_object.data, 'pose_position', text='')

def register():
	bpy.utils.register_class(VIEW3D_posePosition)
	
def unregister():
	bpy.utils.unregister_class(VIEW3D_posePosition)
# __init__.py
# SPDX-FileCopyrightText: 2013-2023 Blender Foundation
#
# SPDX-License-Identifier: GPL-2.0-or-later

bl_info = {
    "name": "Custom FBX Importer",
    "author": "Your Name",
    "version": (1, 0, 0),
    "blender": (4, 3, 0),
    "location": "File > Import > Custom FBX (.fbx)",
    "description": "Import FBX files using custom_fbx_import with all available options",
    "warning": "",
    "doc_url": "",
    "category": "Import-Export",
}

import bpy
from bpy.props import (
    BoolProperty,
    StringProperty,
    FloatProperty,
    EnumProperty,
)
from bpy_extras.io_utils import ImportHelper

# Import your custom importer module (it must be in the same addon package)
from . import custom_fbx_import

class ImportCustomFBX(bpy.types.Operator, ImportHelper):
    """Import FBX files using custom_fbx_import with all available options"""
    bl_idname = "import_scene.custom_fbx"
    bl_label = "Custom FBX Importer"
    filename_ext = ".fbx"
    filter_glob: StringProperty(default="*.fbx", options={'HIDDEN'})

    use_manual_orientation: BoolProperty(
        name="Manual Orientation",
        default=False,
        description="Specify orientation manually instead of using embedded data",
    )
    axis_forward: EnumProperty(
        name="Axis Forward",
        items=[
            ('-Z', "-Z", ""),
            ('-Y', "-Y", ""),
            ('X', "X", ""),
            ('Y', "Y", ""),
            ('Z', "Z", ""),
        ],
        default='-Z',
    )
    axis_up: EnumProperty(
        name="Axis Up",
        items=[
            ('Y', "Y", ""),
            ('Z', "Z", ""),
            ('X', "X", ""),
            ('-X', "-X", ""),
            ('-Y', "-Y", ""),
            ('-Z', "-Z", ""),
        ],
        default='Y',
    )
    global_scale: FloatProperty(
        name="Global Scale",
        default=1.0,
        min=0.001,
        max=1000.0,
    )
    bake_space_transform: BoolProperty(
        name="Bake Space Transform",
        default=False,
    )
    use_custom_normals: BoolProperty(
        name="Use Custom Normals",
        default=True,
    )
    use_image_search: BoolProperty(
        name="Use Image Search",
        default=False,
    )
    use_alpha_decals: BoolProperty(
        name="Use Alpha Decals",
        default=False,
    )
    decal_offset: FloatProperty(
        name="Decal Offset",
        default=0.0,
        min=0.0,
        max=1.0,
    )
    use_anim: BoolProperty(
        name="Import Animation",
        default=True,
    )
    anim_offset: FloatProperty(
        name="Animation Offset",
        default=1.0,
    )
    use_subsurf: BoolProperty(
        name="Use Subsurf",
        default=False,
    )
    use_custom_props: BoolProperty(
        name="Use Custom Properties",
        default=True,
    )
    use_custom_props_enum_as_string: BoolProperty(
        name="Enums as Strings",
        default=True,
    )
    ignore_leaf_bones: BoolProperty(
        name="Ignore Leaf Bones",
        default=False,
    )
    force_connect_children: BoolProperty(
        name="Force Connect Children",
        default=False,
    )
    automatic_bone_orientation: BoolProperty(
        name="Automatic Bone Orientation",
        default=False,
    )
    primary_bone_axis: EnumProperty(
        name="Primary Bone Axis",
        items=[
            ('X', "X", ""),
            ('Y', "Y", ""),
            ('Z', "Z", ""),
            ('-X', "-X", ""),
            ('-Y', "-Y", ""),
            ('-Z', "-Z", ""),
        ],
        default='Y',
    )
    secondary_bone_axis: EnumProperty(
        name="Secondary Bone Axis",
        items=[
            ('X', "X", ""),
            ('Y', "Y", ""),
            ('Z', "Z", ""),
            ('-X', "-X", ""),
            ('-Y', "-Y", ""),
            ('-Z', "-Z", ""),
        ],
        default='X',
    )
    use_prepost_rot: BoolProperty(
        name="Use Pre/Post Rotation",
        default=True,
    )
    colors_type: EnumProperty(
        name="Colors Type",
        items=[
            ('NONE', "None", ""),
            ('SRGB', "sRGB", ""),
            ('LINEAR', "Linear", ""),
        ],
        default='SRGB',
    )
    import_cameras: BoolProperty(
        name="Import Cameras",
        default=False,
    )

    def execute(self, context):
        # Build a dictionary of all options from the operator properties:
        options = {
            "filepath": self.filepath,
            "use_manual_orientation": self.use_manual_orientation,
            "axis_forward": self.axis_forward,
            "axis_up": self.axis_up,
            "global_scale": self.global_scale,
            "bake_space_transform": self.bake_space_transform,
            "use_custom_normals": self.use_custom_normals,
            "use_image_search": self.use_image_search,
            "use_alpha_decals": self.use_alpha_decals,
            "decal_offset": self.decal_offset,
            "use_anim": self.use_anim,
            "anim_offset": self.anim_offset,
            "use_subsurf": self.use_subsurf,
            "use_custom_props": self.use_custom_props,
            "use_custom_props_enum_as_string": self.use_custom_props_enum_as_string,
            "ignore_leaf_bones": self.ignore_leaf_bones,
            "force_connect_children": self.force_connect_children,
            "automatic_bone_orientation": self.automatic_bone_orientation,
            "primary_bone_axis": self.primary_bone_axis,
            "secondary_bone_axis": self.secondary_bone_axis,
            "use_prepost_rot": self.use_prepost_rot,
            "colors_type": self.colors_type,
            "import_cameras": self.import_cameras
        }
        # Call your load function from custom_fbx_import, passing these options:
        return custom_fbx_import.load(self, context, **options)

def menu_func_import(self, context):
    self.layout.operator(ImportCustomFBX.bl_idname, text="Custom FBX Importer (.fbx)")

def register():
    bpy.utils.register_class(ImportCustomFBX)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
    bpy.utils.unregister_class(ImportCustomFBX)

if __name__ == "__main__":
    register()

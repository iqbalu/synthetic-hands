import bpy
from importlib import reload
import numpy as np
import os
import sys

sys.path.insert(
    0, '/home/local2/yhasson/first-person-action-recognition/blender-scripts')

from settings import params
from utils import blender
from utils import filesys

# Insure modules are reloaded in blender
reload(blender)
reload(filesys)

arm = bpy.data.objects['Armature']
cam = bpy.data.objects['Camera']
scene = bpy.context.scene

# Clear camera constraints
for const in cam.constraints:
    cam.constraints.remove(const)

# Camera follows hand
bone_name = 'mixamorig_RightHandIndex4'
const = blender.follow_bone(arm, bone_name=bone_name, track_axis='z',
                            track_axis_neg=True, up_axis='y')

for folder in params['folders'].values():
    filesys.create_dir(folder)

# Get background images
bg_folder = params["folders"]["background"]
bg_names = [bg_folder + filen for filen in os.listdir(bg_folder)]
bg_img = bpy.data.images.load(bg_names[0])

depth_folder = params['folders']['depth']
segm_folder = params['folders']['segm']

blender.set_cycle_nodes(scene, background_img=bg_img,
                        segm=True, segm_folder=segm_folder,
                        segm_mats=["Bodymat"],
                        depth_folder=depth_folder)

# Render
for frame_nb in range(scene.frame_start, scene.frame_stop + 1):
    scene.frame_set(frame_nb)
    bpy.contest.scene.camera = cam

    # Save coordinates
    side = "Right"
    
    





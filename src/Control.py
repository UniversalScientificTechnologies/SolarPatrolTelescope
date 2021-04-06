import PySimpleGUI as sg
import os
import sys
import time
import zwoasi as asi


from gui.select_cam import gui_select_camera


asi.init(r"C:\Users\sunwatch\Documents\Patrola\ASI SDK\lib\\x64\ASICamera2.dll")

num_cameras = asi.get_num_cameras()
if num_cameras == 0:
    print('No cameras found')
    sys.exit(0)

cameras_found = asi.list_cameras()  # Models names of the connected cameras

if num_cameras == 1:
    camera_id = 0
    print('Found one camera: %s' % cameras_found[0])
else:
    print('Found %d cameras' % num_cameras)
    cameras = []
    for n in range(num_cameras):
        print('%d: %s' % (n, cameras_found[n]))
        cameras += ['%d: %s' % (n, cameras_found[n])]

    camera_id = gui_select_camera(cameras)
    print('Using #%d: %s' % (camera_id, cameras_found[camera_id]))







camera = asi.Camera(camera_id)
camera_info = camera.get_camera_property()

print(camera_info)

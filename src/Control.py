import PySimpleGUI as sg
import os
import sys
import time, datetime
import zwoasi as asi
from queue import Queue
import cv2
import zmq
import math
import config

kill_threads = False
import numpy as np

from gui.select_cam import gui_select_camera
from gui.cam_view import gui_camera_preview, gui_control_mount
import camera

px_to_arcsec = 1.04

asi.init(r"C:\Users\sunwa\Documents\Patrola\ASI SDK\lib\x64\ASICamera2.dll")

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


image_queue = Queue()
camera_ctrl = Queue()
camera = camera.camera(camera_id, image_queue, camera_ctrl)
camera.start()

#gui_cam = gui_camera_preview()
gui_control = gui_control_mount()

def compose_label():
    text = ""
    text += "Poloha stredu [{}, {}]\n".format(0, 0)
    text += "Poloha stredu [{}, {}]\n".format(0, 0)
    text += "Poloha stredu [{}, {}]\n".format(0, 0)
    text += "Poloha stredu [{}, {}]\n".format(0, 0)

    return text

print("Connecting to hello Patrola server…")
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://arom-patrola.asu.cas.cz:5555")

cv2.namedWindow("frame", cv2.WINDOW_NORMAL| cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
should_run = True
chb_keep_position_last = False
keep_center = None

file = open(r'C:\Users\sunwa\Documents\Patrola\log_{}.csv'.format(datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S")), "w+", 128)

while should_run:

    event, values = gui_control.read(timeout=10)

    if event == 'val_exposition':
        exposition = int(values['val_exposition'])
        if exposition < 0: exposition = abs(exposition)
        if exposition > 99000: exposition = 99000

        camera_ctrl.put({"action": "set_expo", "value": exposition})
        #gui_control['val_exposition'].value(exposition)


    if event in (sg.WIN_CLOSED, 'Exit'):
        should_run = False
        cv2.destroyAllWindows()

    if event == 'move_up':
        print("move_up")
        socket.send_string("move_up", zmq.NOBLOCK)

    if event == 'move_down':
        print("move_down")
        socket.send_string("move_down")

    if event == 'move_right':
        print("move_right")
        socket.send_string("move_right")

    if event == 'move_left':
        print("move_left")
        socket.send_string("move_left")


    # pohyby -1 a -3 v hodinove ose jsou docela rychle
    if event == 'move_right_time':
        print("move_right")
        socket.send_string("move;-1.8;0;")

    if event == 'move_left_time':
        print("move_left")
        socket.send_string("move;-2.2;0;")

    if event == 'stop':
        print("stop")
        socket.send_string("stop")


    if event == 'btn_keep':
        try:
            keep_center = sun_center
        except Exception as e:
            print(e)

    if not image_queue.empty() and should_run:
        img = np.array(image_queue.get())
        size = img.shape
        frame = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
        gray_blurred = cv2.blur(img, (10, 10))
        small = cv2.resize(np.uint8(gray_blurred), (int(img.shape[0]/4), int(img.shape[1]/4) ))

        ret, thresh = cv2.threshold((gray_blurred/256).astype('uint8'), 50, 255, cv2.THRESH_BINARY)
        contours = cv2.findContours(np.uint8(thresh), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours, hierarchy = contours
        valid = False
        try:
            for i, cnt in enumerate(contours):
                area = cv2.contourArea(cnt)
                #print(area)
                if area > 1000000 and area < 1400000:  # velikost 19.10.2021 byla 1189093.5
                    diameter = math.sqrt(area/math.pi)
                    epsilon = 10*cv2.arcLength(cnt,True)
                    approx = cv2.approxPolyDP(cnt,epsilon,True)
                    M = cv2.moments(cnt)

                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    sun_center = (cx, cy)

                    valid = True
        except Exception as e:
            print(e)

        details = config.conf.get("detail")
        for detail in details:
            det = details[detail]
            cv2.circle(frame, det['center'], det['size'], det['color'], 5)

        colour = (0, 65500, 0) if valid else (0, 0, 65500)
        cv2.drawContours(frame, contours, -1, colour, 3)

        if valid:
            ellipse = cv2.fitEllipse(cnt)
            cv2.ellipse(frame, ellipse, colour, 2)       # vykresluje vypocitanou elipsu
            cv2.circle(frame, sun_center, 5, colour, 3) # vykresluje stred slunce


        #gui_cam['cam_frame'].update(data=cv2.imencode('.png', thresh)[1].tobytes())
        cv2.line(frame, (int(size[1]/2), 0),(int(size[1]/2), size[0]), (32700, 32700, 32700), 2)
        cv2.line(frame, (0, int(size[0]/2)),(size[1], int(size[0]/2)), (32700, 32700, 32700), 2)

        print(frame.shape)
        cv2.imshow("frame", frame)
        del img

        gui_control['sun_cam_position_valid']("Valid: {}".format(valid))

        if valid:
            gui_control['sun_cam_position_text']("[{:.3f}\", {:.3f}\"]".format((cx-size[0]/2)*px_to_arcsec, (cy-size[1]/2)*px_to_arcsec))
            # solarprojective souradnice na stredu kamery
            gui_control['sun_cam_center_text']("CamCenter solarprojective: \n [{:.3f}\", {:.3f}\"]".format( (cx-size[0]/2)*px_to_arcsec, (cy-size[1]/2)*px_to_arcsec) )
            gui_control["mount_position_tex"](compose_label())

        if values['chb_keep_position']:
            if valid:
                if not chb_keep_position_last:
                    if not keep_center:
                        keep_center = sun_center
                    print("Potrebuji drzet stred na souradnicich", keep_center)

                pos_error = (keep_center[0] - sun_center[0], keep_center[1] - sun_center[1])
                print(pos_error)

                time_axis = pos_error[0]
                dec = pos_error[1]

                log = "\n{};{};{};".format(i, time.time(), datetime.datetime.now().isoformat())
                log += "{};{};".format(time_axis, dec)

                if abs(time_axis) < 5:
                    time_axis = 0
                if abs(dec) < 5:
                    dec = 0

                if (time_axis) < -10:
                    time_axis = -10
                if (dec) < -10:
                    dec = -10
                if (time_axis) > 10:
                    time_axis = 10
                if (dec) > 10:
                    dec = 10

                log += "{};{};".format(time_axis, dec)
                log += "{};{};".format(-2+time_axis/10, int((dec*5)))

                file.write(log)

                cmd = "move;{};{};".format(-2+time_axis/10, int((dec*5)))
                print(cmd)
                socket.send_string(cmd)

        chb_keep_position_last = values['chb_keep_position']

camera.kill()
#gui_cam.close()
gui_control.close()

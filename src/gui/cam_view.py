import PySimpleGUI as sg
sg.theme("Default1")

def gui_camera_preview():
    layout = [
            [sg.Image(key="cam_frame")]
        ]

    window = sg.Window('Náhled kamery', layout, grab_anywhere=True, resizable=True)
    return window


def gui_control_mount():
    layout = [
        [sg.Text(key = "mount_position_tex", size=(25, 1))],
        [sg.Text(key = "sun_cam_center_text", size=(25, 1))],
        [sg.Text(key = "sun_cam_position_text", size=(25, 1))],
        [sg.Text(key = "sun_cam_position_valid", size=(25, 1))],
        [sg.Button("<t", key="move_left_time", size=(2,2)), sg.Button("A", key="move_up", size=(2,2)), sg.Button("t>", key="move_right_time", size=(2,2))],
        [sg.Button("<", key="move_left", size=(2,2)), sg.Button("X", size=(2,2), key="stop"), sg.Button(">", key="move_right", size=(2,2))],
        [sg.Button("", size=(2,2)), sg.Button("V", key="move_down", size=(2,2)), sg.Button("", size=(2,2))],
        [sg.Checkbox('Keep position', key="chb_keep_position")],
        [sg.Text('Exp:', size =(8, 1)), sg.InputText(key="val_exposition", enable_events = True)],
        [sg.Button("keep", key="btn_keep", size=(4,1))]
    ]

    window = sg.Window('Ovladani montaze', layout, grab_anywhere=True, resizable=True)
    return window

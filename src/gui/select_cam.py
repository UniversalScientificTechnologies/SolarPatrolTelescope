import PySimpleGUI as sg

def gui_select_camera(cameras):
    layout = [[sg.Text("Vyberte kameru:")],
            [sg.Combo(values=cameras, size=(30, 6))],
            [sg.Button('OK')]]

    window = sg.Window('Select camera', layout)

    event, values = window.read()
    window.close()
    return cameras.index(values[0])

from threading import Thread
from queue import Queue
import zwoasi as asi
import glob
from astropy.io import fits
import gc

class camera(Thread):
    def __init__(self, camera_id, image_queue: Queue):
        super(camera, self).__init__()
        print("Priprava kamery", camera_id)
        self.image_queue = image_queue
        self.should_run = True

        self.camera = asi.Camera(camera_id)
        camera_info = self.camera.get_camera_property()

        print(camera_info)
        # Use minimum USB bandwidth permitted
        self.camera.set_control_value(asi.ASI_BANDWIDTHOVERLOAD, self.camera.get_controls()['BandWidth']['MinValue'])

        # Set some sensible defaults. They will need adjusting depending upon
        # the sensitivity, lens and lighting conditions used.
        self.camera.disable_dark_subtract()

        self.camera.set_control_value(asi.ASI_GAIN, 150)
        self.camera.set_control_value(asi.ASI_EXPOSURE, 30000)
        self.camera.set_control_value(asi.ASI_WB_B, 99)
        self.camera.set_control_value(asi.ASI_WB_R, 75)
        self.camera.set_control_value(asi.ASI_GAMMA, 50)
        self.camera.set_control_value(asi.ASI_BRIGHTNESS, 50)
        self.camera.set_control_value(asi.ASI_FLIP, 0)

        self.camera.set_image_type(asi.ASI_IMG_RAW16)

        try:
            # Force any single exposure to be halted
            self.camera.stop_video_capture()
            self.camera.stop_exposure()
        except:
            pass

        self.simulation_dict = glob.glob("E:\hasn20211011a\*.fits")

    def kill(self):
        self.should_run = False

    def run(self):
        while self.should_run:
            for fimg in self.simulation_dict:
                img = fits.open(fimg)[0].data
                self.image_queue.put(img)

                del img
                gc.collect()

                if not self.should_run:
                    break

            #img = self.camera.capture()
            #self.image_queue.put(img)

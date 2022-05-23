from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.uix.camera import Camera
from kivy.utils import platform
from kivy.uix.image import Image
from android.permissions import request_permissions, Permission

import requests

request_permissions([
    Permission.CAMERA,
    Permission.WRITE_EXTERNAL_STORAGE,
    Permission.READ_EXTERNAL_STORAGE
])


class ClassContent(BoxLayout):
    def __init__(self,**kwargs):
        super(ClassContent,self).__init__(**kwargs)
        
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.class_dialog = None
        self.devices = []
        self.show_class_dialog()
        self.count = 1
        self.camera = Camera()
        self.camera.index = 0
        self.camera.resolution = (640,480)
        print(dir(self.camera))
        self.camera.allow_stretch = True
        


    def show_class_dialog(self):
        if not self.class_dialog:
            self.class_dialog = Popup(title='Test popup',
                                      content=ClassContent(),
                                      size_hint=(.8,.3))

        self.class_dialog.title_font = "nevis"
        self.class_dialog.open()

    def class_dialog_close(self, *args,**kwargs):
        #self.Camera_Click()
        self.password = kwargs["password"]
        result = requests.get("https://python7978.000webhostapp.com/server.php?code=1&number=" + kwargs["password"])
        print("result"+result.text)
        Clock.schedule_interval(self.chk_req,5)
        self.class_dialog.dismiss(force=True)

    def Camera_Click(self):
        self.camera.export_to_png("current.jpg")
        self.add_widget(Image(source="current.jpg"))
        #self.children[0].source = 'current.jpg'
        #self.cam = cv2.VideoCapture("https://192.168.43.1:8080/video")
        #result, frame = self.cam.read()
        #if result:
            # byteframe = cv2.imencode('.jpg', frame)[1].tobytes()
            # byteframe = open(frame,'rb')
            #frame = cv2.imwrite("current.jpg",frame)

        return True
        #     print(frame)
        #     byteframe = open(frame,'rb')
        #     # print(byteframe)
        # return byteframe

    def chk_req(self,dt):
        req = requests.get("https://python7978.000webhostapp.com/check.php?index=" + str(self.count) + "&pass=" + self.password);
        if req.text == "2":
            print("Uploading")
            url = 'https://python7978.000webhostapp.com/upload.php?pass='+self.password+"&index="+str(self.count)
            verify = self.Camera_Click()
            files = {'image': open("current.jpg","rb")}

                # files = {'image': open('image.png', 'rb')}
            print(files)
            post = requests.post(url, files=files)
            print(post.text)
            if(post.text == "1"):
                self.count += 1
                print("H")

class TrackerPhoneApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name="first"))
        return self.sm

#Window.size = (350,550) # Mobile View
LabelBase.register(name="nevis",fn_regular="JetBrainsMono-Regular.ttf")
TrackerPhoneApp().run()
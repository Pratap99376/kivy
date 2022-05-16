

from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton


class MyApp(MDApp):
    def build(self):
        return MDRaisedButton(text='Hello World',pos_hint:{"center_x".5,"center_y":.5})



if __name__ == '__main__':
    MyApp().run()

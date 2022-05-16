from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.utils.fitimage import FitImage
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from kivy.metrics import dp,sp
from kivy.clock import Clock
from kivy.core.window import Window

class HomeScreen(MDScreen):
    pass

class WhatsHappeningImages(ScreenManager):
    def __init__(self, **kwargs):
        super(WhatsHappeningImages, self).__init__(**kwargs)
        self.transition.duration = 1
        self.size_hint_y = None
        self.height = dp(200)
        self.velocity = 10

    def start_animation(self,widget):
        for i in range(10):
            screen = MDScreen(name=f"{i}")
            screen.radius = 10

            if widget == "image":
                image = FitImage(source="flowers.jpg")
                image.radius = [10,10,0,0]
                self.velocity = 10
                if not (i % 2):
                    screen.add_widget(image)
            else:
                screen.radius = [0,0,10,10]
                mylabel = MDLabel(
                    font_name="nevis",
                    text='"Hello,Everyone"',
                    halign="center",
                    valign="middle",
                    theme_text_color="Custom",
                    pos_hint={"center_y": .5},
                    text_color=(1,1,1,1),
                )
                mylabel.font_size = sp(20)
                mylabel.bold = True
                self.velocity = 10.2
                if not (i % 2):
                    screen.md_bg_color = 0, 1, 0, 1
                    screen.add_widget(mylabel)
                else:
                    screen.md_bg_color = 1, 1, 1, 1

            self.add_widget(screen)

        Clock.schedule_interval(self.change_screen,self.velocity)
        Clock.schedule_interval(self.overtake_screen,self.velocity+self.transition.duration)

    def change_screen(self,dt):

        if int(self.current_screen.name) != 9:
            self.current = str(int(self.current_screen.name) + 1)
        else:
            self.current = "0"

    def overtake_screen(self,dt):
        if int(self.current_screen.name) != 9:
            if int(self.current) % 2:
                self.current = str(int(self.current_screen.name) + 1)
        else:
            self.current = "0"

class HeadImageTransition(WhatsHappeningImages):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_animation("image")

class TailImageTransition(WhatsHappeningImages):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.height = 80
        self.start_animation("text")


# t = TailImageTransition()

class ClassContent(MDBoxLayout):
    def __init__(self,**kwargs):
        super(ClassContent,self).__init__(**kwargs)

class DevicesScreen(MDScreen):
    def __init__(self, **kwargs):
        super(DevicesScreen, self).__init__(**kwargs)
        self.class_dialog = None
        self.devices = []

    def show_class_dialog(self):
        if not self.class_dialog:
            self.class_dialog = MDDialog(
                title="[font=nevis]Add Device:[/font]",
                type="custom",
                content_cls=ClassContent(),
                md_bg_color=(1,1,1,1),
            )
        self.class_dialog.open()

    def class_dialog_close(self, *args,**kwargs):
        card = MDCard(orientation="horizontal",
                      elevation=10,
                      radius=[10,],
                      size_hint_y=None,
                      height=dp(60),
                      padding=15,
                      spacing=20,
                      )

        card.add_widget(MDIcon(icon="devices",
                                theme_text_color="Custom",
                                text_color=(1, 1, 0, 1),
                                ))

        print(kwargs)
        card.md_bg_color = kwargs["app"].theme_cls.primary_color
        card.children[0].font_size = sp(40)
        self.children[0].remove_widget(self.ids.nodevice)
        self.ids.classbox.add_widget(card)

        self.class_dialog.dismiss(force=True)

class WhatsHappeningApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.material_style = "M3"
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name="first"))
        self.sm.add_widget(DevicesScreen(name="second"))

        return self.sm

# Window.size = (350,550) # Mobile View
LabelBase.register(name="nevis",fn_regular="nevis.ttf")
WhatsHappeningApp().run()
import random

import kivy
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase


class MyFloatLayout(FloatLayout):
    pass

class MyBoxLayout(BoxLayout):
    pass

class CanvasExample(Widget):
    speed = random.randint(0,200)
    accel = 1.05
    decel = 0.95

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(self.update,0.05)
        Clock.schedule_interval(self.auto_slow, 0.05)



    def speed_up(self):
        prev_speed = self.speed

        if prev_speed * self.accel > 200.0:
            self.speed = 200.0
        else:
            self.speed *= self.accel

        self.change_color(prev_speed)

    def slow_down(self):
        prev_speed = self.speed

        self.speed *= self.decel

        self.change_color(prev_speed)

    def auto_slow(self, dt):
        prev_speed = self.speed
        auto_decel = 0.99

        self.speed *= auto_decel

        self.change_color(prev_speed)

    def on_size(self,*args):
        label = self.ids.lbl
        gas = self.ids.gas
        brake = self.ids.brake
        label.pos = self.center_x-label.size[0]/2,self.center_y-label.size[1]/2
        gas.pos = (self.right-gas.size[0],self.top-gas.size[1])
        brake.pos = (self.right - 2*brake.size[0], self.top - brake.size[1])

    def update(self, dt):
        gas = self.ids.gas
        brake = self.ids.brake
        label = self.ids.lbl

        LabelBase.register(name='sevenSegment',fn_regular='sevenSegment.ttf')
        label.text = str(round(self.speed))


        if gas.state == "down":
            self.speed_up()

        if brake.state == "down":
            self.slow_down()

        prev_speed = self.speed
        #self.speed = random.randint(0,200)
        self.change_color(prev_speed)

    def change_color(self,prev_speed):
        #print(prev_speed, ", ", self.speed)
        if prev_speed > self.speed:
            for i in range(int(self.speed),int(prev_speed)):
                with self.canvas:
                    Color(0,0,0)
                    Rectangle(pos=(i * 5, 0), size=(1, 50))
        else:
            for i in range(int(self.speed)):
                with self.canvas:
                    Color(0, 0, 0)
                    if i >= 0 and i <= 20:
                        Color(0, 1, 0)
                    if i > 20 and i <= 40:
                        Color(0.2, 0.8, 0)
                    if i > 40 and i <= 60:
                        Color(0.6, 0.8, 0)
                    if i > 60 and i <= 80:
                        Color(0.9, 0.9, 0)
                    if i > 80 and i <= 100:
                        Color(1, 1, 0)
                    if i > 100 and i <= 120:
                        Color(1, 0.9, 0.1)
                    if i > 120 and i <= 140:
                        Color(1, 0.6, 0.1)
                    if i > 140 and i <= 160:
                        Color(1, 0.5, 0)
                    if i > 160 and i <= 180:
                        Color(1, 0.2, 0)
                    if i > 180 and i < 200:
                        Color(1, 0, 0)

                    Rectangle(pos=(i*5, 0), size=(1, 50))



class DrawingWindow(App):
    def build(self):
        return CanvasExample()

if __name__ == "__main__":
    DrawingWindow().run()

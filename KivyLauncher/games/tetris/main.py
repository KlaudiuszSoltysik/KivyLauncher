from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.properties import ObjectProperty

import random

class KivyTetrisApp(App):
    pass


class MenuWidget(RelativeLayout):
    pass  


class TetrisWidget(GridLayout):
    squares = []
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        
        for i in range(200):
            obj = Button(background_color = (0.2, 0.2, 0.2, 1),
                         background_normal = "")
            self.squares.append(obj)
            self.add_widget(obj)
            
    
class Panel(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(*kwargs) 
        
        self.orientation = "vertical"
        
        self.label1 = Label(text = "KivyTetris",
                            font_size = self.height * 0.5,
                            font_name = "label_font.ttf",
                            color = (0, 0.25, 0.3, 1),
                            bold = True,
                            size_hint = (1, 0.5))
        
        self.label2 = Label(text = "Next:",
                            font_size = self.height * 0.3,
                            font_name = "label_font.ttf",
                            color = (0, 0.25, 0.3, 1),
                            bold = True,
                            size_hint = (1, 0.3))
        
        self.block = Label(text = "PLACEHOLDER",
                            font_size = self.height * 0.5,
                            font_name = "label_font.ttf",
                            color = (0, 0.25, 0.3, 1),
                            bold = True,
                            size_hint = (1, 0.5))
        
        self.label3 = Label(text = "Points:",
                            font_size = self.height * 0.3,
                            font_name = "label_font.ttf",
                            color = (0, 0.25, 0.3, 1),
                            bold = True,
                            size_hint = (1, 0.3))
        
        self.points = Label(text = "pts",
                            font_size = self.height * 0.5,
                            font_name = "label_font.ttf",
                            color = (0, 0.25, 0.3, 1),
                            bold = True,
                            size_hint = (1, 0.5))
        
        self.add_widget(self.label1)
        self.add_widget(self.label2)
        self.add_widget(self.block)
        self.add_widget(self.label3)
        self.add_widget(self.points)       
        
        
class App(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'horizontal'
        
        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self._keyboard.bind(on_key_down=self.on_key_down)
        
        self.tetris = TetrisWidget()
        self.panel = Panel()
        
        self.add_widget(self.tetris)
        self.add_widget(self.panel)
        
        Clock.schedule_interval(self.update, 1/60)


    def on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "left":
            self.last_key = self.left_arrow
        if keycode[1] == "right":
            self.last_key = self.right_arrow
        if keycode[1] == "down":
            self.last_key = self.down_arrow
        return True
    
    
    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down = self.on_key_down)
        self._keyboard = None
    

    def update(self, dt):
        pass


KivyTetrisApp().run()

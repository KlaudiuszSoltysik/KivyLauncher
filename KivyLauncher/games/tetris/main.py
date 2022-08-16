from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.properties import ObjectProperty

import random
import copy

class KivyTetrisApp(App):
    pass


class GridButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.background_color = (0.2, 0.2, 0.2, 1)
        self.disabled = True
        self.background_disabled_normal = ""
            

class TetrisWidget(GridLayout):    
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        
        self.shapes = []
        
        for i in range(200):
            obj = GridButton()
            self.add_widget(obj)
            
        self.tetris_canvas = self.canvas
        with self.tetris_canvas:
            obj = Shapes()
            
            obj.pos_x = 4
            obj.pos_y = 4
            
            self.shapes.append(obj)
            
    
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
        
        
class Shapes(Line):
    pos_x = 0
    pos_y = 0
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cap = "none"
    

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
        
        Clock.schedule_interval(self.update, 1/2)


    def on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "left":
            self.last_key = self.left_arrow
        if keycode[1] == "right":
            self.last_key = self.right_arrow
        if keycode[1] == "up":
            self.last_key = self.up_arrow
        if keycode[1] == "down":
            self.last_key = self.down_arrow
        return True
    
    
    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down = self.on_key_down)
        self._keyboard = None
    
    
    def left_arrow(self):
        with self.tetris.tetris_canvas:
            obj = Shapes()
            
            obj.pos_x = 6
            obj.pos_y = 4
            
            self.tetris.shapes.append(obj)
            
    
    
    def right_arrow(self):
        pass
    
    
    def up_arrow(self):
        pass
    
    
    def down_arrow(self):
        pass
    

    def update(self, dt):
        self.update_shapes()        
    
    
    def update_shapes(self):
        x_offset = self.tetris.width/20
        unit = self.tetris.width/10
        
        for i in self.tetris.shapes:
            i.points = (unit * i.pos_x - x_offset, 0,
                        unit * i.pos_x - x_offset, unit * i.pos_y)
            i.width = self.tetris.width * 0.1 /2
        

KivyTetrisApp().run()
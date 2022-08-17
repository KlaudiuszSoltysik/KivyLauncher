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
            
        r = random.randint(1, 6)
        
        if r == 1:
            self.new_IShape()
        elif r == 2:
            self.new_OShape()
        elif r == 3:
            self.new_LShape()
        elif r == 4:
            self.new_JShape()
        elif r == 5:
            self.new_SShape()
        else:
            self.new_ZShape()
    
    def update_game(self):
        if self.shapes[-1].active == True:
            self.shapes[-1].pos_y -= 1
            
    
    def new_IShape(self):
        with self.canvas:
            Color(0, 0.25, 0.3)
            obj = IShape()
            self.shapes.append(obj)
            
            
    def new_OShape(self):
        with self.canvas:
            Color(0.5, 0.7, 0.5)
            obj = OShape()
            self.shapes.append(obj)
            
    
    def new_LShape(self):
        with self.canvas:
            Color(1, 0.5, 0)
            obj = LShape()
            self.shapes.append(obj)
            
            
    def new_JShape(self):
        with self.canvas:
            Color(0.95, 0.35, 0.5)
            obj = JShape()
            self.shapes.append(obj)
            
            
    def new_ZShape(self):
        with self.canvas:
            Color(0.45, 0.2, 0.5)
            obj = ZShape()
            self.shapes.append(obj)
            
            
    def new_SShape(self):
        with self.canvas:
            Color(0.9, 0.75, 0.2)
            obj = SShape()
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
        
    
class Shape(Line):
    pos_x = 5
    pos_y = 20
    active = True
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.cap = "none"
        self.joint = "miter"
        
    
    def update(self):
        self.points = (self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4)
        self.width = self.unit / 2
    
    
class IShape(Shape):
    def update(self, window_width):
        self.offset = window_width / 20
        self.unit = window_width / 10
        
        self.x1 = self.unit * self.pos_x - self.offset
        self.y1 = self.unit * (self.pos_y - 1)
        self.x2 = self.unit * self.pos_x - self.offset
        self.y2 = self.unit * (self.pos_y + 1)
        self.x3 = self.unit * self.pos_x - self.offset
        self.y3 = self.unit * (self.pos_y + 2)
        self.x4 = self.unit * self.pos_x - self.offset
        self.y4 = self.unit * (self.pos_y + 3)
        
        super().update()
        
    
class OShape(Shape):
    def update(self, window_width):
        self.offset = window_width / 20
        self.unit = window_width / 10       
        
        self.x1 = self.unit * (self.pos_x - 1)
        self.y1 = self.unit * self.pos_y - self.offset
        self.x2 = self.unit * self.pos_x + self.offset
        self.y2 = self.unit * self.pos_y - self.offset
        self.x3 = self.unit * self.pos_x + self.offset
        self.y3 = self.unit * self.pos_y + self.offset
        self.x4 = self.unit * (self.pos_x - 1)
        self.y4 = self.unit * self.pos_y + self.offset
        
        super().update()
        
    
class LShape(Shape):
    def update(self, window_width):
        self.offset = window_width / 20
        self.unit = window_width / 10
        
        self.x1 = self.unit * (self.pos_x + 1)
        self.y1 = self.unit * self.pos_y - self.offset
        self.x2 = self.unit * self.pos_x - self.offset
        self.y2 = self.unit * self.pos_y - self.offset
        self.x3 = self.unit * self.pos_x - self.offset
        self.y3 = self.unit * (self.pos_y + 1)
        self.x4 = self.unit * self.pos_x - self.offset
        self.y4 = self.unit * (self.pos_y + 2)
        
        super().update()
        
        
class JShape(Shape):
    def update(self, window_width):
        self.offset = window_width / 20
        self.unit = window_width / 10
        
        self.x1 = self.unit * (self.pos_x - 1)
        self.y1 = self.unit * self.pos_y - self.offset
        self.x2 = self.unit * self.pos_x + self.offset
        self.y2 = self.unit * self.pos_y - self.offset
        self.x3 = self.unit * self.pos_x + self.offset
        self.y3 = self.unit * (self.pos_y + 1)
        self.x4 = self.unit * self.pos_x + self.offset
        self.y4 = self.unit * (self.pos_y + 2)
        
        super().update()
        
        
class ZShape(Shape):
    def update(self, window_width):
        self.offset = window_width / 20
        self.unit = window_width / 10
        
        self.x1 = self.unit * (self.pos_x - 1)
        self.y1 = self.unit * self.pos_y - self.offset
        self.x2 = self.unit * self.pos_x + self.offset
        self.y2 = self.unit * self.pos_y - self.offset
        self.x3 = self.unit * self.pos_x + self.offset
        self.y3 = self.unit * self.pos_y + self.offset
        self.x4 = self.unit * (self.pos_x + 2)
        self.y4 = self.unit * self.pos_y + self.offset
        
        super().update()
        
        
class SShape(Shape):
    def update(self, window_width):
        self.offset = window_width / 20
        self.unit = window_width / 10
        
        self.x1 = self.unit * self.pos_x - self.offset
        self.y1 =  self.unit * (self.pos_y - 1)
        self.x2 = self.unit * self.pos_x - self.offset
        self.y2 =  self.unit * self.pos_y + self.offset
        self.x3 = self.unit * self.pos_x + self.offset
        self.y3 =  self.unit * self.pos_y + self.offset
        self.x4 = self.unit * self.pos_x + self.offset
        self.y4 =  self.unit * (self.pos_y + 2)
        
        super().update()
        
    
class App(BoxLayout):
    game_speed = 0.75
    time = 0
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'horizontal'
        
        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self._keyboard.bind(on_key_down = self.on_key_down)
#        self._keyboard.bind(on_key_down = self.on_key_up)
        
        self.tetris = TetrisWidget()
        self.panel = Panel()
        
        self.add_widget(self.tetris)
        self.add_widget(self.panel)
        
        Clock.schedule_interval(self.update, 1/60)


    def on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "left":
            self.tetris.shapes[-1].pos_x -= 1
        if keycode[1] == "right":
            self.tetris.shapes[-1].pos_x += 1
        if keycode[1] == "up":
            pass
        if keycode[1] == "down":
            self.game_speed = 0.25
        return True
    
    
#    def on_key_up(self, keyboard, keycode, text, modifiers):
#        self.game_speed = 1
#        return True
    
    
    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down = self.on_key_down)
#        self._keyboard.unbind(on_key_down = self.on_key_up)
        self._keyboard = None
    

    def update(self, dt): 
        self.time += dt
        
        if self.time >= self.game_speed:
            self.time = 0
            self.tetris.update_game()
            
        self.update_shapes()        
    
    
    def update_shapes(self):
        for i in self.tetris.shapes:
            i.update(self.tetris.width)
        

KivyTetrisApp().run()

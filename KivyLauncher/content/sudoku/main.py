from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.config import Config

class Sudoku(RelativeLayout):
    lines = []
    buttons = []
    
    spacing = 0
    spacing2 = 16
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.grid_init()
        
        Clock.schedule_interval(self.update, 1/60)
    
    def grid_init(self):
        Window.size = (500, 600)
        
        with self.canvas:            
            Color(0.1, 0.1, 0.1)
            self.background = Rectangle(pos = self.pos, 
                                        size = self.size) 
            
            Color(0.95, 0.95, 0.95)
            for i in range(0, 20):
                self.lines.append(Line())
            
            for i in range(0, 81):
                self.buttons.append(SudokuButton(background_normal = "",
                                                 background_color = (0.2, 0.2, 0.2)))
                
            self.title = Label(text = "Sudoku",
                               color = (0, 0.25, 0.3, 1))
            
    def update(self, dt):
        if self.width > 0.8 * self.height:
            self.spacing = int(0.8 * self.height/9)
        else:
            self.spacing = int(self.width/9)
            
        self.update_grid()
        
    def update_grid(self):
        #self.title.font_size = dp(50)
        self.title.font_name = "label_font.ttf"
        self.title.size = self.size
        self.title.size_hint = (1, None)
        self.title.height = 100
        self.title.font_size = dp(40)
        self.title.y = self.height - dp(80)
        
        self.background.size = self.size
        
        for i in range(0, 10):
            self.lines[i].points = [self.width/2 - self.spacing/2 + (i - 4) * self.spacing, 
                                    0.8 * self.height/2 - 4.5 * self.spacing, 
                                    self.width/2 - self.spacing/2 + (i - 4) * self.spacing,
                                    0.8 * self.height/2 + 4.5 * self.spacing]
            if i == 0 or i == 3 or i == 6 or i == 9:
                self.lines[i].width = dp(2)
        
        for i in range(0, 10):
            self.lines[i + 10].points = [self.width/2 - 4.5 * self.spacing, 
                                       0.8 * self.height/2 - self.spacing/2 + (i - 4) * self.spacing, 
                                       self.width/2 + 4.5 * self.spacing,
                                       0.8 * self.height/2 - self.spacing/2 + (i - 4) * self.spacing]
            if i == 0 or i == 3 or i == 6 or i == 9:
                self.lines[i + 10].width = dp(2)
        
        k = 0 
        for i in range(-4, 5):
            for j in range(-4, 5):
                self.buttons[k].size = (self.spacing - dp(self.spacing2), self.spacing - dp(self.spacing2))
                self.buttons[k].pos = (self.width/2 + (j - 0.5) * self.spacing + self.spacing2/2,
                                       0.8 * self.height/2 + (i - 0.5) * self.spacing + self.spacing2/2)
                k += 1
        

class SudokuButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def on_press(self):
        print("pressed")
        return super().on_press()
    
                
class KivySudokuApp(App):
    pass


KivySudokuApp().run()

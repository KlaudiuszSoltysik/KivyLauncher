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

import random

class Sudoku(RelativeLayout):
    lines = []
    buttons = []
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    useable_values = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]    
    
    seconds = 0
    seconds_passed = 0
    minutes = 0
    minutes_passed = 0
    
    spacing = 0
    spacing2 = 16
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.game_init()
        
        Clock.schedule_interval(self.update, 1/60)
    
    
    def game_init(self):
        self.window_init()
        self.board_init()
    
    
    def board_init(self):
        self.generate_useable_values()
        y = 0
        while y < 9:
            x = 0
            while x < 9:
                    print(str(y) + ";" + str(x))
                    if not len(self.useable_values[y][x]):
                        self.useable_values[y][x] = random.sample(range(1, 10), 9)
                        if y == 0:
                            x -= 1
                            y = 8
                        else:
                            y -= 1
                    else:
                        random_value = self.useable_values[y][x].pop()
                        if self.value_check(y, x, random_value):
                            self.board[y][x] = random_value 
                            print("wpisano" + str(random_value))
                            if y == 8:
                                y = 0
                                x += 1
                            else:
                                y += 1
                            if y == 9:
                                x += 1
                                y = 0
    
        
    def generate_useable_values(self):
        for row in range(0, 9):
            for col in range(0, 9):
                self.useable_values[row][col] = random.sample(range(1, 10), 9)   
        
                    
    def value_check(self, row, col, random_value):
        R = int(row/3) * 3
        C = int(col/3) * 3
        
        for i in range(0, 9):
            if self.board[i][col] == random_value:
                return False
            for j in range(0, 9):
                if self.board[row][j] == random_value:
                    return False
        for i in range(R, R + 3):
            for j in range(C, C + 3):
                if random_value == self.board[i][j]:
                    return False
        return True

        
    def window_init(self):
        Window.size = (500, 600)
        
        with self.canvas:            
            Color(0.1, 0.1, 0.1)
            self.background = Rectangle(pos = self.pos, 
                                        size = self.size) 
            
            Color(0.95, 0.95, 0.95)
            for i in range(0, 20):
                self.lines.append(Line())
            
            for i in range(0, 9):
                button_list = []
                for j in range(0, 9):
                    button_list.append(SudokuButton(pos_x = i, pos_y = j))
                self.buttons.append(button_list)
                
            self.title = Label(text = "Sudoku",
                               color = (0, 0.35, 0.4, 1))
            self.timer = Label(color = (0, 0.35, 0.4, 1))
        
                
    def update(self, dt):
        self.seconds_passed += dt
        
        self.calculate_spacing()    
        self.update_time()
        self.update_grid()
        self.update_labels()
        
        
    def update_grid(self):                    
        self.background.size = self.size
        self.update_lines()
        self.update_buttons()
        
    
    def update_lines(self):
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
    
    
    def update_buttons(self):
        k = 0
        for i in range(5, -4, -1):
            l = 0 
            for j in range(-4, 5):
                self.buttons[l][k].size = (self.spacing - dp(self.spacing2), 
                                        self.spacing - dp(self.spacing2))
                
                self.buttons[l][k].pos = (self.width/2 + (j - 0.5) * self.spacing + self.spacing2/2,
                                       0.8 * self.height/2 + (i - 1.5) * self.spacing + self.spacing2/2)
                self.buttons[l][k].text = str(self.board[l][k])
                l +=1
            k += 1
        
        
    def update_time(self):
        if self.seconds_passed > 60:
            self.seconds_passed -= 60
            self.minutes_passed += 1
            
        self.seconds = format(int(self.seconds_passed), '02')
        self.minutes = format(self.minutes_passed, '02')
        
        
    def calculate_spacing(self):
        if self.width > 0.8 * self.height:
            self.spacing = int(0.8 * self.height/9)
        else:
            self.spacing = int(self.width/9)
            
            
    def update_labels(self):
        self.title.font_name = "label_font.ttf"
        self.title.size = self.size
        self.title.font_size = dp(40)
        self.title.pos = (0, (self.height - 80)/2)
        
        self.timer.font_name = "label_font.ttf"
        self.timer.size = self.size
        self.timer.font_size = dp(30)
        self.timer.pos = (0, (self.height - 170)/2)
        self.timer.text = "Time: " + str(self.minutes) + ":" + str(self.seconds)
        
        
class SudokuButton(Button):
    def __init__(self, pos_x, pos_y, **kwargs):
        super().__init__(**kwargs)
        
        self.background_normal = ""
        self.background_color = (0.2, 0.2, 0.2)
        self.pos_x = pos_x
        self.pos_y = pos_y
    
        
    def on_press(self):
        print("pressed")
        return super().on_press()
    
                
class KivySudokuApp(App):
    pass


KivySudokuApp().run()

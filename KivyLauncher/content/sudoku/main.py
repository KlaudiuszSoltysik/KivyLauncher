#naprawić buttony, dodać ekran końcowy i początkowy, wegenerować plansze, dodać rozwiązywanie planszy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.config import Config

import random


class KivySudokuApp(App):
    def build(self):
        return Sudoku()


class SmallGrid(GridLayout):
    pass


class BigGrid(GridLayout):
    pass


class Grid(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        big_grid = BigGrid()
        for i in range(0, 9):
            small_grid = SmallGrid()
            for j in range(0, 9):
                small_grid.add_widget(SudokuButton(pos_x = i, pos_y = j))
                
            big_grid.add_widget(small_grid)
        self.add_widget(big_grid)
        
        
class Sudoku(BoxLayout):
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
    
    useable_values = numberList=[1, 2, 3, 4, 5, 6, 7, 8, 9]  
    
    seconds_passed = 0
    minutes_passed = 0
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'
        
        self.title = Label(text = "KivySudoku",
                           font_size = self.height * 0.8,
                           font_name = "label_font.ttf",
                           color = (0, 0.25, 0.3, 1),
                           bold = True,
                           size_hint = (1, 0.15))
        
        self.timer = Label(font_size = self.height * 0.5,
                           font_name = "label_font.ttf",
                           color = (0, 0.25, 0.3, 1),
                           bold = True,
                           size_hint = (1, 0.1))
        
        self.add_widget(self.title)
        self.add_widget(self.timer)
        self.add_widget(Grid())
        
        self.board_init()
        
        Clock.schedule_interval(self.update, 1/60)
    
    
    def board_init(self):
        for i in range(0, 81):
            row = int(i/9)
            col = i%9
            if self.board[row][col] == 0:
                random.shuffle(self.useable_values)      
                for value in self.useable_values:
                    if self.value_check(row, col, value):
                        self.board[row][col] = value
                        if self.is_full(self.board):
                            return True
                        else:
                            if self.board_init():
                                return True
                break
        self.board[row][col] = 0             


    def solve_board(self):
        for i in range(0, 81):
            row = int(i/9)
            col = i%9
            if self.board[row][col] == 0:
                for value in range(1,10):
                    if self.value_check(row, col, value):
                        self.board[row][col] == value
                        self.solve_board()
                        self.board[row][col] = 0
                return False     
            

    def is_full(self, board):
        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == 0:
                    return False
        return True
                    
                    
    def value_check(self, row, col, value):
        R = int(row/3) * 3
        C = int(col/3) * 3
        
        for i in range(0, 9):
            if self.board[i][col] == value:
                return False
            for j in range(0, 9):
                if self.board[row][j] == value:
                    return False
        for i in range(R, R + 3):
            for j in range(C, C + 3):
                if value == self.board[i][j]:
                    return False
        return True

                
    def update(self, dt):
        self.seconds_passed += dt
         
        self.update_time()
        
        
    def update_time(self):
        if self.seconds_passed > 60:
            self.seconds_passed -= 60
            self.minutes_passed += 1
            
        seconds = str(format(int(self.seconds_passed), '02'))
        minutes = str(format(self.minutes_passed, '02'))
        
        self.timer.text = "Time: " + minutes + ":" + seconds
        
               
class SudokuButton(Button):
    def __init__(self, pos_x, pos_y, **kwargs):
        super().__init__(**kwargs)
        
        self.background_normal = ""
        self.background_color = (0.2, 0.2, 0.2)
        self.pos_x = pos_x
        self.pos_y = pos_y
    
        
    def on_press(self):
        return super().on_press()
    
    
class MenuWidget(RelativeLayout):
    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        return super().on_touch_down(touch)


KivySudokuApp().run()

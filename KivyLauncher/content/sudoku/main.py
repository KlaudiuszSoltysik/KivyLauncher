#dodać ekran końcowy, wygenerować plansze, dodać rozwiązywanie planszy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
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
    buttons = []
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(0, 9):
            obj = SudokuButton()
            self.buttons.append(obj)
            self.add_widget(obj)


class BigGrid(GridLayout): 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.grid1 = SmallGrid() 
        self.grid2 = SmallGrid() 
        self.grid3 = SmallGrid() 
        self.grid4 = SmallGrid() 
        self.grid5 = SmallGrid() 
        self.grid6 = SmallGrid() 
        self.grid7 = SmallGrid() 
        self.grid8 = SmallGrid() 
        self.grid9 = SmallGrid() 
        
        self.add_widget(self.grid1)
        self.add_widget(self.grid2)
        self.add_widget(self.grid3)
        self.add_widget(self.grid4)
        self.add_widget(self.grid5)
        self.add_widget(self.grid6)
        self.add_widget(self.grid7)
        self.add_widget(self.grid8)
        self.add_widget(self.grid9)
        

class MenuWidget(RelativeLayout):
    pass   
    
        
class Sudoku(BoxLayout):
    original_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    player_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
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
    
    last_key = ""
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'
        
        self.title = Label(text = "KivySudoku",
                           font_size = self.height * 0.5,
                           font_name = "label_font.ttf",
                           color = (0, 0.25, 0.3, 1),
                           bold = True,
                           size_hint = (1, 0.1))
        
        self.timer = Label(font_size = self.height * 0.2,
                           font_name = "label_font.ttf",
                           color = (0, 0.25, 0.3, 1),
                           bold = True,
                           size_hint = (1, 0.05))
        
        self.number = Label(font_size = self.height * 0.2,
                           font_name = "label_font.ttf",
                           color = (0, 0.25, 0.3, 1),
                           bold = True,
                           size_hint = (1, 0.05))
        
        self.menu = MenuWidget()
        self.add_widget(self.menu)
        
        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self._keyboard.bind(on_key_down=self.on_key_down)
        
        Clock.schedule_interval(self.update, 1/60)


    def on_key_down(self, keyboard, keycode, text, modifiers):
        for i in range(1, 10):
            if keycode[1] == str(i):
                self.last_key = str(i)
        return True
    
    
    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down = self.on_key_down)
        self._keyboard = None
    
    
    def original_board_init(self):
        for i in range(0, 81):
            row = int(i/9)
            col = i%9
            if self.original_board[row][col] == 0:
                random.shuffle(self.useable_values)      
                for value in self.useable_values:
                    if self.value_check(row, col, value):
                        self.original_board[row][col] = value
                        if self.is_full(self.original_board):
                            return True
                        else:
                            if self.original_board_init():
                                return True
                break
        self.original_board[row][col] = 0  
        
    
    def player_board_init(self, to_del):
        self.player_board = self.original_board
        
        to_remove = random.sample(range(0, 81), to_del)
        
        for i in to_remove:
            row = int(i/9)
            col = i%9  
            self.player_board[row][col] = ""
        
        for i in range(0, 9):
            for j in range(0, 9):
                self.grid.grid1.buttons[j].text = str(self.player_board[i][j])
#                if self.grid.grid1.buttons[j].text == "":
#                    self.grid.grid1.buttons[j].disabled = True


    def solve_board(self):
        for i in range(0, 81):
            row = int(i/9)
            col = i%9
            if self.original_board[row][col] == 0:
                for value in range(1,10):
                    if self.value_check(row, col, value):
                        self.original_board[row][col] == value
                        self.solve_board()
                        self.original_board[row][col] = 0
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
            if self.original_board[i][col] == value:
                return False
            for j in range(0, 9):
                if self.original_board[row][j] == value:
                    return False
        for i in range(R, R + 3):
            for j in range(C, C + 3):
                if value == self.original_board[i][j]:
                    return False
        return True

                
    def update(self, dt):
        self.seconds_passed += dt
        self.number.text = "Enter number: " + str(self.last_key)
        
#        for i in range(0, 9):
#            for j in range(0, 9):
#                self.grid.big_grid.small_grids[i].buttons[j].last_key = self.last_key
         
        self.update_time()
        
        
    def update_time(self):
        if self.seconds_passed > 60:
            self.seconds_passed -= 60
            self.minutes_passed += 1
            
        seconds = str(format(int(self.seconds_passed), '02'))
        minutes = str(format(self.minutes_passed, '02'))
        
        self.timer.text = "Time: " + minutes + ":" + seconds
        
        
    def easy_button(self):
        self.switch_menu()
        self.original_board_init()  
        self.player_board_init(31)    
        
        
    def medium_button(self):
        self.switch_menu()
        self.original_board_init()
        self.player_board_init(51) 
        
        
    def hard_button(self):
        self.switch_menu()
        self.original_board_init()
        self.player_board_init(61) 
        
    
    def switch_menu(self):
        self.seconds_passed = 0
        self.minutes_passed = 0
        
        self.remove_widget(self.menu)
        
        self.grid = BigGrid()
        self.grid.pos_hint = {"center_x": 0.5, "center_y:": 0.5}
        
        self.add_widget(self.title)
        self.add_widget(self.timer)
        self.add_widget(self.number)
        self.add_widget(self.grid)
        
              
class SudokuButton(Button):
    last_key = ""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.background_normal = ""
        self.background_color = (0.2, 0.2, 0.2)
    
        
    def on_press(self):
        if self.last_key != "":
            self.text = self.last_key
        return super().on_press()


KivySudokuApp().run()

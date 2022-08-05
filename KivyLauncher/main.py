from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.metrics import dp

import subprocess
import shutil
import os

class KivyLauncherApp(App):
    pass


class MyLayout(BoxLayout):        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
        
        self.title = Label(text = "KivyLauncher",
                           size_hint = (1, 0.15),
                           color = (1, 0.22, 0.39, 1),
                           font_size = (0.8*self.height))
        self.launcher_layout = LauncherLayout()
        
        self.add_widget(self.title)
        self.add_widget(self.launcher_layout)
        
        Clock.schedule_interval(self.update, 1/60)
        
    def update(self, dt):
        for i in self.launcher_layout.games_layout.games:            
            if(i.clicked):    
                
                with self.canvas.before:
                    Color(1, 1, 1)
                    self.background = Rectangle(source = i.patch + "/image.jpg", 
                                                pos = self.pos,
                                                size = Window.size)
                    
                for j in self.launcher_layout.games_layout.games:  
                    j.disabled = True
                    j.background_color = (1, 1, 1, 0.5)
                       
                for j in self.launcher_layout.buttons_layout.buttons:
                    j.disabled = False
                
                #PLAY BUTTON
                if(self.launcher_layout.buttons_layout.play_button.clicked):
                    exec(open(i.patch + "/main.py").read())
                    i.clicked = False
                    self.launcher_layout.buttons_layout.play_button.clicked = False
                    self.restore_default()
                    
                #SHOW BUTTON    
                if(self.launcher_layout.buttons_layout.show_button.clicked):
                    subprocess.call(['notepad.exe', i.patch + "/main.py"])
                    self.launcher_layout.buttons_layout.show_button.clicked = False

                #UNINSTALL BUTTON
                if(self.launcher_layout.buttons_layout.uninstall_button.clicked):
                    shutil.rmtree(i.patch)
                    ########################
                    #REMOVE HERE
                    self.remove_widget(i)
                    ########################
                    i.clicked = False
                    self.launcher_layout.buttons_layout.uninstall_button.clicked = False
                    self.restore_default()
                    
                #ABOUT BUTTON
                if(self.launcher_layout.buttons_layout.about_button.clicked):
                    subprocess.call(['notepad.exe', i.patch + "/about.txt"])
                    self.launcher_layout.buttons_layout.about_button.clicked = False
                
                #CANCEL BUTTON
                if(self.launcher_layout.buttons_layout.cancel_button.clicked):
                    self.launcher_layout.buttons_layout.cancel_button.clicked = False
                    self.restore_default()
                    i.clicked = False
                    
                self.background.pos = self.pos
                self.background.size = self.size
                    
                
    def restore_default(self):
        self.launcher_layout.games_layout.size_hint_x = 1
        
        for i in self.launcher_layout.buttons_layout.buttons:
            i.disabled = True
            
        for i in self.launcher_layout.games_layout.games:
            i.disabled = False
            i.background_color = (1, 1, 1, 1)
            
        with self.canvas.before:
            Color(0, 0, 0)
            Rectangle(pos = self.pos, size = Window.size)
    
          
class LauncherLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "horizontal"
        
        self.buttons_layout = ButtonsLayout()
        self.games_layout = GamesLayout()
        
        self.add_widget(self.buttons_layout)
        self.add_widget(self.games_layout)
           
           
class ButtonsLayout(BoxLayout):
    buttons = []
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
        self.spacing = dp(10)
        self.padding = dp(10)
        self.size_hint_x = 0.3
        
        self.play_button = PlayButton()
        self.show_button = ShowButton()
        self.uninstall_button = UninstallButton()
        self.about_button = AboutButton()
        self.cancel_button = CancelButton()
        
        self.buttons.append(self.play_button)
        self.buttons.append(self.show_button)
        self.buttons.append(self.uninstall_button)
        self.buttons.append(self.about_button)
        self.buttons.append(self.cancel_button)
        
        for i in self.buttons:
            self.add_widget(i)
 
        
class GamesLayout(StackLayout):
    games = []
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.padding = dp(10)
        self.spacing = dp(10)
        
        self.files = os.listdir("content")
        for i in self.files:
            self.games.append(GameButton("content\\" + i, text = i))
        
        for i in self.games:
            self.add_widget(i)             
   
        
class MyButton(Button):
    clicked = False
    patch = ""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.color = (1, 0.22, 0.39, 1)
        self.background_color = (0.94 ,0.93, 0.93, 1)
        self.disabled = True
        
    def on_release(self):
        self.clicked = True
        return super().on_release()

            
class PlayButton(MyButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.text = "play"

        
class ShowButton(MyButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.text = "show .py"

        
class UninstallButton(MyButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.text = "uninstall"
        

class AboutButton(MyButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.text = "about"
        

class CancelButton(MyButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.text = "cancel"


class GameButton(MyButton):        
    def __init__(self, patch, **kwargs):
        super().__init__(**kwargs)
        
        self.patch = patch
        self.size_hint = (None, None)
        self.size = (dp(200), dp(200))
        self.font_size = self.width*0.2
        self.color = (1, 1, 1, 1)
        self.disabled = False
        self.background_normal = patch + "\image.jpg"
        self.background_down = patch + "\image.jpg"
        self.background_disabled_normal = patch +"\image.jpg"
        self.background_disabled_down = patch + "\image.jpg"
        
        
KivyLauncherApp().run()
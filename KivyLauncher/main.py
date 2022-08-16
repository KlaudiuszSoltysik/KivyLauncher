from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.metrics import dp

import subprocess
import shutil
import os
import webbrowser

class KivyLauncherApp(App):
    pass

class MyLayout(BoxLayout):        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
        
        self.title = Label(text = "KivyLauncher",
                           size_hint = (1, 0.15),
                           color = (0, 0.3, 0.35, 1),
                           font_size = (0.7*self.height),
                           font_name = "label_font.ttf",
                           bold = True)
        self.launcher_layout = LauncherLayout()
        
        self.add_widget(self.title)
        self.add_widget(self.launcher_layout)
        self.restore_default()
        
        Clock.schedule_interval(self.update, 1/60)
    
      
    def update(self, dt):
        for i in self.launcher_layout.games_layout.games:            
            if(i.clicked):    
                
                with self.canvas.before:
                    Color(1, 1, 1)
                    Rectangle(source = i.patch + "/image.jpg", 
                              pos = self.pos, 
                              size = self.size)
                    Color(0, 0, 0, 0.7)
                    Rectangle(pos = self.pos, 
                              size = self.size)
                    
                    
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
                    subprocess.call(["notepad.exe", i.patch + "/main.py"])
                    self.launcher_layout.buttons_layout.show_button.clicked = False

                #UNINSTALL BUTTON
                if(self.launcher_layout.buttons_layout.uninstall_button.clicked):
                    #shutil.rmtree(i.patch)
                    i.text = "uninstalled"
                    i.clicked = False
                    self.launcher_layout.buttons_layout.uninstall_button.clicked = False
                    self.restore_default()
                    
                #ABOUT BUTTON
                if(self.launcher_layout.buttons_layout.about_button.clicked):
                    webbrowser.open("https://github.com/KlaudiuszSoltysik/KivyLauncher-app-games-/tree/main/KivyLauncher/" + i.patch)
                    self.launcher_layout.buttons_layout.about_button.clicked = False
                
                #CANCEL BUTTON
                if(self.launcher_layout.buttons_layout.cancel_button.clicked):
                    self.launcher_layout.buttons_layout.cancel_button.clicked = False
                    self.restore_default()
                    i.clicked = False
                    
                
    def restore_default(self):
        self.launcher_layout.games_layout.size_hint_x = 1
        
        for i in self.launcher_layout.buttons_layout.buttons:
            i.disabled = True
            
        for i in self.launcher_layout.games_layout.games:
            i.disabled = False
            i.background_color = (1, 1, 1, 1)
            
        with self.canvas.before:
            Color(0.1, 0.1, 0.1)
            Rectangle(pos = self.pos, 
                      size = Window.size)
    
          
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
        
        self.play_button = MyButton(text = "play")
        self.show_button = MyButton(text = "show .py")
        self.uninstall_button = MyButton(text = "uninstall")
        self.about_button = MyButton(text = "about")
        self.cancel_button = MyButton(text = "cancel")
        
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
        
        self.files = os.listdir("games")
        for i in self.files:
            self.games.append(GameButton("games\\" + i, text = i))
        
        for i in self.games:
            self.add_widget(i)             
   
        
class MyButton(Button):
    clicked = False
    patch = ""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.font_size = self.height * 0.25
        self.font_name = "label_font.ttf"
        self.background_normal = ""
        self.background_color = (0.95 ,0.95, 0.95, 0.6)
        self.color = (0, 0.25, 0.3, 1)
        self.bold = True
        self.disabled = True
        
    def on_release(self):
        self.clicked = True
        return super().on_release()


class GameButton(MyButton):        
    def __init__(self, patch, **kwargs):
        super().__init__(**kwargs)
        
        self.patch = patch
        self.size_hint = (None, None)
        self.size = (dp(200), dp(200))
        self.font_size = self.width*0.2
        self.color = (1, 1, 1, 1)
        self.background_color = (1, 1, 1, 1)
        self.background_normal = patch + "\image.jpg"
        self.background_down = patch + "\image.jpg"
        self.background_disabled_normal = patch +"\image.jpg"
        self.background_disabled_down = patch + "\image.jpg"
        self.disabled = False
        
        
KivyLauncherApp().run()
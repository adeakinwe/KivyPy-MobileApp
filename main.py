# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:32:03 2020

@author: Adeseto
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def login_success(self, uname, pword):
        with open("db.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "login_success_screen"
        else:
            self.ids.wrong_login.text = "Invalid Username or Password!"

class RootWidget(ScreenManager):
    pass

class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        with open("db.json") as file:
            users = json.load(file)

        users[uname] = {"username": uname, "password": pword, 
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        with open("db.json", "w") as file:
            json.dump(users, file)
        self.manager.current = "sign_up_success_screen"

class SignUpSuccessScreen(Screen):
    def go_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"

class LoginSuccessScreen(Screen):
    def login(self):
        self.manager.current = "login_screen"

class MainApp(App):
    def build(self):
        return RootWidget()
    
if __name__ == "__main__":
    MainApp().run()
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.tabbedpanel import TabbedPanel
# from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.image import AsyncImage
from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_file('new_design.kv')
# This needs to be here to display the manga images on Android


import random

# kivy.require('1.9.0')
kivy.require('2.1.0')

# https://www.youtube.com/watch?v=6gNpSuE01qE
# https://buildozer.readthedocs.io/en/latest/installation.html
## add the following line at the end of your ~/.bashrc file
##export PATH=$PATH:~/.local/bin/
##alias python='python3'
###https://buildozer.readthedocs.io/en/latest/quickstart.html
##buildozer init
##buildozer -v android debug

# class TabLayout(TabbedPanel):
#
#     def __init__(self):
#         super(TabLayout, self).__init__()

# class MyRoot(BoxLayout):

class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1
        # self.row_force_default = True
        # self.row_default_height = 40
        # self.col_force_default = True
        # self.col_default_width = 100
        self.top_grid = GridLayout(
            # row_force_default=True,
            # row_default_height=40,
            # col_force_default=True,
            # col_default_width=100
        )
        self.top_grid.cols = 2

        self.top_grid.add_widget(Label(text="Name: ",
                                       # size_hint_y=None,
                                       # height=50,
                                       # size_hint_x=None,
                                       # width=200
                                       ))
        self.name = TextInput(multiline=False,
                              # size_hint_y=None,
                              # height=50,
                              # size_hint_x=None,
                              # width=400
                              )
        self.top_grid.add_widget(self.name)
        #Add top grid to the app
        self.add_widget(self.top_grid)

        self.submit = Button(text='Submit',
                             font_size=32,
                             size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=200
                             )
        self.submit.bind(on_press=self.press1)
        self.add_widget(self.submit)

    def press1(self, instance):
        name = self.name.text
        self.add_widget(Label(text=name))
        self.name.text = ""

class MyRoot(TabbedPanel):

    def __init__(self):
        super(MyRoot, self).__init__()
        self.dice_roll = self.roll_dice
        self.n_dice_rolls = self.roll_N_dice
        self.dice_count = 3

    def spinner_clicked(self, value):
        self.dice_count = int(value)
        self.ids.dropdown.text = value

    def generate_number(self):
        self.random_label.text = str(self.roll_N_dice(n=self.dice_count))

    def roll_dice(self):
        return random.choice(range(1, 7))

    def roll_N_dice(self, n=3):
        roll_lst = []
        for i in range(n):
            roll_lst.append(self.dice_roll())
        return roll_lst

    def animate_it(self, widget, *args):
        animate = Animation(
            background_color=(0, 0, 1, 1),
            duration=.2
        )
        animate += Animation(
            size_hint=(.6, .6)
        )
        animate += Animation(
            size_hint=(.5, .5)
        )
        # Star the animation
        animate.start(widget)
        animate.bind(on_complete=self.my_callback)

    def my_callback(self, *args):
        self.ids.my_label.text = "Button clicked"

    def add_class_tab(self):
        test_add_class = MyGridLayout()
        self.ids.tst_add_class.add_widget(test_add_class)
        ## test adding image to carousel
        im_1_src = 'https://www.warhammer-community.com/wp-content/uploads/2021/07/dbOjvYzRFOU8mo6s-500x157.png'
        im_1 = Factory.AsyncImage(source=im_1_src, allow_stretch=True)
        self.ids.image_1.add_widget(im_1)

    # class MyGridLayout(GridLayout):
    #
    #     def __init__(self, **kwargs):
    #         super().__init__(**kwargs)
    #         super(self.MyGridLayout, self).__init__(**kwargs)
    #         self.cals = 2
    #         self.add_widget(Label(text="Name: "))
    #         self.name = TextInput(multiline=False)
    #         self.add_widget(self.name)


class KillTeamHelper(App):

    def build(self):
        return MyRoot()
        # return MyGridLayout()

    def on_start(self):
        Clock.schedule_once(lambda dt: self.root.add_class_tab())


kill_team_helper = KillTeamHelper()
kill_team_helper.run()

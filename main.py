import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random
kivy.require('1.9.0')
#https://www.youtube.com/watch?v=6gNpSuE01qE
#https://buildozer.readthedocs.io/en/latest/installation.html
## add the following line at the end of your ~/.bashrc file
##export PATH=$PATH:~/.local/bin/
##alias python='python3'
###https://buildozer.readthedocs.io/en/latest/quickstart.html
##buildozer init
##buildozer -v android debug

class MyRoot(BoxLayout):

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


class NeuralRandom(App):

    def build(self):
        return MyRoot()


neuralRandom = NeuralRandom()
neuralRandom.run()

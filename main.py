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

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 1000))


class NeuralRandom(App):

    def build(self):
        return MyRoot()


neuralRandom = NeuralRandom()
neuralRandom.run()

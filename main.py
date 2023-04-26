import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

options = ["rock", "paper", "scissors", "lizard", "Spock"]
user_score = 0
computer_score = 0
ties = 0

class MyRockPaperScissorsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        title_label = Label(text="Rock, Paper, Scissors")
        layout.add_widget(title_label)
        self.user_input = TextInput(text='', multiline=False)
        layout.add_widget(self.user_input)
        submit_button = Button(text="Submit", on_press=self.play_game)
        layout.add_widget(submit_button)
        self.result_label = Label(text="")
        layout.add_widget(self.result_label)
        return layout

    def play_game(self, instance):
        user_choice = self.user_input.text.lower()
        if user_choice not in options:
            self.result_label.text = "Invalid choice. Try again."
            return
        computer_choice = random.choice(options)
        self.result_label.text = "The computer chose: " + computer_choice
        global user_score, computer_score, ties
        if user_choice == computer_choice:
            self.result_label.text += "\nIt's a tie!"
            ties += 1
        elif (user_choice == "rock" and computer_choice in ["scissors", "lizard"]) or \
             (user_choice == "paper" and computer_choice in ["rock", "Spock"]) or \
             (user_choice == "scissors" and computer_choice in ["paper", "lizard"]) or \
             (user_choice == "lizard" and computer_choice in ["paper", "Spock"]) or \
             (user_choice == "Spock" and computer_choice in ["rock", "scissors"]):
            self.result_label.text += "\nYou win!"
            user_score += 1
        else:
            self.result_label.text += "\nThe computer wins!"
            computer_score += 1
        self.result_label.text += f"\n\nUser score: {user_score}\nComputer score: {computer_score}\nTies: {ties}"

if __name__ == '__main__':
    MyRockPaperScissorsApp().run()

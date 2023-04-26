import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.animation import Animation

options = ["rock", "paper", "scissors", "lizard", "Spock", "fire", "water", "air", "earth"]

win_sound = SoundLoader.load('win.wav')
lose_sound = SoundLoader.load('lose.wav')
tie_sound = SoundLoader.load('tie.wav')
button_sound = SoundLoader.load('button.wav')


class MyRockPaperScissorsApp(App):
    def build(self):
        self.user_score_label = Label(text="User score: 0", font_size="20sp", color=(0, 0, 0, 1))
        self.computer_score_label = Label(text="Computer score: 0", font_size="20sp", color=(0, 0, 0, 1))
        self.tie_label = Label(text="Ties: 0", font_size="20sp", color=(0, 0, 0, 1))
        self.result_label = Label(text="", font_size="20sp", color=(0, 0, 0, 1))
        self.buttons = []
        for option in options:
            button = Button(text=option, font_size="20sp", size_hint=(0.3, 0.3))
            button.bind(on_press=self.play_game)
            self.buttons.append(button)
        box_layout = BoxLayout(orientation="vertical")
        box_layout.add_widget(self.user_score_label)
        box_layout.add_widget(self.computer_score_label)
        box_layout.add_widget(self.tie_label)
        for button in self.buttons:
            box_layout.add_widget(button)
        box_layout.add_widget(self.result_label)
        return box_layout

    def play_game(self, instance):
        user_choice = instance.text.lower()
        computer_choice = random.choice(options)
        user_score = int(self.user_score_label.text.split()[-1])
        computer_score = int(self.computer_score_label.text.split()[-1])
        ties = int(self.tie_label.text.split()[-1])
        if user_choice == computer_choice:
            self.result_label.text += "\nIt's a tie!"
            ties += 1
            tie_sound.play()
            anim = Animation(size_hint=(1.2, 1.2), duration=0.2) + Animation(size_hint=(1, 1), duration=0.2)
            self.result_label.color = (1, 1, 1, 1)
            anim.start(self.result_label)
        elif (user_choice == "rock" and computer_choice in ["scissors", "lizard", "air"]) or \
                (user_choice == "paper" and computer_choice in ["rock", "Spock", "air"]) or \
                (user_choice == "scissors" and computer_choice in ["paper", "lizard", "air"]) or \
                (user_choice == "lizard" and computer_choice in ["paper", "Spock", "water"]) or \
                (user_choice == "Spock" and computer_choice in ["rock", "scissors", "fire"]) or \
                (user_choice == "fire" and computer_choice in ["scissors", "paper", "Spock"]) or \
                (user_choice == "water" and computer_choice in ["fire", "earth", "air"]) or \
                (user_choice == "air" and computer_choice in ["water", "earth", "fire"]) or \
                (user_choice == "earth" and computer_choice in ["water", "air", "Spock"]):
            self.result_label.text += f"\nYou win! {user_choice} beats {computer_choice}!"
            user_score += 1
            win_sound.play()
            anim = Animation(size_hint=(1.2, 1.2), duration=0.2) + Animation(size_hint=(1, 1), duration=0.2)
            self.result_label.color = (0, 1, 0, 1)
            anim.start(self.result_label)
        else:
            self.result_label.text += f"\nYou lose! {computer_choice} beats {user_choice}!"
            computer_score += 1
            lose_sound.play()
            anim = Animation(size_hint=(1.2, 1.2), duration=0.2) + Animation(size_hint=(1, 1), duration=0.2)
            self.result_label.color = (1, 0, 0, 1)
            anim.start(self.result_label)
        self.user_score_label.text = f"User score: {user_score}"
        self.computer_score_label.text = f"Computer score: {computer_score}"
        self.tie_label.text = f"Ties: {ties}"
        button_sound.play()

if __name__ == '__main__':
    MyRockPaperScissorsApp().run()
import time
import itertools
import simpleaudio as sa
from random import *

# Dancing moves: name and steps
dance_moves = [
    {"name": "sugar push", "steps": 6},
    {"name": "left side pass", "steps": 6},
    {"name": "whip", "steps": 8},
    {"name": "under arm", "steps": 6},
    {"name": "sugar tuck", "steps": 6},
]

# Dancing moves sounds
figure_sounds = {
    "sugar push": sa.WaveObject.from_wave_file("sounds/sugar_push.wav"),
    "left side pass": sa.WaveObject.from_wave_file("sounds/left_side_pass.wav"),
    "whip": sa.WaveObject.from_wave_file("sounds/whip.wav"),
    "under arm": sa.WaveObject.from_wave_file("sounds/under_arm.wav"),
    "sugar tuck": sa.WaveObject.from_wave_file("sounds/sugar_tuck.wav"),
}

# Load sounds
tick_sound = sa.WaveObject.from_wave_file("sounds/tick.wav")
accent_sound = sa.WaveObject.from_wave_file("sounds/accent.wav")

# Metronome patameters
bpm = 80  # beats per minute
beat_interval = 60 / bpm  # one step in seconds

# Always starting with sugar push
start_with_sugar_push = True

# Generate sequence of dancing moves (`dance_moves` indexes)
dance_sequence = []

def generate_sequence(start_with_sugar_push):
    if start_with_sugar_push:
        dance_sequence.append(1)

    while len(dance_sequence) < 10:
        new_move = randrange(0, len(dance_moves))+1
        if not dance_sequence or new_move != dance_sequence[-1]:
            dance_sequence.append(new_move)
    print(dance_sequence) # Show the sequence


def play_figure_name(figure_name):
    # Play move sound depending on it's name
    if figure_name in figure_sounds:
        figure_sounds[figure_name].play()


def play_tick(accent=False):
    # Play metronome ticks
    if accent:
        accent_sound.play()
    else:
        tick_sound.play()


def starter_ticks(beat_interval):
    for i in range(3):
        play_tick(accent=False)
        time.sleep(beat_interval)
    play_tick(accent=True)
    time.sleep(beat_interval)


def dance_trainer():
    generate_sequence(start_with_sugar_push) # Generating move sequence
    print("Training started")
    sequence = itertools.cycle(dance_sequence)  # Looping sequence

    # Starting with 4 ticks
    starter_ticks(beat_interval)

    # Get the first move
    current_index = next(sequence)

    while True:
        # Current move
        current_move = dance_moves[current_index -1]
        current_name = current_move["name"]
        current_steps = current_move["steps"]

        # Get the next move
        next_index = next(sequence)
        next_move = dance_moves[next_index - 1]
        next_name = next_move["name"]

        # Current move info
        print(f"Now dancing: {current_name} ({current_steps} steps).")

        # Metronome ticks and give next move
        for step in range(1, current_steps + 1):
            if step == (current_steps // 2):
                print(f"Next move: {next_name}.")
                play_figure_name(next_name)
            if step == current_steps:
                print("TICK (accent)")  # Accent on the last step
                play_tick(accent=True)
            else:
                print("tick")
                play_tick(accent=False)
            time.sleep(beat_interval)  # Time between steps

        # Go to next move
        current_index = next_index

if __name__ == "__main__":
    dance_trainer()

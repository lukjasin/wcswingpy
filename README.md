# WCSwingPy

WCSwingPy is a Python application designed to assist beginner dancers practicing **West Coast Swing** (WCS). The app helps users practice and refine the technique of basic dance moves, allowing them to train at their own pace with a metronome and verbal cues for the dance figures.

### Features:
- **Metronome**: Currently, the app supports 5 basic WCS figures, which you can practice with correct timing and rhythm.
- **Self-Paced Practice**: The app allows you to practice at your own pace and will be enhanced to include more customizable features in the future.

### Prerequisites:
Before running the application, make sure you have the following Python library installed:
- **simpleaudio**: This library is required for playing sound files (such as metronome ticks and figure names).

### How to Run:

1. **Clone or Download** the repository for WCSwingPy.
```bash
git clone https://github.com/lukjasin/wcswingpy.git
```
2. Open your terminal and navigate to the directory where the app is located.
3. Install requirements
```bash
pip install -r requirements
```
4. Run the Python script:
```bash
python3 wcswing.py
```

### How It Works:
- The app will play a metronome sound to help you keep time with the dance moves.
- It will also play verbal cues with the names of the figures you are practicing (e.g., "sugar push", "whip").
- Each figure has a designated number of steps, and you can follow along as the app guides you through the sequence.

### Usage:
- **Metronome**: The metronome is set to 80 BPM (beats per minute) by default. It will play a "tick" sound on every beat and an "accent" on the final step of each figure.
- **Dance Figure Names**: As you practice, the app will announce the name of the next figure, helping you to keep track of what you're working on.


### To Do:
- **Volume Control**: Adjusting the volume of the sounds for metronome ticks and dance figure names as needed.

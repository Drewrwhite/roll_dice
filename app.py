from flask import Flask, request, render_template
import random

import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def parse_input(input_string):
    """Return `input_string` as num between 1 and 6.
    Check if `input_string` is num between 1 and 6.
    If so, return num with the same value. Otherwise, tell  user to enter valid number and quit program.
    """
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

def roll_dice(num_dice):
  """ Return list of integers with length `num_dice`
  Each num in return list is random num between 1 - 6 
  """
  roll_results = []
  for _ in range(num_dice):
    roll = random.randint(1, 6)
    roll_results.append(roll)
  return roll_results

def generate_dice_faces_diagram(dice_values):
  """ Return ASCII diagram of dice faces for results
  """
  # Generate dice faces in list
  dice_faces = []
  for value in dice_values:
    dice_faces.append(DICE_ART[value])
  # Generate dice face rows in list
  dice_faces_rows = []
  for row_idx in range(DIE_HEIGHT):
    row_components = []
    for die in dice_faces:
      row_components.append(die[row_idx])
    row_string = DIE_FACE_SEPARATOR.join(row_components)
    dice_faces_rows.append(row_string)
  # Generate header for RESULTS centered
  width = len(dice_faces_rows[0])
  diagram_header = " RESULTS ".center(width, "~")

  dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
  return dice_faces_diagram

def _get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces

def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/roll_dice', methods=['POST'])
def roll_dice_route():
    if request.method == 'POST':
        num_dice_input = request.form['num_dice']
        num_dice = parse_input(num_dice_input)
        roll_results = roll_dice(num_dice)
        dice_faces = _get_dice_faces(roll_results)
        dice_faces_rows = _generate_dice_faces_rows(dice_faces)
        dice_face_diagram = "\n".join(dice_faces_rows)
        return render_template('roll_dice.html', dice_face_diagram=dice_face_diagram)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
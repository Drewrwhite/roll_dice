from flask import Flask, request, render_template, url_for
import random

DICE_ART = {
    1: "images/dice-1.png",
    2: "images/dice-2.png",
    3: "images/dice-3.png",
    4: "images/dice-4.png",
    5: "images/dice-5.png",
    6: "images/dice-6.png",
}
DIE_HEIGHT = 100
DIE_WIDTH = 100

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
    """Return HTML code for displaying dice images for results."""
    # Generate dice images in list
    dice_images = []
    for value in dice_values:
        dice_images.append(DICE_ART[value])
    # Generate HTML code for displaying dice images
    dice_images_html = ""
    for image in dice_images:
        dice_images_html += '<img src="{}" height="{}" width="{}" alt="Dice">\n'.format(
            url_for("static", filename=image), DIE_HEIGHT, DIE_WIDTH
        )
    # Generate header for RESULTS centered
    diagram_header = '<h2 style="text-align:center">RESULTS</h2>'
    # Wrap dice images in new div element with class
    dice_images_html = '<div class="dice-images">' + dice_images_html + '</div>'
    dice_face_diagram = diagram_header + dice_images_html
    return dice_face_diagram



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
        dice_faces_diagram = generate_dice_faces_diagram(roll_results)
        return render_template('roll_dice.html', dice_face_diagram=dice_faces_diagram)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

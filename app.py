from flask import Flask, request, render_template
import random



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/roll_dice', methods=['POST'])
def roll_dice_route():
    num_dice_input = request.form['num_dice']
    num_dice = parse_input(num_dice_input)
    roll_results = roll_dice(num_dice)
    dice_face_diagram = generate_dice_faces_diagram(roll_results)
    return render_template('roll_dice.html', dice_face_diagram=dice_face_diagram)
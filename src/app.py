from flask import Flask, request, render_template #import main Flask class and request object
from tactics_finder import tactics_finder
import jinja2
import os
from pgn_capsule import pgn_capsule

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir))


app = Flask(__name__) #create the Flask app

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        print("Hello")
        min_cent = int(request.form.get('min'))
        max_cent = int(request.form.get('max'))
        depth = int(request.form.get('depth'))
        game = pgn_capsule(request.form.get('chess_game'))

        fen_list = tactics_finder(game,min_cent,max_cent,depth) 
        output = ""
        for i in fen_list:
            output+="<li>"+i
        temp = jinja_env.get_template(name="list.html")
        return temp.render(output=output)

    temp = jinja_env.get_template(name="home_bootstrap.html")
    return temp.render()

app.run(debug=True, port=5000) #run app in debug mode on port 5000
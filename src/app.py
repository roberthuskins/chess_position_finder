from flask import Flask, request, render_template 
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
    #https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request#16664376
    if request.method == 'POST':
        #if the form is called we go here
        min_cent = int(request.form.get('min'))
        max_cent = int(request.form.get('max'))
        depth = int(request.form.get('depth'))

        #https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request.files
        #this needs to be investigated for memory leaks
        game = request.files.get('chess_game')

        #read method returns a bytes object, so we have to convert to string
        game_string = game.read().decode('utf-8')
        game.close()

        fen_list = tactics_finder(pgn_capsule(game_string),min_cent,max_cent,depth) 
        output = ""
        for i in fen_list:
            output+="<li class=\"list-group-item\">"+i + "</li>"
        temp = jinja_env.get_template(name="list.html")
        return temp.render(output=output)

    temp = jinja_env.get_template(name="home_bootstrap.html")
    return temp.render()

app.run(debug=True, port=5000) 
#run app in debug mode on port 5000
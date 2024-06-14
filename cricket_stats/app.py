from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Configure MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.cricket_db
players_collection = db.players

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_player():
    if request.method == 'POST':
        player = {
            "name": request.form['name'],
            "jersey_number": int(request.form['jersey_number']),
            "matches_played": int(request.form['matches_played']),
            "wickets_taken": int(request.form['wickets_taken']),
            "runs_scored": int(request.form['runs_scored']),
            "special_skill": request.form['special_skill']
        }
        players_collection.insert_one(player)
        return redirect(url_for('player_list'))
    return render_template('add_player.html')

@app.route('/players')
def player_list():
    players = players_collection.find()
    return render_template('player_list.html', players=players)

@app.route('/update/<player_id>', methods=['GET', 'POST'])
def update_player(player_id):
    player = players_collection.find_one({"_id": ObjectId(player_id)})
    if request.method == 'POST':
        updated_player = {
            "name": request.form['name'],
            "jersey_number": int(request.form['jersey_number']),
            "matches_played": int(request.form['matches_played']),
            "wickets_taken": int(request.form['wickets_taken']),
            "runs_scored": int(request.form['runs_scored']),
            "special_skill": request.form['special_skill']
        }
        players_collection.update_one({"_id": ObjectId(player_id)}, {"$set": updated_player})
        return redirect(url_for('player_list'))
    return render_template('update_player.html', player=player)

@app.route('/delete/<player_id>')
def delete_player(player_id):
    players_collection.delete_one({"_id": ObjectId(player_id)})
    return redirect(url_for('player_list'))

@app.route('/search_player', methods=['GET'])
def search_player():
    jersey_number = request.args.get('jersey_number')
    player = players_collection.find_one({'jersey_number': int(jersey_number)})
    if player:
        return render_template('player_details.html', player=player)
    else:
        return render_template('player_not_found.html', jersey_number=jersey_number)

if __name__ == '__main__':
    app.run(debug=True)

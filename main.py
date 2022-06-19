from  flask import Flask,jsonify,request
import csv

movies = []
with open('movies.csv',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    movies = data[1:]

liked_movies = []
not_liked_moves = []
did_not_watch = []

app = Flask(__name__)
@app.route("/get-movie")

def get_movie():
    return jsonify({
        'data':movies[0],
        'status':'success'
    })

@app.route("/liked-movie",methods=['POST'])

def liked_movie():
    movie = movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        'status':'success'
    })

@app.route("/unliked-movie",methods=['POST'])

def unliked_movie():
    movie = movies[0]
    movies = movies[1:]
    not_liked_moves.append(movie)
    return jsonify({
        'status':'success'
    }),201

@app.route("/did-not-watch",methods = ['POST'])

def did_not_watch():
    movie = movies[0]
    movies = movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        'status':'success'
    }),201

if __name__ == '__main__':
    app.run()
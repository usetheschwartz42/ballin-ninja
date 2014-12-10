from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

#
#*********************Index page***************************
#

@app.route('/')
def index():
    return redirect(url_for('music'))

#
#*********************Asset Route**************************
#

@app.route('/static/<asset>')
def assets(asset):
    return url_for('static', filename=asset)

#
#*********************Music Page***************************
#

#Songs
songs = []

#Song Dictionaries
songOne = {'name': 'Song One', 'album': 'Test', 'artist': 'Aspect', 'id': 0}
songTwo = {'name': 'Song Two', 'album': 'Strings', 'artist': 'Aspect', 'id': 1}
songThree = {'name': 'Song Three', 'album': 'Test', 'artist': 'Aspect', 'id': 2}

songs.append(songOne)
songs.append(songTwo)
songs.append(songThree)



@app.route('/music')
def music():
    return render_template('music.html', songs=songs, numSongs=len(songs), currentSong=songOne['id'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

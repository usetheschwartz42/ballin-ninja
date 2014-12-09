from flask import Flask, url_for, redirect, render_template
import sys
sys.path.append('./config')
import config

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

songs = config.songs()

@app.route('/music')
def music():
    return render_template('music.html', songs=songs, numSongs=len(songs), currentSong=4)

#**********************************************************

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

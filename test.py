

print('start')

from flask import Flask
from flask import Response
from flask import request, session, abort
from flask import redirect
from flask import render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def game():
    return render_template('game.html')


@app.route('/gameover', methods=['GET', 'POST'])
def gameover():
    return render_template('gameover.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)



print('all ok')
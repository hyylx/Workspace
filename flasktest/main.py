from flask import Flask
from flask import request
from gw_quppa import VTECQuppa


Qtag = VTECQuppa()
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1> ' \
           '<p>Getting Location ' + str(Qtag.get_location()) + ' for ' + str(Qtag.get_tag_message()) + '</p>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin"method="post">
             <p><input name="username"></p>
             <p><input name="password" type="password"></p>
             <p><button type="submit">Sign In</button></p>
             </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username']=='xin' and request.form['password']=='12345':
        return '<h3>Hello!</h3>'
    else:
        return '<h3>No!</h3>'

if __name__ == "__main__":
    app.run(debug=True)


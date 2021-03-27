from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'My name is Patrick majoring in Engineering Undecalred Program. I like playing badminton. I want to be the role of frontend.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Saving file will reload the server
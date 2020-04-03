from flask import Flask, render_template

#create an instance of an application/initialize my flask application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return  render_template('contact.html')

@app.route('/<name>')
def about(name):
    return render_template('about.html',name=name)

@app.route('/<a>/<b>')
def sum(a,b):
    total=int(a)+int(b)
    return render_template('index.html',total=total)


if __name__ == '__main__':
    app.run()

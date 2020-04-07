from flask import Flask, render_template, request, redirect, url_for

#create an instance of an application/initialize my flask application
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return  render_template('contact.html')

# @app.route('/<name>')
# def about(name):
#     return render_template('about.html',name=name)

# @app.route('/<a>/<b>')
# def sum(a,b):
#     total=int(a)+int(b)
#     return render_template('index.html',total=total)

@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/service')
def service():
    return render_template('service.html')



@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/inventories', methods=['GET','POST'])
def inventories():
    
    if request.method == 'POST':
        name = request.form['name']
        inv_type = request.form['type']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']

        print(name)
        print(inv_type)
        print(buying_price)
        print(selling_price)

        return redirect(url_for('inventories'))


    return render_template('inventories.html')





if __name__ == '__main__':
    app.run()

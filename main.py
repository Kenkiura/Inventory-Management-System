from flask import Flask, render_template, request, redirect, url_for


import pygal



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



#A route to receive stock data from stock modal

@app.route('/add_stock', methods=['POST'])
def add_stock():

    #check if the method is POST
    if request.method == 'POST':
        stock = request.form['stock']
        print(stock)

        return redirect(url_for('inventories'))

#Create a route to receive sale data from sale modal

@app.route('/add_sale', methods=['POST'])
def add_sale():

    #check if the method is POST
    if request.method == 'POST':
        sale = request.form['sale']
        print(sale)


        return redirect(url_for('inventories'))



#Create a route to receive edit data from edit modal

@app.route('/edit', methods=['POST'])
def edit():

    #check if the method is POST

    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']


        print(name)
        print(type)
        print(buying_price)
        print(selling_price)



        return redirect(url_for('inventories'))


#DATA VISUALIZATION

@app.route('/data_visualization')
def data_visualization():

    #Initialize the pie_chart
    pie_chart = pygal.Pie()

    #Add components to your pie_chart

    #1. Add pie_chart titles
    #2. Partition your chart using a tuple
    my_pie_data =[('Nairobi', 63), ('Mombasa', 20), ('Kilifi', 17), ('Machakos', 30), ('Kiambu', 7)]

    pie_chart.title = 'Corona Virus distribution in Kenya'
    pie_chart.add(my_pie_data([0]))
    

    pie_data = pie_chart.render_data_uri

    return pie_chart.render()


    pie_chart.title = 'Distribution of corona virus in Kenya'
    pie_chart.add('Nairobi', 63)
    pie_chart.add('Mombasa', 20)
    pie_chart.add('Kilifi', 17)
    pie_chart.add('Machakos', 30)
    pie_chart.add('Kiambu', 7)

    pie_data = pie_chart.render_data_uri()
    


    #return pie_chart.render()
    #end of pie_chart

    #start of line_graph

    line_graph = pygal.Line()

    line_graph.title = 'Browser usage evolution (in %)'
    line_graph.x_labels =  range(2002, 2013)
    line_graph.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    line_graph.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    line_graph.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    line_graph.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    
    line_data = line_graph.render_data_uri()

    #return render_template('chart.html', line = line_data, pie = pie_data)




    #return 'My charts come here'






if __name__ == '__main__':
    app.run()

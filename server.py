from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/dojo')
def hello_dojo():
    return render_template('dojo.html')

@app.route('/say/<string:name>')
def hello_person(name):
    return render_template('person.html', name=name)

@app.route('/repeat/<int:num>/<string:object>')
def print_times(num, object):
    return render_template('repeat.html', num=num, object=object)

if __name__ == "__main__":
    app.run(debug=True)
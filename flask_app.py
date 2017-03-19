from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/result/', methods=['POST', 'GET'])
def result():
    error = None
    if request.method == 'POST':
        result = request.form
        for key, val in result.items():
            if key == 'name':
                name = val
            elif key == 'age':
                age = val
            elif key == 'favninja':
                ninja = val
        if name == '' or age == '' or ninja == '':
            error = 'Please fill in all fields.'
    return render_template("result.html", name=name, age=age,
                           ninja='Patrick Huston', error=error)


if __name__ == '__main__':
    app.run()

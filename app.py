from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def register_form():
    return render_template('register.html')

@app.route('/success', methods=['POST'])
def success():
    name = request.form['name']
    roll = request.form['roll']
    email = request.form['email']
    year = request.form['year']
    return render_template('success.html', name=name, roll=roll, email=email, year=year)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('calculator.html')
# @app.route('/products')
# def product():
#     return 'This is product page'

if __name__ == "__main__":
    app.run(debug=True)
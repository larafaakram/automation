from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    numbers = []
    if request.method == 'POST':
        try:
            num = int(request.form['number'])
            if num % 2 == 0:
                result = f"{num} is an even number."
            else:
                result = f"{num} is an odd number."
            
            numbers = list(range(1, num + 1))
        except ValueError:
            result = "Please enter a valid integer."

    return render_template('index.html', result=result, numbers=numbers)

if __name__ == "__main__":
    app.run(debug=True)

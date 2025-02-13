from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def compare_numbers():
    result = None  # Initialize result

    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])

            if num1 > num2:
                result = f"{num1} is greater than {num2}"
            elif num2 > num1:
                result = f"{num2} is greater than {num1}"
            else:
                result = "The numbers are equal."
        except ValueError:
            result = "Invalid input. Please enter numbers."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)  # Debug mode for development.  Set debug=False in production.
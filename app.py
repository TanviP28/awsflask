from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi_result = None

    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Classify BMI
        if bmi < 18.5:
            category = 'Underweight'
        elif 18.5 <= bmi < 24.9:
            category = 'Normal Weight'
        elif 25 <= bmi < 29.9:
            category = 'Overweight'
        else:
            category = 'Obese'

        bmi_result = {'bmi': bmi, 'category': category}

    return render_template('bmi_calculator.html', bmi_result=bmi_result)

if __name__ == '__main__':
    app.run(debug=True)

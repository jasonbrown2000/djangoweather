drinks = {
    "beer": {
        "calories": 182,
        "alcohol_units": 2.3
    },
    "wine": {
        "calories": 159,
        "alcohol_units": 2.3
    },
    "spirit": {
        "calories": 61,
        "alcohol_units": 1.0
    },
    "cider": {
        "calories": 216,
        "alcohol_units": 2.6
    },
    "champagne": {
        "calories": 89,
        "alcohol_units": 1.5
    },
    "alcopops": {
        "calories": 170,
        "alcohol_units": 1.1
    },
}

@app.route('/calculator.html', methods=['POST'])
def calculator():
    total_calories = 0
    total_alcohol_units = 0

    for drink in request.form.getlist('drink'):
        total_calories += drinks[drink]['calories']
        total_alcohol_units += drinks[drink]['alcohol_units']

    calculation_result = f'Total calories: {total_calories}, Total alcohol units: {total_alcohol_units}'

    return render_template('result.html', total_calories=total_calories, total_alcohol_units=total_alcohol_units)
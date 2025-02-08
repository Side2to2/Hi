from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    first_operand = data.get('first_operand')
    second_operand = data.get('second_operand')
    operator = data.get('operator')

    if not all([first_operand, second_operand, operator]):
        return jsonify({'error': 'Invalid input'}), 400

    try:
        first_operand = float(first_operand)
        second_operand = float(second_operand)
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400

    if operator == '+':
        result = first_operand + second_operand
    elif operator == '-':
        result = first_operand - second_operand
    elif operator == '*':
        result = first_operand * second_operand
    elif operator == '/':
        if second_operand == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = first_operand / second_operand
    else:
        return jsonify({'error': 'Invalid operator'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

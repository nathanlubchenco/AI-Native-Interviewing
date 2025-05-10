from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json() or {}
    x = data.get('x')
    y = data.get('y')
    if y == 0:
        return jsonify({'error': 'division by zero'}), 400
    # BUG: using integer division instead of float
    result = x // y
    return jsonify({'result': result})

@app.route('/median', methods=['POST'])
def median():
    data = request.get_json() or {}
    nums = data.get('nums', [])
    n = len(nums)
    if n == 0:
        return jsonify({'error': 'empty list'}), 400
    mid = n // 2
    if n % 2 == 1:
        # BUG: list is not sorted before selecting median
        med = nums[mid]
    else:
        med = (nums[mid - 1] + nums[mid]) / 2
    return jsonify({'median': med})

if __name__ == '__main__':
    app.run(port=5000)
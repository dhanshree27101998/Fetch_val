from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a GET endpoint
@app.route('/api/data', methods=['GET'])
def get_data():
    # Access query parameters
    print("in get_data")
    param1 = request.args.get('param1')
    param2 = request.args.get('param2')
    headers = dict(request.headers)

    # Create a response dictionary
    response_data = {
        'param1': param1,
        'param2': param2,
        'message': 'GET request received!',
        'headers': headers
    }

    # Return the response as JSON
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/personal_data', methods=['GET'])
def personal_data():
    login = request.args.get('login')
    if login == 'is-21fiot-22-038':
        personal_info = {
            'surname': 'Delita',
            'name': 'Diana',
            'course': '2 course',
            'group': 'IC-21'
        }
        return jsonify(personal_info)
    else:
        return jsonify({'error': 'Invalid login'}), 401

if __name__ == '__main__':
    app.run(debug=True)

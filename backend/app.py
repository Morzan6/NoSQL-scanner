from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return jsonify({'':'noSQL goes brr'})

if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify
from multiprocessing import Value
app = Flask(__name__)

counter = Value('i', 0)
app = Flask(__name__)

@app.route('/')
def index():
    with counter.get_lock():
        counter.value += 1
        out = counter.value

    return jsonify(count=out)

app.run()

if __name__ == '__main__':  
    app.run()
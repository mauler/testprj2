#!flask/bin/python

from flask import Flask, jsonify

from task2.app import Task2

app = Flask(__name__)
task2 = Task2()


@app.route('/fib/<int:fib_start>/<int:fib_end>', methods=['GET'])
def get_fibonacci(fib_start, fib_end):
    return jsonify(task2.get_fibonacci(fib_end, fib_start))


@app.route('/health', methods=['GET'])
def get_health():
    return jsonify(task2.get_app_status())


def main():
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    main()

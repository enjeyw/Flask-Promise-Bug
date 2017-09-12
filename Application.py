from flask import Flask, render_template, jsonify

application = Flask(__name__)


@application.route('/')
def index():
    return render_template('index.html')

@application.route('/foo/', methods = ['GET'])
def get_foo():
    return jsonify({'message': 'bar'}), 200

if __name__ == '__main__':
    # application.run(threaded = True) # This works
    application.run()                # This doesn't


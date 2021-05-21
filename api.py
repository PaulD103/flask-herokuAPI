from flask import Flask

app = Flask(__name__)

@app.route('/data')
def get_data():
    return {'data': 'This is the data of your api!'}

# flask-herokuAPI

## Requirements
* [Python](https://www.python.org): A recent Python 3 interpreter to run the Flask backend on.

## Creating a Flask API Backend
The next step is to create the Flask project. For this, open your terminal and change your directory to a place, where you want to create your API. <br>
Now type this into your terminal. <br>

**Create directory** <br>
`mkdir api` <br>
**Move into this directory** <br>
`cd api` <hr><br>

I always create a virtual environment called venv in my project directory, so let's do that now: <br>
`$ python3 -m venv venv` <br>
After that you have to activate that environment: <br>
`$ source venv/bin/activate
(venv) $ _` <br>

Note that the above is for Unix-based operating systems. If you are using Windows, then you will do this instead: <br>
`$ python -m venv venv` <br>
`$ venv\Scripts\activate` <br>
`(venv) $ _` <hr><br>

For this simple example you need only one Python package - **Flask**: <br>
`(venv) $ pip install flask python-dotenv` <br>

For this example I'm going to create a small, single file and single endpoint application. Here is my Flask API project, written as a single file called _api.py_:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/data')
def get_data():
    return {'data': 'This is the data of your api!'}
```

This little API responds to the _/data_ URL with a **JSON** payload such as this:
```
{"data": "This is the data of your api!"}
```

As you probably know, Flask imports the application from the place indicated by the **FLASK_APP** environment variable. To avoid having to manually set this variable every time, I'm going to write a _.flaskenv_ file, which Flask automatically imports into the environment on startup if it finds the **python-dotenv** package installed. Here is my _.flaskenv_ file:
```
FLASK_APP=api.py
FLASK_ENV=development
```
I also added the **FLASK_ENV** variable, with a setting of **development**, which enables Flask's debug mode. In a **production version**, you have to delete the second line! <br><br>

## Run your project
At this point this basic Flask project is complete. To make sure that it is working well you can start it: <br>
`(venv) $ flask run` <br>
This will be the output:
```
 * Serving Flask app "api.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 673-234-166
```
To stop the Flask server press Ctrl-C.

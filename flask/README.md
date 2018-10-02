# Flask

Flask is a web framework for python, which offers you certain functions to operate or deliver data over the web. It is light weight and is very useful to get any app up and runing in no time.

# Why Flask?

Being light and utlizing speed of development in python, Flask is very usefu and efficient as well.

# What are templates?

While sending HTML as response from a request function from flask app, It is common to put dynamic data in that page, Say you need to show new posts which have been put in the database, You can generate the page dynamically by string formatiing and certain operators but using this apporach is highly inefficient and slows down the development curve,

This is where templates come into picture, Basically you pass variables while rendering templates and write some python code to play with those variables, It eases the stuff down.

# Lifting flask server

```python
from flask import Flask

app = Flask(__name__)

app.run(host="0.0.0.0", port=3004)
```

# Registering a route

```python
from flask import Flask

app = Flask(__name__)

@app.route("/your/path")
def routeFunc():
    return "Hello World", 200

app.run(host="0.0.0.0", port=3004)
```

# Using Templates

Refer [example](./example)

# References

* https://pymbook.readthedocs.io/en/latest/flask.html
* https://www.tutorialspoint.com/flask/
* https://www.youtube.com/watch?v=zRwy8gtgJ1A
* https://www.udemy.com/python-flask-tutorial-step-by-step/ (Free Course)
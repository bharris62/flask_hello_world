from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello, World!"


@app.route("/jedi/<first>/<last>")
def name_jedi(first, last):
    return "Your Name is {}{}".format(last[0:2], first[0:2])


@app.route("/hello/<name>")
def hi_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten!
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

if __name__ == "__main__":
    app.run()
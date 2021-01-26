
from flask import Flask, render_template,url_for
app = Flask(__name__)
debug=1
class Item:
    def __init__(self):
        pass
    
def create_Item(i:Item):
    
@app.route('/')
def Home():
    return render_template("Home.html")
@app.route("/wikiedit")
def Edit_Wiki():
    return "WikiEdit"


if __name__ == '__main__':
    if debug:
        app.run(host="localhost",port="835",debug=True)
    else:
        app.run(host="127.0.0.1",port=443)
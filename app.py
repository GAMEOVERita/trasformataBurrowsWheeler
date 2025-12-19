from flask import Flask, render_template, request
import client, config

app = Flask(__name__) # this is how Flask recognizes this file as the main file of the program

# flask goated, this is how simple it is to create a webpage with python
# sets the route for the function "index()" at the default page of the website and accept the use of both "GET" and "POST"
@app.route('/', methods=["GET", "POST"])
def index(output: str=""):
    if request.method == "POST":

        action = request.form.get("action")

        isDeTRSF = (action == "detransform") #flag to check whether the user wants to use btw() or reverse_btw()
        input_str = request.form.get("input_str")
        if input_str != "" and input_str != None:
            output = client.clientConnection(isDeTRSF, input_str)

    return render_template("index.html", output=output) # this renders the page "index.html" and passes the var "output"


if __name__ == "__main__":
    app.run(debug=config.debug)

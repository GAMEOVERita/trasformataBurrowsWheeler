from flask import Flask, render_template, request
import client, config

app = Flask(__name__) # this is how Flask recognizes this file as the main file of the program

# flask goated, this is how simple it is to create a webpage with python
# sets the route for the function "index()" at the default page of the website and accept the use of both "GET" and "POST"
@app.route('/', methods=["GET", "POST"])
def index(output: str=""):
    if request.method == "POST":

        action = request.form.get("action")

        # my original code 
        # i didn't really like it because it was bulky
        """
        if action == "transform": 
            isDeTRSF, input_str = False, request.form.get("input_str").encode() 
        elif action == "detransform": 
            isDeTRSF, input_str = True, request.form.get("input_str").encode()
        """

        # final code
        # easier to read and leaner
        isDeTRSF = (action == "detransform") #flag to check whether the user wants to use btw() or reverse_btw()
        input_str = request.form.get("input_str")
        if input_str != "" and input_str != None:
            output = client.clientConnection(isDeTRSF, input_str)

    return render_template("index.html", output=output) # this renders the page "index.html" and passes the var "output"

# flask run --debug
# python app.py
if __name__ == "__main__":
    app.run(debug=config.debug)





# here are some of the resorces i used 
"""
# flask official docs
https://flask.palletsprojects.com/en/stable/quickstart/

# explains how to add your customs cmd arguments to python --- NOT YET IMPLEMENTED
https://www.geeksforgeeks.org/python/command-line-arguments-in-python/

# flask tutorials on yt
https://www.youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX

# explains how to write shorter for loops
https://blog.teamtreehouse.com/python-single-line-loops
"""
from flask import Flask, render_template, request
import client

app = Flask(__name__) # this is how Flask recognizes this file as the main file of the program

# come collegare la pagina html a flask
@app.route('/', methods=["GET", "POST"])
#@app.route('/')
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
        isDeTRSF = (action == "detransform")
        input_str = request.form.get("input_str")
        if input_str != "" and input_str != None:
            output = client.clientConnection(isDeTRSF, input_str)

    return render_template('index.html', output=output)

# flask run --debug
if __name__ == '__main__':
    app.run(debug=True)






"""
# flask official docs
https://flask.palletsprojects.com/en/stable/quickstart/

# explains how to add your customs cmd arguments to python --- NOT YET IMPLEMENTED
https://www.geeksforgeeks.org/python/command-line-arguments-in-python/

# python official docs - explains how to use multiprocessing --- NOT YET IMPLEMENTED
https://docs.python.org/3/library/multiprocessing.html

# flask tutorials on yt
https://www.youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX

# explains how to write shorter for loops
https://blog.teamtreehouse.com/python-single-line-loops
"""
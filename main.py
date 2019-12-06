import webbrowser
from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)


#from HTML

@app.route("/")
def index():
    return render_template('index.html')

def move_forward():
    #Moving forward code
    print("Moving Forward...")

#Python Code



#End Python Code

#to HTML

f = open('excecute.js','w')

message = """<html>
<head></head>
<body><p>Hello World!""" """</p></body>
</html>"""



f.write(message)
f.close()

webbrowser.open_new_tab('excecute.js')
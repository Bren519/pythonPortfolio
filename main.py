import webbrowser
from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)


#from HTML

@app.route('/index')
def json():
    return render_template('index.html')


@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return "nothing"


#Python Code



#End Python Code

#to HTML

f = open('index.js','w')

message = """
function test (){
document.getElementById("dump").innerHTML = "<h1>Working!</h1>"
}



"""



f.write(message)
f.close()

webbrowser.open_new_tab('index.js')
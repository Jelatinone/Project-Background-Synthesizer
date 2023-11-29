"""
QAUNT

CREATOR:
    CODY WASHINGTON
    
DATE: 
    11/27/2023

DESCRIPTION:
    CUSTOMIZABLE WALLPAPER APPLICATION

"""
###------------------ IMPORTS ------------------###
from flask import Flask, render_template_string
import webbrowser

###------------------ SETUP ------------------ ###
WebApplication: Flask = Flask(__name__, static_folder = 'src')

HTML_CONTENT: str = """

"""

###------------------ RUN CODE ------------------###
@WebApplication.route('/')
def index():
    return render_template_string(HTML_CONTENT)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    WebApplication.run(debug=True)

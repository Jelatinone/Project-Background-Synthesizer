"""
PROJECT:
    QUANT

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


"""
This specifies the exact HTML content and JS that operate the main website processes
"""
HTML_CONTENT: str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quant</title>
    <style>
        body {
            margin: 0;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-size: cover;
            background-position: center;
            transition: opacity 2s ease-in-out;
        }

        #generate-btn {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            padding: 10px 20px;
            font-size: 16px;
            background-color: #3498db;
            color: #fff;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s ease, opacity 0.3s ease;
        }

        #download-btn {
            position: fixed;
            bottom: 20px;
            left: calc(95%);
            transform: translateX(-50%);
            padding: 10px 20px;
            font-size: 16px;
            background-color: #2ecc71;
            color: #fff;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s ease, opacity 0.3s ease;
        }

        #generate-btn:hover, #download-btn:hover {
            background-color: #2980b9;
        }

        #download-link {
            display: none;
        }
    </style>
</head>
<body id="background-container">
    <button id="generate-btn" onclick="generateBackground()">Generate Background</button>
    <button id="download-btn" onclick="downloadBackground()">Download</button>
    <a id="download-link" download="background.jpg"></a>

    <script>
        /**
         * Generate a background based on a generated long seed based on randomly supplied characters within a range
         */
        async function generateBackground() {
            const button = document.getElementById('generate-btn');
            button.disabled = true;
            button.style.backgroundColor = '#ccc';

            document.body.style.opacity = '0';

            const seed = generateRandomSeed(2);
            const imageUrl = `https://source.unsplash.com/1920x1080/?${seed}`;

            await sleep(1000);

            document.body.style.backgroundImage = `url('${imageUrl}')`;

            await sleep(500);

            document.body.style.opacity = '1';

            await sleep(500);

            button.disabled = false;
            button.style.backgroundColor = '#3498db';
        }

        /**
         * Downloads the background when the button is clicked
         */
        function downloadBackground() {
            const imageUrl = document.body.style.backgroundImage.slice(5, -2); 
            const link = document.getElementById('download-link');
            link.href = imageUrl;
            link.click();
        }

        /**
         * Places a timeout on the process
         */
        function sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }

        function generateRandomSeed(length) {
            const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
            let seed = '';
            for (let i = 0; i < length; i++) {
                seed += characters.charAt(Math.floor(Math.random() * characters.length));
            }
            return seed;
        }

        generateBackground();
    </script>
</body>
</html>

"""

###------------------ RUN CODE ------------------###
@WebApplication.route('/')
def index():
    return render_template_string(HTML_CONTENT)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:5000')
    WebApplication.run(debug=True)
    
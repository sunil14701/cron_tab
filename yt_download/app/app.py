import shutil
from flask import Flask, render_template, request, jsonify, url_for, redirect, send_from_directory
import subprocess
import os 

app = Flask(__name__)

template_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_folder)
download_folder = "./yt_videos"

def empty_folder():
    file = os.listdir(download_folder)
    if(file):
        os.remove(os.path.join(download_folder, file[0]))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    empty_folder()
    user_input = request.form.get('userInput')
    print(user_input)
    try:
        process = subprocess.Popen(['python', 'yt_download.py', f"{user_input}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        if process.returncode == 0:
            return render_template('end.html')
        else:
            return render_template('end.html', error=f'Script failed with error: {error.decode("utf-8")}')
    except Exception as e:
        return render_template('end.html', error=str(e))

@app.route('/download')
def download():
    file = os.listdir(download_folder)
    if file:
        return send_from_directory(download_folder, file[0], as_attachment=True)
    else:
        return "No files found in the folder."

if __name__ == '__main__':
    app.run(debug=True, port=5000)

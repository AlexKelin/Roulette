from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# This assumes you have a 'templates' folder with the HTML file
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Use 0.0.0.0 to make it accessible from other devices on the network
    app.run(host='0.0.0.0', port=5001, debug=True)
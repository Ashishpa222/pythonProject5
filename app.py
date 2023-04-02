from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        # process the uploaded file here
    return 'File uploaded successfully!'

@app.route('/team')
def team():
    return 'Our team is called XYZ'

if __name__ == '__main__':
    app.run(debug=True)

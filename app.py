from flask import Flask, render_template, request
from rules import diagnose_symptoms

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    symptoms = set(request.form.getlist('symptoms'))
    diagnosis = diagnose_symptoms(symptoms)
    return render_template('result.html', diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

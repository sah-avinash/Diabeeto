from flask import Flask, render_template, request
import pickle

application = Flask(__name__)


@application.route('/', methods=['GET'])
def homepage():
    return render_template('Index.html')

@application.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            pregnancies = float(request.form['pregnancies'])
            glucose = float(request.form['glucose'])
            bp = float(request.form['bp'])
            skin = float(request.form['skin'])
            insulin = float(request.form['insulin'])
            bmi = float(request.form['bmi'])
            pedigree = float(request.form['pedigree'])
            age = float(request.form['age'])

            data = [[pregnancies, glucose, bp, skin, insulin, bmi, pedigree, age]]

            model = pickle.load(open('diabetes_predict.pkl', 'rb'))
            pred = model.predict(data)
            res = " "
            if pred == 1:
                res = "Yes, The Patient has Diabetes"
            elif pred == 0:
                res = "No, The Patient doesn't have Diabetes"

            return render_template('Result.html', pred=res)
        except Exception as e:
            print("Error Occured:", e)
    return render_template('Index.html')


if __name__ == '__main__':
    application.run(port=8000, debug=True)

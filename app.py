#Importing the libraries
import pickle
from flask import Flask, render_template, request

#Global Variables
app = Flask(__name__)
loadedModel = pickle.load(open('sales model.pkl', 'rb'))

#User-defined functions/ API Routes
@app.route('/', methods=['GET'])
def Home():
    return render_template('sales.html')

@app.route('/prediction', methods=['POST'])
def predict():
    tv = float(request.form['tv'])
    radio = float(request.form['radio'])
    social_media = float(request.form['social_media'])
    

    prediction = loadedModel.predict([[tv, radio, social_media]])[0]

    prediction = str(round(prediction, 2))

    return render_template('sales.html', output=prediction)

#Main function
if __name__ == '__main__':
    app.run(debug=True)
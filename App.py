from flask import Flask, render_template, request
import pickle
#from millify import millify
#import pyttsx3 

app = Flask(__name__)

with open('modello.pkl', 'rb') as file:
    modello_r2_tuple = pickle.load(file)

modello = modello_r2_tuple[0]
r2 = modello_r2_tuple[1]

#engine = pyttsx3.init()


@app.route('/')
def hello_world():
    return render_template("index.html", data=r2)

@app.route('/predizione', methods=['POST'])
def predizione():
    High = int(request.form['High'])
    Low = int(request.form['Low'])
    previsione = modello.predict([[High,Low]])
    for numero in previsione:
       # engine.say("Il prezzo previsto si aggira intorno a " + millify(numero))
        #engine.runAndWait()
    return render_template('predizione.html', data=numero)

if __name__ == '__main__':
    app.run(debug=True)

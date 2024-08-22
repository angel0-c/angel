from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/index')
def home(): 
    return render_template('index.html')


@app.route('/portaforio')
def portaforio(): 
    return render_template('portaforio.html')

@app.route('/contacto')
def contacto(): 
    return render_template('contacto.html')

@app.route('/mensaje')
def mensaje(): 
    return render_template('mensaje.html')
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
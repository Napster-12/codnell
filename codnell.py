from flask import Flask, render_template


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('cod.html')


@app.route('/sec')
def product():
    return render_template('xil.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/live')
def live():
    return render_template('live.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,render_template
app=Flask(__name__)
app.secret_key="secret_key"

@app.route('/')
def firstPage():
    return render_template('loginPage.html')
@app.route('/homePage')
def homePage():
    return render_template('homePage.html')
if __name__=='__main__':
    app.run(debug=True)
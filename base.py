from flask import Flask,render_template,request,redirect,url_for
base=Flask(__name__)

@base.route('/')
def home():
    return "Welcome to home page Hunny"

@base.route('/welcome')
def welcome():
    return "Welcome to Maveric systems Limited"

@base.route('/index')
def index():
    return render_template('index.html')

@base.route('/success/<int:score>')
def success(score):
    return "The score is "+ str(score)

@base.route('/fail/<int:score>')
def fail(score):
    return "The person is failed and score is "+ str(score)
 
@base.route('/calculate', methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        avg_marks=(maths+science+history)/3
        if avg_marks>=50:
            result="success"
        else:
            result="fail"
        
       # return redirect(url_for(result,score=avg_marks))
        return render_template('results.html',results=avg_marks)

        
        


@base.route('/calculatemarks')
def calculatemarks():
    return render_template('calculate.html')
    

if __name__=='__main__':
    base.run(debug=True)
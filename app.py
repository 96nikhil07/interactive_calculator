from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Calculator"

@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    
    else:
        if request.method=='POST':
            input1=int(request.form['input1'])
            input2=int(request.form['input2'])
            operation=request.form['operation']
            
            if operation=="Add":
                result=input1+input2
            elif operation=="Sub":
                result=input1-input2
            elif operation=="Multiply":
                result=input1*input2
            elif operation=="Divide":
                result=input1/input2
                
        return render_template('calculate.html', result=result)
                
            
    
    

if __name__=='__main__':
    app.run(debug=True)
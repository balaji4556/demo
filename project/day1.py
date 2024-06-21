from flask import Flask,render_template,request

app= Flask(_name_)

@app.route("/",methods=['POST','GET'])
def home():
    if request.method == 'POST':
        num1= int(request.form['num1'])
        num2= int(request.form['num2'])
        num3= request.form['num3']
        # num1=int(num1)
        # num2=int(num2)
        
        if num3=="add":
            sum=num1+num2
            return render_template('home.html',output=sum)
        elif num3=="sub":
            sub=num1-num2
            return render_template('home.html',output=sub)
        elif num3=="mult":
            mult=num1*num2
            return render_template('home.html',output=mult)
        elif num3=="div":
            div=num1%num2
            return render_template('home.html',output=div)
        else:
            return render_template('home.html',output="opps can't find the output")
        
        # database 
       
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/blog")
def blog():
    return "welcome to blog page"
@app.route("/login")
def login():
    return "welcome to login page"
@app.route("/signup")
def signup():
    return "welcome to signup page"
    




if _name_ == "_main_":
    app.run(debug=True, host="0.0.0.0")


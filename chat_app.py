from flask import Flask, render_template,request,session,redirect,url_for,flash
from flask_socketio import SocketIO, emit
from database1 import workig,loginpage,chakuser

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!Q123"
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('sendMessage')
def handle_message(data):
    print("Received message from {}: {}".format(data['username'], data['message']))
    # Send the message to all clients except the sender
    emit('receiveMessage', data, broadcast=True, include_self=False)

@app.route("/logout")
def logout():
    
    session.clear()
    return redirect(url_for("login"))




@app.route("/")
def index():
    if 'username' in session:
        return render_template("index2.html")
    return redirect(url_for('login'))

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        user=loginpage(username,password)
        if user:
            session['username']=username
            return redirect(url_for('index'))    
        return "Invalid username or password",401
    return render_template("login.html")

@app.route("/singup",methods=['GET','POST'])
def singup():
    if request.method=='POST':
        username=request.form['username1']
        password=request.form['password1']
        conf_pass=request.form['confi_pass']
        if chakuser(username):

            
            return  '''<html>
                <script>alert("users alredy exists plz enter diffet name")</script>
                </html>'''
        
        if (password==conf_pass):
            workig(username,password)
            return redirect("login")
        else:
            return  '''<html>
                <script>alert("password mathc nhi hua")</script>
                </html>'''
        
    return render_template("signup.html")
   
    
    

if __name__ == "__main__":
    socketio.run(app, debug=True)

# pair programing with Jonnie Abella and Charlie Ventura
from flask import Flask, render_template, session, redirect,request

app = Flask (__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/', methods=['GET'] )                           # use method = GET every time you visit website to use in function 
def hello_world (): 
    if request.method == 'GET':  
                    #^ use method = ['POST'] to post things to submit
                    # session ['name'] = 'adrian' <<< test code
        
        session['count'] = 0
    return redirect('/re')

@app.route ('/re', methods=['GET'])  #this method is the one we use to refresh the page and increase count by 1.
def oneCount ():
    if request.method== 'GET':
        session['count'] += 1
    return render_template('index.html')

@app.route('/plusAddTwo')
def plusAdd ():
    session['count']+= 1
    return redirect ('/re')


@app.route('/destroy_session',methods=['POST'])
def clear():
    session.clear()
    return redirect('/')

    

if __name__ == "__main__":
    app.run(debug= True)
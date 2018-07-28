import bottle
app=bottle.Bottle()
@app.route('/')#decorator function
def home():
 return 'HomePage'

@app.route('/hello')
def hello():
    return 'Hello Page'

@app.route('/user/<name>')
def user(name):
  return 'Hello' + str(name)


@app.route('/login')
def login():
    return '''<form action ='/login1' method='post'>
              user:<input type = 'text' name = 'uname'/> 
              <input type ='submit' value='submit'/>
              </form>'''
@app.post('/login1')
def login1():
    a=bottle.request.forms.get('uname')
    return 'Hello' + str(a)



@app.route('/Querydb')
def Querydb():
    import sqlite3
    con=sqlite3.connect('MyDB')
    cur=con.cursor()
    cur.execute('Select * from log_data')
    result=cur.fetchall()
    s='<table border=1>'
    for i, j, k, l in result:
        s=s+'<tr>'+'<td>'+i+'</td>'+'<td>'+j+'</td>'+'<td>'+k+'</td>'+'<td>'+l+'</td>'+'</tr>'
    s=s+'<table>'
    return s

app.run()#app.run(host='give the ip', port=3434) #give host and IP







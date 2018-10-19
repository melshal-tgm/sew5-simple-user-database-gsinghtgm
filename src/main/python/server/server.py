from flask import Flask, request,redirect,render_template
app = Flask(__name__)

@app.route("/")
def sql_database():
   from user import sql_query
   results=sql_query('''SELECT * FROM users''')
   return results

@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_datainsert():
    from user import sql_edit_insert, sql_query
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        picture = request.form['picture']
        sql_edit_insert(''' INSERT INTO users (username,email,picture) VALUES (?,?,?) ''', (username,email,picture) )
    results = sql_query(''' SELECT * FROM users''')
    return results

@app.route('/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_datadelete():
    from user import sql_delete, sql_query
    if request.method == 'GET':
        email = request.args.get('lname')
        picture = request.args.get('fname')
        sql_delete(''' DELETE FROM users where email = ? and picture = ?''', (email,picture) )
    results = sql_query(''' SELECT * FROM users''')
    return results

@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_editlink():
    from user import sql_query, sql_query2
    if request.method == 'GET':
        eemail = request.args.get('eemail')
        epicture = request.args.get('epicture')
        eresults = sql_query2(''' SELECT * FROM users where email = ? and picture = ?''', (eemail,epicture))
    results = sql_query(''' SELECT * FROM users''')
    return results

@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_dataedit():
    from user import sql_edit_insert, sql_query
    if request.method == 'POST':
        old_email = request.form['old_email']
        old_picture = request.form['old_picture']
        username = request.form['username']
        email = request.form['email']
        picture = request.form['picture']
        sql_edit_insert(''' UPDATE users set username=?,email=?,picture=? WHERE username=? ''', (username,email,picture,username) )
    results = sql_query(''' SELECT * FROM users''')
    return results

if __name__ == '__main__':
    app.run(debug=True)
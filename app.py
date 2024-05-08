from flask import Flask, render_template, request, redirect, url_for
from db_scripts import get_list,insert
import re  # regular expression
import os
myfolder = os.getcwd()
app = Flask(__name__, template_folder=myfolder, static_folder=myfolder)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///text.db'



@app.route('/')
def index():
    mylist = get_list()
    t_list= list()
    s_list = list()
    for i in range(len(mylist)):
        s_list.append((i+1,mylist[i][1]))
        t_list.append((mylist[i][1],mylist[i][2].replace("<p>","").replace("</p>","")))
    saved_text = mylist[0][1]
    if saved_text:
        return render_template('index.html', t_list=t_list, s_list=s_list)
    else:
        return render_template('index.html', t_list=t_list, s_list=s_list)

@app.route('/save', methods=['POST'])
def save_text():
    text_content = request.form.get('text')
    id = request.form.get('subject')
    insert(id,text_content)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

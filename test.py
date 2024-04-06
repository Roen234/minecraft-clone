# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 17:41:07 2022

@author: roenr
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 17:41:07 4022

@author: roenr
"""
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('test.html')
if __name__ == '__main__':
    app.run(debug=True)
#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/foo/<int:a>/<int:b>', methods=['GET'])
def sum_numbers(a, b):
    return str(a + b)

#app.run()

import requests
def get_sum_numbers(a=100, b=1000):
    print("Running get sum numbers")
    resp = requests.get(f'http://127.0.0.1:5000/foo/{a}/{b}')
    print(resp)
    print(resp.content)
    print(resp.text)
    print("Done")



get_sum_numbers()






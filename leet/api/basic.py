#!/usr/bin.env python
# Copyright (C) Pearson Assessments - 2020. All Rights Reserved.
# Proprietary - Use with Pearson Written Permission Only

import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/foo', methods=['GET'])
def sample():
    return "a sample API"

app.run()


from flask import Flask
import pandas as pd
import matplotlib.pyplot as plt
import json
from alpha_vantage.techindicators import TechIndicators

app = Flask(__name__)

@app.route('/')
def alphavantage():
    key = 'DQYCL9VT50BGQGW4'
    ta = TechIndicators(key, output_format='pandas')
    data_1, meta_1 = ta.get_sma('KO', interval='daily', time_period=200, series_type='close')
    return render_template('index.html', data=json.loads(data_1.to_string))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Saving file will reload the server
    alphavantage()

from flask import Flask
import matplotlib.pyplot as plt
import pandas as pd
import sys
from alpha_vantage.techindicators import TechIndicators

api_key = "DQYCL9VT50BGQGW4"

import base64
from io import BytesIO

app = Flask(__name__)


@app.route('/<ti>/<t1>/<t2>')
def images(ti, t1, t2):
    periods = 60
    TechI = TechIndicators(key=api_key, output_format='pandas')
    name = 'get_'+ti.lower()
    method = getattr(TechI, name)
    data_rsi1, meta_data_rsi1 = method(symbol=t1.upper(), interval='1min', time_period=periods, series_type='close')
    data_rsi2, meta_data_rsi2 = method(symbol=t2.upper(), interval='1min', time_period=periods, series_type='close')
    df1 = data_rsi1
    df2 = data_rsi2
    fig, ax1 = plt.subplots()
    ax1.plot(df1, 'b-')
    ax2 = ax1.twinx()
    ax2.plot(df2, 'r-')
    plt.title(t1.upper() + ' ' + ti.upper() + ' (In blue) vs ' + t2.upper() + ' ' + ti.upper() + ' (Red)')
    plt.figure(figsize=(30, 30))
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Saving file will reload the server

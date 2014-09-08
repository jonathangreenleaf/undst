import numpy as np
import pandas as pd

from flask import Flask, make_response
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    msg = '''please enter the api request like:<br>
            {flask server}/api/v1.0/temp/begin_utc/end_utc/format<br>
            begin_utc / end_utc are unix timestamps (int)<br>
            format is either csv or json (string)<br>
            e.g. <a href="http://jonathangreenleaf.com/api/v1.0/temp/1405083600/1405083640/json">
            http://jonathangreenleaf.com/api/v1.0/temp/1405083600/1405083640/json</a><br>
            or <a href="http://jonathangreenleaf.com/api/v1.0/temp/1405083600/1405083640/json">
            http://jonathangreenleaf.com/api/v1.0/temp/1405083600/1405083640/csv</a>'''
    return msg + '<br>You entered: %s' % path

if __name__ == '__main__':
    app.run()

@app.route('/api/v1.0/temp/<int:begin_utc>/<int:end_utc>/<format>', methods = ['GET'])
def get_temps(begin_utc, end_utc, format):

    store = pd.HDFStore('data.h5')
    df = store["df"]
    r = df[(df['timeStamp']>=begin_utc) & (df['timeStamp']<=end_utc)]
    store.close()
    if format == 'csv':
        return r.to_csv(index=False, header=False, columns= ["temp", "timeStamp"])
    else:
        return r.to_json(orient="records")

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.debug = True
    app.run()

import numpy as np
import pandas as pd
#import datetime
#import pytz

from flask import Flask, make_response
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)

@app.route('/flask', defaults={'path': ''})
@app.route('/flask/<path:path>')
def catch_all(path):
    msg = '''
            API example using Flask, numpy, pandas <br>
            pointed at an -> <a href ="http://www.hdfgroup.org/HDF5/">HDF5</a> binary data store <br>
            Nginx is pointed at a vanilla Flask server for this, Gunicorn for the rest of the site<br><br>

            this is driven by this <a href="https://github.com/jonathangreenleaf/undst">code</a> <br><br>

            please enter the api request like:<br>
            {flask server}/api/v1.0/temp/begin_utc/end_utc/format<br>
            begin_utc / end_utc are unix timestamps (int)<br>
            format is either csv or json (string)<br>
            e.g. <a href="http://jonathangreenleaf.com/flask/api/v1.0/temp/1405083600/1405083640/json">
            http://jonathangreenleaf.com/flask/api/v1.0/temp/1405083600/1405083640/json</a><br>
            or <a href="http://jonathangreenleaf.com/flask/api/v1.0/temp/1405083600/1405083640/csv">
            http://jonathangreenleaf.com/flask/api/v1.0/temp/1405083600/1405083640/csv</a>'''
    return msg + '<br>You entered: %s' % path

@app.route('/flask/api/v1.0/temp/<int:begin_utc>/<int:end_utc>/<format>', methods = ['GET'])
def get_temps(begin_utc, end_utc, format):

    #begin_utc = datetime.datetime(begin_utc, pytz.UTC)
    #end_utc = datetime.datetime(end_utc, pytz.UTC)

    store = pd.HDFStore('/home/super_jgreenleaf/undst/data.h5')
    df = store["df"]
    r = df[(df['timeStamp']>=begin_utc) & (df['timeStamp']<=end_utc)]
    store.close()
    if format == 'csv':
        #pass
        return r.to_csv(index=False, header=False, columns= ["temp", "timeStamp"])
    else:
        #pass
        return r.to_json(orient="records")

    #format = "%Y-%m-%d %H:%M:%S.%f"    
    #return datetime.datetime.strptime(begin_utc, format)

    #return datetime.datetime(begin_utc, pytz.UTC)
    return 'blah'

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    #app.debug = True

   # if not app.debug:
    #    import logging
     #   from logging.handlers import RotatingFileHandler
      #  file_handler = RotatingFileHandler('/tmp/hhh.log', 'a', 1 * 1024 * 1024, 10)
       # file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
       # app.logger.setLevel(logging.DEBUG)
       # file_handler.setLevel(logging.DEBUG)
       # app.logger.addHandler(file_handler)
       # app.logger.info('hhh startup')

    app.run(debug=True)

#if __name__ == '__main__':
    #app.debug = True
#    app.run(debug=False)

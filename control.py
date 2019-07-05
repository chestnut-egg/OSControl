import os
import time
from flask import *
import logging
import configparser

app = Flask(__name__)
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

cp = configparser.ConfigParser()
cp.read('myconfig.conf')



@app.route('/os')
def oss():
    ps = os.popen('ps -ef')
    list = []
    for temp in ps.readlines():
        logger.info(temp)
        list.append(temp)
    info={}
    info['pslist'] = list
    return render_template('ps.html', info = info)


@app.route('/log')
def log():
    logger.info('-----------log----------')
    log = cp.get('log_address','tool_log')
    log_context = os.popen('tail -100 '+str(log))

    list = []
    for temp in log_context.readlines():
        logger.info(temp)
        list.append(temp)
    info={}
    info['log_context'] = list

    return render_template('log.html', info = info)

@app.route('/df')
def df():
    df = os.popen('df -h')
    list = []
    for temp in df.readlines():
        logger.info(temp)
        list.append(temp)
    info={}
    info['dflist'] = list
    return render_template('df.html', info = info)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
from flask import Flask, request, redirect, url_for
import requests


app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
def index():
    return 'index ../..'


@app.route('/result/<string:acc_key>/<string:ip>/<string:type>/<string:continent_name>/<string:city>/<string'
           ':zip>')
def result(acc_key, ip, type, continent_name, city, zip):
    return '<h3>IP: {};  <br> Type: {}; <br> Continent Name: {}; <br> City: {}; <br> Zip: {};<br>Your ' \
           'Access Key:{} </h3>'.format(ip, type, continent_name, city, zip, acc_key)


@app.route('/fetch', methods=['GET', 'POST'])
def numverify():
    if request.method == 'GET':
        return '''<h1>Please fill out the parameters</h1>
                    <form method="POST" action="/fetch">
                    <input type="text" name="acc_key">
                    <input type="text" name="ip">
                    <input type="submit" value="Request">
                </form>'''
    else:
        acc_key = request.form['acc_key']
        ip = request.form['ip']

        req = requests.get('http://api.ipstack.com/' + ip + '?access_key=' + acc_key)
        response = req.json()

        type = response["type"]
        continent_name = response["continent_name"]
        city = response["city"]
        zip = response["zip"]

        return redirect(url_for('result', acc_key=acc_key, ip=ip, type=type,
                                continent_name=continent_name, city=city, zip=zip))


if __name__ == '__main__':
    app.run()
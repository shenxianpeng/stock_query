# coding:utf8

import flask
from flask import render_template

from app.main.stock_query import stock_check, result_parse, get_stock
from app.main.stock_query_detail import stock_check_detail, result_parse_detail, get_stock_detail
from app.main.weather import weather_query, get_city

app = flask.Flask(__name__, template_folder='app/templates')

@app.route('/', methods=['GET', 'POST'])
def homepage():
    result = {}
    return render_template("/homepage.html", result=result)


@app.route('/stock.html', methods=['GET', 'POST'])
def stock():
    if flask.request.method == 'GET':
        result = {}
        return render_template("stock.html", result=result)
    elif flask.request.method == 'POST' and flask.request.form.get('query', None) == "查询":
        stock_no = flask.request.form['storkcode']
        code = stock_check(stock_no)
        if code != 0:
            result = result_parse(get_stock(code))
            return render_template("stock.html", result=result)
        else:
            return render_template("stock.html", warning="请输入正确的股票代码")


@app.route('/stock_detail.html', methods=['GET', 'POST'])
def stock_detail():
    if flask.request.method == 'GET':
        result = {}
        return render_template("stock_detail.html", result=result)
    elif flask.request.method == 'POST' and flask.request.form.get('query', None) == "查询":
        stock_no = flask.request.form['storkcode']
        code = stock_check_detail(stock_no)
        if code != 0:
            result = result_parse_detail(get_stock_detail(code))
            return render_template("stock_detail.html", result=result)
        else:
            return render_template("stock_detail.html", warning="请输入正确的股票代码")

@app.route('/weather.html', methods=['GET', 'POST'])
def weather():
    if flask.request.method == 'GET':
        result = {}
        return render_template("weather.html", result=result)
    elif flask.request.method == 'POST' and flask.request.form.get('query', None) == "查询":
        city = flask.request.form['city']
        city = get_city(city)
        if city != 0:
            result = weather_query(get_city(city))
            return render_template("weather.html", result=result)
        else:
            return render_template("weather.html", warning="请输入城市名称")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4501)
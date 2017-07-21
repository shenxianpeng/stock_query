# coding:utf8
import configparser

import flask
from flask import render_template

from stock_query import stock_check, result_parse, get_stock
from stock_query_detail import stock_check_detail, result_parse_detail, get_stock_detail

app = flask.Flask(__name__)


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

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4501)

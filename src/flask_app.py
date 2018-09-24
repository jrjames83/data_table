import re
import csv

from flask import Flask, url_for, jsonify, render_template, request, abort

from data_loader import load_coin_data


app = Flask(__name__)


@app.route('/')
def index():
    try:
        template_data = load_coin_data()
        return render_template('index.html', template_data=template_data)
    except:
        abort(404)

@app.route('/apidocs/')
def api_docs():
    return render_template('apidocs.html')

# /api/coins/?name=Bitcoin&min_price=5000
@app.route('/api/coins/')
def return_json_response():
    try:
        name_filter = request.args.get('name')
        price_filter = request.args.get('min_price')
        print(name_filter, price_filter)
        dict_rows = load_coin_data()

        if name_filter and price_filter:
            filtered_names = [row for row in dict_rows if name_filter.lower() in row.get('Name').lower()]
            filtered_prices = [row for row in filtered_names if row.get('Price') != "" 
                and float(row.get('Price')) > float(price_filter)]
            return jsonify(filtered_prices)

        elif price_filter and not name_filter:
            dict_rows = [row for row in dict_rows if row.get('Price') != ""
                            and float(row.get('Price')) > float(price_filter)]
        
        elif name_filter:
            dict_rows = [row for row in dict_rows
                if name_filter.lower() in row.get('Name').lower()]

        return jsonify(dict_rows)
    except:
        raise
        abort(404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

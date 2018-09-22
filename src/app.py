import re
import csv

from flask import Flask, url_for, jsonify, render_template

from data_loader import load_coin_data

app = Flask(__name__)

# Sort by columns
# Filter by name
# Status checkbox
# Add some charts
# Verify data


@app.route('/')
def hello():
    template_data = load_coin_data()
    print(template_data)
    return render_template('index.html', template_data = template_data)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

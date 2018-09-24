import csv
from itertools import groupby

def load_coin_data(sort_by=None, sort_order=None):
    """To Do - add sorting and ordering logic"""
    with open('static/coins.txt') as f:
        reader = csv.reader(f)
        next(reader)
        dict_rows = []
        for row in reader:
            # This file is a tricky - 
            # couldn't think of a clever way with regex, so here we are. 
            # Would have greatly preferred pd.read_csv()
            _row = row[0].strip()
            name = _row[:18].strip()
            cap = _row[18:33].strip()
            price = _row[38:55].strip()
            supply = _row[56:75].strip()
            status = _row[78:].strip()
            dict_rows.append({
                "Name": name,
                "Market Cap": cap,
                "Price": price,
                "Supply": supply,
                "Status": status
            })
    return dict_rows


def grouped_data_loader(grouping_key):
    """Doing some groupby and sum without pandas here"""
    
    check_keys = ['Name', 'Market Cap', 'Price', 'Supply', 'Status']
    """Summarizes key distributional aspects of the underlying data"""
    dict_rows = load_coin_data()
    dict_rows = sorted(dict_rows, key=lambda row: row.get('Name'))
    contains_all_keys = []
    for row in dict_rows:
        if all([row.get(check_k) for check_k in check_keys]):
            contains_all_keys.append(row)
    grouped = groupby(contains_all_keys ,key=lambda x: x.get('Name'))
    
    summary_dict = {}
    
    for key, g in grouped:
        _key = key
        _vals = list(g)
        _allprices = [float(x.get('Price')) for x in _vals]
        _allsupply = [float(x.get('Supply')) for x in _vals]
        summary_dict[_key] = {"Prices": _allprices, "Supply": _allsupply}
    
    return summary_dict

    

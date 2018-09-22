import csv


# Convert into a class that has load_html_data, load_json_data, filtering options, etc...

def load_coin_data(sorted=False):
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
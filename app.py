import pandas as pd
from flask import Flask, render_template
import json

verbs_df = pd.read_csv('data/verbs_list.csv')
verbs_list = verbs_df.values.tolist()

app = Flask(__name__)


@app.route('/')
def index(data=verbs_list):
    return render_template('index.html', data=json.dumps(data))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
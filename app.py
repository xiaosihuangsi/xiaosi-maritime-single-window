from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

# Define a custom filter to format datetime
def format_datetime(datetime_str):
    if datetime_str is not None:
        return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d %H:%M:%S')
    else:
        return 'None'

# Register the custom filter with Jinja2 environment
app.jinja_env.filters['datetime'] = format_datetime

@app.route('/')
def index():
    # Fetch data
    response = requests.get('https://meri.digitraffic.fi/api/port-call/v1/port-calls')
    port_calls = response.json()['portCalls']
    # Count the number of portCallId.
    num_port_calls = len(port_calls)
    # Pass the enumerate function to the template context.
    context = {
        'port_calls': port_calls,
        'num_port_calls': num_port_calls,
        'enumerate': enumerate  # Pass enumerate function to the template
    }
    # Render the template and pass data.
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

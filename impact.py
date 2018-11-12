import requests
import datetime
from random import randint
import os
import pytz

if not "PD_API_KEY" in os.environ:
    raise Exception('Please set the PD_API_KEY environment variable to a PD API token')

token = os.environ["PD_API_KEY"]

# change the below to the metrics you want to send...
metrics = {
    'PFKNVH3': [
        {
            'range': range(10, 13),
            'length': 10
        },
        {
            'range': range(125, 135),
            'length': 10
        },
        {
            'range': range(0, 10),
            'length': 3
        }
    ],
    'PU6348I': [
        {
            'range': range(1500, 1600),
            'length': 14
        },
        {
            'range': range(100, 300),
            'length': 5
        },
        {
            'range': range(1500, 1600),
            'length': 10
        }
    ]
}

# start from now rounded to the nearest minute
now_exact = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
now = now_exact - \
    datetime.timedelta(seconds=now_exact.second,
                       microseconds=now_exact.microsecond)

headers = {'Content-Type': 'application/json', 'Authorization': f"Token token={token}"}
payload = {'observation': {'value': None, 'observed_at': None}}

for metric_id, time_spans in metrics.items():
    # find out how many minutes' worth of data to send for this metric
    total_minutes = 0
    for time_span in time_spans:
        total_minutes += time_span['length']

    print(f"Sending {total_minutes} data points for metric {metric_id}...")
    # start at total_minutes minutes before now
    start = now - datetime.timedelta(minutes=total_minutes)

    url = f"https://api.pagerduty.com/business_impact_metrics/{metric_id}/observations"
    minute_offset = 0
    for time_span in time_spans:
        for i in range(time_span['length']):
            payload['observation']['value'] = randint(
                time_span['range'][0], time_span['range'][-1])
            payload['observation']['observed_at'] = (
                start + datetime.timedelta(minutes=minute_offset)).isoformat()
            r = requests.post(url, json=payload, headers=headers)
            r.raise_for_status()
            print(f"  Sent observation: {r.json()['observation']['observed_at']}: {r.json()['observation']['value']}")
            minute_offset += 1

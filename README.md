# mimpact
Simple impact metric sender script

## PagerDuty Setup:

Fetch an user API token from pagerduty.com.
```
-> Go to pagerduty app
-> Go to User profile
-> Go to User Settings tab
-> Under API Access, create User API Token
```

### Pre reqs

-> brew (https://docs.brew.sh/Installation)

-> Xcode (Apple App Store) 

### Setup

```
$ brew install python3                                   # install python3 if you don't have it already
$ git clone https://github.com/martindstone/mimpact.git  # get this code
$ cd mimpact
$ python3 -m venv venv                                   # set up a virtual environment to run python3 by default
$ . venv/bin/activate                                    # activate the virtual environment
$ pip install -r requirements.txt                        # install all the dependencies
```

### Things you will want to change in the script file (impact.py):

Change the Impact Metrics ids to whichever ones you have created and optionally make different time spans. The structure looks like this:
```
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
```

Each metric has a series of time spans - for each span, for _length_ minutes long, it will populate values randomly chosen from the _range_. You can have as many spans as you want; the script will add up the total length and the first time stamp will be that number of minutes before now.

### Run the script
```
python impact.py
```

### Sample output

```
Sending 23 data points for metric PFKNVH3...
  Sent observation: 2018-11-12T03:16:00Z: 10.0
  Sent observation: 2018-11-12T03:17:00Z: 12.0
  Sent observation: 2018-11-12T03:18:00Z: 12.0
  Sent observation: 2018-11-12T03:19:00Z: 11.0
  Sent observation: 2018-11-12T03:20:00Z: 12.0
  Sent observation: 2018-11-12T03:21:00Z: 12.0
  Sent observation: 2018-11-12T03:22:00Z: 11.0
  Sent observation: 2018-11-12T03:23:00Z: 10.0
  Sent observation: 2018-11-12T03:24:00Z: 12.0
  Sent observation: 2018-11-12T03:25:00Z: 10.0
  Sent observation: 2018-11-12T03:26:00Z: 125.0
  Sent observation: 2018-11-12T03:27:00Z: 129.0
  Sent observation: 2018-11-12T03:28:00Z: 127.0
  Sent observation: 2018-11-12T03:29:00Z: 125.0
  Sent observation: 2018-11-12T03:30:00Z: 134.0
  Sent observation: 2018-11-12T03:31:00Z: 131.0
  Sent observation: 2018-11-12T03:32:00Z: 129.0
  Sent observation: 2018-11-12T03:33:00Z: 130.0
  Sent observation: 2018-11-12T03:34:00Z: 134.0
  Sent observation: 2018-11-12T03:35:00Z: 130.0
  Sent observation: 2018-11-12T03:36:00Z: 2.0
  Sent observation: 2018-11-12T03:37:00Z: 2.0
  Sent observation: 2018-11-12T03:38:00Z: 6.0
Sending 29 data points for metric PU6348I...
  Sent observation: 2018-11-12T03:10:00Z: 1503.0
  Sent observation: 2018-11-12T03:11:00Z: 1527.0
  Sent observation: 2018-11-12T03:12:00Z: 1513.0
  Sent observation: 2018-11-12T03:13:00Z: 1540.0
  Sent observation: 2018-11-12T03:14:00Z: 1513.0
  Sent observation: 2018-11-12T03:15:00Z: 1566.0
  Sent observation: 2018-11-12T03:16:00Z: 1551.0
  Sent observation: 2018-11-12T03:17:00Z: 1558.0
  Sent observation: 2018-11-12T03:18:00Z: 1574.0
  Sent observation: 2018-11-12T03:19:00Z: 1543.0
  Sent observation: 2018-11-12T03:20:00Z: 1507.0
  Sent observation: 2018-11-12T03:21:00Z: 1547.0
  Sent observation: 2018-11-12T03:22:00Z: 1545.0
  Sent observation: 2018-11-12T03:23:00Z: 1568.0
  Sent observation: 2018-11-12T03:24:00Z: 159.0
  Sent observation: 2018-11-12T03:25:00Z: 254.0
  Sent observation: 2018-11-12T03:26:00Z: 298.0
  Sent observation: 2018-11-12T03:27:00Z: 205.0
  Sent observation: 2018-11-12T03:28:00Z: 224.0
  Sent observation: 2018-11-12T03:29:00Z: 1521.0
  Sent observation: 2018-11-12T03:30:00Z: 1592.0
  Sent observation: 2018-11-12T03:31:00Z: 1546.0
  Sent observation: 2018-11-12T03:32:00Z: 1539.0
  Sent observation: 2018-11-12T03:33:00Z: 1581.0
  Sent observation: 2018-11-12T03:34:00Z: 1557.0
  Sent observation: 2018-11-12T03:35:00Z: 1598.0
  Sent observation: 2018-11-12T03:36:00Z: 1501.0
  Sent observation: 2018-11-12T03:37:00Z: 1553.0
  Sent observation: 2018-11-12T03:38:00Z: 1574.0
```
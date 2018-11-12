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
$ brew install python
$ brew install pip
$ git clone https://github.com/martindstone/mimpact.git
$ cd mimpact
$ python3 -m venv venv
$ . venv/bin/activate
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
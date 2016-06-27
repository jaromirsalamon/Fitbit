# Fitbit data reading over API
This implementation using Python Fitbit API implementation library which source is here: https://github.com/orcasgit/python-fitbit and  documentation can be found here: https://python-fitbit.readthedocs.io/en/latest/

## What is implemented
Since I needed for my purposes detail data about heart rate so only this functionality was implemented. You can choose start and end date between you will get CSV files with date in the name to /output folder with 5-15 seconds period of heart rate for particular date.

## Project structure
- /fitbit - Python Fitbit API implementation library copy, original see here: https://github.com/orcasgit/python-fitbit
- config.ini-sample - Credentials and tokens configuration file, where the [Login Parameters] needs to be popualted manualy and [Authorization Parameters] are handled automatically by credentials.py
- credentials.py - Handling config.ini [Authorization Parameters], contains encapsulations (getters, has and setters) over the config.ini
- fitbit.py - implentation of reading data per day with authorization through API and write them to CSV file for particular date between two given dates:
```python
line 15: date1 = datetime.date(2016, 5, 10)
line 16: # date2 = datetime.date(2016, 6, 12)
line 17: date2 = datetime.date.today() - datetime.timedelta(days = 1)
```
- gather_keys_oauth2.py - Python Fitbit API implementation oAuth2 exaple copy, original see here: https://github.com/orcasgit/python-fitbit with slight adjustment:
```python
line 35: cherrypy.config.update({'server.socket_host': '127.0.0.1','server.socket_port': 8000})
```

## TODO
- get rid of direct copy of /fitbit and make dependency external
- get rid of direct copy of gather_keys_oauth2.py and make dependency external
- maybe implement steps
- investigate what else can be extracted

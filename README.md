# TradingMonkey_API

1. Create a virtual environment. (Only do this the first time)
<br>
`python -m venv venv`

2. Activate the virtual environement
<br>
`source venv/bin/activate`
<br>
`venv\Scripts\activate.bat`

3. Install the dependencies
<br>
`pip install -r requirements.txt`

4. Create a .env file
<br>
Create a file at the root of the project with the name ".env" and save the following to the file:
<br>
```
IEX_TOKEN=<value>
IEX_API_VERSION=iexcloud-sandbox
MSSQL_SERVER=<value>
MSSQL_DB=<value>
MSSQL_UID=<value>
MSSQL_PWD=<value>
```

env.py
```
from os import environ
environ['IEX_TOKEN'] = ''
environ['IEX_API_VERSION'] = 'iexcloud-sandbox'
environ['MSSQL_SERVER'] = ''
environ['MSSQL_DB'] = ''
environ['MSSQL_UID'] = ''
environ['MSSQL_PWD'] = ''
```
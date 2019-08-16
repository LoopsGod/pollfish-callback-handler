# Pollfish S2S Callbacks
Example code for handling and parsing a Pollfish Server 2 Server (S2S) or webhook callback, using Flask. 

Pollfish Docs: https://www.pollfish.com/docs/s2s

## Setting up
In order to get set up, you are going to need to clone this repository. After that, set up a virtualenv and satisfy the requirements by running ``pip install -r requirements.txt``. (please make sure you're in the root directory when you run ``pip install``). Additional explanation can be found on the Flask quickstart and documentation. 

## Code samples
Find some code samples below. 

#### Routing & handling
Include handler function.
 
```python
# Include the handler function(s)
from handlers.pollfish_handler import verify
```

Setup routing. 
```python
@app.route('/webhooks/pollfish-s2s')
def verify_survey():
    return verify()
```

#### Query strings in handler function
Get the arguments from the Pollfish request query strings. You should have defined those in your application / dashboard. 

Flask has an easy function for getting and parsing query strings: request.args.get()
```python
from flask import request

def verify():
    device_id = request.args.get('device_id')
    cpa = request.args.get('cpa')
    request_uuid = request.args.get('request_uuid')
    timestamp = request.args.get('timestamp')
    tx_id = request.args.get('tx_id')
```

For the complete code, check the files : ) 

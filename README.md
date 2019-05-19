# Pollfish S2S Callbacks
Example code for handling and parsing a Pollfish Server 2 Server (S2S) or webhook callback, using flask. 

#### Code samples

Get the arguments from the Pollfish request query strings. You should have defined those in your application / dashboard. 

Flask has an easy method for getting and parsing query strings: flask.request.args.get()
```python
def verify():
    argument1 = flask.request.args.get('YOURARGUMENT1')
    argument2 = flask.request.args.get('YOURARGUMENT2')
```

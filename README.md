# Stock-python-api
This is a simple Flask RESTful API which utilizes the nsepy module to return a json with the stock data in specified time range.
## To run
- Clone repo and make a virtual environment
- Type `pip install`
- Type `python3 api.py`
- Use a REST client and send a POST request to http://localhost:5000/stocks
- The body of the request should be in the form of request.json

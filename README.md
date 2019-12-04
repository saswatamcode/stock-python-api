[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/Naereen/ama)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-for-VSCode](https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg)](https://code.visualstudio.com/)
[![GitHub forks](https://img.shields.io/github/forks/saswatamcode/stock-python-api.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/saswatamcode/stock-python-api/network/)
[![GitHub stars](https://img.shields.io/github/stars/saswatamcode/stock-python-api.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/saswatamcode/stock-python-api/stargazers/)
[![GitHub issues](https://img.shields.io/github/issues/saswatamcode/stock-python-api.svg)](https://GitHub.com/saswatamcode/stock-python-api/issues/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

# Stock-python-api
This is a simple Flask RESTful API which utilizes the nsepy module to return a json with the stock data in specified time range.
## To run
- Clone repo and make a virtual environment
- Type `pip install`
- Type `python3 api.py`
- Use a REST client and send a POST request to http://localhost:5000/stocks
- The body of the request should be in the form of request.json

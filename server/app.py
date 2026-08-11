#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:contract_id>')
def get_contract(contract_id):
    """Return contract information for a valid contract id."""
    contract = next((item for item in contracts if item['id'] == contract_id), None)
    if contract is None:
        return '', 404
    return contract['contract_information'], 200

@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    """Confirm customer existence without returning sensitive details."""
    if customer_name.lower() not in customers:
        return '', 404
    return '', 204

if __name__ == '__main__':
    app.run(port=5555, debug=True)

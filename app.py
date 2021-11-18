from flask import Flask, render_template, request, flash, redirect
from forex_python.converter import CurrencyCodes, CurrencyRates
from helpers import is_valid_amount,  is_valid_currency, get_currencies
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

CURRENCY_CODES = get_currencies()

@app.route("/")
def show_home():
    """Renders the homepage"""

    return render_template("index.html", currencies=CURRENCY_CODES)

@app.route("/convert", methods=["POST"])
def convert():
    """Process data from the form to calculate currency conversion."""
    
    from_curr = request.form["from_currency"][:3]
    to_curr = request.form["to_currency"][:3]
    amount = request.form["amount"]
    valid_from_curr = is_valid_currency(from_curr)
    valid_to_curr = is_valid_currency(to_curr)
    valid_amount = is_valid_amount(amount)
    
    if not valid_from_curr:
        flash(f"Invalid FROM currency: {from_curr}")
    if not valid_to_curr:
        flash(f"Invalid TO currency: {to_curr}")
    if not valid_amount:
        flash(f"Invalid amount: {amount}")
    
    if valid_from_curr and valid_to_curr and valid_amount:
        amount = float(amount)
        rates = CurrencyRates()
        codes = CurrencyCodes()
        converted_amount = rates.convert(from_curr, to_curr, amount)
        from_info = {
          "symbol": codes.get_symbol(from_curr),
          "name": codes.get_currency_name(from_curr),
          "code": from_curr 
        }
        to_info = {
          "symbol": codes.get_symbol(to_curr),
          "name": codes.get_currency_name(to_curr),
          "code": to_curr
        }
        return render_template("result.html", from_info=from_info, 
                amount="{:,.2f}".format(amount), to_info=to_info, 
                converted_amount="{:,.2f}".format(converted_amount) )
    else:
        return redirect("/")
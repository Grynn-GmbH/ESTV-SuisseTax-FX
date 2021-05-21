import frappe
from frappe import DuplicateEntryError, DoesNotExistError, enqueue
from .util import xml_to_currency_exchange
from datetime import datetime


def create_FX_entry(currency, rate):
    try:
        now = datetime.now()
        doc = frappe.new_doc('Currency Exchange')
        doc.for_buying = 1
        doc.for_selling = 1
        doc.date = now.date()
        doc.exchange_rate = rate
        doc.from_currency = 'CHF'
        doc.to_currency = currency
        doc.insert()
    except (DoesNotExistError, DuplicateEntryError):
        pass


def restore(doc=None, event=None):
    currencies = xml_to_currency_exchange()
    enabled_currencies = frappe.get_list('Currency', filters={"enabled": 1})
    rates = {currency['name'].lower(
    ): currencies.get(currency['name'].lower()) for currency in enabled_currencies}
    rates.pop('chf', None)
    for currency, rate in rates.items():
        arg = {'currency': currency.upper(), 'rate': rate}
        enqueue('estv_suissetax_fx.cron.create_FX_entry', **arg)


def run_daily():
    restore()


def run_monthly():
    restore()


restore()

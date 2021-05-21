import frappe
from .util import xml_to_currency_exchange


def restore(doc=None, event=None):
    currencies = xml_to_currency_exchange()
    print(currencies)


def run_daily():
    restore()


def run_monthly():
    restore()


restore()

import frappe
from .util import xml_to_currency_exchange


def restore():
    currencies = xml_to_currency_exchange()
    dict


def run_daily():
    restore()


def run_monthly():
    restore()


restore()

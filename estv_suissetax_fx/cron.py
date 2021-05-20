import frappe
import requests


def restore():
    frappe.log('runn successfully')
    frappe.error_log('this is Error')


def run_daily():
    restore()


def run_monthly():
    restore()

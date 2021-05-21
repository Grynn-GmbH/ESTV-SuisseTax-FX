import requests
import json
import xmltodict


def xml_to_currency_exchange():
    xml_url = 'https://www.backend-rates.ezv.admin.ch/api/xmlavgmonth'
    r = requests.get(xml_url, allow_redirects=True)
    dct = json.loads(json.dumps((xmltodict.parse(r.text))))
    currency_exchange = {exchange['@code']: float(exchange['kurs']) / int(exchange['waehrung'].split(' ')[0])
                         for exchange in dct['monatsmittelkurs']['devise']}
    return currency_exchange

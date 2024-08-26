import argparse
import requests


# App  version
version = '1.0.0'

# Lib for parsing arguments
parser = argparse.ArgumentParser(
    prog='rundict.py',
    description=f'Command to get word first meaning. Using https://www.dictionaryapi.com api. Version {version}')

parser.add_argument('word')
parser.add_argument('-m', '--multiple', action='store_true', help='Print all meanings of the word')
args = parser.parse_args()

# Key and API endpoint
key = "5949a3d3-0ae5-4e40-8232-aaa18792b7e8"  # could be added to a Secret Manager AWS/Vault services at HashiCorp/etc.
url = f"https://www.dictionaryapi.com/api/v3/references/sd4/json/{args.word}?key={key}"

response = requests.get(url)
if response.status_code != 200:
    print(f"Error({response.status_code}): Could NOT get the dictionaryapi API")
    exit(1)  # Code for API issue

for entry in response.json():

    if not args.multiple:
        # exit application in case the word is not in api dic
        if isinstance(entry, str):
            print(f"Word '{args.word}' not found")
            print("Try:", ",".join(response.json()))
            exit(1)
        meta = entry.get('meta')

        hwi = entry.get('hwi')
        fl = entry.get('fl')
        get_def = entry.get('def')
        if hwi and hwi.get('prs'):
            # check if word is a noun or a verb
            print(hwi.get('prs')[0].get('mw'), f"({fl}):", f"{get_def[0].get('sseq')[0][0][1].get('dt')[0][1]}")
            exit(0)

    else:
        # future function to print all word meaning
        print(f"Multiples meaning will be print on version version 1.0.1. Current version {version}")
        exit(0)
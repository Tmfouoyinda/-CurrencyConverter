import requests

class CurrencyConverter:
    def __init__(self):
        self.result = None
        self.data = None

    def api(self):
        try:
            response = requests.get('.....')
            response.raise_for_status()
            self.data = response.json()
        except requests.exceptions.HTTPError:
            print("Pas de connexion internet")
        except requests.exceptions.ConnectionError:
            print("Connection error")

    def convert(self, amount, rate_origin, rate_target):
        rates = self.data["conversion_rates"]
        rate_target = rates[rate_target]
        rate_origin = rates[rate_origin]

        self.result = (amount / rate_origin) * rate_target
        return self.result

if __name__ == "__main__":

    converter = CurrencyConverter()
    converter.api()
    montant = float(input("Montant : "))
    source = input("Devise source (ex: EUR) : ").upper()
    target = input("Devise cible  (ex: XOF) : ").upper()

    result = converter.convert(montant, source, target)
    print(f"{montant} {source} = {result:.2f} {target}")

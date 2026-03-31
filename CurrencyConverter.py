import requests



class  CurrencyConverter():
    def api(self):
        try:
            reponse = requests.get('https://v6.exchangerate-api.com/v6/75fd07dbe1f5c791cd5414a1/latest/USD')
            reponse.raise_for_status()
            self.data = reponse.json()
        except requests.exceptions.HTTPError:
            print("Pas de connexion internet")
        except requests.exceptions.ConnectionError:
            print("Connection error")


    def converter(self, montant, taux_source, taux_target):
        rates = self.data["conversion_rates"]
        taux_target = rates[taux_target]
        taux_source = rates[taux_source]

        self.result = (montant / taux_source) * taux_target
        return self.result
if __name__ == "__main__":

    converter = CurrencyConverter()
    converter.api()
    montant = float(input("Montant : "))
    source = input("Devise source (ex: EUR) : ").upper()
    target = input("Devise cible  (ex: XOF) : ").upper()

    result = converter.converter(montant, source, target)
    print(f"{montant} {source} = {result:.2f} {target}")
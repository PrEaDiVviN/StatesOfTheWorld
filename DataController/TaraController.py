from DataObtain.TaraDataObtainer import TaraDataObtainer
from Services.PersistenceService.PersistenceService import PersistenceService


class TaraController:
    def __init__(self):
        self.persist = PersistenceService()
        self.obtain = TaraDataObtainer()

    def save_tari_to_database(self):
        self.obtain.get_html_text()
        countries = self.obtain.get_tara_data()
        for country in countries:
            tara = self.persist.Tara(nume_scurt=country[0],
                                     nume_oficial=country[1],
                                     link_tara=country[2],
                                     capitala=country[3],
                                     link_capitala=country[4])
            print(country)
            self.persist.add_item(tara)
        self.persist.save()


if __name__ == "__main__":
    controller = TaraController()
    controller.save_tari_to_database()

from DataObtain.TaraDataObtainer import TaraDataObtainer
from Services.PersistenceService.PersistenceService import PersistenceService


class TaraController:
    @staticmethod
    def save_tari_to_database():
        persist = PersistenceService()
        obtain = TaraDataObtainer()
        obtain.get_html_text()
        countries = obtain.get_tara_data()
        for country in countries:
            tara = persist.Tara(nume_scurt=country[0], nume_oficial=country[1], link_tara=country[2], capitala=country[3], link_capitala=country[4])
            persist.add_item(tara)
        persist.save()


if __name__ == "__main__":
    TaraController.save_tari_to_database()

from DataObtain.TaraDataObtainer import TaraDataObtainer
from Services.PersistenceService.PersistenceService import PersistenceService


class TaraController:
    """ A wrapping class acting as a Controller linking PersistenceService And TaraDataObtainer. """
    def __init__(self):
        """ Initializes TaraController with the PersistenceService and TaraDataObtainer. """
        self.persist = PersistenceService()
        self.obtain = TaraDataObtainer()

    def save_tari_to_database(self):
        """ Saves all entities got using TaraDataObtainer to the database using PersistenceService. """
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

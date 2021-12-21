from DataObtain.OtherDetailsDataObtainer import OtherDetailsDataObtainer
from Services.PersistenceService.PersistenceService import PersistenceService


class OtherDetailsController:
    @staticmethod
    def save_tari_steaguri_to_database():
        persist = PersistenceService()
        obtain = OtherDetailsDataObtainer()
        countries = persist.persisence_session.query(persist.Tara).order_by(persist.Tara.id)
        for tara in countries:
            obtain.get_html_text(tara.link_tara)
            steaguri = obtain.get_tara_steaguri_data()
            tara_steaguri = persist.TaraSteaguri(id_tara=tara.id, drapel_link=steaguri[0], stema_link=steaguri[1])
            print(steaguri)
            persist.add_item(tara_steaguri)
        persist.save()

    @staticmethod
    def save_geografie_to_database():
        persist = PersistenceService()
        obtain = OtherDetailsDataObtainer()
        countries = persist.persisence_session.query(persist.Tara).order_by(persist.Tara.id)
        for tara in countries:
            obtain.get_html_text(tara.link_tara)
            geografie = obtain.get_geografie_data()
            print(tara.nume_scurt, geografie)
            geografie_instance = persist.Geografie(id_tara=tara.id,suprafata_totala=geografie[0],
                                                   apa_procent_suprafata_totala=geografie[1],
                                                   cel_mai_inalt_punct_nume=geografie[2],
                                                   link_cel_mai_inalt_punct=geografie[3],
                                                   cel_mai_inalt_punct_inaltime=geografie[4],
                                                   cel_mai_jos_punct_nume=geografie[5],
                                                   link_cel_mai_jos_punct=geografie[6],
                                                   cel_mai_jos_punct_inaltime=geografie[7],
                                                   fus_orar=geografie[8])

            persist.add_item(geografie_instance)
        persist.save()


if __name__ == "__main__":
    OtherDetailsController.save_geografie_to_database()

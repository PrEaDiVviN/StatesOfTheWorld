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

    @staticmethod
    def save_geografie_vecini_to_database():
        persist = PersistenceService()
        obtain = OtherDetailsDataObtainer()
        countries = persist.persisence_session.query(persist.Tara).order_by(persist.Tara.id)
        for tara in countries:
            obtain.get_html_text(tara.link_tara)
            vecini = obtain.get_geografie_vecini_data()
            print(tara.nume_scurt, vecini)
            for vecin in vecini:
                vecin_instance = persist.GeografieVecini(id_tara=tara.id, nume_vecin=vecin)
                persist.add_item(vecin_instance)
        persist.save()

    @staticmethod
    def save_populatie_to_database():
        persist = PersistenceService()
        obtain = OtherDetailsDataObtainer()
        countries = persist.persisence_session.query(persist.Tara).order_by(persist.Tara.id)
        for tara in countries:
            obtain.get_html_text(tara.link_tara)
            populatie_data = obtain.get_populatie_data()
            populatie_instance = persist.Populatie(id_tara=tara.id, recensamant_populatie=populatie_data[0], densitate_populatie=populatie_data[1])
            print(tara.id, populatie_data)
            persist.add_item(populatie_instance)
        persist.save()

    @staticmethod
    def save_limba_to_database():
        persist = PersistenceService()
        obtain = OtherDetailsDataObtainer()
        countries = persist.persisence_session.query(persist.Tara).order_by(persist.Tara.id)
        for tara in countries:
            obtain.get_html_text(tara.link_tara)
            limba_data = obtain.get_limba_data()
            limba_instance = persist.Limba(id_tara=tara.id,limba_oficiala=limba_data[0], link_limba_oficiala=limba_data[1], etnonime = limba_data[2], limbi_regionale_minoritate=limba_data[3])
            print(tara.nume_scurt, tara.id, limba_data)
            persist.add_item(limba_instance)
        persist.save()

    @staticmethod
    def save_guvernare_to_database():
        persist = PersistenceService()
        obtain = OtherDetailsDataObtainer()
        countries = persist.persisence_session.query(persist.Tara).order_by(persist.Tara.id)
        for tara in countries:
            obtain.get_html_text(tara.link_tara)
            guvernare_data = obtain.get_guvernare_data()
            guvernare_instance = persist.Guvernare(id_tara=tara.id, sistem_politic=guvernare_data[0],
                                               presedinte=guvernare_data[1], link_presedinte=guvernare_data[2],
                                               prim_ministru=guvernare_data[3], link_prim_ministru=guvernare_data[4])
            print(tara.nume_scurt, tara.id, guvernare_data)
            persist.add_item(guvernare_instance)
        persist.save()

    @staticmethod
    def save_identificatori_to_database():
        persist = PersistenceService()
        obtain = OtherDetailsDataObtainer()
        countries = persist.persisence_session.query(persist.Tara).order_by(persist.Tara.id)
        for tara in countries:
            obtain.get_html_text(tara.link_tara)
            identificatori_data = obtain.get_identificatori_data()
            identificatori_instance = persist.Identificator(id_tara=tara.id, cod_cio=identificatori_data[0],
                                               cod_mobil=identificatori_data[1], prefix_mobil=identificatori_data[2],
                                               domeniu_internet=identificatori_data[3])
            print(tara.nume_scurt, tara.id, identificatori_data)
            persist.add_item(identificatori_instance)
        persist.save()

    @staticmethod
    def save_economie_to_database():
        persist = PersistenceService()
        obtain = OtherDetailsDataObtainer()
        countries = persist.persisence_session.query(persist.Tara).order_by(persist.Tara.id)
        for tara in countries:
            obtain.get_html_text(tara.link_tara)
            economie_data = obtain.get_economie_data()
            economie_instance = persist.Economie(id_tara = tara.id, pib_ppc_total=economie_data[0], pib_ppc_cap_locuitor=economie_data[1],
                                                 pib_nominal_total=economie_data[2], pib_nominal_cap_locuitor=economie_data[3],
                                                 gini=economie_data[4], idu=economie_data[5], moneda=economie_data[6])

            print(tara.nume_scurt, tara.id, economie_data)
            persist.add_item(economie_instance)
        persist.save()


if __name__ == "__main__":
    OtherDetailsController.save_economie_to_database()

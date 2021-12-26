from DataObtain.OtherDetailsDataObtainer import OtherDetailsDataObtainer
from Services.PersistenceService.PersistenceService import PersistenceService


class OtherDetailsController:

    def __init__(self):
        self.persist = PersistenceService()
        self.obtain = OtherDetailsDataObtainer()
        self.countries = self.persist.persisence_session.query(self.persist.Tara).order_by(self.persist.Tara.id)

    def save_tari_steaguri_to_database(self):

        for tara in self.countries:
            self.obtain.get_html_text(tara.link_tara)
            steaguri = self.obtain.get_tara_steaguri_data()
            tara_steaguri = self.persist.TaraSteaguri(id_tara=tara.id,
                                                      drapel_link=steaguri[0],
                                                      stema_link=steaguri[1])
            self.persist.add_item(tara_steaguri)
        self.persist.save()

    def save_geografie_to_database(self):
        for tara in self.countries:
            self.obtain.get_html_text(tara.link_tara)
            geografie = self.obtain.get_geografie_data()
            geografie_instance = self.persist.Geografie(id_tara=tara.id, suprafata_totala=geografie[0],
                                                        apa_procent_suprafata_totala=geografie[1],
                                                        cel_mai_inalt_punct_nume=geografie[2],
                                                        link_cel_mai_inalt_punct=geografie[3],
                                                        cel_mai_inalt_punct_inaltime=geografie[4],
                                                        cel_mai_jos_punct_nume=geografie[5],
                                                        link_cel_mai_jos_punct=geografie[6],
                                                        cel_mai_jos_punct_inaltime=geografie[7],
                                                        fus_orar=geografie[8])
            self.persist.add_item(geografie_instance)
        self.persist.save()

    def save_geografie_vecini_to_database(self):
        for tara in self.countries:
            self.obtain.get_html_text(tara.link_tara)
            vecini = self.obtain.get_geografie_vecini_data()
            for vecin in vecini:
                vecin_instance = self.persist.GeografieVecini(id_tara=tara.id,
                                                              nume_vecin=vecin)
                self.persist.add_item(vecin_instance)
        self.persist.save()

    def save_populatie_to_database(self):
        for tara in self.countries:
            self.obtain.get_html_text(tara.link_tara)
            populatie_data = self.obtain.get_populatie_data()
            populatie_instance = self.persist.Populatie(id_tara=tara.id,
                                                        recensamant_populatie=populatie_data[0],
                                                        densitate_populatie=populatie_data[1])
            print(tara.nume_scurt , populatie_data)
            self.persist.add_item(populatie_instance)
        self.persist.save()

    def save_limba_to_database(self):
        for tara in self.countries:
            self.obtain.get_html_text(tara.link_tara)
            limba_data = self.obtain.get_limba_data()
            limba_instance = self.persist.Limba(id_tara=tara.id,
                                                limba_oficiala=limba_data[0],
                                                link_limba_oficiala=limba_data[1],
                                                etnonime=limba_data[2],
                                                limbi_regionale_minoritate=limba_data[3])
            self.persist.add_item(limba_instance)
        self.persist.save()

    def save_guvernare_to_database(self):

        for tara in self.countries:
            self.obtain.get_html_text(tara.link_tara)
            guvernare_data = self.obtain.get_guvernare_data()
            guvernare_instance = self.persist.Guvernare(id_tara=tara.id,
                                                        sistem_politic=guvernare_data[0],
                                                        presedinte=guvernare_data[1],
                                                        link_presedinte=guvernare_data[2],
                                                        prim_ministru=guvernare_data[3],
                                                        link_prim_ministru=guvernare_data[4])
            self.persist.add_item(guvernare_instance)
        self.persist.save()

    def save_identificatori_to_database(self):

        for tara in self.countries:
            self.obtain.get_html_text(tara.link_tara)
            identificatori_data = self.obtain.get_identificatori_data()
            identificatori_instance = self.persist.Identificator(id_tara=tara.id,
                                                                 cod_cio=identificatori_data[0],
                                                                 cod_mobil=identificatori_data[1],
                                                                 prefix_mobil=identificatori_data[2],
                                                                 domeniu_internet=identificatori_data[3])
            self.persist.add_item(identificatori_instance)
        self.persist.save()

    def save_economie_to_database(self):

        for tara in self.countries:
            self.obtain.get_html_text(tara.link_tara)
            economie_data = self.obtain.get_economie_data()
            economie_instance = self.persist.Economie(id_tara=tara.id, pib_ppc_total=economie_data[0],
                                                      pib_ppc_cap_locuitor=economie_data[1],
                                                      pib_nominal_total=economie_data[2],
                                                      pib_nominal_cap_locuitor=economie_data[3],
                                                      gini=economie_data[4],
                                                      idu=economie_data[5],
                                                      moneda=economie_data[6])
            self.persist.add_item(economie_instance)
        self.persist.save()


if __name__ == "__main__":
    controller = OtherDetailsController()
    controller.save_populatie_to_database()

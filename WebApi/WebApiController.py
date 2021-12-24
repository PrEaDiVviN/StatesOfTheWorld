import copy

from flask import Flask
import json
import sys


sys.path.insert(0, '../')
from Services.PersistenceService.PersistenceService import PersistenceService


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/top-10-tari-populatie")
def show_first_10_population():

    persist = PersistenceService()
    list_tari = list()
    for populatie\
            in persist.persisence_session.query(persist.Populatie)\
            .order_by(persist.func.length(persist.Populatie.recensamant_populatie).desc(), persist.Populatie.recensamant_populatie.desc()).limit(10).all():
        tara = persist.persisence_session.query(persist.Tara).filter(persist.Tara.id == populatie.id_tara).first()
        tara_steaguri = persist.persisence_session.query(persist.TaraSteaguri).filter(persist.TaraSteaguri.id_tara == populatie.id_tara).first()
        geografie = persist.persisence_session.query(persist.Geografie).filter(persist.Geografie.id_tara == populatie.id_tara).first()
        geografie_vecini = persist.persisence_session.query(persist.GeografieVecini).filter(persist.GeografieVecini.id_tara == populatie.id_tara).all()
        list_vecini = list()
        for vecin in geografie_vecini:
            list_vecini.append(copy.deepcopy(vecin.nume_vecin))
        guvernare = persist.persisence_session.query(persist.Guvernare).filter(persist.Guvernare.id_tara == populatie.id_tara).first()
        limba = persist.persisence_session.query(persist.Limba).filter(persist.Limba.id_tara == populatie.id_tara).first()
        economie = persist.persisence_session.query(persist.Economie).filter(persist.Economie.id_tara == populatie.id_tara).first()
        identificatori = persist.persisence_session.query(persist.Identificator).filter(persist.Identificator.id_tara == populatie.id_tara).first()

        tara_json = {
            "id": tara.id,
            "nume_scurt": tara.nume_scurt,
            "tara": {
                "nume_oficial": tara.nume_oficial,
                "capitala": tara.capitala,
                "link_tara": tara.link_tara,
                "link_capitala": tara.link_capitala,
            },
            "tara_steaguri": {
                "drapel_link": tara_steaguri.drapel_link,
                "stema_link": tara_steaguri.stema_link,
            },
            "populatie": {
                "recensamant_populatie": populatie.recensamant_populatie,
                "densitate_populatie": populatie.densitate_populatie,
            },
            "limba": {
                "limba_oficiala": limba.limba_oficiala,
                "link_limba_oficiala": limba.link_limba_oficiala,
                "etnonime": limba.etnonime,
                "limbi_regioname_minoritate": limba.limbi_regionale_minoritate
            },
            "geografie": {
                "suprafata_totala": geografie.suprafata_totala,
                "apa_procent_suprafata": geografie.apa_procent_suprafata_totala,
                "fus_orar": geografie.fus_orar,
                "cel_mai_inalt_punct_nume": geografie.cel_mai_inalt_punct_nume,
                "link_cel_mai_inalt_punct": geografie.link_cel_mai_inalt_punct,
                "cel_mai_inalt_punct_inaltime": geografie.cel_mai_inalt_punct_inaltime,
                "cel_mai_jos_punct_nume": geografie.cel_mai_jos_punct_nume,
                "link_cel_mai_jos_punct": geografie.link_cel_mai_jos_punct,
                "cel_mai_jos_punct_inaltime": geografie.cel_mai_jos_punct_inaltime,
            },
            "geografie_vecini": {
                "lista_vecini": list_vecini,
            },
            "guvernare": {
                "sistem_politic": guvernare.sistem_politic,
                "presedinte": guvernare.presedinte,
                "prim_ministru": guvernare.prim_ministru,
                "link_presedinte": guvernare.link_presedinte,
                "link_prim_ministru": guvernare.link_prim_ministru,
            },
            "identificatori": {
                "cod_cio": identificatori.cod_cio,
                "cod_mobil": identificatori.cod_mobil,
                "prefix_mobil": identificatori.prefix_mobil,
                "domeniu_internet": identificatori.domeniu_internet,
            },
            "economie": {
                "pib_ppc_total": economie.pib_ppc_total,
                "pib_ppc_cap_locuitor": economie.pib_ppc_cap_locuitor,
                "pib_nominal_total": economie.pib_nominal_total,
                "pib_nominal_cap_locuitor": economie.pib_nominal_cap_locuitor,
                "gini": economie.gini,
                "idu": economie.idu,
                "moneda": economie.moneda
            }
        }
        list_tari.append(copy.deepcopy(tara_json))
    return {
        "content": "tot",
        "numar_tari": "10",
        "rezultat": list_tari,
    }

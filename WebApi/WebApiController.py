import copy

from flask import Flask, request
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
        "content": "all-data",
        "numar_tari": len(list_tari),
        "rezultat": list_tari,
    }


@app.route("/top-10-tari-densitate")
def show_first_10_density():

    persist = PersistenceService()
    list_tari = list()
    for populatie\
            in persist.persisence_session.query(persist.Populatie)\
            .order_by(persist.func.length(persist.Populatie.densitate_populatie).desc(), persist.Populatie.densitate_populatie.desc()).limit(10).all():
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
        "content": "all-data",
        "numar_tari": len(list_tari),
        "rezultat": list_tari,
    }

@app.route("/toate-tarile-fus-orar")
def all_countries_fus_orar():
    # %2B = + in https://en.wikipedia.org/wiki/Percent-encoding
    gtm = request.args.get('value', default="UTC+2", type=str)
    print(gtm)
    persist = PersistenceService()
    list_tari = list()
    for geografie\
            in persist.persisence_session.query(persist.Geografie)\
            .filter(persist.Geografie.fus_orar == gtm):
        tara = persist.persisence_session.query(persist.Tara).filter(persist.Tara.id == geografie.id_tara).first()
        tara_steaguri = persist.persisence_session.query(persist.TaraSteaguri).filter(persist.TaraSteaguri.id_tara == geografie.id_tara).first()
        populatie = persist.persisence_session.query(persist.Populatie).filter(persist.Populatie.id_tara == geografie.id_tara).first()
        geografie_vecini = persist.persisence_session.query(persist.GeografieVecini).filter(persist.GeografieVecini.id_tara == geografie.id_tara).all()
        list_vecini = list()
        for vecin in geografie_vecini:
            list_vecini.append(copy.deepcopy(vecin.nume_vecin))
        guvernare = persist.persisence_session.query(persist.Guvernare).filter(persist.Guvernare.id_tara == geografie.id_tara).first()
        limba = persist.persisence_session.query(persist.Limba).filter(persist.Limba.id_tara == geografie.id_tara).first()
        economie = persist.persisence_session.query(persist.Economie).filter(persist.Economie.id_tara == geografie.id_tara).first()
        identificatori = persist.persisence_session.query(persist.Identificator).filter(persist.Identificator.id_tara == geografie.id_tara).first()

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
        "content": "all-data",
        "numar_tari": len(list_tari),
        "rezultat": list_tari,
    }

@app.route("/toate-tarile-limba-oficiala")
def all_countries_language():
    li = request.args.get('contains', default="engleză", type=str)
    persist = PersistenceService()
    list_tari = list()
    for limba\
            in persist.persisence_session.query(persist.Limba)\
            .filter(persist.Limba.limba_oficiala.contains(li)):
        tara = persist.persisence_session.query(persist.Tara).filter(persist.Tara.id == limba.id_tara).first()
        tara_steaguri = persist.persisence_session.query(persist.TaraSteaguri).filter(persist.TaraSteaguri.id_tara == limba.id_tara).first()
        populatie = persist.persisence_session.query(persist.Populatie).filter(persist.Populatie.id_tara == limba.id_tara).first()
        geografie_vecini = persist.persisence_session.query(persist.GeografieVecini).filter(persist.GeografieVecini.id_tara == limba.id_tara).all()
        list_vecini = list()
        for vecin in geografie_vecini:
            list_vecini.append(copy.deepcopy(vecin.nume_vecin))
        guvernare = persist.persisence_session.query(persist.Guvernare).filter(persist.Guvernare.id_tara == limba.id_tara).first()
        geografie = persist.persisence_session.query(persist.Geografie).filter(persist.Geografie.id_tara == limba.id_tara).first()
        economie = persist.persisence_session.query(persist.Economie).filter(persist.Economie.id_tara == limba.id_tara).first()
        identificatori = persist.persisence_session.query(persist.Identificator).filter(persist.Identificator.id_tara == limba.id_tara).first()

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
        "content": "all-data",
        "numar_tari": len(list_tari),
        "rezultat": list_tari,
    }

@app.route("/toate-tarile-regim-politic")
def all_countries_regim():
    sistem_politic = request.args.get('contains', default="republică prezidențială", type=str)
    persist = PersistenceService()
    list_tari = list()
    for guvernare\
            in persist.persisence_session.query(persist.Guvernare)\
            .filter(persist.Guvernare.sistem_politic.contains(sistem_politic)):
        tara = persist.persisence_session.query(persist.Tara).filter(persist.Tara.id == guvernare.id_tara).first()
        tara_steaguri = persist.persisence_session.query(persist.TaraSteaguri).filter(persist.TaraSteaguri.id_tara == guvernare.id_tara).first()
        populatie = persist.persisence_session.query(persist.Populatie).filter(persist.Populatie.id_tara == guvernare.id_tara).first()
        geografie_vecini = persist.persisence_session.query(persist.GeografieVecini).filter(persist.GeografieVecini.id_tara == guvernare.id_tara).all()
        list_vecini = list()
        for vecin in geografie_vecini:
            list_vecini.append(copy.deepcopy(vecin.nume_vecin))
        limba = persist.persisence_session.query(persist.Limba).filter(persist.Limba.id_tara == guvernare.id_tara).first()
        geografie = persist.persisence_session.query(persist.Geografie).filter(persist.Geografie.id_tara == guvernare.id_tara).first()
        economie = persist.persisence_session.query(persist.Economie).filter(persist.Economie.id_tara == guvernare.id_tara).first()
        identificatori = persist.persisence_session.query(persist.Identificator).filter(persist.Identificator.id_tara == guvernare.id_tara).first()

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
        "content": "all-data",
        "numar_tari": len(list_tari),
        "rezultat": list_tari,
    }
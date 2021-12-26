import copy
import sys
from flask import Flask, request
sys.path.insert(0, '../')
from Services.PersistenceService.PersistenceService import PersistenceService

persist = PersistenceService()
app = Flask(__name__)


def construct_response_country_json(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare, limba, economie, identificatori):
    return {
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


def construct_response_json(content, number, list_countries):
    return {
        "content": content,
        "numar_tari": number,
        "rezultat": list_countries,
    }


def get_all_country_data_by_id(id_country):
    tara = persist.persisence_session.query(persist.Tara).filter(persist.Tara.id == id_country).first()
    tara_steaguri = persist.persisence_session.query(persist.TaraSteaguri).filter(
        persist.TaraSteaguri.id_tara == id_country).first()
    geografie = persist.persisence_session.query(persist.Geografie).filter(
        persist.Geografie.id_tara == id_country).first()
    geografie_vecini = persist.persisence_session.query(persist.GeografieVecini).filter(
        persist.GeografieVecini.id_tara == id_country).all()
    list_vecini = list()
    for vecin in geografie_vecini:
        list_vecini.append(copy.deepcopy(vecin.nume_vecin))
    guvernare = persist.persisence_session.query(persist.Guvernare).filter(
        persist.Guvernare.id_tara == id_country).first()
    limba = persist.persisence_session.query(persist.Limba).filter(persist.Limba.id_tara == id_country).first()
    economie = persist.persisence_session.query(persist.Economie).filter(
        persist.Economie.id_tara == id_country).first()
    identificatori = persist.persisence_session.query(persist.Identificator).filter(
        persist.Identificator.id_tara == id_country).first()
    populatie = persist.persisence_session.query(persist.Populatie).filter(
        persist.Populatie.id_tara == id_country).first()
    return tara, tara_steaguri, geografie, list_vecini, guvernare, limba, economie, identificatori, populatie


@app.route("/top-10-tari-populatie")
def show_first_10_population():

    list_tari = list()
    for populatie\
            in persist.persisence_session.query(persist.Populatie)\
            .order_by(persist.func.length(persist.Populatie.recensamant_populatie).desc(), persist.Populatie.recensamant_populatie.desc()).limit(10).all():
        tara, tara_steaguri, geografie, list_vecini, guvernare, limba, economie, identificatori, _ = \
            get_all_country_data_by_id(populatie.id_tara)

        tara_json = construct_response_country_json(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare, limba, economie, identificatori)
        list_tari.append(copy.deepcopy(tara_json))
    return construct_response_json("all-data", len(list_tari), list_tari)


@app.route("/top-10-tari-densitate")
def show_first_10_density():

    list_tari = list()
    for populatie\
            in persist.persisence_session.query(persist.Populatie)\
            .order_by(persist.func.length(persist.Populatie.densitate_populatie).desc(), persist.Populatie.densitate_populatie.desc()).limit(10).all():
        tara, tara_steaguri, geografie, list_vecini, guvernare, limba, economie, identificatori, _ = \
            get_all_country_data_by_id(populatie.id_tara)

        tara_json = construct_response_country_json(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare, limba, economie, identificatori)
        list_tari.append(copy.deepcopy(tara_json))
    return construct_response_json("all-data", len(list_tari), list_tari)


@app.route("/toate-tarile-fus-orar")
def all_countries_fus_orar():
    # %2B = + in https://en.wikipedia.org/wiki/Percent-encoding
    gtm = request.args.get('value', default="UTC+2", type=str)
    list_tari = list()
    for geografie\
            in persist.persisence_session.query(persist.Geografie)\
            .filter(persist.Geografie.fus_orar == gtm):
        tara, tara_steaguri, _, list_vecini, guvernare, limba, economie, identificatori, populatie = \
            get_all_country_data_by_id(geografie.id_tara)

        tara_json = construct_response_country_json(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare,
                                                    limba, economie, identificatori)
        list_tari.append(copy.deepcopy(tara_json))
    return construct_response_json("all-data", len(list_tari), list_tari)


@app.route("/toate-tarile-limba-oficiala")
def all_countries_language():
    li = request.args.get('contains', default="engleză", type=str)
    list_tari = list()
    for limba\
            in persist.persisence_session.query(persist.Limba)\
            .filter(persist.Limba.limba_oficiala.contains(li)):
        tara, tara_steaguri, geografie, list_vecini, guvernare, _, economie, identificatori, populatie = \
            get_all_country_data_by_id(limba.id_tara)

        tara_json = construct_response_country_json(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare,
                                                    limba, economie, identificatori)
        list_tari.append(copy.deepcopy(tara_json))
    return construct_response_json("all-data", len(list_tari), list_tari)


@app.route("/toate-tarile-regim-politic")
def all_countries_regim():
    sistem_politic = request.args.get('contains', default="republică prezidențială", type=str)
    list_tari = list()
    for guvernare\
            in persist.persisence_session.query(persist.Guvernare)\
            .filter(persist.Guvernare.sistem_politic.contains(sistem_politic)):
        tara, tara_steaguri, geografie, list_vecini, _, limba, economie, identificatori, populatie = \
            get_all_country_data_by_id(guvernare.id_tara)

        tara_json = construct_response_country_json(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare,
                                                    limba, economie, identificatori)
        list_tari.append(copy.deepcopy(tara_json))
    return construct_response_json("all-data", len(list_tari), list_tari)

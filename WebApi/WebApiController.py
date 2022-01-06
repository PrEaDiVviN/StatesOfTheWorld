import copy
import sys
from flask import Flask, request
sys.path.insert(0, '../')
from Services.PersistenceService.PersistenceService import PersistenceService

persist = PersistenceService()
app = Flask(__name__)


def construct_response_country_dict(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare, limba, economie, identificatori):
    """ A function that constructs a dict representation of the database entities given as parameters. Each entity is
    prefixed with its name.

    :param tara: Tara entity
    :param tara_steaguri: TaraSteaguri entity
    :param populatie: Populatie entity
    :param geografie: Geografie entity
    :param list_vecini: A list of GeografieVecini entities
    :param guvernare: Guvernare entity
    :param limba: Limba entity
    :param economie: Economie entity
    :param identificatori: Identificatori entity
    :return: Dict representation of given database entities
    """

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


def construct_response_dict(content, number, list_countries):
    """ Construct a Dict response which will be sent when a request is done containing: number of elements,
    content="alldata" and a list of countries. The list of countries in code is created using
    construct_response_country_dict function().

    :param content: String which means how much content was sent
    :param number: Number of elements in the list
    :param list_countries: List of Dict countries
    :return: Dict response sent to requesting user.
    """
    return {
        "content": content,
        "numar_tari": number,
        "rezultat": list_countries,
    }


def get_all_country_data_by_id(id_country):
    """ A function used to obtain all data from database about a country and return it as tuple following the order:
    tara, tara_steaguri, geografie, list_vecini, guvernare, limba, economie, identificatori, populatie

    :param id_country: Country id to by Interrogated
    :return: Country data as tuple
    """
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


@app.route("/")
def show_all_available_routes():
    """ A route that presents all the acceptable routes.
    :return: All acceptable routes with a HTML representation.
    """
    main_html = open('./Static/main.html', mode='r')
    html_text = main_html.read()
    return html_text


@app.route("/top-10-tari-populatie")
def show_first_10_population():
    """ A route that creates a first 10 top based on country population and returns to the requesting user as a Dict.

    :return: Top 10 countries by population formatted as a Dict.
    """

    list_tari = list()
    for populatie\
            in persist.persisence_session.query(persist.Populatie)\
            .order_by(persist.func.length(persist.Populatie.recensamant_populatie).desc(), persist.Populatie.recensamant_populatie.desc()).limit(10).all():
        tara, tara_steaguri, geografie, list_vecini, guvernare, limba, economie, identificatori, _ = \
            get_all_country_data_by_id(populatie.id_tara)

        tara_json = construct_response_country_dict(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare, limba, economie, identificatori)
        list_tari.append(copy.deepcopy(tara_json))
    return construct_response_dict("all-data", len(list_tari), list_tari)


@app.route("/top-10-tari-densitate")
def show_first_10_density():
    """ A route that creates a first 10 top based on country density and returns to the requesting user as a Dict.

    :return: Top 10 countries by density formatted as a Dict.
    """

    list_tari = list()
    for populatie\
            in persist.persisence_session.query(persist.Populatie)\
            .order_by(persist.func.length(persist.Populatie.densitate_populatie).desc(),
                      persist.Populatie.densitate_populatie.desc()).limit(10).all():
        tara, tara_steaguri, geografie, list_vecini, guvernare, limba, economie, identificatori, _ = \
            get_all_country_data_by_id(populatie.id_tara)

        tara_json = construct_response_country_dict(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare, limba, economie, identificatori)
        list_tari.append(copy.deepcopy(tara_json))
    return construct_response_dict("all-data", len(list_tari), list_tari)


@app.route("/toate-tarile-fus-orar")
def all_countries_fus_orar():
    """ A route that return all countries on a specified time zone as a Dict. By default the time-zone is "UTC+2". A different
    timezone can be specified using request param 'value'. An example: "/toate-tarile-fus-orar?value=UTC%2B3". Be
    careful to change '+' character into '%2B' which is his urlencode.

    :return: All countries on a specified time zone as a Dict.
    """
    # %2B = + in https://en.wikipedia.org/wiki/Percent-encoding
    gtm = request.args.get('value', default="UTC+2", type=str)
    list_tari = list()
    for geografie\
            in persist.persisence_session.query(persist.Geografie)\
            .filter(persist.Geografie.fus_orar == gtm):
        tara, tara_steaguri, _, list_vecini, guvernare, limba, economie, identificatori, populatie = \
            get_all_country_data_by_id(geografie.id_tara)

        tara_json = construct_response_country_dict(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare,
                                                    limba, economie, identificatori)
        list_tari.append(copy.deepcopy(tara_json))
    return construct_response_dict("all-data", len(list_tari), list_tari)


@app.route("/toate-tarile-limba-oficiala")
def all_countries_language():
    """ A route that return all countries on a specified language as a Dict. By default the language is "engleză".
    A different language can be specified using request param 'contains'. An example:
    "/toate-tarile-limba-oficiala?contains=franceză".

    :return: All countries on a specified language as a Dict.
    """
    li = request.args.get('contains', default="engleză", type=str)
    list_tari = list()
    for limba\
            in persist.persisence_session.query(persist.Limba)\
            .filter(persist.Limba.limba_oficiala.contains(li)):
        tara, tara_steaguri, geografie, list_vecini, guvernare, _, economie, identificatori, populatie = \
            get_all_country_data_by_id(limba.id_tara)
        tara_json = construct_response_country_dict(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare,
                                                    limba, economie, identificatori)
        list_tari.append(copy.deepcopy(tara_json))
    return construct_response_dict("all-data", len(list_tari), list_tari)


@app.route("/toate-tarile-regim-politic")
def all_countries_regim():
    """ A route that return all countries on a specified political regime as a Dict. By default the regime is
    "republică prezidențială". A different regime can be specified using request param 'contains'. An example:
    "/toate-tarile-regim-politic?contains=democrație".

    :return: All countries on a specified language as a Dict.
    """
    sistem_politic = request.args.get('contains', default="republică prezidențială", type=str)
    list_tari = list()
    for guvernare\
            in persist.persisence_session.query(persist.Guvernare)\
            .filter(persist.Guvernare.sistem_politic.contains(sistem_politic)):
        tara, tara_steaguri, geografie, list_vecini, _, limba, economie, identificatori, populatie = \
            get_all_country_data_by_id(guvernare.id_tara)

        tara_json = construct_response_country_dict(tara, tara_steaguri, populatie, geografie, list_vecini, guvernare,
                                                    limba, economie, identificatori)
        list_tari.append(copy.deepcopy(tara_json))
    return construct_response_dict("all-data", len(list_tari), list_tari)

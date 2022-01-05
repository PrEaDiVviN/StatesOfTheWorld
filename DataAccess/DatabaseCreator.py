from DataAccess.EngineConnector.EngineContext import EngineContext
import logging
from datetime import datetime
import sqlalchemy
from Models import Tara, Economie, Geografie, GeografieVecini, Guvernare, Identificator, Limba, Populatie, TaraSteaguri


def lower_10_append_zero_to_string(number):
    """ A function that convers a int into a string and appends '0' to front if that int < 10.

    :param number: Int
    :return: String
    """
    if number < 10:
        return "0" + str(number)
    return str(number)


def construct_file_name():
    """ A function that constructs a file name by appending 'CreationHistory/', current year,
    current month, current day, current hours, current minutes, current seconds, '_migration.log'.

    :return: The filename as a string
    """
    current_time = datetime.now()
    year = lower_10_append_zero_to_string(current_time.year)
    month = lower_10_append_zero_to_string(current_time.month)
    day = lower_10_append_zero_to_string(current_time.day)
    hours = lower_10_append_zero_to_string(current_time.hour)
    minutes = lower_10_append_zero_to_string(current_time.minute)
    seconds = lower_10_append_zero_to_string(current_time.second)
    name = 'CreationHistory/' + year + '-' + month + '-' + day + '-' + hours + minutes + seconds + '_migration.log'
    return name


def set_file_logging():
    """ A function that changes the default logging for sqlalchemy to a specified filename. It is set
    at the construction of the object to the result of construct_file_name() function call.
    """
    file_name = construct_file_name()
    handler = logging.FileHandler(file_name)
    logging.getLogger('sqlalchemy').handlers = [handler]


if __name__ == "__main__":
    set_file_logging()
    EngineContext.save()

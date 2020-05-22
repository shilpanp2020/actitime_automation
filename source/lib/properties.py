from time import sleep

from pyjavaproperties import Properties


def get_properties():
    input_stream = open(".\\resources\\data\\config.properties")
    prop = Properties()
    prop.load(input_stream)
    return prop


def get_browser():
    prop = get_properties()
    value = prop.getProperty("browser_name")
    sleep(2)
    return value


def get_url():
    prop = get_properties()
    return prop.getProperty("url")


def get_username():
    prop = get_properties()
    return prop.getProperty("username")


def get_password():
    prop = get_properties()
    return prop.getProperty("password")


def get_implicit_wait():
    prop = get_properties()
    return int(prop.getProperty("i_wait"))


def get_explicit_wait():
    prop = get_properties()
    return int(prop.getProperty("e_wait"))


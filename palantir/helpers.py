import configparser
import psycopg2
import requests


def config(filename='config.ini', section='db'):
    # create a parser
    parser = configparser.ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db


def get_camera_list():
    conn = None
    camera_list = []
    try:
        conn = get_connect()
        curr = conn.cursor()
        curr.execute("select camera_link_id, link from camera_link where is_actual ='Y'")
        camera_list = curr.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return camera_list


def get_connect():
    param = config()
    conn = psycopg2.connect(**param)
    return conn


def get_picture(link):
    img = None
    try:
        response = requests.get(link)
        img = response.content
    except (Exception, requests.RequestException) as error:
        print(error)
    return img


def db_write_picture(camera_link_id, img):
    conn = None
    try:
        conn = get_connect()
        curr = conn.cursor()
        curr.execute("insert into camera_picture(camera_link_id, picture) values (%s,%s)",
                     (camera_link_id, psycopg2.Binary(img)))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

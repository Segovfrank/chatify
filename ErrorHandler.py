import logging

logging.basicConfig(filename='logs.log', level=logging.INFO, format="%(asctime)s:%(levelname)s: %(message)s")
logging.getLogger().addHandler(logging.StreamHandler())

def connectionError():
    logging.error("CONN: Client key and server key do not match!")

def parsingError():
    logging.error("PARSE: Error parsing")

def broadCastError():
    logging.error("BRD: Error sending broadcast")



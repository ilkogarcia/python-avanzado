import logging

logging.basicConfig(level=logging.DEBUG, filename="ejemplo_logs.log", filemode="w")

logging.debug("Registro de eventos de depuración")
logging.info("Registro de eventos informativos")
logging.warning("Registro de advertecias")
logging.error("Registro de errores")
logging.critical("Registro de errores críticos")


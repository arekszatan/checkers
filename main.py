from application import Application
import log
import logging

if __name__ == "__main__":
    log.set_logger_conf()
    logging.info("Start of application")
    app = Application()
    app.run()
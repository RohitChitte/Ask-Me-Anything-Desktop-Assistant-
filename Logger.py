import logging


class customelog:
    def __init__(self):
        pass
    def getlog(self):
        logging.basicConfig(level=logging.DEBUG, filename='Logger.Log',
                            format='%(asctime)s %(levelname)s     %(message)s')
        logger = logging.getLogger()
        return logger

    def loginfo(self,msg):
        self.getlog().info(str(msg))

    def logdebug(self,msg):
        self.getlog().debug(str(msg))

    def logwarning(self,msg):
        self.getlog().warning(str(msg))

    def logerror(self,msg):
        self.getlog().error(str(msg))

    def logexception(self,msg):
        self.getlog().exception(str(msg))

    def logcritical(self,msg):
        self.getlog().critical(str(msg))


"""
log = customelog()
log.loginfo("This msg is logged using custome loger class")
log.logdebug("This msg is logged using custome loger class")
log.logerror("This msg is logged using custome loger class")
log.logwarning("This msg is logged using custome loger class")
log.logexception("This msg is logged using custome loger class")

"""

"""
logging.basicConfig(level=logging.DEBUG,filename='temp.Log',format='%(asctime)s %(levelname)s     %(message)s')
logging.debug('this is for dubugging')
logging.info("This is info logg")
logging.warning("This is warning log")
logging.error("This is my error log")
logging.exception("This is my exception log")
logging.critical('This is my critical log')
lg = logging.getLogger()
lg.debug("using lg and get logger ")
"""
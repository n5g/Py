import logging

#137
#выведет в консоль
logging.warning("warning massage")
logging.info("info massage")
logging.error("error message")

logging.basicConfig(filename="test.log", level=logging.DEBUG) #Создат файл в директории проекта
logging.warning("warning massage")
logging.info("info massage")
logging.error("error message")


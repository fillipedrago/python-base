#!/home/gitpod/.pyenv/shims/python
import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs", logging.DEBUG)
# ch = logging.StreamHandler() # Console/terminal/stderr
# ch.setLevel(log_level)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=10**6, # max bytes padrão é 10**6, que é 1 MB
    backupCount=10, # quantidade de arquivos salvos de backup
    ) 

fh.setLevel(log_level)
fmt = logging.Formatter( 
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
# ch.setFormatter(fmt)
fh.setFormatter(fmt)
# log.addHandler(ch)
log.addHandler(fh)



#Exploração
# log.debug("Mensagem pro dev, QA, SysAdmin")
# log.info("Mensagem geral para usuários")
# log.warning("Aviso que não causa erro")
# log.error("Erro que afeta uma única execução")
# log.critical("Erro geral (que afeta todo mundo). Ex: banco de dados sumiu")


# print("-----")

# Exemplo real de uso

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
    # print(f"Deu erro {str(e)}")
#!/home/gitpod/.pyenv/shims/python
import os
import logging


# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)

# Criando nova instância, que não é mais o root logger:
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
# instancia
log = logging.Logger("logs", logging.DEBUG)
# level
ch = logging.StreamHandler() # Console/terminal/stderr
ch.setLevel(log_level)
# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
#destino
log.addHandler(ch)



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
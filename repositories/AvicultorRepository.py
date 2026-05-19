from helpers.database import get_conn
from helpers.logger import logger

'''
  Manipulação do banco de dados para a entidade Avicultor.
'''


class AvicultorRepository():
    def getByIdAvicultor(self, id):
        conn = get_conn()
        # 2 - Recuperar o cursor
        cursor = conn.cursor()
        # 3 - Preparar a consultar: query | statement
        logger.info("Preparando statement.")
        stmt = "select * from tb_avicultores where id=?"
        cursor.execute(stmt, (id, ))
        # 4.1 - Iterar nos resultados: resultset (fetchall, fecthone)
        row = cursor.fetchone()
        return row

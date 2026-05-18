# Manipulação do dados com o banco de dados
class AvicultorRepository():
    def listarByIdAvicultores(self):
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

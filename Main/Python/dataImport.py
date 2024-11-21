from database import database_connection  
from datetime import datetime
from decimal import Decimal

class ImportData:
    def __init__(self) -> None:
        pass

    def obtem_mes_atual(self) -> int:
        """Retorna o mês atual."""
        return datetime.today().month

    def obtem_gasto_cartao(self) -> Decimal:
        """Obtém o gasto total no cartão para a próxima data de vencimento da fatura."""
        try:
            connection, cursor = database_connection()
            query = """
                SELECT SUM(VALOR_PARCELA) 
                FROM TB_TRANSAC_FINANC 
                WHERE MONTH(DATA_VENCIMENTO_PARCELA) = ?
            """
            mes_fechamento = self.obtem_mes_atual() + 1

            cursor.execute(query, (mes_fechamento,))
            retorno_query = cursor.fetchone()

            if retorno_query and retorno_query[0] is not None:
                return retorno_query[0]
            else:
                print('Nenhum valor em aberto para o mês atual.')
                return Decimal(0)
        except Exception as e:
            print(f"Erro ao obter gasto do cartão: {e}")
            return Decimal(0)

    def obtem_demais_valores(self) -> Decimal:
        """Obtém outros valores registrados no mês atual, excluindo certas categorias e formas de pagamento."""
        try:
            connection, cursor = database_connection()
            query = """
                SELECT SUM(VALOR) 
                FROM TB_REG_FINANC
                WHERE 
                    IDFORMA_PAGAMENTO != 100
                    AND IDCATEGORIA NOT IN (800, 900)
                    AND MONTH(DATA_REGISTRO) = ?
            """
            mes_fechamento = self.obtem_mes_atual()

            cursor.execute(query, (mes_fechamento,))
            retorno_query = cursor.fetchone()

            if retorno_query and retorno_query[0] is not None:
                return retorno_query[0]
            else:
                return Decimal(0)
        except Exception as e:
            print(f"Erro ao obter demais valores: {e}")
            return Decimal(0)
        
    def obtem_aplicacao_financ(self) -> Decimal:
        try:
            connecton, cursor = database_connection()
            query = """
               SELECT TOP 1 SALDO_ATUAL
               FROM TB_APLICACAO_FINANC
               ORDER BY IDREGISTRO DESC
            """
            cursor.execute(query)
            retorno_query = cursor.fetchone()

            if retorno_query and retorno_query[0] is not None:
                return retorno_query[0]
            else:
                return Decimal(0)
        except Exception as e:
            print(f"Erro ao obter os valores aplicados")
            return Decimal(0)

    def gasto_por_categoria(self) -> dict:
        """Obtém o gasto total por categoria."""
        mes_atual = self.obtem_mes_atual()
        try:
            connection, cursor = database_connection()
            registro_gastos_categoria = {}
            categorias_map = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
            
            for id_categoria in categorias_map:
                query = """
                    SELECT
		                SUM(VALOR_PARCELA)
	                FROM 
		                TB_ACOMPANHAMENTO_FINANC
	                WHERE 
		                IDCATEGORIA = ?
		                AND MONTH(DT_PAGAMENTO) >= ?
	                GROUP BY
		                IDCATEGORIA
	                ORDER BY
		                IDCATEGORIA ASC    
                """
                cursor.execute(query, id_categoria, mes_atual)
                retorno_query = cursor.fetchone()

                if retorno_query and retorno_query[0] is not None:
                    registro_gastos_categoria[id_categoria] = retorno_query[0]
                else:
                    registro_gastos_categoria[id_categoria] = Decimal(0)

            return registro_gastos_categoria
        except Exception as e:
            print(f"Erro ao obter gastos por categoria: {e}")
            return {}

    def obtem_valor_total_gasto(self) -> float:
        """Calcula o valor total gasto."""
        gasto_cartao = self.obtem_gasto_cartao()
        demais_valores = self.obtem_demais_valores()
        return float(gasto_cartao) + float(demais_valores)
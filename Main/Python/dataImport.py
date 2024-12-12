from database import database_connection  
from datetime import datetime
from decimal import Decimal
from dateutil.relativedelta import relativedelta

class ImportData:
    def __init__(self) -> None:
        pass

    def obtem_gasto_cartao(self) -> Decimal:
        """Obtém o gasto total no cartão para a próxima data de vencimento da fatura."""
        try:
            connection, cursor = database_connection()
            query = """
                SELECT SUM(VALOR_PARCELA) 
                FROM TB_TRANSAC_FINANC 
                WHERE MONTH(DATA_VENCIMENTO_PARCELA) = ?
            """
            mes_fechamento = (datetime.today() + relativedelta(months=1)).month

            cursor.execute(query, (mes_fechamento))
            retorno_query = cursor.fetchone()
            connection.commit()
            cursor.close()
            connection.close()
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
            mes_fechamento = datetime.today().month

            cursor.execute(query, (mes_fechamento,))
            retorno_query = cursor.fetchone()
            connection.commit()
            cursor.close()
            connection.close()            
            if retorno_query and retorno_query[0] is not None:
                return retorno_query[0]
            else:
                return Decimal(0)
        except Exception as e:
            print(f"Erro ao obter demais valores: {e}")
            return Decimal(0)
        
    def obtem_aplicacao_financ(self) -> Decimal:
        try:
            connection, cursor = database_connection()
            query = """
               SELECT TOP 1 
               FORMAT(SALDO_ATUAL, 'N2', 'pt-BR')
               FROM TB_APLICACAO_FINANC
               ORDER BY ID_APLICACAO DESC
            """
            cursor.execute(query)
            retorno_query = cursor.fetchone()
            connection.commit()
            cursor.close()
            connection.close()
            if retorno_query and retorno_query[0] is not None:
                return retorno_query[0]
            else:
                return Decimal(0)
        except Exception as e:
            print(f"Erro ao obter os valores aplicados")
            return Decimal(0)

    def gasto_por_categoria(self) -> dict:
        """Obtém o gasto total por categoria."""
        mes_atual = datetime.today().month
        mes_posterior = (datetime.today() + relativedelta(months=1)).month
        registro_gastos_categoria = {}
        categorias_map = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]

        try:
            # Estabelecendo conexão explicitamente
            connection, cursor = database_connection()

            for id_categoria in categorias_map:
                query = """
                    SELECT
                        FORMAT(SUM(VALOR_PARCELA), 'N2', 'pt-BR')
                    FROM 
                        TB_ACOMPANHAMENTO_FINANC
                    WHERE 
                        IDCATEGORIA = ?
                        AND MONTH(DT_PAGAMENTO) IN (?, ?)
                    GROUP BY
                        IDCATEGORIA
                """
                cursor.execute(query, (id_categoria, mes_atual, mes_posterior))
                retorno_query = cursor.fetchone()

                registro_gastos_categoria[id_categoria] = retorno_query[0] if retorno_query and retorno_query[0] is not None else Decimal(0)

            # Fechar conexão corretamente
            connection.commit()
            cursor.close()
            connection.close()

            return registro_gastos_categoria
        except Exception as e:
            print(f"Erro ao obter gastos por categoria: {e}")
            return {}

    def dados_grafico_aplicacaoFinanc(self):
        meses = []
        valores = []
        connection, cursor = database_connection()
        query = """
            SELECT
                CASE
                    WHEN MONTH(DATA_APLICACAO) = 1 THEN 'JAN'
                    WHEN MONTH(DATA_APLICACAO) = 2 THEN 'FEV'
                    WHEN MONTH(DATA_APLICACAO) = 3 THEN 'MAR'
                    WHEN MONTH(DATA_APLICACAO) = 4 THEN 'ABR'
                    WHEN MONTH(DATA_APLICACAO) = 5 THEN 'MAI'
                    WHEN MONTH(DATA_APLICACAO) = 6 THEN 'JUN'
                    WHEN MONTH(DATA_APLICACAO) = 7 THEN 'JUL'
                    WHEN MONTH(DATA_APLICACAO) = 8 THEN 'AGO'
                    WHEN MONTH(DATA_APLICACAO) = 9 THEN 'SET'
                    WHEN MONTH(DATA_APLICACAO) = 10 THEN 'OUT'
                    WHEN MONTH(DATA_APLICACAO) = 11 THEN 'NOV'
                    ELSE 'DEZ'
                END "MÊS",
                VALOR_APLICACAO "Valor"
            FROM
                TB_APLICACAO_FINANC
            WHERE 
                DATA_APLICACAO >= DATEADD(MONTH, -12, GETDATE())
            ORDER BY
                MONTH(DATA_APLICACAO) ASC,
                YEAR(DATA_APLICACAO) ASC
        """
        cursor.execute(query)
        resultado = cursor.fetchall()
        
        connection.commit()
        cursor.close()
        connection.close()
        
        for tupla in resultado:
            meses.append(tupla[0])
            valores.append(float(tupla[1]))    
        
        dados = {"Mês":meses,
                 "Valores":valores}
        
        return dados   
    
    def dados_grafico_gastoMensal(self):
        meses = []
        valores = []
        connection, cursor = database_connection()
        query = """
            SELECT 
                CASE
                    WHEN MONTH(DATA_GASTO) = 1 THEN 'JAN'
                    WHEN MONTH(DATA_GASTO) = 2 THEN 'FEV'
                    WHEN MONTH(DATA_GASTO) = 3 THEN 'MAR'
                    WHEN MONTH(DATA_GASTO) = 4 THEN 'ABR'
                    WHEN MONTH(DATA_GASTO) = 5 THEN 'MAI'
                    WHEN MONTH(DATA_GASTO) = 6 THEN 'JUN'
                    WHEN MONTH(DATA_GASTO) = 7 THEN 'JUL'
                    WHEN MONTH(DATA_GASTO) = 8 THEN 'AGO'
                    WHEN MONTH(DATA_GASTO) = 9 THEN 'SET'
                    WHEN MONTH(DATA_GASTO) = 10 THEN 'OUT'
                    WHEN MONTH(DATA_GASTO) = 11 THEN 'NOV'
                    ELSE 'DEZ'
                END "Mês", 
                CAST(SUM(valor / COALESCE(NULLIF(N_PARCELAS, 0), 1)) AS DECIMAL(10, 2)) AS "Valor Gasto"
            FROM TB_REG_FINANC
            WHERE 
                IDCATEGORIA NOT IN (800, 900)
                AND data_gasto >= DATEADD(MONTH, -6, GETDATE()) -- Últimos 6 meses
            GROUP BY
                MONTH(data_gasto),
                YEAR(data_gasto)
            ORDER BY
                YEAR(data_gasto) ASC,
                MONTH(data_gasto) ASC;
        """
        cursor.execute(query)
        resultado_query = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        
        for tupla in resultado_query:
            meses.append(tupla[0])
            valores.append(float(tupla[1]))
        
        dados = {
            "Mês":meses,
            "Valores":valores
        }
        return dados
        
    def obtem_valor_total_gasto(self) -> float:
        """Calcula o valor total gasto."""
        gasto_cartao = self.obtem_gasto_cartao()
        demais_valores = self.obtem_demais_valores()
        return float(gasto_cartao) + float(demais_valores)

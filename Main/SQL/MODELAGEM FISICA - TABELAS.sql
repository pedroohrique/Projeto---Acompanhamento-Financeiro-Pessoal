CREATE TABLE TB_REG_FINANC(
	ID_REGISTRO INT PRIMARY KEY IDENTITY(10,10),
	DATA_REGISTRO DATE,
	DATA_GASTO DATE,
	VALOR DECIMAL(12,2),
	DESCRICAO VARCHAR(100),
	LOCAL_GASTO VARCHAR(100),
	PARCELAMENTO CHAR(1),
	N_PARCELAS INT,
	IDCATEGORIA INT,
	IDFORMA_PAGAMENTO INT

)
GO

CREATE TABLE TB_CATEGORIA(
	ID_CATEGORIA INT PRIMARY KEY,
	DESCRICAO VARCHAR(100)
)
GO

CREATE TABLE TB_FORMA_PAGAMENTO(
	ID_FORMA INT PRIMARY KEY,
	DESCRICAO VARCHAR(100)

)
GO

CREATE TABLE TB_TRANSAC_FINANC(
	ID_TRANSACAO INT PRIMARY KEY IDENTITY(1,1),
	IDREGISTRO INT,
	DATA DATE,
	QTD_PARCELAS INT,
	N_PARCELA INT,
	VALOR_PARCELA DECIMAL(12,2),
	VALOR_TOTAL DECIMAL(12,2),
	DATA_VENCIMENTO_PARCELA DATE

)
GO

CREATE TABLE TB_APLICACAO_FINANC(
	IDREGISTRO INT,
	DATA_APLICACAO DATE,
	DESCRICAO VARCHAR(100),
	LOCAL_APLICACAO VARCHAR(100),
	ORIGEM_APLICACAO VARCHAR(100),
	VALOR_APLICACAO DECIMAL(12,2),
	SALDO_ATUAL DECIMAL(12,2)
	
)
GO

CREATE TABLE TB_ACOMPANHAMENTO_FINANC(
	ID INT PRIMARY KEY IDENTITY (10,10),
	IDREGISTRO INT,
	DT_COMPRA DATE,
	DT_PAGAMENTO DATE,
	VALOR_TOTAL DECIMAL (10,2),
	VALOR_PARCELA DECIMAL (10,2),
	VALOR_PENDENTE DECIMAL (10,2),
	QT_PARCELAS INT,
	QT_PARCELAS_PENDENTES INT,
	IDCATEGORIA INT
	

)
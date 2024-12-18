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
GO

USE [FINANCEIRO]
GO

/****** Object:  Table [dbo].[TB_CHECKLIST_FINANC]    Script Date: 12/12/2024 14:18:43 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[TB_CHECKLIST_FINANC](
	[ID_DESPESA] [int] IDENTITY(1,1) NOT NULL,
	[DESPESA] [varchar](50) NULL,
	[VALOR_DESPESA] [decimal](10, 2) NULL,
	[DT_REGISTRO] [date] NULL,
	[DT_VENCIMENTO] [date] NULL,
	[DT_PAGAMENTO] [date] NULL,
	[TIPO_DESPESA] [varchar](15) NULL,
	[CONTADOR_PAGAMENTO] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[ID_DESPESA] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

USE [FINANCEIRO]
GO

/****** Object:  Table [dbo].[TB_MENSAGENS_COLETADAS]    Script Date: 12/12/2024 14:19:21 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[TB_MENSAGENS_COLETADAS](
	[ID_COLETA] [int] NOT NULL,
	[DATA_COLETA] [date] NULL,
	[DATA_GASTO] [date] NULL,
	[DESCRICAO] [varchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[ID_COLETA] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO


USE [FINANCEIRO]
GO

/****** Object:  Trigger [dbo].[TGR_INSERE_ACOMPANHAMENTO]    Script Date: 20/10/2024 10:02:23 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TRIGGER [dbo].[TGR_INSERE_ACOMPANHAMENTO]
ON [dbo].[TB_REG_FINANC]
AFTER INSERT
AS

BEGIN

	DECLARE

		@IDREG INT, -- ARMAZENA O IDREGISTRO - OK
		@DT_COMPRA DATE, -- REGISTRAR� A DATA DA COMPRA - OK
		@V_TOTAL DECIMAL(10,2), -- VALOR TOTAL DA COMPRA - OK
		@V_EM_ABERTO DECIMAL(10,2), -- VALOR EM ABERTO PARA O M�S ATUAL - OK
		@V_T_P DECIMAL(10,2), -- ARMAZENA O VALOR TOTAL RESTANTE DA COMPRA - OK
		@QTD_PARCELAS_T INT,  -- QTD TOTAL DE PARCELAS - OK
		@QTD_PARCELAS_P INT, -- QRD PARCELAS PENDENTES
		@ID_C INT,  -- ARMAZENA O ID CATEGORIA - OK
		@ID_F INT,
		@DT_VENCIMENTO DATE --OK


		SELECT @IDREG = ID_REGISTRO FROM INSERTED
		SELECT @DT_COMPRA = DATA_GASTO  FROM INSERTED
		SELECT @V_TOTAL = VALOR FROM INSERTED
		SELECT @QTD_PARCELAS_T = N_PARCELAS FROM INSERTED
		SELECT @ID_C = IDCATEGORIA FROM INSERTED
		SELECT @ID_F = IDFORMA_PAGAMENTO FROM INSERTED
		
		SET @DT_VENCIMENTO = @DT_COMPRA
		SET @V_EM_ABERTO = @V_TOTAL
		SET @V_T_P = 0.0
		SET @QTD_PARCELAS_P = 0

		IF @ID_F != 100

			BEGIN

			INSERT 
				INTO TB_ACOMPANHAMENTO_FINANC (IDREGISTRO, DT_COMPRA, DT_PAGAMENTO, VALOR_TOTAL, VALOR_PARCELA, VALOR_PENDENTE, QT_PARCELAS, QT_PARCELAS_PENDENTES, IDCATEGORIA)
			VALUES
				(@IDREG, @DT_COMPRA, @DT_VENCIMENTO, @V_TOTAL, @V_EM_ABERTO, @V_T_P, @QTD_PARCELAS_T, @QTD_PARCELAS_P, @ID_C)


			END



END




GO

ALTER TABLE [dbo].[TB_REG_FINANC] ENABLE TRIGGER [TGR_INSERE_ACOMPANHAMENTO]
GO



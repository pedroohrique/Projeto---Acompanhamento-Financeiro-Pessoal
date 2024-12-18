USE [FINANCEIRO]
GO
/****** Object:  Trigger [dbo].[TGR_INSERE_ACOMPANHAMENTO2]    Script Date: 03/10/2024 14:58:32 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TGR_INSERE_ACOMPANHAMENTO2]
ON [dbo].[TB_TRANSAC_FINANC]
AFTER INSERT
AS

BEGIN

	DECLARE

		@IDREG INT, --OK
		@DT_COMPRA DATE, --OK
		@DT_VENCIMENTO DATE, --OK
		@V_TOTAL DECIMAL(10,2), -- OK
		@V_EM_ABERTO DECIMAL(10,2), -- OK
		@V_T_P DECIMAL(10,2), --OK
		@QTD_PARCELAS INT, --OK 
		@QTD_PARCELAS_P INT, --OK
		@ID_C INT


		SELECT @IDREG = IDREGISTRO FROM INSERTED
		SELECT @DT_COMPRA = DATA FROM INSERTED
		SELECT @DT_VENCIMENTO = DATA_VENCIMENTO_PARCELA FROM INSERTED
		SELECT @V_TOTAL = VALOR_TOTAL FROM INSERTED
		SELECT @V_EM_ABERTO = VALOR_PARCELA  FROM INSERTED
		SELECT @QTD_PARCELAS = QTD_PARCELAS  FROM INSERTED
		SELECT @ID_C = IDCATEGORIA FROM INSERTED
		

		SET @QTD_PARCELAS_P = (@QTD_PARCELAS - DATEDIFF(MONTH, @DT_COMPRA, GETDATE()))
		SET @V_T_P = (@QTD_PARCELAS_P * @V_EM_ABERTO)


		INSERT 
			INTO TB_ACOMPANHAMENTO_FINANC (IDREGISTRO, DT_COMPRA, DT_PAGAMENTO, VALOR_TOTAL, VALOR_PARCELA, VALOR_PENDENTE, QT_PARCELAS, QT_PARCELAS_PENDENTES, IDCATEGORIA)
		VALUES
			(@IDREG, @DT_COMPRA, @DT_VENCIMENTO, @V_TOTAL, @V_EM_ABERTO, @V_T_P, @QTD_PARCELAS, @QTD_PARCELAS_P, @ID_C)

END




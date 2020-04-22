from cawebhelper import CAWebHelper
import unittest

class CNTA021(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        # I N S T A N C I A
        inst.oHelper = CAWebHelper("http://localhost:9096/","FIREFOX")

        # S E T U P
        inst.oHelper.SetUp("SIGAGCT","P12117","ADMIN","","08/01/2018","T1","D MG 01 ","69")

        # M E N U
        inst.oHelper.UTProgram("CNTA020")

    #---------------------------------------------------------------------------------
    # A U T O R: Thamarav@
    # D A T E: 08/01/2018 
    # C T 0 0 1: Incluir (Tipo de Contrato Compra, medi��o eventual, contrato fixo, 
    # multa/bonifica��o na medi��o, n�o permite multa manual, limite financeiro) 
    #---------------------------------------------------------------------------------

    def test_CNTA021_001(self):
        #------------------------------------------------------
        # Na inclus�o, informar no segundo par�metro a filial
        #------------------------------------------------------
        self.oHelper.SetButton('Incluir', 'D MG 01 ')

        self.oHelper.UTSetValue("aCab","CN1_DESCRI", "COMPRA")
        self.oHelper.UTSetValue("aCab","CN1_MEDEVE", "1") #1=Sim    
        self.oHelper.UTSetValue("aCab","CN1_TPMULT", "2") #2=Medi��o
        self.oHelper.UTSetValue("aCab","CN1_MULMAN", "1") #1=N�o permite
        self.oHelper.UTSetValue("aCab","CN1_ESPCTR", "1") #1=Compra

        #------------------------------------------------------
        # Exemplo de utiliza��o com mudan�a de pastas 
        #------------------------------------------------------        
        #self.oHelper.ClickFolder('Informativos/Impostos')
        #self.oHelper.UTSetValue("aCab","CN1_ALINSS", "15,00")

        self.oHelper.SetButton("Confirmar")

        #--------------------------------------------
        # Mensagem de registro inclu�do com sucesso 
        #--------------------------------------------
        self.oHelper.SetButton('Fechar')
        
        #--------------------------------------------
        # Pesquisa de registro
        #--------------------------------------------
        # self.oHelper.SearchBrowse('Filial+codigo + Loja',"D MG    %s" %codigo, True)

        #--------------------------------------------
        # Resultado esperado
        #--------------------------------------------
        self.oHelper.SetButton('Visualizar')

        self.oHelper.UTCheckResult("aCab","CN1_DESCRI", "COMPRA")
        self.oHelper.UTCheckResult("aCab","CN1_MEDEVE", "1") #1=Sim    
        self.oHelper.UTCheckResult("aCab","CN1_TPMULT", "2") #2=Medi��o
        self.oHelper.UTCheckResult("aCab","CN1_MULMAN", "1") #1=N�o permite
        self.oHelper.UTCheckResult("aCab","CN1_ESPCTR", "1") #1=Compra
       
        #-----------------------------------------------------------------------------------------------
        # An�lise do resultado esperado dos campos autopreenchidos de acordo com o inicializador padr�o
        #-----------------------------------------------------------------------------------------------
        self.oHelper.UTCheckResult("aCab","CN1_MEDAUT", "2") #2-N�o
        self.oHelper.UTCheckResult("aCab","CN1_CROFIS", "2") #2-N�o
        self.oHelper.UTCheckResult("aCab","CN1_TPLMT" , "2") #1-Financeiro
        self.oHelper.UTCheckResult("aCab","CN1_CROCTB", "2") #2-Nao
        self.oHelper.UTCheckResult("aCab","CN1_CTRFIX", "1") #1-Sim
        self.oHelper.UTCheckResult("aCab","CN1_VLRPRV", "1") # 1-Sim

        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()
    
    #------------------------------------------------------------------------------------
    # M�todo respons�vel por posicionar o Protheus no browse para execu��o do pr�ximo CT
    #------------------------------------------------------------------------------------
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()
#-----------------------------------------------------------------------
# M�todo respons�vel por s� permitir a execu��o do teste via TestSuite 
# (particularidade o Python)
#-----------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
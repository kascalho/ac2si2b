def  inicializar ():
	tab  = []
	para  i  no  intervalo ( 3 ):
		linha  = []
		para  j  no  intervalo ( 3 ):
			linha . anexar ( "." )
		guia . anexar ( linha )
	voltar  guia

def  main ():
	jogo  =  inicializar ()
	imprimir ( jogo )

if  __name__  ==  "__main__" :
	principal ()

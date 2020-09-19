importar  jogovelha
import  sys

erroInicializar  =  False
jogo  =  jogovelha . inicializar ()

se  len ( jogo ) ! =  3 :
	erroInicializar  =  True
mais :
	para  linha  no  jogo :
		se  len ( linha ) ! =  3 :
			erroInicializar  =  True
		mais :
			para  elemento  em  linha :
				se  elemento  ! =  '.' :
					erroInicializar  =  True
se  erroInicializar :
	sys . saída ( 1 )
mais :
	sys . saída ( 0 )

#coding:utf-8
"""

 mon premier script sur python 
script de calcul utile pour tous le monde

 """


affiche = open("core/script.txt", "r").read()
	

# création du fichier main 

commencer = True 
print("""
          
        ENTRER VOTRE NOM POUR UTILISER CE PROGRAMME
 
""")
user_id = input( "<=> " )
print("     ", user_id, "Bienvenu sur mon programme Math")
 
print(affiche)

# definition de la boucle 

while commencer :

	a = 1
	b = 2
	c = 3
	d = 4
	e = 5

	print(""" 
           [1] =  Multiplication
           [2] = Addition
           [3] = Soustraction
           [4] = Division 
           [5] = Pour Fermer le programme """)


	print("""     
               Veuillez choisir un numéro 
          """)

	put = input(" <==> ")

	try : 
		put = int(put)
	except :

		print("""
                  Veuillez choisir des numeros valides
""")

	if put == a :


#Tablle de multiplication


		def X(x, y, z):
			xx = x
			while xx <= z:
				print(y, "x", xx, "=", xx * y, )
				xx += 1
		print("""
		
            TABLE DE MULTIPLICATION M

""")
		print("""

              Entrer le début de la table de M

""")
		x1 = input(" <==> ")
		print("""

              Entrer  le nombre à multiplier

""")
		x2 = input(" <==> ")
		print("""

                Entrer la fin de la table M

""")
		x3 = input(" <==> ")
		try :
			x1 = int(x1)
			x2 = int(x2)
			x3 = int(x3)
			print("""
           
                     Table de multiple de : """, x2)
		except :
			print("""

				Oups !! Entrer des nombres valides
""")
		try : 
			X(x1, x2, x3)
		except :
			pass


# Table d'addition 
	
	elif put == b :


		def  A(x, y, z) :
			xx = x
			xx = 0
			while xx <= z :
				xx += 1
				print(y, "+", xx, "=", y + xx)
		print(""" 

			Entrer le début de votre table A 
""")
		a1 = input(" <==> ")
		print(""" 

			Entrer le nombre à additionner
""")
		a2 = input(" <==> ")
		print(""" 

			Entrer le fin de la table de A
""")
		a3 = input(" <==> ")
		try :
			a1 = int(a1)
			a2 = int(a2)
			a3 = int(a3)
			print (""" 
				
				Table d'addition d'Addition de A""", a3)
		except :
			print ("""
			
            Oups !! Entrer des données valides
""")
		try :
			A(a1, a2, a3)
		except :
			pass 

# Table de soustraction  

	elif put == c :



		def S(x, y, z) :
			ss = x
			while ss <= z :
				print(y + ss, "-", y, "=", y + ss -y )
				ss += 1
		print(""" 

		     Entrer le début de votre table S
""")
		s1 = input(" <==> ")
		print(""" 

			Entrer le nombre à soustrait
""")
		s2 = input(" <==> ")
		print(""" 

			Entrer la fin de la table S
""")
		s3 = input(" <==> ")
		try :
			s1 = int(s1)
			s2 = int(s2)
			s3 = int(s3)
			print("""

				Table de Soustraction de : """, s1)
		except :
			print("""

				Oups !! Entrer des nombres valides

""")
		try :
			S(s1, s2, s3)
		except :
			pass 

# Table de division 

	elif put == d :

		def  D(x, y, z) :
			xx = x
			xx = 0
			while xx <= z :
				xx += 1
				print(y * xx, "÷", y, "=", y * xx // y )
		print(""" 

			Entrer le début de la table de D 
""")
		d1 = input(" <==> ")
		print(""" 

			Entrer le nombre à diviser 
""")
		print(""" 

			Entrer le nombre à diviser

""")
		d2 = input(" <==> ")
		print(""" 

			Entrer la fin de la table D
""")
		d3 = input(" <==> ")
		try :
			d1 = int(d1)
			d2 = int(d2)
			d3 = int(d3)
			print(""" 

				Table de division de : """, d2 
	)
		except :
			print ("""

				Oups !! entrer des données valides
""")
		try :
			D(d1, d2, d3)
		except :
			pass

# obtion pour quitter le programme 
	elif put == e : 
		print("""
                    
              Programme fermer à bientôt """, user_id
)
		break
	else : 
		pass


# PROGRAMME FINIR 



































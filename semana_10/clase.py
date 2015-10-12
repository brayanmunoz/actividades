class vehiculo():
	def __init__(self,modelo,cilindraje_motor,numero_ejes):
		self.cilindraje_motor = cilindraje_motor
		self.modelo = modelo
		self.numero_ejes = numero_ejes
	def mostrar_detalles(self):
		return 'los datos del vehiculo son:'+str(self.cilindraje_motor)+'	'+str(self.modelo)+'	'+str(self.numero_ejes)
	def arrancar(self):
		return 'RUMM'
v1= vehiculo(2015,1000,50)
v2= vehiculo(2014,5000,25)
print v2.arrancar()

print v1.mostrar_detalles()
print v2.mostrar_detalles()

class vehiculo_aereo(vehiculo):
	def __init__(self,modelo,cilindraje_motor,numero_ejes,n_alas,n_alerones):
		vehiculo.__init__(self,modelo,cilindraje_motor,numero_ejes)
		self.n_alas = n_alas
		self.n_alerones = n_alerones
	def mostrar_detalles(self):
		return' los datos del vehiculo aereo son:'+str(self.cilindraje_motor)+'	'+str(self.modelo)+'	'+str(self.numero_ejes)+'	'+str(self.n_alas)+'	'+str(self.n_alerones)
va1= vehiculo_aereo(2015,1000,50,2,2)
va2= vehiculo_aereo(2014,5000,25,2,2)

print va1.mostrar_detalles()
print va2.mostrar_detalles()

class vehiculo_anfibio(vehiculo):
	def __init__(self,modelo,cilindraje_motor,numero_ejes,n_helices,n_turbinas,tamano_popa):
		vehiculo.__init__(self,modelo,cilindraje_motor,numero_ejes)
		self.n_helices = n_helices
		self.n_turbinas = n_turbinas
		self.tamano_popa = tamano_popa
	def mostrar_detalles(self):
		return'los datos del vehiculo anfibio son :'+str(self.cilindraje_motor)+'	'+str(self.modelo)+'	'+str(self.numero_ejes)+'	'+str(self.n_helices)+'	'+str(self.n_turbinas)+'	'+str(self.tamano_popa)
van1= vehiculo_anfibio(2015,1000,50,2,2,3)
van2= vehiculo_anfibio(2014,5000,25,2,2,3)

print van1.mostrar_detalles()
print van2.mostrar_detalles()
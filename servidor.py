import Pyro4

@Pyro4.expose
class Calculadora(object):
    def somar(self, entrada1, entrada2):
        resultado = entrada1 + entrada2
        return resultado

    def subtrair(self, entrada1, entrada2):
        resultado = entrada1 - entrada2
        return resultado
    
    def multiplicar(self, entrada1, entrada2):
        resultado = entrada1 * entrada2
        return resultado
    
    def dividir(self, entrada1, entrada2):
        try:
            resultado = entrada1 / entrada2
            return resultado
        except ZeroDivisionError:
            return "División Inválida"
        

daemon = Pyro4.Daemon()                # hacer un demonio Pyro
ns = Pyro4.locateNS()                  # encontrar el servidor de nombres
uri = daemon.register(Calculadora)   # registrar el fabricante de saludo como un objeto Pyro
ns.register("calculadoraTop", uri)   # registrar el objeto con un nombre en el servidor de nombres

print("LISTO!.")
daemon.requestLoop()                   # iniciar el bucle de eventos del servidor para esperar las llamadas
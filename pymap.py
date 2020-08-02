import trojan
import nmap3
import platform
import os
import socket
from colorama import Fore,Back,init

print(Fore.RESET + "")
a = (Fore.RED + "[+]")
b = (Fore.RESET + "")
ip = "ip obtenida: \n\n"

def scan():
	try:
		target = input("introduce el target a escanear: ")
		print(ip + a,b, Fore.MAGENTA + socket.gethostbyname(target) + b)
		print("\n\n")
						
	except socket.gaierror as e:
		limpiarL()
		print("\n\nhost erroneo, verifique su escritura o elimine los https://, http:// ejemplo: \n [www.example.com]\n\n")
		
	escaneo = input("¿desea hacer un escaneo de puertos al ip obejetivo? Y/N: " )
	escaneou = escaneo.upper()
	if escaneou == "Y":
		nmap = nmap3.Nmap()
		results = nmap.scan_top_ports(target)
		resultado = str(results)
		print ("el resultado es: \n\n" + resultado)
		
	else:
		print ("Proceso terminado")
		print("\n\ngracias por usar nuestra herramienta :)")

	
	res = input("¿desea guardar el resultado en un archivo? Y/N: ")
	resp = res.upper()
	if resp == "Y":
		pr = socket.gethostbyname(target)
		archivo = open("ips/1._ip.txt","w")
		archivo.write("el ip de " + target + " es igual a " + pr + "\n\n" + resultado)
		archivo.close()
	input("proceso terminado presione enter para continuar: ")
	trojan.limpiarL()
	print(Fore.YELLOW + "\t\t-----Buscar una victoria implca sacrificios-----", Fore.RESET + "")

	
if __name__ == "__main__":
	scan()

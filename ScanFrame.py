import pickle
import Lex
import AfLib

if __name__ == "__main__":

    res = Lex.generateLexer('slr-1.yal')

    if res:

        # Definir el contenido del nuevo archivo Python Scan.py
        contenido = """# Este es un archivo Python generado automaticamente
import pickle 
            
def step_simulate_AFD(afd,c,lookAhead):
    res = afd.step_simulation(c, lookAhead)
    state = list(res)[0] if len(list(res))>0 else None

    if state in afd.accept:
        return (0,state.action)
    elif state in afd.states:
        return (1,"")
    else:
        return (2,"")
            
def segmentRecognize(afd,i,content):
    accept = (False,0,"")
    first = i
    # Bucle hasta que se alcance el final del contenido
    while i <= len(content):  # Asegura que haya espacio para lookAhead
        char = content[i] if i<len(content) else ""  # Caracter actual
        lookAhead = content[i + 1] if i<len(content)-1 else ""  # Caracter siguiente
        
        # Procesa el caracter aqui
        res = step_simulate_AFD(afd, char, lookAhead)
        if res[0] == 0:
            last = i+1
            accept = (True,last,content[first:last],res[1]) #Estado de aceptacion, ultima posicion de lookAhead, contenido aceptado, accion
        
        elif res[0] == 2:
            if accept[0]:
                return accept
            else:
                return (False,i,"","")

        i += 1  # Incrementa la posicion para el proximo caracter
            
def tokensRecognize(afd,txtContent):
    # Inicializa la posicion
    first = 0
    while first<=len(txtContent):
        res = segmentRecognize(afd,first,txtContent)
    
        if res[0]:
            print("ACEPTADO")
            print(res[2])
            print(res[3])
        else:
            message = f"ERROR al reconocer archivo txt en caracter no. {res[1]}: "
                
            return False

        first = res[1]
            
    return True

if __name__ == "__main__":
    #Lectura del objeto pkl
    with open('afd.pkl', 'rb') as archivo_entrada:
        afd = pickle.load(archivo_entrada)
            
    #Lectura del documento txt
    with open('texto.txt', 'r', encoding='utf-8') as file:
        txtContent = file.read()  # Leer todo el contenido del archivo
        
    tokensRecognize(afd,txtContent)
"""


        # Especificar el nombre del archivo que deseas crear
        nombre_archivo = 'Scan.py'

        # Abrir el archivo para escritura
        with open(nombre_archivo, 'w') as archivo:
            # Escribir el contenido al archivo
            archivo.write(contenido)

        print(f'Archivo {nombre_archivo} generado con exito.')

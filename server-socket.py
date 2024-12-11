import socket 
import threading
import sys
import os 

class Servidor():
    def __init__(self, host="localhost", port=7000, FILES_DIR='./Files'):
        # Arreglo para guardar los clientes conectados 🌸🩰
        self.clientes = []
        self.FILES_DIR = FILES_DIR
        if not os.path.exists(self.FILES_DIR):
            os.makedirs(self.FILES_DIR)

        # Configuración del socket 🌸🩰
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)

        # Hilos para aceptar y procesar las conexiones 🌸🩰
        aceptar = threading.Thread(target=self.aceptarCon)
        procesar = threading.Thread(target=self.procesarCon)
        aceptar.daemon = True 
        aceptar.start()
        procesar.daemon = True 
        procesar.start()

        # Manejo de entrada del usuario 🌸🩰
        try:
            while True:
                msg = input('-> ')
                if msg == 'salir':
                    break
            self.sock.close()
            sys.exit()
        except:
            self.sock.close()
            sys.exit()

    def msg_to_all(self, msg, cliente):
        # Enviar mensaje a todos los clientes excepto al emisor 🌸🩰
        for c in self.clientes:
            if c != cliente:
                try:
                    c.send(msg.encode('utf-8'))
                except:
                    self.clientes.remove(c)

    def aceptarCon(self):
        # Aceptar nuevas conexiones 🌸🩰
        print("aceptarCon iniciado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clientes.append(conn)
                print(f"Cliente conectado desde {addr}")
            except:
                pass

    def procesarCon(self):
        # Procesar datos de clientes conectados 🌸🩰
        print("ProcesarCon iniciado")
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024).decode('utf-8')  # Recibir el mensaje del cliente 🌸🩰
                        if data:
                            print(f"Comando recibido: {data}")
                            self.procesar_comando(data, c)
                    except:
                        pass

    def procesar_comando(self, msg, cliente):
        # Procesar el comando recibido del cliente 🌸🩰
        if msg == 'lsFiles':  # Comando para listar archivos 🌸🩰
            archivos = os.listdir(self.FILES_DIR)
            respuesta = "Archivos disponibles:\n" + "\n".join(archivos)
            cliente.send(respuesta.encode('utf-8'))

        elif msg.startswith('get '):  # Comando para obtener un archivo 🌸🩰
            filename = msg.split(' ', 1)[1]
            filepath = os.path.join(self.FILES_DIR, filename)
            if os.path.exists(filepath):
                with open(filepath, 'rb') as f:
                    cliente.sendall(f.read())  # Enviar el archivo completo 🌸🩰
            else:
                cliente.send(f"El archivo {filename} no existe.".encode('utf-8'))

        elif msg.startswith('msg '):  # Comando para enviar mensajes entre clientes 🌸🩰
            mensaje = msg.split(' ', 1)[1]
            self.msg_to_all(f"Mensaje de un cliente: {mensaje}", cliente)

        else:
            # Enviar respuesta si el comando no es reconocido 🌸🩰
            cliente.send("Comando no reconocido.".encode('utf-8'))

# Iniciar el servidor 🌸🩰
server = Servidor()

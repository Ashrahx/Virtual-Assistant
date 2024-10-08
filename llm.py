import openai
import json

#Clase para utilizar cualquier LLM para procesar un texto
#Y regresar una funcion a llamar con sus parametros
#se usa el modelo 0613
class LLM():
    def __init__(self):
        pass
    
    def process_functions(self, text):
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                    #Comportamiento
                    {"role": "system", "content": "Eres un asistente virtual femenino"},
                    {"role": "user", "content": text},
            ], functions=[
                {
                    "name": "get_weather",
                    "description": "Obtener el clima actual",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "ubicacion": {
                                "type": "string",
                                "description": "La ubicación, debe ser una ciudad",
                            }
                        },
                        "required": ["ubicacion"],
                    },
                },
                {
                    "name": "send_email",
                    "description": "Enviar un correo",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "recipient": {
                                "type": "string",
                                "description": "La dirección de correo que recibirá el correo electrónico",
                            },
                            "subject": {
                                "type": "string",
                                "description": "El asunto del correo",
                            },
                            "body": {
                                "type": "string",
                                "description": "El texto del cuerpo del correo",
                            }
                        },
                        "required": ["recipient", "subject", "body"],
                    },
                },
                {
                    "name": "open_chrome",
                    "description": "Abrir el explorador Chrome en un sitio específico",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "website": {
                                "type": "string",
                                "description": "El sitio al cual se desea ir"
                            }
                        }
                    }
                },
                 {
                    "name": "who",
                    "description": "¿Qué eres? o ¿Quién eres?",
                    "parameters": {
                        "type": "object",
                        "properties": {
                        }
                    },
                },
                {
                    "name": "request_song",
                    "description": "Solicitar una canción en YouTube o Spotify",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "platform": {
                                "type": "string",
                                "description": "La plataforma de música (YouTube o Spotify)",
                            },
                            "song_name": {
                                "type": "string",
                                "description": "El nombre de la canción a solicitar",
                            }
                        },
                        "required": ["platform", "song_name"],
                    },
                },
                {
                    "name": "contar_chiste",
                    "description": "Contar un chiste aleatorio",
                    "parameters": {
                        "type": "object",
                        "properties": {}
                    },
                },
                {
                    "name": "hello",
                    "description": "Saludar al usuario",
                    "parameters": {
                        "type": "object",
                        "properties": {
                        }
                    },
                }
            ],
            function_call="auto",
        )
        
        message = response["choices"][0]["message"]
        
        #Openai condiciona si llamar una función o no
        if message.get("function_call"):
            #Sip
            function_name = message["function_call"]["name"]
            args = message.to_dict()['function_call']['arguments']
            print("Funcion a llamar: " + function_name)
            args = json.loads(args)
            return function_name, args, message
        
        return None, None, message
    
    #Una vez que llamamos a la funcion (e.g. obtener clima, encender luz, etc)
    #Podemos llamar a esta funcion con el msj original, la funcion llamada y su
    #respuesta, para obtener una respuesta en lenguaje natural
    def process_response(self, text, message, function_name, function_response):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[
                #Comportamiento
                {"role": "system", "content": "Eres un asistente virtual femenino"},
                {"role": "user", "content": text},
                message,
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                },
            ],
        )
        return response["choices"][0]["message"]["content"]

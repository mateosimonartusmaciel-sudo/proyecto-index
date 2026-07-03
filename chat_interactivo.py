# chat_interactivo.py

def chat():
    print("🤖 Bienvenido al Chat Interactivo")
    print("Escribe 'salir' para terminar.\n")

    while True:
        usuario = input("Tú: ")

        if usuario.lower() == "salir":
            print("🤖 Chat finalizado. ¡Hasta luego!")
            break

        # Respuestas simples predefinidas
        if "hola" in usuario.lower():
            print("🤖 ¡Hola! ¿Cómo estás?")
        elif "bien" in usuario.lower():
            print("🤖 Me alegra escuchar eso 😃")
        elif "mal" in usuario.lower():
            print("🤖 Lamento que te sientas así 😔, espero que mejore.")
        elif "gracias" in usuario.lower():
            print("🤖 ¡De nada! 😊")
        else:
            print("🤖 No entendí lo que dijiste, pero suena interesante.")

if __name__ == "__main__":
    chat()

    
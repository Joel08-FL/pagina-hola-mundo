# test.py

def test_hola_mundo():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            contenido = f.read()
            assert "Hola Mundo" in contenido
        print("✅ Prueba pasada: El texto 'Hola Mundo' está presente.")
    except AssertionError:
        print("❌ Prueba fallida: El texto 'Hola Mundo' NO está presente.")
        exit(1)
    except FileNotFoundError:
        print("❌ Prueba fallida: El archivo index.html no se encontró.")
        exit(1)

# Ejecutamos la prueba al correr el archivo
test_hola_mundo()

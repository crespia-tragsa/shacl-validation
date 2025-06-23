from pyshacl import validate
import os

def validar_jsonld_con_shacl(data_path, shapes_path):
    """
    Valida un archivo JSON-LD de datos contra un archivo JSON-LD de formas SHACL.

    Args:
        data_path (str): Ruta al archivo JSON-LD con los datos a validar.
        shapes_path (str): Ruta al archivo JSON-LD con las formas SHACL.
    """
    print(f"\n--- Validando: {os.path.basename(data_path)} ---")

    try:
        conforms, results_graph, results_text = validate(
            data_path,
            shacl_graph=shapes_path,
            data_graph_format="json-ld",  # Especifica que los datos están en JSON-LD
            shacl_graph_format="json-ld", # Especifica que las formas están en JSON-LD
            inference="rdfs",             # Habilita la inferencia RDFS si tu ontología la usa
            debug=False
        )

        if conforms:
            print(f"✅ Los datos en '{os.path.basename(data_path)}' CUMPLEN con las formas SHACL.")
        else:
            print(f"❌ ¡Los datos en '{os.path.basename(data_path)}' NO CUMPLEN con las formas SHACL!")
            print("\n--- Detalles de las Violaciones ---")
            print(results_text)

    except Exception as e:
        print(f"🚨 Ocurrió un error durante la validación: {e}")

# --- Rutas de los archivos ---
if __name__ == "__main__":
    # Asegúrate de que estos archivos estén en el mismo directorio que tu script,
    # o proporciona las rutas completas.
    DATA_FILE = "datos.jsonld"
    SHAPES_FILE = "shapes.jsonld"

    # Validar los datos
    validar_jsonld_con_shacl(DATA_FILE, SHAPES_FILE)

    # --- Prueba con datos NO VÁLIDOS ---
    # Para probar una validación fallida, puedes crear un archivo 'datos_invalidos.jsonld'
    # que no cumpla con las reglas (ej. sin 'ex:tieneNombre' para ex:Persona)
    # y luego descomentar la siguiente línea:
    # invalid_data_file = "datos_invalidos.jsonld"
    # validar_jsonld_con_shacl(invalid_data_file, SHAPES_FILE)

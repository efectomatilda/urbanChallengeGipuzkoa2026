from studio import artifacts, tool
from ejecucion import execute_program


@tool
def ejecutar_codigo(code: str) -> str:
    """Analiza archivos completos con Python. Usa pandas y print para consultar datos;
    read_text(ruta) para documentación y save_html(nombre, contenido) para un informe.
    Cada llamada empieza de nuevo. No hay Internet. Hasta 6.000 caracteres por programa.
    """
    try:
        output, generated = execute_program(code)
        if generated:
            return artifacts(*[item["path"] for item in generated], message=output)
        return output
    except Exception as error:
        return "ERROR DE EJECUCIÓN: " + str(error) + ". Revisa el programa antes de concluir."

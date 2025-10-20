import csv

def generar_reporte_clientes():
    clientes = [
        {"nombre": "Juan Pérez", "edad": 45, "plan": "Salud Total", "prima": 250.0},
        {"nombre": "María López", "edad": 30, "plan": "Salud Plus", "prima": 180.0},
        {"nombre": "Carlos Díaz", "edad": 52, "plan": "Salud Familiar", "prima": 300.0},
    ]

    ###Calcular total y promedio###
    total_prima = sum(c["prima"] for c in clientes)
    promedio_prima = total_prima / len(clientes)

    ###Mostrar reporte###
    print("=== Reporte de Clientes de Salud Mapfre ===")
    for c in clientes:
        print(f"{c['nombre']} | {c['plan']} | Edad: {c['edad']} | Prima: ${c['prima']}")
    print("===========================================")
    print(f"Total de clientes: {len(clientes)}")
    print(f"Promedio de prima: ${promedio_prima:.2f}")

if __name__ == "__main__":
    generar_reporte_clientes()

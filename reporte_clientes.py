import csv
from datetime import datetime
def generar_reporte():
    clientes = []
    with open("clientes.csv", newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            clientes.append(row)
    total_clientes = len(clientes)
    total_monto = sum(float(c["Monto"]) for c in clientes)
    promedio_edad = sum(int(c["Edad"]) for c in clientes) / total_clientes
    with open("reporte.txt", "w", encoding="utf-8") as f:
        f.write(f"📊 Reporte de Clientes - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total de clientes: {total_clientes}\n")
        f.write(f"Promedio de edad: {promedio_edad:.1f}\n")
        f.write(f"Monto mensual total: S/. {total_monto:.2f}\n")
    print("✅ Reporte generado con éxito.")
if __name__ == "__main__":
    generar_reporte()

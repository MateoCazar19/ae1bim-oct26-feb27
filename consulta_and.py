from sqlalchemy import and_
from configuracion import SessionLocal
from crear_base_entidades import HistoriaClinica


def main():
    db = SessionLocal()
    try:
        historias = (
            db.query(HistoriaClinica)
            .filter(
                and_(
                    HistoriaClinica.veterinario_id == 1,
                    HistoriaClinica.diagnostico_principal.ilike("%itis%"),
                )
            )
            .all()
        )

        print("Historias clínicas del veterinario 1 con diagnóstico que contiene 'itis':")
        for h in historias:
            print(
                f"- Mascota: {h.nombre_mascota} | Diagnóstico: {h.diagnostico_principal} | "
                f"Tratamiento: {h.tratamiento_prescrito}"
            )
    finally:
        db.close()


if __name__ == "__main__":
    main()

from configuracion import SessionLocal
from crear_base_entidades import HistoriaClinica


def main():
    db = SessionLocal()
    try:
        historias = (
            db.query(HistoriaClinica)
            .order_by(HistoriaClinica.fecha_atencion.desc())
            .all()
        )

        print("Historias clínicas ordenadas por fecha de atención (descendente):")
        for h in historias:
            print(
                f"- {h.fecha_atencion} | Mascota: {h.nombre_mascota} | "
                f"Diagnóstico: {h.diagnostico_principal}"
            )
    finally:
        db.close()


if __name__ == "__main__":
    main()

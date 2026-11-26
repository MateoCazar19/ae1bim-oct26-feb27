from configuracion import SessionLocal
from crear_base_entidades import Consultorio


def main():
    db = SessionLocal()
    try:
        consultorios = (
            db.query(Consultorio)
            .filter(Consultorio.especialidad_principal == "Medicina General")
            .all()
        )

        print("Consultorios de Medicina General:")
        for c in consultorios:
            print(
                f"- ID: {c.id} | {c.nombre_numero} | "
                f"Especialidad: {c.especialidad_principal} | Clínica ID: {c.clinica_id}"
            )
    finally:
        db.close()


if __name__ == "__main__":
    main()

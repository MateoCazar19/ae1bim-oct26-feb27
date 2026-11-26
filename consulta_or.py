from sqlalchemy import or_
from configuracion import SessionLocal
from crear_base_entidades import Veterinario


def main():
    db = SessionLocal()
    try:
        veterinarios = (
            db.query(Veterinario)
            .filter(
                or_(
                    Veterinario.numero_licencia.like("VET-AZ-%"),
                    Veterinario.numero_licencia.like("VET-GU-%"),
                )
            )
            .all()
        )

        print("Veterinarios con licencia VET-AZ o VET-GU:")
        for v in veterinarios:
            print(
                f"- {v.nombres_apellidos} | Licencia: {v.numero_licencia} | "
                f"Correo: {v.correo_electronico}"
            )
    finally:
        db.close()


if __name__ == "__main__":
    main()

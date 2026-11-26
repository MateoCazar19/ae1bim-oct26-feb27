from configuracion import SessionLocal
from crear_base_entidades import Clinica


def main():
    db = SessionLocal()
    try:
        clinicas = db.query(Clinica).all()

        print("Clínicas y cantidad de Historias Clínicas asociadas:")
        for clinica in clinicas:
            total_historias = sum(
                len(veterinario.historias_clinicas)
                for consultorio in clinica.consultorios
                for veterinario in consultorio.veterinarios
            )
            print(
                f"- {clinica.nombre_comercial} ({clinica.direccion}): "
                f"{total_historias} historia(s) clínica(s)"
            )
    finally:
        db.close()


if __name__ == "__main__":
    main()

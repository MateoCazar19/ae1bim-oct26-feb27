import datetime
from configuracion import SessionLocal
from crear_base_entidades import (
    Clinica,
    Consultorio,
    HistoriaClinica,
    Veterinario,
    crear_tablas,
)


def poblar():
    crear_tablas()
    db = SessionLocal()

    try:
        if db.query(Clinica).count() > 0:
            print("La base de datos ya contiene registros. No se insertaron duplicados.")
            return

        # 1. Clínicas
        clinica_norte = Clinica(
            nombre_comercial="VetCare Norte",
            direccion="Av. Remigio Crespo 450, Cuenca",
            veterinario_responsable="Dra. Valeria Andrade",
        )
        clinica_sur = Clinica(
            nombre_comercial="Clínica Animal Sur",
            direccion="Av. 24 de Mayo 1280, Quito",
            veterinario_responsable="Dr. Andrés Villavicencio",
        )
        clinica_costa = Clinica(
            nombre_comercial="Salud Canina & Felina",
            direccion="Cdla. Kennedy Norte Mz. 14, Guayaquil",
            veterinario_responsable="Dra. Camila Paredes",
        )
        db.add_all([clinica_norte, clinica_sur, clinica_costa])
        db.flush()

        # 2. Consultorios
        cons_1 = Consultorio(
            nombre_numero="Consultorio 101",
            especialidad_principal="Medicina General",
            clinica_id=clinica_norte.id,
        )
        cons_2 = Consultorio(
            nombre_numero="Consultorio 102",
            especialidad_principal="Dermatología",
            clinica_id=clinica_norte.id,
        )
        cons_3 = Consultorio(
            nombre_numero="Consultorio A",
            especialidad_principal="Cirugía",
            clinica_id=clinica_sur.id,
        )
        cons_4 = Consultorio(
            nombre_numero="Consultorio B",
            especialidad_principal="Medicina General",
            clinica_id=clinica_costa.id,
        )
        db.add_all([cons_1, cons_2, cons_3, cons_4])
        db.flush()

        # 3. Veterinarios
        vet_1 = Veterinario(
            nombres_apellidos="Valeria Andrade",
            correo_electronico="v.andrade@vetcare.ec",
            numero_licencia="VET-AZ-1042",
            consultorio_id=cons_1.id,
        )
        vet_2 = Veterinario(
            nombres_apellidos="Mateo Salgado",
            correo_electronico="m.salgado@vetcare.ec",
            numero_licencia="VET-AZ-2089",
            consultorio_id=cons_2.id,
        )
        vet_3 = Veterinario(
            nombres_apellidos="Andrés Villavicencio",
            correo_electronico="a.villavicencio@animalsur.ec",
            numero_licencia="VET-PI-3015",
            consultorio_id=cons_3.id,
        )
        vet_4 = Veterinario(
            nombres_apellidos="Camila Paredes",
            correo_electronico="c.paredes@saludcf.ec",
            numero_licencia="VET-GU-4091",
            consultorio_id=cons_4.id,
        )
        db.add_all([vet_1, vet_2, vet_3, vet_4])
        db.flush()

        # 4. Historias Clínicas
        historias = [
            HistoriaClinica(
                fecha_atencion=datetime.date(2026, 10, 12),
                diagnostico_principal="Gastroenteritis leve",
                tratamiento_prescrito="Dieta blanda 5 días y probióticos",
                nombre_mascota="Rocky",
                veterinario_id=vet_1.id,
            ),
            HistoriaClinica(
                fecha_atencion=datetime.date(2026, 10, 18),
                diagnostico_principal="Vacunación anual y desparasitación",
                tratamiento_prescrito="Refuerzo múltiple canino y antiparasitario oral",
                nombre_mascota="Luna",
                veterinario_id=vet_1.id,
            ),
            HistoriaClinica(
                fecha_atencion=datetime.date(2026, 10, 22),
                diagnostico_principal="Dermatitis alérgica por pulgas",
                tratamiento_prescrito="Shampoo medicado y control ambiental",
                nombre_mascota="Milo",
                veterinario_id=vet_2.id,
            ),
            HistoriaClinica(
                fecha_atencion=datetime.date(2026, 11, 2),
                diagnostico_principal="Profilaxis dental",
                tratamiento_prescrito="Limpieza ultrasónica y antibioticoterapia preventiva",
                nombre_mascota="Toby",
                veterinario_id=vet_3.id,
            ),
            HistoriaClinica(
                fecha_atencion=datetime.date(2026, 11, 10),
                diagnostico_principal="Otitis externa unilateral",
                tratamiento_prescrito="Limpieza ótica y gotas antibióticas por 7 días",
                nombre_mascota="Nala",
                veterinario_id=vet_1.id,
            ),
        ]
        db.add_all(historias)
        db.commit()
        print("Base de datos poblada con éxito.")
    except Exception as e:
        db.rollback()
        print(f"Error al poblar la base de datos: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    poblar()

import datetime
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

from configuracion import engine

Base = declarative_base()


class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_comercial = Column(String(120), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(120), nullable=False)

    consultorios = relationship(
        "Consultorio",
        back_populates="clinica",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Clinica(id={self.id}, nombre='{self.nombre_comercial}')>"


class Consultorio(Base):
    __tablename__ = "consultorios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_numero = Column(String(60), nullable=False)
    especialidad_principal = Column(String(80), nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinicas.id"), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship(
        "Veterinario",
        back_populates="consultorio",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return (
            f"<Consultorio(id={self.id}, nombre_numero='{self.nombre_numero}', "
            f"especialidad='{self.especialidad_principal}')>"
        )


class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres_apellidos = Column(String(120), nullable=False)
    correo_electronico = Column(String(120), nullable=False, unique=True)
    numero_licencia = Column(String(50), nullable=False, unique=True)
    consultorio_id = Column(Integer, ForeignKey("consultorios.id"), nullable=False)

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias_clinicas = relationship(
        "HistoriaClinica",
        back_populates="veterinario",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return (
            f"<Veterinario(id={self.id}, nombre='{self.nombres_apellidos}', "
            f"licencia='{self.numero_licencia}')>"
        )


class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_atencion = Column(Date, nullable=False, default=datetime.date.today)
    diagnostico_principal = Column(String(250), nullable=False)
    tratamiento_prescrito = Column(String(300), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)
    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"), nullable=False)

    veterinario = relationship("Veterinario", back_populates="historias_clinicas")

    def __repr__(self):
        return (
            f"<HistoriaClinica(id={self.id}, mascota='{self.nombre_mascota}', "
            f"fecha={self.fecha_atencion})>"
        )


def crear_tablas():
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente en SQLite.")


if __name__ == "__main__":
    crear_tablas()

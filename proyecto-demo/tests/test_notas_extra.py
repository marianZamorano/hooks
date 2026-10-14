"""Pruebas adicionales de las reglas de negocio."""
import unittest

import notas

ESTUDIANTES = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Luis", "nota": 51},
    {"nombre": "Sofia", "nota": 40},
    {"nombre": "Diego", "nota": 72},
]


class TestExtra(unittest.TestCase):
    def test_promedio_con_decimales(self):
        self.assertAlmostEqual(notas.calcular_promedio([50, 51]), 50.5)

    def test_nota_final_cero(self):
        self.assertAlmostEqual(notas.nota_final(0, 0, 0, 0), 0)

    def test_examen_final_pesa_40(self):
        self.assertAlmostEqual(notas.nota_final(0, 0, 100, 0), 40)

    def test_ranking_por_defecto_trae_tres(self):
        nombres = [e["nombre"] for e in notas.mejores_estudiantes(ESTUDIANTES)]
        self.assertEqual(nombres, ["Ana", "Diego", "Luis"])

    def test_buscar_inexistente(self):
        db = notas.crear_base_demo()
        self.assertEqual(notas.buscar_estudiante(db, "Pedro"), [])


if __name__ == "__main__":
    unittest.main()

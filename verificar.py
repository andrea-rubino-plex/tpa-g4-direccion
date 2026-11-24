#!/usr/bin/env python3
"""Verifica que cierre_propuesta.csv no rompa algunas reglas duras. Uso: python3 verificar.py [archivo.csv]
El archivo debe tener las columnas: proyecto_id, decision (cerrar, mantener o pendiente), receptor_id, regla_aplicada."""
import csv, sys
per = {r["persona_id"]: r for r in csv.DictReader(open("datos/personas.csv"))}
proy = {r["proyecto_id"]: r for r in csv.DictReader(open("datos/proyectos.csv"))}
pend = list(csv.DictReader(open("datos/pendientes.csv")))
ruta = sys.argv[1] if len(sys.argv) > 1 else "cierre_propuesta.csv"
try: filas = list(csv.DictReader(open(ruta)))
except FileNotFoundError: sys.exit(f"No encuentro {ruta}: crea la propuesta primero.")
if any(None in f or None in f.values() or "<<<<<<<" in (f.get("proyecto_id") or "") for f in filas) or filas and not {"proyecto_id", "decision", "receptor_id"} <= set(filas[0]):
    sys.exit(f"{ruta} está mal formado (¿marcas de conflicto «<<<<<<<» o faltan columnas?): arréglalo y vuelve a correr.")
errores = []
vistos = {f["proyecto_id"] for f in filas}
for p in proy:
    if p not in vistos: errores.append(f"{p}: no aparece en la propuesta")
for f in filas:
    p, d, r = f["proyecto_id"], (f["decision"] or "").strip().lower(), (f["receptor_id"] or "").strip()
    if p not in proy: errores.append(f"{p}: no es un proyecto del portafolio"); continue
    if d not in ("cerrar", "mantener", "pendiente"): errores.append(f"{p}: la decisión «{d}» no es válida"); continue
    if not f.get("regla_aplicada", "").strip(): errores.append(f"{p}: regla 10, falta la regla aplicada")
    if d != "cerrar": continue
    if any(x["proyecto_id"] == p and x["prioridad"] == "alta" and x["estado"] == "abierto" for x in pend):
        errores.append(f"{p}: regla 3, tiene un pendiente de prioridad alta abierto")
    if not r: errores.append(f"{p}: regla 4, se cierra sin receptor"); continue
    if r not in per: errores.append(f"{p}: el receptor {r} no existe"); continue
    if per[r]["estado"] == "licencia": errores.append(f"{p}: regla 4, el receptor {r} está de licencia")
print(f"{len(filas)} filas revisadas, {len(errores)} problemas")
for x in errores: print(" -", x)
sys.exit(1 if errores else 0)

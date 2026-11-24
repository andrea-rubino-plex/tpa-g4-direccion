# Guía del grupo 4 Dirección y planificación: cierre y traspaso de proyectos

Su proyecto: decidir qué hacer con los 14 proyectos de `datos/proyectos.csv` antes de fin de año (cerrar y traspasar, mantener o dejar pendiente), con reglas que el equipo acuerda y que Claude aplica. Los pendientes son los de Jira (`pendientes.csv`) y la carpeta de Drive de cada proyecto es `carpeta_drive.csv`. Hay casos difíciles a propósito.

**Hoy cada persona hará los tres roles, uno por fase.** En una fase todos tienen el mismo rol y trabajan a la vez, sin esperar a nadie. Quien dicta avisa «cambio de fase».

| Minutos | Fase |
|---|---|
| 0 a 6 | Tu espacio |
| 6 a 14 | Calentamiento: poda el CLAUDE.md |
| 14 a 27 | **Fase 1: autores** |
| 27 a 37 | **Fase 2: revisores** |
| 37 a 53 | **Fase 3: dueños** |
| 53 a 55 | Cierre |

## Tu espacio (6 minutos si ya está listo, 8 a 10 si no)
Los pasos 1 a 3 bloquean todo lo demás. **Háganlos antes del taller** y en el taller solo queda el paso 4. Si no los hicieron, tomen 8 a 10 minutos y acorten el calentamiento a la mitad.
1. **Una persona del grupo** pulsa **Use this template → Create a new repository**, ponle el nombre de tu grupo y déjalo **público**. En Settings → Collaborators invita a las demás. Esa persona es la dueña del repositorio.
2. **Cada colaboradora acepta la invitación**, desde el correo o desde el enlace `github.com/<dueña>/<repo>/invitations`. Sin aceptarla, no puede abrir ramas ni pull requests.
3. **La dueña instala la app de Claude para GitHub en ese repositorio**, desde `claude.ai/code` o desde Settings → Integrations. Después, **cada persona conecta su cuenta de GitHub** en `claude.ai/code`.
4. **Todas** abren el repositorio en `claude.ai/code` y piden: *«Lee este proyecto y dime en cinco líneas qué problema resuelve, qué archivos hay y qué reglas debo respetar.»*

**Plan B, si a alguien no le funciona GitHub en 6 minutos.** Quien dicta tiene dos salidas y te dice cuál usar:
- **Un repositorio ya creado** por quien dicta, con tu usuario de GitHub invitado de antemano. Aceptas la invitación y sigues la guía igual.
- **Una carpeta de Drive** compartida con tu grupo, con los mismos archivos. No hay ramas ni pull requests, así que se hace así:
  1. Copia `reglas.md` y nómbrala `reglas - A.md`, con tu inicial (la copia es tu rama).
  2. Pide a Claude lo mismo de la fase 1, pero que guarde la propuesta como `propuesta - A.csv`.
  3. En la fase 2, la persona que te toca escribe su revisión en un archivo `revisión de A - B.md` con el veredicto.
  4. En la fase 3, el grupo abre las propuestas juntas, elige una y le pide a Claude: *«Compara estos archivos, explícame qué cambió cada uno y propón cómo unirlos. No apliques nada hasta que yo elija.»* El Merge y el comentario de GitHub no existen: quien dicta decide quién copia la versión elegida sobre `reglas.md`.
  
  Solo se leen los `.md` y `.csv` reales. Los Docs y Sheets nativos no los lee Claude desde la carpeta.

## Calentamiento: poda el CLAUDE.md (8 minutos)
Cada persona, por su lado, pide: *«Dime qué de este archivo puedes deducir del código y las carpetas, y propón la versión más resumida posible, con solo lo que una sesión nueva, sin memoria, necesita saber. No modifiques el archivo.»*
Comparen en el grupo: ¿qué reglas conservó cada versión? Las que nadie puede deducir (quién aprueba, la regla sin excepciones, los datos permitidos, la rama y el pull request) tienen que estar.

## Fase 1: Autores (13 minutos)
Las reglas 1 y 2 chocan: el plazo y la ficha completa no pueden ir primero las dos. **Cada persona elige una opción distinta**, la resuelve en su propia rama y abre su propio pull request:
- **Opción 1, plazo primero:** todo proyecto vencido se cierra este trimestre, y lo que falta pasa como pendiente al receptor, con nombre y fecha.
- **Opción 2, ficha primero:** no se cierra nada hasta que su ficha esté completa, y lo vencido se mantiene con una fecha nueva.
- **Opción 3, riesgo primero:** se cierran ahora solo los proyectos de riesgo bajo (sin pendientes altos, sin sobregasto, con documentos). Los demás quedan con un plan de cierre fechado.
- **Opción 4, la tuya:** define la prioridad que te parezca mejor y explícala.

En grupos de dos usen las opciones 1 y 2, de tres, la 1, 2 y 3, y de cuatro, todas.

Pide: *«Crea una rama, cambia las reglas 1 y 2 de reglas.md para que [tu opción], decide qué hacer con cada proyecto de datos/proyectos.csv en cierre_propuesta.csv con las columnas proyecto_id, decision (cerrar, mantener o pendiente), receptor_id y regla_aplicada, corre verificar.py, haz commit con un mensaje que diga qué cambió y por qué, y abre un pull request. En el texto del pull request declara tus supuestos (qué umbral usaste para «sin actividad hace mucho tiempo», qué hiciste con los proyectos que te parezcan repetidos) y lista los casos que no pudiste resolver con las reglas.»*

Si terminas antes, mira qué proyectos quedaron pendientes y por qué.

## Fase 2: Revisores (10 minutos)
Cada persona revisa el pull request de **otra**, en círculo: la primera revisa a la segunda, la segunda a la tercera, la última a la primera. En grupos de dos, se intercambian. Si el pull request que te toca no llegó, revisa `ejemplo-para-revisar/`.

Pide: *«Lee este pull request y dime si cambia solo lo que se pidió, si hay información que no debería estar y si se entiende sin quien lo escribió. Corre verificar.py y dime qué problemas hay, incluso los que el verificador no detecta. Deja tu revisión como comentario del pull request, con un veredicto: aprobar, pedir cambios o no aprobar.»*

Revisa también con `REVIEW.md`, que ahora tiene seis puntos. Pasar el verificador no basta.

## Fase 3: Dueños (16 minutos, todos juntos)
Ahora el grupo decide como dueño del repositorio. En grupos de dos, si hay empate, decide quien dicta o la dueña del repositorio.

**Antes de votar (1 minuto, sin Claude).** Cada dueño escribe en el chat dos números: *«problemas que dio verificar.py: N»* y *«problemas que encontró mi revisor: M»*. Comparen. Luego votan el pull request a aceptar: gana el que dejó menos problemas sin resolver.

1. **Aceptar (2 minutos).** Lean las revisiones y acepten el pull request que ganó con el botón **Merge** de GitHub: aceptar lo hace una persona.
2. **Un conflicto (6 minutos).** Los demás pull requests chocan ahora con `main`. Abran uno en `claude.ai/code` y pidan: *«Explícame qué cambió cada rama y propón cómo unirlas. No apliques nada hasta que yo elija.»* Decidan como grupo y digan: *«Elijo la opción … y completa el merge con su commit. Corre verificar.py.»* Resuelvan solo uno. Lo que quede se anota como decisión pendiente para el jefe de planificación. **No recarguen la página ni abran una sesión nueva durante el conflicto:** «Elijo la opción …» solo funciona en la misma sesión.
3. **Traspaso (7 minutos).** Pidan: *«Escribe traspaso.md con las seis preguntas a partir de lo que hicimos hoy, en una rama nueva. Haz commit, abre un pull request y deja el enlace. Al final marca cuál de las seis costó más responder y cuál no se pudo responder con lo que hay en el repositorio.»*
   Mientras Claude escribe, repártanse las seis preguntas y llenen a mano, bajo cada una, **«Evidencia en el repositorio»** y **«Decisión del grupo»** (30 segundos por pregunta). Cada pregunta necesita un enlace a un archivo, un pull request o una línea de `datos/`. Si no hay, escriban «no hay».
   Pruébenlo: *«Abre una sesión nueva sobre la rama del traspaso, o haz Merge primero y ábrela sobre main.»* Ahí pidan: *«Lee CLAUDE.md y traspaso.md y dime cuál es el siguiente paso y qué no debo tocar.»*

Si sobra tiempo, fuera del reparto: *«Completa proyecto.md con el problema y para quién es. Para «cómo se mide», propón una métrica que se pueda calcular con datos/, calcula su valor de hoy y propón una meta. Pregúntame lo que falte.»*

## Cierre (2 minutos)
Peguen en el chat el enlace de su repositorio y dos frases:
- La decisión que le llevarían al jefe de planificación.
- «La pregunta que nos quedó sin respuesta es…», y dicen cuál de las seis: responsabilidad, acceso, coordinación, calidad, visibilidad o riesgo.

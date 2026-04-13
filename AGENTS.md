# AGENTS.md — awesome-nafarroa

## Propósito

Selección de software open source que da **soporte específico a Navarra / Nafarroa** — su gobierno foral, ayuntamientos, universidades, empresas, infraestructuras y patrimonio. Todo el contenido en español. El foco es la Comunidad Foral de Navarra: el software debe dirigirse específicamente a esta comunidad foral o a sus municipios.

## Ámbito

- **1 provincia** (Navarra es comunidad foral uniprovincial).
- Principales ciudades: Pamplona / Iruña (capital), Tudela, Barañáin, Burlada / Burlata, Estella-Lizarra, Tafalla, Zizur Mayor / Zizur Nagusia.
- **Universidades**: UPNA / NUP (Universidad Pública de Navarra), UNAV (Universidad de Navarra).
- **Instituciones**: Gobierno de Navarra / Nafarroako Gobernua, NASTAT (Instituto de Estadística de Navarra), Tracasa (Trabajos Catastrales de Navarra), SODENA (Sociedad de Desarrollo de Navarra), SITNA (Sistema de Información Territorial de Navarra), Parlamento de Navarra / Nafarroako Parlamentua.

## Criterios de inclusión

### Incluir

- Software que interactúa con el **Gobierno de Navarra** o sus organismos (Sede Electrónica, Portal de Transparencia, datos abiertos, gobierno abierto).
- Herramientas para **ayuntamientos** de Navarra.
- Software de **universidades navarras** (UPNA, UNAV) cuando sea específico de la región o la universidad.
- Herramientas de **datos abiertos** de Navarra (gobiernoabierto.navarra.es, NASTAT).
- Software relacionado con el **SITNA** (Sistema de Información Territorial de Navarra) y cartografía foral.
- Herramientas del **Catastro de Navarra** (catastro propio, distinto del estatal).
- Software de **transporte** navarro (Villavesa/TCC, bus comarcal, Renfe cercanías Pamplona).
- Herramientas de **cartografía y SIG** específicas de Navarra (SITNA, IDENA, Tracasa).
- Software sobre **cultura y patrimonio** navarro (Camino de Santiago por Navarra, megalitos, patrimonio industrial).
- Herramientas de **turismo** de la región.
- Software de **medio ambiente** regional (Bardenas Reales, Señorío de Bertiz, Selva de Irati).
- Software sobre **deportes** navarros (CA Osasuna, Xota FS).
- Proyectos del **sistema sanitario navarro** (Servicio Navarro de Salud - Osasunbidea).
- Herramientas de **meteorología** y clima regional.
- Proyectos de **euskera** y herramientas lingüísticas específicas de la zona vascófona de Navarra.
- Proyectos de **San Fermín / Sanfermines** y fiestas.

### No incluir

- Software **genérico** que funciona en toda España sin funcionalidad específica de Navarra — eso pertenece a awesome-spain.
- Software de **ámbito europeo** — eso pertenece a awesome-europe.
- Software de **otras comunidades autónomas** españolas.
- Software creado por navarros que **no tiene funcionalidad específica** de la región.
- Repositorios **archivados o de solo lectura** — van a `DELETED.md`.
- Repos donde el autor indica que el proyecto está **roto, sin mantenimiento o deprecado**.
- Repos **sin README significativo** o que son claramente repos de test/experimento.
- Ejercicios de clase o trabajos académicos sin utilidad real.
- Cursos genéricos impartidos en universidades navarras (Python, ML, etc.) sin datos específicos de Navarra.

### Zona gris — usar criterio

- Proyectos de universidades navarras que podrían ser genéricos — incluir si tienen datos o configuración específica de Navarra.
- Software que cubre Navarra junto con otras regiones — incluir si Navarra es un foco principal.
- Software en euskera que no es exclusivo de Navarra — incluir solo si tiene un vínculo claro con la zona vascófona de Navarra.

## Estándares de calidad

**Mismo listón que [awesome-spain](https://github.com/GeiserX/awesome-spain):**

- **No repos archivados**: si se descubre archivado tras la inclusión, mover a `DELETED.md` inmediatamente.
- **No repos extremadamente sin mantenimiento**: al menos un commit en los últimos 3 años, salvo que sea un proyecto claramente estable/completo.
- **No repos rotos**: si el README dice «deprecated», «no longer maintained», «use X instead» o similar — no incluir. Mover a `DELETED.md` si ya está listado.
- **Estrellas mínimas**: preferir repos con al menos unas pocas estrellas, pero herramientas nicho excepcionales con 0-1 estrellas pueden incluirse si cubren un hueco importante.
- **Verificar cada repo** antes de añadir: comprobar `archived`, `pushed_at`, `stargazers_count` vía `gh api repos/owner/name`.

## Formato de entrada

```markdown
- [Nombre](https://github.com/owner/repo) [![Stars](...)](stargazers) [![Last Commit](...)](commits) [![Language](...)](repo) [![License](...)](LICENSE) [![Tag](...)](url) - Descripción que empieza en mayúscula y termina con punto.
```

Las insignias se generan automáticamente con `scripts/transform-readme.py`. Para contribuir, basta con añadir la entrada en formato simple:

```markdown
- [Nombre](https://github.com/owner/repo) - Descripción que empieza en mayúscula y termina con punto.
```

- La descripción **no debe empezar con el nombre** del proyecto.
- Máximo una línea por entrada.
- Validar con awesome-lint-extra: `python3 lint.py` o mediante el workflow de CI.
- Entradas en **orden alfabético** dentro de cada categoría.
- Categorías en **orden alfabético** en el índice y en el cuerpo del documento.
- Entradas en `DELETED.md` también en **orden alfabético** dentro de cada sección.

## Verificación antes de añadir

Antes de incluir un repositorio, comprobar:

- **Existe y es público**: el enlace de GitHub funciona y el repo no es privado.
- **No está archivado o de solo lectura**: si archivado, va a `DELETED.md` (sección «Archivados»).
- **No está deprecado**: comprobar si el README dice «deprecated», «unmaintained», «broken», «use X instead».
- **Actividad razonable**: al menos un commit en los últimos 3 años, salvo que sea un proyecto estable/completo.
- **No es un duplicado**: cruzar con `README.md` y `DELETED.md`.
- **Calidad mínima**: tiene documentación (README) y no es un repositorio vacío o de test.

## Pull requests y contribuciones

- Las PRs deben usar la plantilla en `.github/PULL_REQUEST_TEMPLATE.md`.
- **Obligatorio**: incluir en la PR la **URL del servicio, API o institución navarra** a la que el software da soporte.
- Plantillas de issues disponibles para sugerir proyectos (`anadir-proyecto.md`) y solicitar retirada (`retirar-proyecto.md`).

## Estructura

- Secciones con `##`, subsecciones con `###`.
- Índice de contenido al principio entre comentarios `<!--lint disable/enable awesome-list-item-->`.
- Al final: sección Contribuir, Nota y Descargo de responsabilidad (como párrafos en negrita, no encabezados ##).

## Temas prohibidos

No se aceptan proyectos relacionados con: pornografía, contenido NSFW, loterías o apuestas, religión, política partidista.

## Difusión

- Notificar a los propietarios de repos abriendo un issue titulado «Listado en awesome-nafarroa» con un breve mensaje en español (tuteo) ofreciendo retirar si lo prefieren. Solo 1 issue por organización/usuario — no spamear repos del mismo propietario.
- Publicar en comunidades navarras (Reddit, foros de la UPNA, Telegram de devs navarros) tras alcanzar masa crítica.
- Enviar PR a [sindresorhus/awesome](https://github.com/sindresorhus/awesome) tras 30 días desde la creación del repo.

## Aprendizajes

- Las búsquedas en GitHub con `"navarra"` devuelven muchos falsos positivos (equipos de fútbol/basket con "Navarra" en nombre, repos de Cartagena de Indias, etc.). Filtrar siempre.
- Navarra tiene catastro propio (distinto del estatal), lo que genera repos específicos como CatastRoNav y navarra_cadastre.
- SITNA (sitna.navarra.es) es la principal infraestructura de datos espaciales de Navarra con organización GitHub `sitna`.
- `JaimeObregon/metanavarra` (27 estrellas, transparencia del Gobierno de Navarra) está archivado — en DELETED.md.
- La UPNA y la UNAV no tienen presencia significativa en GitHub con repos específicos de Navarra.
- Tracasa (Trabajos Catastrales de Navarra) no tiene organización pública en GitHub.
- NASTAT (Instituto de Estadística de Navarra) no tiene presencia en GitHub.
- Los cursos genéricos impartidos en TECNUN (UNAV) no se incluyen por ser contenido genérico.
- Civio tiene `presupuesto-navarra` como adaptación de su herramienta DVMI.
- SCN Gorosti tiene `guillermodean/Megalitos` para divulgación de estaciones megalíticas.
- Los repos de COVID-19 en Navarra (javikalsan, antonio-remirez, Ninjalice) tienen actividad antigua pero datos específicos; solo incluido javikalsan por tener ETL reproducible.

*Generated by [LynxPrompt](https://lynxprompt.com) CLI*

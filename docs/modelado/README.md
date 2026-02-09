
# Explicacion
---

## ¿Qué resuelve el sistema?

El sistema organiza información estructurada sobre videojuegos y permite la generación de artículos relacionado con ellos.
---


## Por qué esas entidades, relaciones y reglas

### Developer, Publisher, Genre
- Se modelaron como entidades independientes porque:
- Un desarrollador puede trabajar en muchos juegos.
- Un publisher puede publicar muchos juegos.
- Un género puede clasificar muchos juegos.
- Y un juego puede tener varios de cada uno.
- Por eso se modelaron como relaciones muchos a muchos (N:N).

### Tablas intermedias (GameDeveloper, GamePublisher, GameGenre)
Se crearon porque:
- Las relaciones N:N necesitan resolverse en el modelo relacional.
- Además, estas relaciones tienen atributos propios.

### User y Article
Se modeló como relación 1:N porque:
- Un usuario puede escribir muchos artículos.
- Cada artículo pertenece a un solo usuario.
- Cada artículo está relacionado con un solo juego.

### Regla de integridad
Un juego solo puede tener un género primario. Esto garantiza coherencia en la clasificación y demuestra control de reglas de negocio.
---

## Supuestos
Cada artículo trata sobre un solo juego.
- Un artículo tiene un solo autor.
- Un juego puede tener múltiples desarrolladores y publishers.
- Un juego puede tener varios géneros, pero solo uno principal.
- Los timestamps en entidades principales permiten auditoría del sistema.
- No se modelan plataformas, reviews numéricas ni comentarios para mantener el alcance controlado.

# Prueba técnica Evolta





## Roadmap

- Obtener el ultimo comentarios de cada prospecto (parámetro de entrada: idprospecto)
- Obtener los 5 primeras acciones de cada prospecto (parámetro de entrada: idprospecto)
- Registrar un nuevo evento de un prospecto.
- Actualizar el comentario de un prospecto (parámetro de entrada: idprospecto)
- Cargar un CSV de 2500 comentarios masivamente de 2500 prospectos diferentes.


## API Reference


#### Obtener el ultimo comentarios de cada prospecto (parámetro de entrada: idprospecto)

```http
  GET /api/comment?idprospecto=${idprospecto}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `idprospecto` | `string` | **Required**. Id of item to fetch|

#### Obtener los 5 primeras acciones de cada prospecto (parámetro de entrada: idprospecto)

```http
  GET /api/event?idprospecto=${idprospecto}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `idprospecto`      | `string` | **Required**. Id of item to fetch |


---

#### Registrar un nuevo evento de un prospecto.

```http
  POST /api/event
```


## Body example

```json
{
    "columna1": "123456",
    "columna2":"blabla",
    "columna3":"blabla",
    "columna4":"blabla",
    "columna5":"7",
    "columna6":"blabla",
    "columna7":"blabla",
    "columna8":"blabla",
    "columna9":"654321",
    "columna10":"blabla",
    "columna11":"blabla",
    "columna12":"blabla",
    "columna13":"blabla",
    "columna14":"blabla",
    "columna15":"blabla",
    "columna16":"blabla",
    "columna17":"blabla",
    "columna18":"blabla",
    "columna19":"blabla",
    "columna20":"blabla",
    "columna21":"blabla",
    "columna22":"blabla",
    "columna23":"100",
    "columna24":"blabla",
    "columna25":"blabla",
    "columna26":"blabla",
    "columna27":"blabla"
}
```

---

#### Actualizar el comentario de un prospecto (parámetro de entrada: idprospecto)

```http
  PUT /api/comment
```

## Body example

```json
{
    "idprospecto": "439730",
    "comment":"comentario nuevo"    
}
```

---
#### Cargar un CSV de 2500 comentarios masivamente de 2500 prospectos diferentes.

```http
  POST /api/comment
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `file`      | `media` | **Required**. file *.csv  |
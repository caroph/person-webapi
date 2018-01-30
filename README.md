# person-webapi

Um projeto para testes de webapi com python e flask.  
Ainda em desenvolvimento ...

### GET /persons/
- Retorno:
```
[
    {
        "age": 15,
        "id": 1,
        "name": "Pessoa 1"
    },
    {
        "age": 30,
        "id": 2,
        "name": "Pessoa 2"
    },
    {
        "age": 22,
        "id": 3,
        "name": "Pessoa 3"
    }
]
```

### GET /persons/1
- Retorno
```
{
    "age": 22,
    "id": 1,
    "name": "Pessoa 1"
}
```

### POST /persons/
- Envio
```
{
	"name": "Pessoa 4",
	"age": 15
}
```
- Retorno
```
{
    "mensagem": "Pessoa salva com sucesso.",
    "status": 200
}
```

### PUT/PATCH /persons/1
- Envio
```
{
	"name": "Pessoa com o nome alterado",
	"age": 15
}
```
- Retorno
```
{
    "mensagem": "Pessoa salva com sucesso.",
    "status": 200
}
```

### DELETE /persons/1
- Retorno
```
{
    "mensagem": "Pessoa excluída com sucesso",
    "status": 200
}
```

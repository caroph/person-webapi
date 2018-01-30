# person-webapi

Um projeto para testes de webapi com python e flask.  
Ainda em desenvolvimento ...

## GET /persons/
- Retorno:
```
[
    {
        "age": 15,
        "id": 1,
        "name": "Pessoa com o nome alterado"
    },
    {
        "age": 30,
        "id": 3,
        "name": "Lidia Daiane Freitas de Oliveira"
    },
    {
        "age": 22,
        "id": 4,
        "name": "Caroline Pereira Hoegen"
    },
    {
        "age": 24,
        "id": 5,
        "name": "Jéssika Pereira Hoegen"
    }
]
```

## GET /persons/1
- Retorno
```
{
    "age": 22,
    "id": 4,
    "name": "Caroline Pereira Hoegen"
}
```

## POST /persons/
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

## PUT/PATCH /persons/1
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

## DELETE /persons/1
- Retorno
```
{
    "mensagem": "Pessoa excluída com sucesso",
    "status": 200
}
```

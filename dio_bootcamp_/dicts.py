contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},
}

# Iterar sobre, assim:

for k in contatos:
    print(f'`{k}: {contatos[k]}')

# ou ( esse é o ideal e mais utilizado )
for k, v in contatos.items():
    print(f'`{k}: {v}')
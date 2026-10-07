from produto import Produto

p1 = Produto()
p1.nome = "Luva de vaqueta"
p1.quantidade = 12
p1.codigo = 546367834
p1.preco = 20.99
p1.tipo = "Luva"

p2 = Produto()
p2.nome = "óculos"
p2.quantidade = 25
p2.codigo = 55765685
p2.preco = 29.99
p2.tipo = "De Sol"

print(f"{p1.nome}: {p1.quantidade}: {p1.codigo}: {p1.preco}: {p1.tipo} un.")
print(f"{p2.nome}: {p2.quantidade}: {p2.codigo}: {p2.preco}: {p2.tipo} un.")
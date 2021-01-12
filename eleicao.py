def votacao(candidatos):
  print("Votação:")
  candidato_votado = input()
  while candidatos.get(candidato_votado) != None:
    candidatos[candidato_votado] += 1
    candidato_votado = input()
  return candidatos

def mostra_resultado(dicionario):
  for chave,valor in dicionario.items():
    print(f"{chave} com {valor} voto(s)") 

print("Pleito eleitoral:")
quantidade = int(input())
candidatos = dict()


for i in range(quantidade):
  candidato = input()
  candidatos[candidato] = 0
votacao = votacao(candidatos)
mostra_resultado(votacao)
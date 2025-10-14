# Usamos float para médias com decimais
media_aluno = float(input("Digite a média do aluno: "))

if media_aluno >= 7.0:
    print("Parabéns! Aluno Aprovado!")

elif media_aluno >= 5.0:
    print("Atenção! Aluno em Recuperação.")

else:
    print("Que pena. Aluno Reprovado.")

# Esta linha não está indentada, então executa sempre no final.
print("Fim do programa.")

texto = """A inteligência artificial é uma área da computação que permite que máquinas 
simulem a capacidade humana de aprendizado e tomada de decisão. Ela utiliza 
aprendizado de máquina, redes neurais e algoritmos para analisar grandes volumes 
de dados, identificar padrões e prever resultados. A IA está presente em diversas 
áreas, como assistentes virtuais, reconhecimento facial, sistemas de recomendação 
e até na medicina, ajudando no diagnóstico de doenças. Empresas utilizam IA para 
otimizar processos e melhorar a experiência do usuário. Com avanços constantes, a 
IA está se tornando essencial para inovação e automação em diferentes setores."""

palavras_chave = ["inteligência", "artificial", "dados", "aprendizado", "rede"]
contagens = {}  
palavras = texto.lower().split()

for palavra in palavras_chave:
    contagens[palavra] = palavras.count(palavra)

for palavra, quantidade in contagens.items():
    print(f"{palavra}: {quantidade}")
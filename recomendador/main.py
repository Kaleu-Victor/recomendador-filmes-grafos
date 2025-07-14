import networkx as nx

G = nx.Graph()


def cadastrarUsuario(grafo, nome_usuario):
    grafo.add_node(nome_usuario, tipo="usuario")


def cadastrarFilme(grafo, nome_filme):
    grafo.add_node(nome_filme, tipo="filme")


def cadastrarFilmeParaUsuario(
    grafo, nome_usuario, nome_filme):
    grafo.add_edge(nome_usuario, nome_filme)


def recomendar_filmes(
    grafo, nome_usuario):
    filmes_recomendados = set()

    filmes_usuario = set()

    for vizinho in grafo.neighbors(nome_usuario):
        if (grafo.nodes[vizinho].get("tipo") == "filme"):
            filmes_usuario.add(vizinho)

    for no in grafo.nodes:
            if (grafo.nodes[no].get("tipo") == "usuario" and no != nome_usuario):
                filmes_outro_usuario = set()

                for vizinho in grafo.neighbors(no):
                    if grafo.nodes[vizinho].get("tipo") == "filme":  
                        filmes_outro_usuario.add(vizinho)  

                for (filme) in (filmes_outro_usuario):  
                    if filme not in filmes_usuario:  
                        filmes_recomendados.add(filme)  
    return filmes_usuario, filmes_recomendados


cadastrarUsuario(G, "Ana")
cadastrarUsuario(G, "João")
cadastrarUsuario(G, "Carlos")

cadastrarFilme(G, "Carros 3")
cadastrarFilme(G, "Homem Aranha 2")
cadastrarFilme(G, "Velozes e Furiosos 5")
cadastrarFilme(G, "Bastardos Inglórios")

cadastrarFilmeParaUsuario(G, "Ana", "Carros 3")
cadastrarFilmeParaUsuario(G, "João", "Homem Aranha 2")
cadastrarFilmeParaUsuario(G, "João", "Carros 3")
cadastrarFilmeParaUsuario(G, "Carlos", "Velozes e Furiosos 5")
cadastrarFilmeParaUsuario(G, "Carlos", "Carros 3")

def mostrar_recomendacoes(grafo, nome_usuario):  
    filmes_assistidos, recomendados = recomendar_filmes(grafo, nome_usuario)

    print(f"===== Recomendação para o usuário: {nome_usuario} =====")
    
    if filmes_assistidos:
        print("Filmes que já assistiu:")
        for f in filmes_assistidos:
            print(f"{f}")
    else:
        print("Ainda não assistiu a nenhum filme.")

    if recomendados:
        print("\nFilmes recomendados para você:")
        for f in recomendados:
            print(f"{f}")
    else:
        print("\nNenhuma recomendação disponível no momento.")

    print("\n--- Relações no grafo ---")
    for no in grafo.nodes:
        tipo = grafo.nodes[no].get("tipo", "desconhecido")
        conexoes = ", ".join(grafo.neighbors(no))
        print(f"{no} ({tipo}): {conexoes}")

mostrar_recomendacoes(G, "Ana")
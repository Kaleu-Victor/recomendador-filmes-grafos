import networkx as nx  # importação da biblioteca networkx para uso do grafo

G = nx.Graph()  # criação do grafo


def cadastrarUsuario(grafo, nome_usuario):
    grafo.add_node(nome_usuario, tipo="usuario")  # função que cadastra usuário (nó)


def cadastrarFilme(grafo, nome_filme):
    grafo.add_node(nome_filme, tipo="filme")  # função que cadastra filme (nó)


def cadastrarFilmeParaUsuario(
    grafo, nome_usuario, nome_filme
):  # função que vincula filme e usuário (aresta)
    grafo.add_edge(nome_usuario, nome_filme)


def recomendar_filmes(
    grafo, nome_usuario):  # função responsável por fazer a recomendação de filmes dos usuários A e B para C
    filmes_recomendados = set()  # cria um conjunto para guardar os filmes que vamos recomendar

    filmes_usuario = set()  # cria um conjunto que guarda os filmes que o usuário já assistiu

    for vizinho in grafo.neighbors(nome_usuario):  # percorre todos os nós que estão ligados ao nó do usuário
        if (grafo.nodes[vizinho].get("tipo") == "filme"):  # garante que os nós percorridos sejam do tipo "filme"
            filmes_usuario.add(vizinho)  # adiciona o filme assistido

    for no in grafo.nodes:  # percorre todos os nós do grafo
            if (grafo.nodes[no].get("tipo") == "usuario" and no != nome_usuario): # pega todos os usuários exceto o que será recomendado
                filmes_outro_usuario = set()  # pega os filmes que esses usuarios assistiram

                for vizinho in grafo.neighbors(no):
                    if grafo.nodes[vizinho].get("tipo") == "filme":  # adiciona os filmes assistidos
                        filmes_outro_usuario.add(vizinho)  # adiciona o filme assistido

                for (filme) in (filmes_outro_usuario):  # percorre todos os filmes de todos os usuários exceto o principal
                    if filme not in filmes_usuario:  # se o usuário não tiver visto o filme
                        filmes_recomendados.add(filme)  # filme para recomendação

    return filmes_usuario, filmes_recomendados

# cadastando os usuários
cadastrarUsuario(G, "Ana")
cadastrarUsuario(G, "João")
cadastrarUsuario(G, "Carlos")

# cadastrando os filmes
cadastrarFilme(G, "Carros 3")
cadastrarFilme(G, "Homem Aranha 2")
cadastrarFilme(G, "Velozes e Furiosos 5")
cadastrarFilme(G, "Bastardos Inglórios")

# Relacionar usuários e filmes
cadastrarFilmeParaUsuario(G, "Ana", "Carros 3")
cadastrarFilmeParaUsuario(G, "João", "Homem Aranha 2")
cadastrarFilmeParaUsuario(G, "João", "Carros 3")
cadastrarFilmeParaUsuario(G, "Carlos", "Velozes e Furiosos 5")
cadastrarFilmeParaUsuario(G, "Carlos", "Carros 3")

def mostrar_recomendacoes(grafo, nome_usuario):
    filmes_assistidos, recomendados = recomendar_filmes(grafo, nome_usuario)
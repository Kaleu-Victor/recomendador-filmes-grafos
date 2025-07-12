import networkx as nx # importação da biblioteca networkx para uso do grafo

G = nx.Graph() # criação do grafo

def cadastrarUsuario(grafo, nome_usuario):
    grafo.add_node(nome_usuario, tipo = "usuario") # função que cadastra usuário (nó)


def cadastrarFilme(grafo, nome_filme):
    grafo.add_node(nome_filme, tipo = "filme") # função que cadastra filme (nó)

def cadastrarFilmeParaUsuario(grafo, nome_usuario, nome_filme): # função que vincula filme e usuário (aresta)
    grafo.add_edge(nome_usuario, nome_filme)

def recomendar_filmes(grafo, nome_usuario): # função responsável por fazer a recomendação de filmes dos usuários A e B para C
    filmes_recomendados = set() # cria um conjunto para guardar os filmes que vamos recomendar
        
    filmes_usuario = set() # cria um conjunto que guarda os filmes que o usuário já assistiu
    
    for vizinho in grafo.neighbors(nome_usuario): # percorre todos os nós que estão ligados ao nó do usuário
        if grafo.nodes[vizinho].get("tipo") == "filme": # garante que os nós percorridos sejam do tipo "filme"
            filmes_usuario.add(vizinho) # adiciona ao conjunto
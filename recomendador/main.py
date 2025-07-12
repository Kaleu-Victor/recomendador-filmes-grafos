import networkx as nx

G = nx.Graph()

def cadastrarUsuario(grafo, nome_usuario):
    grafo.add_node(nome_usuario, tipo = "usuario")

def cadastrarFilme(grafo, nome_filme):
    grafo.add_node(nome_filme, tipo = "filme")

def cadastrarFilmeParaUsuario(grafo, nome_usuario, nome_filme):
    grafo.add_edge(nome_usuario, nome_filme)
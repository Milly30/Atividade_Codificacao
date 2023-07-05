class Artigo:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor


    def getArtigo(self):
        return f"Titulo {self.titulo} | Autor: {self.autor}"


class Edicao:
    def __init__(self,numero,volume,data):
        self.numero = numero
        self.volume = volume
        self.data = data
        self.artigos = []


    def Adicionar_Artigo_Novo(self,artigo):
        self.artigos.append(artigo)


    def getEdicao(self):
        return  f"Edição número: {str(self.numero)} | Volume {str(self.volume)} | Data {str(self.data)}"


    def ShowArtigos(self):
        for artigo in self.artigos:
            print(artigo.getArtigo())


    def getNumArtigos(self):
        return len(self.artigos)


    def __getApagar_artigo__ (self,titulo):
        for artigo in self.artigos:
            if artigo.titulo == titulo:
                self.artigos.remove(artigo)


class Revista:
    def __init__(self,titulo,ISSN,periodicidade):
        self.titulo = titulo
        self.ISSN = ISSN
        self.peiodicidade = periodicidade
        self.edicoes = []


    def Adicionar_Edicao_nova(self,edicao):
        self.edicoes.append(edicao)


    def Publicar_Edicao(self,edicao):
        NumArtigos = edicao.NumArtigos()
        if (NumArtigos >= 10 and NumArtigos <= 15):
            return "PARABÉNS!! A sua edição foi lançada com êxito."
        else:
            return "OPS, ocorreu um problema na publicação. A edição precisa ter entre 10 e 15 artigos para poder ser lançada. "


    def Show_edicoes(self):
        for edicao in self.edicoes:
            print(edicao.getEdicao())

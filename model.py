from config import *

class Pokemon(db.Entity):
    nome = Required(str)
    idpokedex = Required(int)
    tipo_primario = Required(str)
    tipo_secundario = Optional(str)
    geracao = Required(int)
    regiao = Required(str)
    genero = Required(str)
    tem_evolucao = Required(bool)
    evolui_de = Optional(int)
    imagem = Required(str)
    data_cadastro = Required(datetime, default=datetime.now)

    def __str__(self):
        evolui_de = self.evolui_de.nome if self.evolui_de else "Nenhuma"
        evolui_para = self.evolui_para.nome if self.evolui_para else "Nenhuma"
        return (f"{self.nome} (ID: {self.idpokedex}) - Tipos: {self.tipo_primario}"
            f"{' / ' + self.tipo_secundario if self.tipo_secundario else ''} | "
            f"Evolui de: {evolui_de}")
    
    def json(self):
         return {
              "nome": self.nome,
              "idpokedex": self.idpokedex,
              "tipo_primario": self.tipo_primario,
              "tipo_secundario": self.tipo_secundario,
              "geracao": self.geracao,
              "regiao": self.regiao,
              "genero": self.genero,
              "tem_evolucao": self.tem_evolucao,
              "evolui_de": self.evolui_de,
              "imagem": self.imagem,
              "data_cadastro": self.data_cadastro.date().isoformat(),
         }
    
db.bind(provider='sqlite', filename='pokemon.db', create_db=True)
db.generate_mapping(create_tables=True)
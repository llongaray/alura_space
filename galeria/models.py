from django.db import models
max_num = 200
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta")
    ]

    nome = models.CharField(max_length=max_num, null=False, blank=False)
    legenda = models.CharField(max_length=max_num, null=False, blank=False)
    categoria = models.CharField(max_length=max_num, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=max_num, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"

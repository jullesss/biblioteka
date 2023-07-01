from rest_framework import generics
"""
Deve ser possível também usuários não autenticados acessarem a plataforma para visualizar informações sobre os livros, como disponibilidade, título, etc. -> permission
"""

class AlbumView(generics.ListCreateAPIView):
    ...



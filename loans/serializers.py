from rest_framework import serializers
from .models import Loan
from users.serializers import UserSerializer
from users.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .exceptions import BlockedError


class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    username = serializers.CharField()

    class Meta:
        model = Loan
        fields = ['id', 'user', 'copy', 'loan_date', 'username', 'retun_date']
        read_only_fields = ['return_date']
      #  extra_kwargs = {"return_date": {"read_only": True}}

    def create(self, validated_data: dict) -> Loan:
        user = get_object_or_404(User, user=validated_data.get("username"))

        if user.blocked:
            raise BlockedError()
        
        import ipdb; ipdb.set_trace()
        # filtro em Copy SE available é true e se pertence ao book (vindo ja no validated).
        # fazer uma condicional ... se não houver nenhuma copia avail, não existe, entao msg de erro.
        # se houver copia filtrada, pegar a primeira primeira e relacionar

        # Copy.objects.filter(available=True, book=validated_data.get('book')).first()

        #estruturar o insomnia



from rest_framework import serializers
from chairmanapp.models import Societymember

class SerializeSocietymember(serializers.ModelSerializer):

    # firstname = serializers.CharField(max_length=30)
    # lastname = serializers.CharField(max_length=30)
    # contact_no = serializers.CharField(max_length=30)
    # block_no = serializers.IntegerField()
    # email = serializers.EmailField()

    class Meta:
        model = Societymember
        fields = '__all__'

        

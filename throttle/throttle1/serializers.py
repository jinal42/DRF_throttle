from rest_framework import serializers
from .models import Custom,Owner

# class CustomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Custom
#         fields = ["id","name", "roll","city"]

class CustomSerializer2(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="customer-detail")
    class Meta:
        model = Custom
        fields = ['url','id','name', 'roll','city']


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id','name','cust_name']

class CustomSerializer(serializers.ModelSerializer):
    ownby=OwnerSerializer(many=True,read_only=True)
    class Meta:
        model = Custom
        # fi
        fields = ['id','name','roll','city','ownby']

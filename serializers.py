
from rest_framework import serializers
from .models import AdmissionModel

# use the Modelserializers in serializers 
class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionModel
        fields = ['id','Name','Age','City','Roll_No','Address','Fees']

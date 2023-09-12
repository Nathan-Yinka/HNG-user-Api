from rest_framework import serializers
from .models import Person
from .validation import validate_name_space
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
        
    def validate_name(self, name):   # called when we use the is_valid() on  the serializer
        if name:
            name = validate_name_space(name)     # cleaning the posted data and extra white space,and also ensure that the posted data is a string and not any other data type
            if not name:
                raise serializers.ValidationError("field must be a string")
            
            if Person.objects.filter(name=name).exists():
                raise serializers.ValidationError("Person with this Name already exists.",code="conflict")
        return name
        
            
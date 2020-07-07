from rest_framework import serializers

class HelloSerialzier(serializers.Serializer):
    """ Serialzies a name field for testing our APIview"""
    name = serializers.CharField(max_length=10)
    

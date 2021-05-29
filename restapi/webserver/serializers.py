from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):


	class Meta:
		model=User
		#fields=('firstname','lastname','userid')
		fields='__all__'
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework.serializers import (
	EmailField,
	CharField,
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField,
	ValidationError,
	)


class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	email = CharField(required=False, allow_blank=True)
	class Meta:
		model = User
		fields = [
				'id',
				'email',
				'password',
				'token',

		]
		extra_kwargs = {"password":
							{"write_only": True}
							}

	def validate(self, data):
		user_obj = None
		email = data.get("email", None)
		password = data["password"]
		if not email:
			raise ValidationError("ingrese usuario o contraseña")

		user = User.objects.filter(
#				Q(email=email) |
				Q(email=email)
			).distinct()
#		user = user.exclude(email__isnull=True).exclude(email___iexact='')
		if user.exists() and user.count() == 1:
			user_obj = user.first()
		else: 
			raise ValidationError("Usuario no valido.")
		
		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError("credecianles incorrectas, porfavor vuelva a intentar.")

		data["id"] = user_obj.id
		data["token"] = "SOME RANDONM TOKEN"


		return data
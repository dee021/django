from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password # 기본 패스워드 검증 도구
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token # token 모델
from rest_framework.validators import UniqueValidator # 이메일 중복 방지를 위한 검증 도구

from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset = User.objects.all())],
    )
    password = serializers.CharField(
        write_only = True, # 클라이언트->서버 방향의 역직렬화는 가능 / 서버 -> 클라이언트 방향의 직렬화는 불가능
        required = True,
        validators = [validate_password],
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True
    )

    class Meta:
        model = User
        fields = ('username','password', 'password2', 'email')
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password': 'Password fiedls didn\'t match.'}
            )
        return data
    
    def create(self, validated_data): # create 오버라이딩. 유저를 생성하고 토큰을 생성.
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True, write_only = True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user = user)
            return token
        raise serializers.ValidationError(
            {"error":"Unable to log in with provided credentials."}
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("nickname", "position", 'subjects', 'image')


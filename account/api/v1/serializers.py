
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'password_confirm', 'first_name', 'last_name', 'mobile', 'profile_pic']
        extra_kwargs = {'password':{'write_only':True}}
    def save(self, **kwargs):
        user = User(
            username=self.validated_data.get('username'),
            email=self.validated_data.get('email'),
            first_name=self.validated_data.get('first_name'),
            last_name=self.validated_data.get('last_name'),
            mobile=self.validated_data.get('mobile'),
            profile_pic=self.validated_data.get('profile_pic')
            )
        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                {
                    'error':"password didn't match"
                }
            )
        user.set_password(self.validated_data.get('password'))
        user.save()

        return user



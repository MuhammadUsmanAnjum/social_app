from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer

class UserCreateSerializer(BaseUserCreateSerializer):    
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'password',]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email','register_on_holiday' ,'first_name', 'last_name', ]
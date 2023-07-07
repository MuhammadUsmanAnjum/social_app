from rest_framework.permissions import IsAuthenticated
from users.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .ip_api import get_wan_ip, get_country_from_ip, is_holiday
from .serializers import UserSerializer
 
 
class HolidayCoincides(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        try:
            user = request.user
            date = user.date_joined.date()
            wan_ip = get_wan_ip()
            country_code = get_country_from_ip(wan_ip)
            coincides_with_holiday = is_holiday(country_code, date)
            signup_detail =  {'wan_ip':wan_ip, 'country':country_code, 'register_on_holiday':coincides_with_holiday}
            if coincides_with_holiday:
                user.register_on_holiday = coincides_with_holiday
                user.save()
                serializer = UserSerializer(user)
                res = {'registeration_detail':signup_detail, 'user_detail':serializer.data}
                return Response(res, status=status.HTTP_200_OK)
            else:
                serializer = UserSerializer(user)
                res = {'registeration_detail':signup_detail, 'user_detail':serializer.data}
                return Response(res, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
from rest_framework.response import Response
from . models import User, Income, Expanse
from rest_framework.views import APIView #TODO modelviewset swagger 
from . seriliazers import UserSeriliazer, IncomeSeriliazer, ExpanceSeriliazer
# from django.contrib.auth.models import User
# from django.contrib.auth.hashers import make_password
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
from django.db.models import Count,Sum      #TODO caunt ni organish 


# Create your views here.
class GetUser(APIView):
    def get(self, request):
        user= User.objects.all()
        seriliazer=UserSeriliazer(user,many=True)
        return Response( seriliazer.data)

class IncomeView(APIView):
    def get(self, request):
        income= Income.objects.all()
        seriliazer=IncomeSeriliazer(income,many=True)
        return Response( seriliazer.data)
    def post(self, request):
        data=request.data
        seriliazer=IncomeSeriliazer(data=data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        else:
            return Response(seriliazer.errors)

class ExpanseView(APIView):
    def get(self, request):
        expanse=Expanse.objects.all()
        seriliazer=ExpanceSeriliazer(expance,many=True)
        return Response( seriliazer.data)
    def post(self, request):
        data=request.data
        seriliazer=ExpanceSeriliazer(data=data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data)
        else:
            return Response(seriliazer.errors)



class IncomeSumView(APIView):
    def post(self, request):
        data=request.data
        start_date=data["start_date"]
        end_date=data["end_date"]
        total=Income.objects.filter(add_date__date__gte=start_date,add_date__date__lte=end_date).aggregate(total_amount=Sum("amount"))
        return Response(total)
    
class ExpanseSumView(APIView):
    def post(self, request):
        data=request.data
        start_date=data["start_date"]
        end_date=data["end_date"]
        total=Expanse.objects.filter(add_date__date__gte=start_date,add_date__date__lte=end_date).aggregate(total_amount=Sum("amount"))
        return Response(total)
    
class MonthSumView(APIView):
    def post(self, request):
        data=request.data
        start_date=data["start_date"]
        end_date=data["end_date"]
        total_income=Income.objects.filter(add_date__date__gte=start_date,add_date__date__lte=end_date).aggregate(total_amount=Sum("amount"))
        total_expanse=Expanse.objects.filter(add_date__date__gte=start_date,add_date__date__lte=end_date).aggregate(total_amount=Sum("amount"))
        if total_income.keys()>total_expanse.keys():
            return f" SIZ {start_date} va {end_date}  oraligida {total_income-total_expanse} miqdorida foydadasiz "
        else:
            return f" SIZ {start_date} va {end_date}  oraligida {total_income-total_expanse} miqdorda zarardasiz  "
        print(total_expanse.keys())
    
# class UserRegister(APIView):
#     def post(self, request):
#         data = request.data
#         user = User.objects.create(
#             first_name=data["first_name"],
#             last_name=data["last_name"],
#             username=data["username"],
#             email=data["email"],
#             password=make_password(data["password"]),
#         )

#         token, created = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key})


# class LoginUser(APIView):
#     def post(self, request):
#         data = request.data
#         user = authenticate(username=data["username"], password=data["password"])
#         if user is not None:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key})
#         else:
#             return Response({"error": "username or password incorrect"})
        



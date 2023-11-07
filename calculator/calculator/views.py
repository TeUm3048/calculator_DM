from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.request import Request

from computing.natural.Natural import Natural
from .serializers import NaturalSerializer
from .models import num1, NaturalModel


def index(request):
    return render(request, "index.html")


class NaturalOperatorView(APIView):
    parser_classes = [JSONParser]

    def get(self, request: Request):
        operators = ["mod_operator"]
        example = {
            "operator": "natural_mod",
            "args": [
                {
                    "num": "6"
                },
                {
                    "num": "4"
                }
            ]
        }
        result = {
            "num": "2"
        }
        data = {"operators": operators, "POST": example, "result": result}

        return Response(data)

    def post(self, request: Request):
        try:
            operator = request.data['operator']
            args = request.data['args']
            serialized_args = list(map(lambda x: NaturalSerializer(data=x), args))
        except Exception:
            return Response({"Error": "Invalid value", "request": request.data}, status=500)
        for a_ser in serialized_args:
            if not (a_ser.is_valid()):
                return Response({"Error": "Invalid value", "args": args}, status=500)

        res = Natural("0")
        match operator:
            case 'natural_compare':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                res = a.compare(b)
            case 'natural_is_not_zero':
                a = Natural(serialized_args[0].data["num"])
                res = a.is_not_zero(b)
            case 'natural_add':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                res = a.add(b)
            case 'natural_subtract':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                res = a.subtract(b)
            case 'natural_multiply_by_digit':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                res = a.multiply_by_digit(b)
            case 'natural_multiply_by_power_of_10':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                res = a.multiply_by_power_of_10(b)
            case 'natural_mod':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                res = a.mod(b)
            case 'natural_multiply':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                res = a.multiply(b)
            case 'natural_subtract_product_from_natural':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                c = int(serialized_args[2].data["num"])
                res = a.subtract_product_from_natural(b, c)
            case 'natural_get_digit_of_division_with_power':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                res = a.get_digit_of_division_with_power(b)
            case 'natural_div':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                res = a.div(b)
            case 'natural_gcd':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                res = a.gcd(b)
            case 'natural_lcm':
                a = Natural(serialized_args[0].data["num"])
                b = Natural(serialized_args[1].data["num"])
                res = a.lcm(b)
            case 'natural_increment':
                a = Natural(serialized_args[0].data["num"])
                a.increment()
                res = a
            case _:
                return Response(f'No such operator: "{operator}"', status=404)

        res_ser = NaturalSerializer(NaturalModel(res))

        return Response(res_ser.data)

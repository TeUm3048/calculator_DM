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
                    "type": "natural",
                    "num": "6"
                },
                {
                    "type": "natural",
                    "num": "4"
                }
            ]
        }
        result = {
            "type": "natural",
            "num": "2"
        }
        data = {"operators": operators, "POST": example, "result": result}

        return Response(data)

    def post(self, request: Request):
        try:
            operator = request.data['operator']
            args = request.data['args']
            a_ser = NaturalSerializer(data=args[0])
            b_ser = NaturalSerializer(data=args[1])
        except Exception:
            return Response({"Error": "Invalid value", "request": request.data}, status=300)

        if not (a_ser.is_valid() and b_ser.is_valid()):
            return Response({"Error": "Invalid value", "args": args}, status=300)

        res = Natural("0")
        match operator:
            case 'natural_mod':
                a = Natural(a_ser.data["num"])
                b = Natural(b_ser.data["num"])
                res = a.mod(b)
            case _:
                return Response(f'No such operator: "{operator}"', status=404)

        res_ser = NaturalSerializer(NaturalModel(res))

        return Response(res_ser.data)

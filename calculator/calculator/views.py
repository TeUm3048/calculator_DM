from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from computing.integer.Integer import Integer
from computing.natural.Natural import Natural
from computing.rational.Rational import Rational
from computing.polynom.Polynom import Polynom

from .models import IntegerModel, NaturalModel, RationalModel, PolynomModel
from .serializers import (IntegerSerializer, NaturalSerializer,
                          RationalSerializer, PolynomSerializer)


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


class IntegerOperatorView(APIView):
    parser_classes = [JSONParser]

    def get(self, request: Request):
        operators = ["mod_operator"]
        example = {
            "operator": "integer_mod",
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
            serialized_args = list(map(lambda x: IntegerSerializer(data=x), args))
        except Exception:
            return Response({"Error": "Invalid value", "request": request.data}, status=500)
        for a_ser in serialized_args:
            if not (a_ser.is_valid()):
                return Response({"Error": "Invalid value", "args": args}, status=500)

        res = Integer("0")
        match operator:
            case 'integer_absolute':
                a = Integer(serialized_args[0].data["num"])
                res = a.absolute()
            case 'integer_determinate_sign':
                a = Integer(serialized_args[0].data["num"])
                res = a.determinate_sign()
            case 'integer_multiply_by_negative_one':
                a = Integer(serialized_args[0].data["num"])
                res = a.multiply_by_negative_one()
            case 'integer_from_natural':
                a = Natural(serialized_args[0].data["num"])
                res = Integer.from_natural(a)
            case 'integer_to_natural':
                a = Integer(serialized_args[0].data["num"])
                res = a.to_natural()
            case 'integer_add':
                a = Integer(serialized_args[0].data["num"])
                b = Integer(serialized_args[1].data["num"])
                res = a.add(b)
            case 'integer_to_natural':
                a = Integer(serialized_args[0].data["num"])
                res = a.to_natural()
            case 'integer_subtract':
                a = Integer(serialized_args[0].data["num"])
                b = Integer(serialized_args[1].data["num"])
                res = a.subtract(b)
            case 'integer_multiply':
                a = Integer(serialized_args[0].data["num"])
                b = Integer(serialized_args[1].data["num"])
                res = a.multiply(b)
            case 'integer_div':
                a = Integer(serialized_args[0].data["num"])
                b = Integer(serialized_args[1].data["num"])
                res = a.div(b)
            case 'integer_mod':
                a = Integer(serialized_args[0].data["num"])
                b = Integer(serialized_args[1].data["num"])
                res = a.mod(b)
            case _:
                return Response(f'No such operator: "{operator}"', status=404)

        res_ser = IntegerSerializer(IntegerModel(res))

        return Response(res_ser.data)


class RationalOperatorView(APIView):
    parser_classes = [JSONParser]

    def get(self, request: Request):
        operators = ["mod_operator"]
        example = {
            "operator": "integer_mod",
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
            serialized_args = list(map(lambda x: RationalSerializer(data=x), args))
        except Exception:
            return Response({"Error": "Invalid value", "request": request.data}, status=500)
        for a_ser in serialized_args:
            if not (a_ser.is_valid()):
                return Response({"Error": "Invalid value", "args": args}, status=500)

        res = Rational("0")
        match operator:
            case 'rational_simplify':
                a = Rational(serialized_args[0].data["num"])
                res = a.simplify()
            case 'rational_is_integer':
                a = Rational(serialized_args[0].data["num"])
                res = a.is_integer()
            case 'rational_from_integer':
                a = Integer(serialized_args[0].data["num"])
                res = Rational.from_integer(a)
            case 'rational_to_integer':
                a = Rational(serialized_args[0].data["num"])
                res = a.to_integer()
            case 'rational_add':
                a = Rational(serialized_args[0].data["num"])
                b = Rational(serialized_args[1].data["num"])
                res = a.add(b)
            case 'rational_subtract':
                a = Rational(serialized_args[0].data["num"])
                b = Rational(serialized_args[1].data["num"])
                res = a.subtract(b)
            case 'rational_multiply':
                a = Rational(serialized_args[0].data["num"])
                b = Rational(serialized_args[1].data["num"])
                res = a.multiply(b)
            case 'rational_divide':
                a = Rational(serialized_args[0].data["num"])
                b = Rational(serialized_args[1].data["num"])
                res = a.divide(b)
            case _:
                return Response(f'No such operator: "{operator}"', status=404)

        res_ser = RationalSerializer(RationalModel(res))

        return Response(res_ser.data)


class PolynomOperatorView(APIView):
    parser_classes = [JSONParser]

    def get(self, request: Request):
        operators = ["mod_operator"]
        example = {
            "operator": "integer_mod",
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
            serialized_args = list(map(lambda x: PolynomSerializer(data=x), args))
        except Exception:
            return Response({"Error": "Invalid value", "request": request.data}, status=500)
        for a_ser in serialized_args:
            if not (a_ser.is_valid()):
                return Response({"Error": "Invalid value", "args": args}, status=500)

        res = Polynom("0")
        match operator:
            case 'polynom_add':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                b = Polynom(list(map(Rational, serialized_args[1].data["num"])))
                res = a.add(b)
            case 'polynom_subtract':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                b = Polynom(list(map(Rational, serialized_args[1].data["num"])))
                res = a.subtract(b)
            case 'polynom_multiply_by_scalar':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                b = Rational(list(map(Rational, serialized_args[0].data["num"]))[0])
                res = a.multiply_by_scalar(b)
            case 'polynom_multiply_by_monomial':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                b = Rational(list(map(Rational, serialized_args[0].data["num"]))[0])
                res = a.multiply_by_monomial(b)
            case 'polynom_get_leading_coefficient':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                res = a.get_leading_coefficient()
            case 'polynom_get_degree':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                res = a.get_degree()
            case 'polynom_factor_polynomial_coefficients':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                res = a.factor_polynomial_coefficients()
            case 'polynom_multiply':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                b = Polynom(list(map(Rational, serialized_args[1].data["num"])))
                res = a.multiply(b)
            case 'polynom_div':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                b = Polynom(list(map(Rational, serialized_args[1].data["num"])))
                res = a.add(b)
            case 'polynom_mod':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                b = Polynom(list(map(Rational, serialized_args[1].data["num"])))
                res = a.add(b)
            case 'polynom_gcd':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                b = Polynom(list(map(Rational, serialized_args[1].data["num"])))
                res = a.add(b)
            case 'polynom_derive':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                res = a.derive()
            case 'polynom_eliminating_duplicate_roots':
                a = Polynom(list(map(Rational, serialized_args[0].data["num"])))
                res = a.eliminating_duplicate_roots()
            case _:
                return Response(f'No such operator: "{operator}"', status=404)

        res_ser = PolynomSerializer(PolynomModel(res))

        return Response(res_ser.data)

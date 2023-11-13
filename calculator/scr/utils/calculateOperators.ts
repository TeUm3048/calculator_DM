import axios from "axios";
import {
  NaturalNumber,
  NaturalOperator,
  IntegerNumber,
  IntegerOperator,
  RationalNumber,
  RationalOperator,
  PolynomOperator,
  PolynomNumber,
} from "./Operators";

const calculateOperator = async <Num, Op>(
  operator: Op,
  args: Num[],
  apiPath: string
) => {
  const body = {
    operator: operator,
    args: args,
  };

  return axios
    .post<Num>(apiPath, body, {
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      return response.data;
    })
    .catch((error) => {
      if (axios.isAxiosError(error)) {
        throw error;
      } else {
        throw error;
      }
    });
};

export type calculateOperatorFn<Num, Op> = (
  operator: Op,
  args: Num[]
) => Promise<Num>;

export const calculateNaturalOperator = (
  operator: NaturalOperator,
  args: NaturalNumber[]
) => calculateOperator(operator, args, "api/natural");

export const calculateIntegerOperator = (
  operator: IntegerOperator,
  args: IntegerNumber[]
) => calculateOperator(operator, args, "api/integer");

export const calculateRationalOperator = (
  operator: RationalOperator,
  args: RationalNumber[]
) => calculateOperator(operator, args, "api/rational");
export const calculatePolynomOperator = (
  operator: PolynomOperator,
  args: PolynomNumber[]
) => calculateOperator(operator, args, "api/polynom");

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

const calculateOperator = async <Num, Op>(operator: Op, args: Num[]) => {
  const body = {
    operator: operator,
    args: args,
  };

  return axios
    .post<Num>("/api/", body, {
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

export type calculateOperatorFn<Num, Op> = typeof calculateOperator<Num, Op>;

export const calculateNaturalOperator = calculateOperator<
  NaturalNumber,
  NaturalOperator
>;

export const calculateIntegerOperator = calculateOperator<
  IntegerNumber,
  IntegerOperator
>;

export const calculateRationalOperator = calculateOperator<
  RationalNumber,
  RationalOperator
>;
export const calculatePolynomOperator = calculateOperator<
  PolynomNumber,
  PolynomOperator
>;

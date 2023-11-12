import axios from "axios";
import {
  NaturalNumber,
  NaturalOperator,
  IntegerNumber,
  IntegerOperator,
  RationalNumber,
  RationalOperator,
} from "./Operators";

const calculateOperator = async <Num, Op>(operator: Op, args: string[]) => {
  const body = {
    operator: operator,
    args: args.map((el) => {
      return { num: el };
    }),
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

import axios from "axios";
import {
  NaturalNumber,
  NaturalOperatorData,
  NaturalOperator,
} from "./NaturalOperator";
import Natural from "../Pages/Natural";

const calculateNaturalOperator = async (
  operator: NaturalOperator,
  args: string[]
) => {
  const body: NaturalOperatorData = {
    operator: operator,
    args: args.map((el) => {
      return { num: el };
    }),
  };

  return axios
    .post<NaturalNumber>("/api/", body, {
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

export default calculateNaturalOperator;

import axios from "axios";
import { NaturalNumber, NaturalOperatorData } from "./NaturalOperator";

const calculateNaturalOperator = async (body: NaturalOperatorData) => {
  return axios
    .post<NaturalNumber>("/api", body, {
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

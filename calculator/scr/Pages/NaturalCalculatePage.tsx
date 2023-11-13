import CalculatorModule from "../Components/CalculatorModule";
import { calculateNaturalOperator } from "../utils/calculateOperators";
import { natural_calculate_operators } from "../utils/Operators/";

const NaturalCalculatePage = () => {
  return (
    <CalculatorModule
      calculateOperator={calculateNaturalOperator}
      calculate_operators={natural_calculate_operators}
      parseStringToNum={(s) => {
        return { num: s };
      }}
    ></CalculatorModule>
  );
};

export default NaturalCalculatePage;

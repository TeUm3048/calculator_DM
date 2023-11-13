import CalculatorModule from "../Components/CalculatorModule";
import { calculateRationalOperator } from "../utils/calculateOperators";
import { rational_calculate_operators } from "../utils/Operators";

const RationalCalculatingPage = () => {
  return (
    <CalculatorModule
      calculateOperator={calculateRationalOperator}
      calculate_operators={rational_calculate_operators}
      parseStringToNum={(s) => {
        return { num: s };
      }}
    ></CalculatorModule>
  );
};

export default RationalCalculatingPage;

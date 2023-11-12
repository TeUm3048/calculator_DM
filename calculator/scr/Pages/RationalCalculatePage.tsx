import CalculatorModule from "../Components/CalculatorModule";
import { calculateRationalOperator } from "../utils/calculateOperators";
import { rational_calculate_operators } from "../utils/Operators";

const RationalCalculatingPage = () => {
  return (
    <CalculatorModule
      calculateOperator={calculateRationalOperator}
      calculate_operators={rational_calculate_operators}
    ></CalculatorModule>
  );
};

export default RationalCalculatingPage;

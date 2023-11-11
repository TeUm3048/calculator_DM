import CalculatorModule from "../Components/CalculatorModule/CalculatorModule";
import { calculateIntegerOperator } from "../utils/calculateOperators";
import { integer_calculate_operators } from "../utils/Operators";

const IntegerCalculatingPage = () => {
  return (
    <CalculatorModule
      calculateOperator={calculateIntegerOperator}
      calculate_operators={integer_calculate_operators}
    ></CalculatorModule>
  );
};

export default IntegerCalculatingPage;

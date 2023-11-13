import CalculatorModule from "../Components/CalculatorModule";
import { calculateIntegerOperator } from "../utils/calculateOperators";
import { integer_calculate_operators } from "../utils/Operators";

const IntegerCalculatingPage = () => {
  return (
    <CalculatorModule
      calculateOperator={calculateIntegerOperator}
      calculate_operators={integer_calculate_operators}
      parseStringToNum={(s) => {
        return { num: s };
      }}
    ></CalculatorModule>
  );
};

export default IntegerCalculatingPage;

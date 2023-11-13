import { CalculatorModulePolynom } from "../Components/CalculatorModule";
import { calculatePolynomOperator } from "../utils/calculateOperators";
import { polynom_calculate_operators } from "../utils/Operators/";

const PolynomCalculatePage = () => {
  return (
    <CalculatorModulePolynom
      calculateOperator={calculatePolynomOperator}
      calculate_operators={polynom_calculate_operators}
      parseStringToNum={(s) => {
        return { num: s.split(" ") };
      }}
    ></CalculatorModulePolynom>
  );
};

export default PolynomCalculatePage;

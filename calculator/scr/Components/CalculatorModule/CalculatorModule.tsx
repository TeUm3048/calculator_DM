import { FormEventHandler, useRef, useState } from "react";
import styles from "./CalculatorModule.module.css";
import { CalcButton } from "./CalcButton";
import { calculateOperatorFn } from "../../utils/calculateOperators";

interface Props<Num, Op> {
  calculateOperator: calculateOperatorFn<Num, Op>;
  calculate_operators: { value: string; operator: Op }[];
  parseStringToNum: (s: string) => Num;
}

const CalculatorModule = <Num extends { num: any }, Op>({
  calculateOperator,
  calculate_operators,
  parseStringToNum,
}: Props<Num, Op>) => {
  const [num1, setNum1] = useState<string>();
  const [num2, setNum2] = useState<string>();
  const [errorMessage, setErrorMessage] = useState<string>();
  // const [num3, setNum3] = useState<string>();
  const [operator, setOperator] = useState<Op>();
  const refInput1 = useRef<HTMLInputElement>(null);
  const refInput2 = useRef<HTMLInputElement>(null);
  // const refInput3 = useRef<HTMLInputElement>(null);

  const handleSubmit: FormEventHandler = async (e) => {
    e.preventDefault();
    setErrorMessage("");

    if (!refInput1 || !refInput1.current) {
      setErrorMessage("Input1 is not valid");
      throw new TypeError("Input1 is not valid");
    }
    if (!refInput2 || !refInput2.current) {
      setErrorMessage("Input2 is not valid");
      throw new TypeError("Input2 is not valid");
    }
    // if (!refInput3 || !refInput3.current) {
    //   throw new TypeError("Input3 is not valid");
    // }

    setNum1(refInput1.current.value);
    setNum2(refInput2.current.value);
    // setNum3(refInput3.current.value);

    if (!operator) {
      setErrorMessage("Не выбран оператор");
      return;
    }

    const operator_args = [];
    if (num1) operator_args.push(num1);
    if (num2) operator_args.push(num2);
    // if (num3) operator_args.push(num3);

    calculateOperator(operator, operator_args.map(parseStringToNum))
      .then((value) => {
        setNum1(value.num);
        setNum2("");
        // setNum3("");
        setOperator(undefined);
      })
      .catch((error) => {
        setErrorMessage("Упс, что-то пошло не так...");
        throw error;
      });
  };

  return (
    <div className={styles.wrapper}>
      <input
        className={styles.input}
        type="text"
        ref={refInput1}
        value={num1}
        onChange={(e) => setNum1(e.currentTarget.value)}
      />
      <input
        className={styles.input}
        type="text"
        ref={refInput2}
        value={num2}
        onChange={(e) => setNum2(e.currentTarget.value)}
      />
      <div className={styles.error}>{errorMessage}</div>

      {/* <input
        className={styles.input}
        type="text"
        ref={refInput3}
        value={num3}
        onChange={(e) => setNum3(e.currentTarget.value)}
      /> */}
      <div className={styles.btn_container}>
        {calculate_operators.map((el) => {
          return (
            <CalcButton
              buttonOperator={el.operator}
              currentOperator={operator}
              setOperator={setOperator}
            >
              {el.value}
            </CalcButton>
          );
        })}
        <button className={styles.btn} onClick={handleSubmit}>
          =
        </button>
      </div>
    </div>
  );
};

export default CalculatorModule;

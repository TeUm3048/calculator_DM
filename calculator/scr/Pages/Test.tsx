import { FormEventHandler, useRef, useState } from "react";
import { NaturalOperator, NaturalNumber } from "../utils/NaturalOperator";
import calculateNaturalOperator from "../utils/calculateNaturalOperator";
import { natural_calculate_operators } from "../Calculate";
import styles from "./Test.module.css";

const Test = () => {
  const [num1, setNum1] = useState<string>();
  const [num2, setNum2] = useState<string>();
  const [num3, setNum3] = useState<string>();
  const [operator, setOperator] = useState<NaturalOperator>();
  const refInput1 = useRef<HTMLInputElement>(null);
  const refInput2 = useRef<HTMLInputElement>(null);
  const refInput3 = useRef<HTMLInputElement>(null);

  const handleSubmit: FormEventHandler = async (e) => {
    e.preventDefault();
    if (!refInput1 || !refInput1.current) {
      throw new TypeError("Input1 is not valid");
    }
    if (!refInput2 || !refInput2.current) {
      throw new TypeError("Input2 is not valid");
    }
    if (!refInput3 || !refInput3.current) {
      throw new TypeError("Input2 is not valid");
    }

    setNum1(refInput1.current.value);
    setNum2(refInput2.current.value);
    setNum3(refInput3.current.value);

    if (!num1 || !operator) {
      return;
    }

    calculateNaturalOperator(
      operator,
      num3 && num2 ? [num1, num2, num3] : num2 ? [num1, num2] : [num1]
    ).then((value) => {
      setNum1(value.num);
      setNum2("");
      setNum3("");
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
      {/* <input
        className={styles.input}
        type="text"
        ref={refInput3}
        value={num3}
        onChange={(e) => setNum3(e.currentTarget.value)}
      /> */}
      <div className={styles.btn_container}>
        {natural_calculate_operators.map((el) => {
          return (
            <button
              className={styles.btn}
              onClick={(e) => {
                setOperator(el.operator);
              }}
            >
              {el.value}
            </button>
          );
        })}
        <button onClick={handleSubmit}> = </button>
      </div>
    </div>
  );
};

export default Test;

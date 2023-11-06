import { FormEventHandler, useRef, useState } from "react";
import { NaturalOperator, NaturalNumber } from "../utils/NaturalOperator";
import calculateNaturalOperator from "../utils/calculateNaturalOperator";

const Test = () => {
  const [num1, setNum1] = useState<string>();
  const [num2, setNum2] = useState<string>();
  const [operator, setOperator] = useState<NaturalOperator>();
  const refInput1 = useRef<HTMLInputElement>(null);
  const refInput2 = useRef<HTMLInputElement>(null);

  const handleSubmit: FormEventHandler = async (e) => {
    e.preventDefault();
    if (!refInput1 || !refInput1.current) {
      throw new TypeError("Input1 is not valid");
    }
    if (!refInput2 || !refInput2.current) {
      throw new TypeError("Input2 is not valid");
    }

    setNum1(refInput1.current.value);
    setNum2(refInput2.current.value);

    if (!num1 || !num2 || !operator) {
      return;
    }

    calculateNaturalOperator({
      operator: operator,
      args: [
        { num: num1, type: "natural" },
        { num: num2, type: "natural" },
      ],
    }).then((value) => {
      setNum1(value.num);
      setNum2("");
    });
  };

  return (
    <div>
      <input
        type="text"
        ref={refInput1}
        value={num1}
        onChange={(e) => setNum1(e.currentTarget.value)}
      />
      <input
        type="text"
        ref={refInput2}
        value={num2}
        onChange={(e) => setNum2(e.currentTarget.value)}
      />
      <button
        onClick={(e) => {
          setOperator("natural_mod");
        }}
      ></button>
      <button onClick={handleSubmit}> = </button>
    </div>
  );
};

export default Test;

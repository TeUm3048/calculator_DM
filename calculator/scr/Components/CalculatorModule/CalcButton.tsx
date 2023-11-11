import React, { memo, useMemo } from "react";
import styles from "./Test.module.css";
import { FormEventHandler } from "react";

interface Props<Op> {
  children: any;
  buttonOperator: Op;
  currentOperator: Op | undefined;
  setOperator: (value: Op) => void;
}

export const CalcButton = <Op,>({
  children,
  buttonOperator,
  currentOperator,
  setOperator,
}: Props<Op>) => {
  const setOperatorHandle: FormEventHandler = (e) => {
    e.preventDefault();
    setOperator(buttonOperator);
  };

  const classNames = [
    styles.btn,
    buttonOperator == currentOperator ? styles.active : "",
  ].join(" ");

  return (
    <button className={classNames} onClick={setOperatorHandle}>
      {children}
    </button>
  );
};

type Operator =
  | "compare"
  | "increment"
  | "add"
  | "subtract"
  | "multiply_by_digit"
  | "multiply_by_power_of_10"
  | "multiply"
  | "div"
  | "mod"
  | "gcd"
  | "lcm";

export type NaturalOperator = `natural_${Operator}`;

export type NaturalNumber = {
  type: "natural";
  num: `${number}`;
};

export interface NaturalOperatorData {
  operator: NaturalOperator;
  args: [NaturalNumber, NaturalNumber?];
}

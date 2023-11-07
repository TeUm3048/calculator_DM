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
  | "lcm"
  | "is_not_zero"
  | "get_digit_of_division_with_power";

export type NaturalOperator = `natural_${Operator}`;

export interface NaturalNumber {
  num: string;
}

export interface NaturalOperatorData {
  operator: NaturalOperator;
  args: NaturalNumber[];
}

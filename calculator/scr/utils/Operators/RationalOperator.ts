export enum RationalOperator {
  rational_simplify = "rational_simplify",
  rational_is_integer = "rational_is_integer",
  rational_add = "rational_add",
  rational_subtract = "rational_subtract",
  rational_multiply = "rational_multiply",
  rational_divide = "rational_divide",
}

export const rational_calculate_operators: {
  value: string;
  operator: RationalOperator;
}[] = [
  { value: "simplify", operator: RationalOperator.rational_simplify },
  { value: "is_Int", operator: RationalOperator.rational_is_integer },
  { value: "+", operator: RationalOperator.rational_add },
  { value: "-", operator: RationalOperator.rational_subtract },
  { value: "*", operator: RationalOperator.rational_multiply },
  { value: "/", operator: RationalOperator.rational_divide },
];

export interface RationalNumber {
  num: string;
}

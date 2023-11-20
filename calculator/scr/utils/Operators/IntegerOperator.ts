export enum IntegerOperator {
  integer_absolute = "integer_absolute",
  integer_determinate_sign = "integer_determinate_sign",
  integer_multiply_by_negative_one = "integer_multiply_by_negative_one",
  integer_add = "integer_add",
  integer_subtract = "integer_subtract",
  integer_multiply = "integer_multiply",
  integer_div = "integer_div",
  integer_mod = "integer_mod",
}

export const integer_calculate_operators: {
  value: string;
  operator: IntegerOperator;
}[] = [
  { value: "abs", operator: IntegerOperator.integer_absolute },
  { value: "sign", operator: IntegerOperator.integer_determinate_sign },
  { value: "(-)", operator: IntegerOperator.integer_multiply_by_negative_one },
  { value: "+", operator: IntegerOperator.integer_add },
  { value: "-", operator: IntegerOperator.integer_subtract },
  { value: "*", operator: IntegerOperator.integer_multiply },
  { value: "//", operator: IntegerOperator.integer_div },
  { value: "mod", operator: IntegerOperator.integer_mod },
];

export interface IntegerNumber {
  num: string;
}

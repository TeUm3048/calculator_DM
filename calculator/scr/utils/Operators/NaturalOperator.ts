export enum NaturalOperator {
  natural_compare = "natural_compare",
  natural_increment = "natural_increment",
  natural_add = "natural_add",
  natural_subtract = "natural_subtract",
  natural_multiply_by_digit = "natural_multiply_by_digit",
  natural_multiply_by_power_of_10 = "natural_multiply_by_power_of_10",
  natural_multiply = "natural_multiply",
  natural_div = "natural_div",
  natural_mod = "natural_mod",
  natural_gcd = "natural_gcd",
  natural_lcm = "natural_lcm",
  natural_is_not_zero = "natural_is_not_zero",
  natural_get_digit_of_division_with_power = "natural_get_digit_of_division_with_power",
  natural_subtract_product_from_natural = "natural_subtract_product_from_natural",
}

export const natural_calculate_operators: {
  value: string;
  operator: NaturalOperator;
}[] = [
  { value: "<>", operator: NaturalOperator.natural_compare },
  { value: "!= 0", operator: NaturalOperator.natural_is_not_zero },
  { value: "+", operator: NaturalOperator.natural_add },
  { value: "-", operator: NaturalOperator.natural_subtract },
  {
    value: "*10^",
    operator: NaturalOperator.natural_multiply_by_power_of_10,
  },
  { value: "mod", operator: NaturalOperator.natural_mod },
  { value: "*", operator: NaturalOperator.natural_multiply },
  // { value: "-k*b", operator: NaturalOperator.natural_subtract_product_from_natural },
  {
    value: "// 1 digit",
    operator: NaturalOperator.natural_get_digit_of_division_with_power,
  },
  { value: "//", operator: NaturalOperator.natural_div },
  { value: "gcd", operator: NaturalOperator.natural_gcd },
  { value: "lcm", operator: NaturalOperator.natural_lcm },
  { value: "++", operator: NaturalOperator.natural_increment },
];

export interface NaturalNumber {
  num: string;
}

import { NaturalOperator } from "./utils/NaturalOperator";

let Calculate = {
  buttons: [
    { val: "1" },
    { val: "2" },
    { val: "3" },
    { val: "4" },
    { val: "5" },
    { val: "6" },
    { val: "7" },
    { val: "8" },
    { val: "9" },
    { val: "0" },
    { val: "+" },
    { val: "-" },
    { val: "*" },
    { val: "/" },
  ],
  operations: [
    { val: "CE" },
    { val: "AC" },
    { val: "=" },
    { val: "x^2" },
    { val: "x^3" },
  ],
};

export const natural_calculate_operators: {
  value: string;
  operator: NaturalOperator;
}[] = [
  { value: "<>", operator: "natural_compare" },
  // { value: "!= 0", operator: "natural_is_not_zero" },
  { value: "+", operator: "natural_add" },
  { value: "-", operator: "natural_subtract" },
  { value: "*10^", operator: "natural_multiply_by_power_of_10" },
  { value: "mod", operator: "natural_mod" },
  { value: "*", operator: "natural_multiply" },
  // { value: "-k*b", operator: "natural_subtract_product_from_natural" },
  { value: "// 1 digit", operator: "natural_get_digit_of_division_with_power" },
  { value: "//", operator: "natural_div" },
  { value: "gcd", operator: "natural_gcd" },
  { value: "lcm", operator: "natural_lcm" },
  { value: "++", operator: "natural_increment" },
];
export default Calculate;

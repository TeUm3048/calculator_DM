export enum PolynomOperator {
  polynom_add = "polynom_add",
  polynom_subtract = "polynom_subtract",
  polynom_multiply_by_scalar = "polynom_multiply_by_scalar",
  polynom_multiply_by_monomial = "polynom_multiply_by_monomial",
  polynom_get_leading_coefficient = "polynom_get_leading_coefficient",
  polynom_get_degree = "polynom_get_degree",
  polynom_factor_polynomial_coefficients = "polynom_factor_polynomial_coefficients",
  polynom_multiply = "polynom_multiply",
  polynom_div = "polynom_div",
  polynom_mod = "polynom_mod",
  polynom_gcd = "polynom_gcd",
  polynom_derive = "polynom_derive",
  polynom_eliminating_duplicate_roots = "polynom_eliminating_duplicate_roots",
}

export const polynom_calculate_operators: {
  value: string;
  operator: PolynomOperator;
}[] = [
  { value: "+", operator: PolynomOperator.polynom_add },
  { value: "-", operator: PolynomOperator.polynom_subtract },
  { value: "*k", operator: PolynomOperator.polynom_multiply_by_scalar },
  { value: "*x^k", operator: PolynomOperator.polynom_multiply_by_monomial },
  { value: "lead", operator: PolynomOperator.polynom_get_leading_coefficient },
  { value: "deg", operator: PolynomOperator.polynom_get_degree },
  {
    value: "factorize",
    operator: PolynomOperator.polynom_factor_polynomial_coefficients,
  },
  { value: "*", operator: PolynomOperator.polynom_multiply },
  { value: "mod", operator: PolynomOperator.polynom_mod },
  // { value: "-k*b", operator: PolynomOperator.polynom_subtract_product_from_polynom },
  { value: "//", operator: PolynomOperator.polynom_div },
  { value: "gcd", operator: PolynomOperator.polynom_gcd },
  { value: "d/dx", operator: PolynomOperator.polynom_derive },
  {
    value: "eliminate",
    operator: PolynomOperator.polynom_eliminating_duplicate_roots,
  },
];

export interface PolynomNumber {
  num: string[];
}

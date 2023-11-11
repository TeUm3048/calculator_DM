
export type calculateOperatorFn<Num, Op> = (
  operator: Op,
  args: string[]
) => Promise<Num>;

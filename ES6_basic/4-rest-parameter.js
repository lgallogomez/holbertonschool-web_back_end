export default function returnHowManyArguments(...argss) {
  let total = 0;
  for (const number of argss) {
    total += 1;
  }
  return total;
}

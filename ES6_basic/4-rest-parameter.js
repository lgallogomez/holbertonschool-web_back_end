export default function returnHowManyArguments(...argss) {
  let total = 0;
  for (let element of argss) {
    element += element;
    total += 1;
  }
  return total;
}

export default function concatArrays(array1, array2, string) {
  const allArrays = [...array1, ...array2, ...string];
  return allArrays;
}

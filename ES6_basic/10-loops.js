export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  let value;
  for (value of array) {
    value = array[idx];
    array[idx] = appendString + value;
    idx += 1;
  }
  return array;
}

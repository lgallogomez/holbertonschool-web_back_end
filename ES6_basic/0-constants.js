export function taskFirst() {
  const task = 'I refer const when I can.';
  return task
}

export function getLast() {
  return ' us okay';
}

export function taskNext() {
  let combination =  'But sometimes let';
  combination += getLast();

  return combination;
}
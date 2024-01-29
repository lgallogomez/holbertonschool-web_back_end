export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new Error('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new Error('length must be a number');
    }
    if (typeof students !== 'object') {
      throw new Error('length must be a number');
    }
    this._name = name;
    this._lenght = length;
    this._students = students;
  }
}

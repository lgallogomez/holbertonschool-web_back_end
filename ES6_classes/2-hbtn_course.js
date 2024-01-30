export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw (TypeError('Name must be a string'));
    }
    if (typeof length !== 'number') {
      throw (TypeError('length must be a number'));
    }
    if (typeof students !== 'object') {
      throw (TypeError('length must be a number'));
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }

  set name(name) {
    if (typeof (name) !== 'string') {
      throw (new TypeError('Name must be a string'));
    }
    this._name = name;
  }

  set length(length) {
    if (typeof (length) !== 'number') {
      throw (new TypeError('Lenght must be a number'));
    }
    this._length = length;
  }

  set students(students) {
    if (typeof (students) !== 'object') {
      throw (new TypeError('students must be an object'));
    }
    this._students = students;
  }
}

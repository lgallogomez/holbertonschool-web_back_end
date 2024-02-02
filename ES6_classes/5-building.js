export default class Building  {
  constructor(sqft) {
    if (this)
    this._sqft = sqft
  }

  get sqft() {
    return this_sqft;
  }

  set sqft(sqft) {
    this._sqft = sqft;
  }
}
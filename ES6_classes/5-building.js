//revisar que cada edificio 
export default class Building {
  constructor(sqft) {
    if (new.target !== Building && typeof(this.evacuationWarningMessage) !== 'function') { //new.target or this.constructor = who's my created me.
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}

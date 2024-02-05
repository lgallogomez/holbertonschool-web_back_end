export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }
  cloneCar() {
    return(new this.constructor()); //build me new instance, using the constructor os the current object 
  }
}

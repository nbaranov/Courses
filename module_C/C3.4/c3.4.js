
function ElectricalAppliance(name, power) {
    this.name = name
    this.power = power;
    this.isPlug = false;
}

ElectricalAppliance.prototype.plugin = function() {
    this.isPlug = true;
    console.log(this.name + " plugged!");
};

ElectricalAppliance.prototype.unplug = function() {
    this.isPlugged = false;
    console.log(this.name + " unplugged!");
};

function Tv(name, brand, power, size) {
    this.name = name;
    this.brand = brand;
    this.power = power;
    this.size = size;
    this.isPlug = false;
}

Tv.prototype = new ElectricalAppliance();

function Console(name, brand, power, model) {
    this.name = name;
    this.brand = brand;
    this.power = power;
    this.model = model;
    this.isPlug = false;
}

Console.prototype = new ElectricalAppliance();

const tvLG = new Tv("TV", "LG", 23, 42);
const ps4 = new Console("PS4", "Sony", 42, "ps4");

console.log(tvLG)
console.log(ps4)

tvLG.plugin()
ps4.plugin()

console.log(tvLG)
console.log(ps4)

tvLG.unplug()
ps4.unplug()

console.log(tvLG)
console.log(ps4)
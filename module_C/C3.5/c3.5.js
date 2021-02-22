class ElectricalAppliance {
    constructor (name, power) {
        this.name = name;
        this.power = power;
        this.isPlug = false;
    }

    plugin() {
        this.isPlug = true;
        console.log(this.name + " plugged!");
    };

    unplug() {
        this.isPlugged = false;
        console.log(this.name + " unplugged!");
    };
};


class Tv extends ElectricalAppliance {
    constructor (name, power, brand, size) {
        super(name, power);
        this.brand = brand;
        this.size = size;
        this.isPlug = false;
    }
}


class Console extends ElectricalAppliance {
    constructor (name, power, brand, model) {
        super(name, power)
        this.brand = brand;
        this.model = model;
        this.isPlug = false;
    }
}

const tvLG = new Tv("TV", 23, "LG", 42);
const ps4 = new Console("PS4", 42,  "Sony", "ps4 slim");

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
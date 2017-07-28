class Person{
	constructor (first_name, last_name, address){
		this.first_name = first_name;
		this.last_name = last_name;
		this.address = address;
	}
	getFullName(): function(first_name, last_name){
		return this.first_name + this.last_name;
	}
	getAddress(): function(address){
		return this.address;
	}
}
var Tom_Cruise = new Person("Tom", "Cruise",  "1111 Calle Vista Dr, Beverly Hills, CA");
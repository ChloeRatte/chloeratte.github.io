class Person{
	constructor (firstName, lastName, address){
		this.first_name = firstName;
		this.last_name = lastName;
		this.address = address;
		}
		getFullName(){
			return this.first_name + this.last_name;
		}
		getAddress(){
			return this.address;
		}
	}
var Tom_Cruise = new Person("Tom", " Cruise",  "1111 Calle Vista Dr, Beverly Hills, CA");
var name = Tom_Cruise.getFullName();
document.getElementById("myName").innerHTML = name;
var address = Tom_Cruise.getAddress();
document.getElementById("myAddress").innerHTML = address;


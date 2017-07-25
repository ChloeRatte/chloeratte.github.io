function bigImg(x) {
    x.style.height = 400;
    x.style.width = 400;
}

function normalImg(x) {
    x.style.height = 200;
    x.style.width = 200;
}

var tog = true;
function myFunction(){
	if(tog){
		document.getElementById("demo").innerHTML = "My full name is Chloe Jade Ratte, and I live in New Jersey with my mom, dad, and brother. I love webcomics, reading, writing, and, now, coding! I am a rising junior at Bloomfield High, where I took an introductory java course. I have one younger brother, a cat, and a tortoise. I am now in girls who code, and have completed multiple Scratch projects. I hope to enjoy my time here.";	
	}
	else{
		document.getElementById("demo").innerHTML = " ";
	}
	tog = !tog;
}
function myFunction2(){
	if(tog){
		document.getElementById("demo").innerHTML = "";	
	}
	else{
		document.getElementById("demo").innerHTML = " ";
	}
	tog = !tog;
}
function myFunction3(){
	if(tog){
		document.getElementById("demo").innerHTML = "My full name is Chloe Jade Ratte, and I live in New Jersey with my mom, dad, and brother. I love webcomics, reading, writing, and, now, coding! I am a rising junior at Bloomfield High, where I took an introductory java course. I have one younger brother, a cat, and a tortoise. I am now in girls who code, and have completed multiple Scratch projects. I hope to enjoy my time here.";	
	}
	else{
		document.getElementById("demo").innerHTML = " ";
	}
	tog = !tog;
}
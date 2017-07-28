function bigImg(x) {
    x.style.height = 300;
    x.style.width = 300;
}

function normalImg(x) {
    x.style.height = 200;
    x.style.width = 200;
}

window.onload = function quote(){
    var a = Math.floor(Math.random() * 11);
	if(a == 0){
		document.getElementById("contain2").innerHTML = "Stars & Stardust in infinite space is my only home.";
	}
	if(a == 1){
		document.getElementById("contain2").innerHTML = "Things start and things end, and isn't it lovely, in theory?";
	}
	if(a == 2){
		document.getElementById("contain2").innerHTML = "We may be doomed to fail, but we must not fail to try.";
	}
	if(a == 3){
		document.getElementById("contain2").innerHTML = "He is holding a cat.";
	}
	if(a == 4){
		document.getElementById("contain2").innerHTML = "Tell those with power, safe in their tower, we will not obey.";
	}
	if(a == 5){
		document.getElementById("contain2").innerHTML = "Death is only the end if you assume the story is about you.";
	}
	if(a == 6){
		document.getElementById("contain2").innerHTML = "Do not let numbers define you. You are blood and earth, not theory and chalk.";
	}
	if(a == 7){
		document.getElementById("contain2").innerHTML = "There is a thin, semantic line between weird and beautiful, and that line is covered in jellyfish.";
	}
	if(a == 8){
		document.getElementById("contain2").innerHTML = "We all make choices. But, in the end, our choices make us.";
	}
	if(a == 9){
		document.getElementById("contain2").innerHTML = "You won, and she choose you, and she loved you, and she's gone.";
	}
	if(a == 10){
		document.getElementById("contain2").innerHTML = "Why won't you let yourself just be whoever you are?";
	}
}

var tog = true;
var tog3 = true;
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
	if(tog3){
		document.getElementById("demo").innerHTML = "email: chloeratte88@gmail.com";	
	}
	else{
		document.getElementById("demo").innerHTML = " ";
	}
	tog3 = !tog3;
}
#!/usr/bin/node
let a = Math.floor(Number(process.argv[2]));
let b = Math.floor(Number(process.argv[3]));
function add(a, b){
	console.log(a + b);
};
add(a, b);

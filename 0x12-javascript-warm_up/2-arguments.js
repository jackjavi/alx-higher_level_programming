#!/usr/bin/node
const count = process.argv.length;
console.log(count === 2 ? 'No arguement' : count === 3 ? 'Arguement found' : 'Arguements found');

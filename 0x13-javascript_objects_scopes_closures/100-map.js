#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((mem, index) => {return mem * index});
console.log(list);
console.log(newList);

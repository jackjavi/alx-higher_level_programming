#!/usr/bin/node

const { readFile } = require("fs");

const filename = process.argv[2];
readFile(filename, "utf8", (err, result) => {
	if (err) {
		console.log(err);
		return;
	}
	console.log(result);
	return;
})

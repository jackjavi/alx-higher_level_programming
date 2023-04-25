#!/usr/bin/node

const { writeFile } = require("fs");

const path = process.argv[2];
const content = process.argv[3];

writeFile(
	path,
	content,
	(err) => {
		if (err) {
			console.log(err);
		}
	});

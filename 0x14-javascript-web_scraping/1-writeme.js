#!/usr/bin/node

/*
  Script that writes a string to a file.

  Usage: ./1-writeme.js <file-path> <string-to-write>

  The first argument is the file path.
  The second argument is the string to write.
  The content of the file must be written in utf-8.
  If an error occurred during writing, print the error object.
*/

const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});

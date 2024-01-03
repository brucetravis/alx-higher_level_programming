#!/usr/bin/node

/*
  Script that gets the contents of a webpage and stores it in a file.

  Usage: ./5-request_store.js <URL> <file-path>

  The first argument is the URL to request.
  The second argument is the file path to store the body response.
  The file must be UTF-8 encoded.
  You must use the module request.
*/

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});

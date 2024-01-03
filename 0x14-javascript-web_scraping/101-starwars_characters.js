#!/usr/bin/node

/*
  Script that prints all characters of a Star Wars movie.

  Usage: ./101-starwars_characters.js <Movie-ID>

  The first argument is the Movie ID - example: 3 = “Return of the Jedi”.
  Display one character name per line in the same order of the list “characters” in the /films/ response.
  You must use the Star Wars API.
  You must use the module request.
*/

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const charactersUrls = movie.characters;

    charactersUrls.forEach((characterUrl) => {
      request(characterUrl, (err, res, charBody) => {
        if (err) {
          console.error(err);
        } else {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    });
  }
});

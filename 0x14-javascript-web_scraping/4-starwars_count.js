#!/usr/bin/node

/*
  Script that prints the number of movies where the character “Wedge Antilles” is present.

  Usage: ./4-starwars_count.js <API-URL>

  The first argument is the API URL of the Star Wars API: https://swapi-api.alx-tools.com/api/films/.
  Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API.
  You must use the module request.
*/

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const moviesWithWedgeAntilles = films.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );

    console.log(moviesWithWedgeAntilles.length);
  }
});

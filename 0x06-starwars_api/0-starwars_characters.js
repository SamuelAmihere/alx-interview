#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi.dev/api/films';

function fetchCharacterNames (characterUrls) {
  return characterUrls.map((url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, _, body) => {
        if (error) {
          reject(error);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  });
}

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const movieUrl = `${API_URL}/${movieId}/`;

  request(movieUrl, (err, _, body) => {
    if (err) {
      console.log(err);
      return;
    }

    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    const characterPromises = fetchCharacterNames(characterUrls);

    Promise.all(characterPromises)
      .then((names) => {
        console.log(names.join('\n'));
      })
      .catch((error) => {
        console.log(error);
      });
  });
}

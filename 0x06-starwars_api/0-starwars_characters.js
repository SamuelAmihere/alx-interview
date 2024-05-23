#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi.dev/api/films';

function fetchCharacterNames(characterUrls) {
    return characterUrls.map(url => {
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

    console.time('Total time for getCharacters');

    request(movieUrl, (err, _, body) => {
        console.timeEnd('Total time for getCharacters');

        if (err) {
            console.error('An error occurred:', err);
            return;
        }

        const movieData = JSON.parse(body);
        const characterUrls = movieData.characters;

        console.time('Time for fetching character data');

        const characterPromises = fetchCharacterNames(characterUrls);

        Promise.all(characterPromises)
            .then(names => {
                console.timeEnd('Time for fetching character data');
                console.log(names.join('\n'));
            })
            .catch(error => {
                console.error('An error occurred:', error);
                console.timeEnd('Time for fetching character data');
            });
    });
} else {
    console.error('Please provide a movie ID as a positional argument.');
    process.exit(1);
}


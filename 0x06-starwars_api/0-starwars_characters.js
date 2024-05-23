#!/usr/bin/node
const request = require('request');

function getCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    request(url, (error, response, body) => {
        if (error) {
            console.error('An error occurred:', error);
            return;
        }

        const movieData = JSON.parse(body);
        const characterUrls = movieData.characters;

        characterUrls.forEach((characterUrl, index) => {
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error('An error occurred:', error);
                    return;
                }

                const characterData = JSON.parse(body);
                console.log(characterData.name);
            });
        });
    });
}

const movieId = process.argv[2];
if (!movieId) {
    console.error('Please provide a movie ID as a positional argument.');
    process.exit(1);
}

getCharacters(movieId);

#!/usr/bin/node
const inputSize = parseInt(process.argv[2]);
let squareIndicator = '';
if (!inputSize) {
 console.log('Missing size');
} else {
     for (let i = 0; i < inputSize; i++) {
       for (let j = 0; j < inputSize; j++) {
         squareIndicator += 'X';
       }
    if (i !== inputSize - 1) {
     squareIndicator += '\n';
  }
 }
 console.log(squareIndicator);
}

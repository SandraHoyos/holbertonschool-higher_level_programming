#!/usr/bin/node
const inputSize = parseInt(process.argv[2]);
let squareIndicator = '';
if (!inputSize) {
 console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}

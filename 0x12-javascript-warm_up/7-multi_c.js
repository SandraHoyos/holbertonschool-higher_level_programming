#!/usr/bin/node

const x = parseInt(process.argv[2]);
let argsCount = 0;

if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
while (argsCount < x) {
  console.log('C is fun');
  argsCount++;
}

#!/usr/bin/node

const argsToConvert = parseInt(process.argv[2]);
if (!argsToConvert) {
  console.log('Not a number');
}
else {
    console.log('My number: '+ argsToConvert);
}

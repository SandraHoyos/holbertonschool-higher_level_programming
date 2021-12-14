#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let number = process.argv;
  number.sort();
  number.slice(2);
  console.log(parseInt(number[number.length - 2]));
}

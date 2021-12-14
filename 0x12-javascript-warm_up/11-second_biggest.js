#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let number = process.argv;
  number.slice(2);
  number.sort();
  console.log(parseInt(number[number.length - 2]));
}

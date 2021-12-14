#!/usr/bin/node
const max = process.argv;
if (!max[3]) {
  console.log(0);
} else if (max[2] && max[3]) {
  max.sort();
  const number = max.length;
  console.log(parseInt(max[number - 2]));
}

#!/usr/bin/node
let num = 0;
const args = process.argv.splice(2);
if (args.length > 1) {
  args.sort();
  num = args.reverse();
}
console.log(parseInt(num[1]));

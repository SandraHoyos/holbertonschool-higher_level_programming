#!/usr/bin/node
let num = 0;
let args = process.argv.slice(2);
if (args.length > 1) {
args.sort();
num = args[args.length - 2];
}
console.log(parseInt(num));

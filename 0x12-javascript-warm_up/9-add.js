#!/usr/bin/node
function add (a, b) {
  result(a + b);
  return result;
}

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
add(num1, num2);
console.log(add(num1, num2));

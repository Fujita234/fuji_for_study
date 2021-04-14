const fetch = require('node-fetch');

process.stdin.resume();
process.stdin.setEncoding('utf8');
// Your code here!

const abc = 
  fetch('https://yesno.wtf/')
  .then(response => response.json())
  .then(jsonData => console.log(jsonData))

console.log("XXXXXXXX")

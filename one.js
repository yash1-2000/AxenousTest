const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
   
//   readline.question('Who are you?', name => {
//     console.log(`Hey there ${name}!`);
//     readline.close();
//   });

const name = readline.question('Who are you?', name => {
    readline.close();
    return name
  });

console.log(`hi ${name}`)
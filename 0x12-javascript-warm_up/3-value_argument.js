#!/usr/bin/node

const args = process.argv.slice(2);

if (args !== null) {
  args.forEach((arg, index) => {
    console.log(`${args}`);
  });
} else {
  console.log('No argument');
}

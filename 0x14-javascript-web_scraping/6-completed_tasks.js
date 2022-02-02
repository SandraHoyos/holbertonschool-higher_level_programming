#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const allTodos = JSON.parse(body);
    const complete = {};
    allTodos.forEach((todo) => {
      if (todo.completed && complete[todo.userId] == null) {
        complete[todo.userId] = 1;
      } else if (todo.completed) {
        complete[todo.userId] += 1;
      }
    });
    console.log(complete);
  }
});

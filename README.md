# MY FINAL PROJECT

The goal of the final project is a visibility web page of my work.

- What does it do?  
  Example: "This is a web project which shows my various engagements."

- What is the "new feature" which you have added that we haven't seen before?  
  Example: "For security reasons I have decided not to use my email adress."

## Prerequisites

There are no additional modules to be installed.

## Project Checklist

- [] It is available on GitHub.
- [] It uses the Flask web framework.
- [] It makes use of HTML and CSS in the front end.
- [] It makes use of the reading and writing to a file feature.
- [] It lets the user enter a value in a text box at some point.
  This value is received and processed by my back end Python code.
- [] It doesn't generate any error message even if the user enters a wrong input.
- [] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code.
- All user feedback is visible in the browser.
- [] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.

## Project Best Points

- The solution functions from the begining to the end as the user has defined it.
- The components interactions between.
- In the context of communication between main (index.html) and contact (contact.html) page there are different phases of interaction. (i) The simple interaction could be described as: user types URL (local host) into navigator; navigator sends GET request to Flask; Flask receptions the GET request; html file is found on the disk; Flask sends html to navigator; navigator presents the page html together with css; user sees the first page. (ii) The complexe interaction with submit form could be described as: user charges the contact form and it fulfills the form; user presses the submit button in navigator; the contact form is sent via request POST; application Flask receives the POST; it extracts the files; Flask process the files via different ways (database, email, txt.file); Flask responds to user via browser

## Project Pain Points

- It does not use at least one module from the Python Standard Library other than the random module.
- It does not contain at least one class written by my that has both properties and methods. This includes instantiating the class and using the methods in my app.
- It does not make use of JavaScript in the front end and use the localStorage of the web browser.
- It does not use modern JavaScript (for example, let and const rather than var).
- It does not contain conditional statements.
- It does not contain loops.

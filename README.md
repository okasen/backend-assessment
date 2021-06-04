![Generic badge](coveragebadge.svg)

![Generic badge](https://img.shields.io/github/workflow/status/okasen/backend-assessment/Python%20package?style=for-the-badge)
## About these tasks ##

These tasks were completed as part of backend team induction exercises, meant to grow and improve professional development skills. The tasks are basic, but are as follows:

Task 1: Create an extra field from the provided user JSON (in assets) for a full name, created from the existing forename and surname.

Task 2: Create a method to show only records of users over 30 years old.

Task 3: Replace the "company ID" field with a nesting "company" field, containing the information from the company JSON provided in assets.

### My processes for solving ###

I used a Test Driven Development pattern to solve these tasks, going through a Red, Green, Refactor pattern to create the best code I could! In effect, I first created tests that would determine that the code was behaving properly. Then, I created actual classes and methods that were capable of passing the test (but just barely/non-elegantly). At this point, I made pull requests for my colleages to review. Using their guidance, I refactored my code to be better. In these cases, better meant:

- using existing libraries to streamline code
- making my code more single-responsibility and DRY-adhering
- making my code more legible and clear
- testing more efficiently, and not introducing logic into the tests
- many other things!

I completed each task in the red-green-refactor pattern one by one. Then, I started to analyse the codebase as a whole using a variety of static analysis and testing tools (namely using pre-commit to run mypy, flake8, black, etc). I also ran code coverage reports and mutation testing.

Finally, I set up a CI pipeline with github actions. I spent a lot of time customising the YAML, mostly because I wanted my coverage test to automatically commit a coverage percentage badge with each run of the workflow. I am happy to say that it succeeded, and that the coverage badge at the top of this readme is *automatically updated with each push to Master!*

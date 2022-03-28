# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, slack, or any other method with the owners of this repository before making a change.
Please note we have a code of conduct, please follow it in all your interactions with the project.

## Getting started

### Prerequisites

- Install [Vagrant](https://www.vagrantup.com/downloads).
- Install [Virtual Box](https://www.virtualbox.org/wiki/Downloads).
- Install [Python 3.9](https://www.python.org/downloads/).

### Getting a copy of the repository

1. Go to the [Xpense](https://github.com/redhat-beyond/Xpense) GitHub repository.
2. Fork the repository and create a separate branch regarding your contribution.
3. Clone your forked repository to your local machine. the command should be something like: `git clone https://github.com/<YOUR_GITHUB_NAME>/Xpense.git`
4. Open any terminal and navigate to the project directory.

### How to run the project

1. Run the `vagrant up` command in the project directory.
2. Use any browser and navigate to - http://localhost:8000

After the dependencies were installed and the VM initialized, you can proceed working on the project code.

# Pull Request Process

1. Create Issue with relevant information about your PR
2. Fork the repository on GitHub
3. Clone the project to your own machine
4. create a branch with relevant name for your pr
5. Commit changes to your own branch
6. push your work back up to your forked repo
7. Submit a Pull Request so that we can review your changes
8. Link the PR to the relevant issue
9. Send the PR to the slack group and ask for reviewers(one student and one mentor at least)
10. Ensure that your code follows the PEP 8 Style guide for Python code before submitting a pull request.
    We have also set up Flake8 to ensure that our style guides are being followed(PR's that don't pass this may not get reviewed until those are solved)
11. Make sure the PR passes CI checks.

# Pull Request Standards

- Each Pull Request should focus on single responsibility principle.
- **The Pull Request should not break any of the existing functionality**
- <ins>Description-</ins> the PR description should explain what changes have been made, and why. In addition, they should include a link to the relevant `issue`
- Each pull request requires the approval of at least <ins>1 team members</ins> and one mentor before merging.
- The Pull Requests title should be in the format of: <Component name>: explanation in a few words

**Note: Be sure to fetch and merge the latest changes from the "upstream" repository before making a pull request!**

**Note: If your PR do not meet one of the requirements, the PR will not be reviewed!**

### Commiting:

• Please read this: [How to Write a Git Commit Message](https://cbea.ms/git-commit/) and follow the guidelines.

• Make sure the commit is [signed-off](https://docs.pi-hole.net/guides/github/how-to-signoff/)

# Issues

### What can I work on

Scan through our existing issues to find one that interests you. You can narrow down the search using labels as filters. See
[Labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) for more information. We assign issues to specific contributors, although you are more than welcome to open a PR with a fix if you find an issue to work on.

### Create a new issue

If you spot a problem/bug or think that some changes are needed , search if an issue already exists. If a related issue doesn't exist, you can open a new issue using a relevant issue form.

### Issue template

• **Title**
Must be clear, concise, and accurately describe what the issue is about.

• **Description**
Must include a clear explanation about the reasons for doing the work. Preferably in the form of a user story
that clearly mentions the stakeholders involved and their wishes.

• **Acceptance criteria**
Must be a list of measurable achievements that indicate the work in the issue is done.

##### Issue reporting guidelines

• When describing issues try to phrase your issue in terms of the behavior you think needs changing rather than the code you think needs changing.

• If reporting a bug, then try to include a pull request with a failing test case. This will help us quickly identify if there is a valid issue, and make sure that it gets fixed more quickly if there is one.

• Closing an issue doesn't necessarily mean the end of a discussion. If you believe your issue has been closed incorrectly, explain why and we'll consider if it needs to be reopened.

### Reviewing PRs:

1. Always provide constructive feedback
2. Keep your ego out of code reviews
3. Be precise about what needs to be improved
4. Don't just hope for the code to work, Check it yourself!
5. Be strict about temporary code
6. Visualize the bigger picture

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

#### Examples of behavior that contributes to creating a positive environment include:

• Using welcoming and inclusive language

• Being respectful of differing viewpoints and experiences

• Gracefully accepting constructive criticism

• Focusing on what is best for the community

• Showing empathy towards other community members

#### Examples of unacceptable behavior by participants include:

• The use of sexualized language or imagery and unwelcome sexual attention or advances

• Trolling, insulting/derogatory comments, and personal or political attacks

• Public or private harassment

• Publishing others' private information, such as a physical or electronic address, without explicit permission

• Other conduct which could reasonably be considered inappropriate in a professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.
Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces when an individual is representing the project or its community. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing or otherwise unacceptable behavior may be reported by contacting the project team on GitHub. All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality about the reporter of an incident. Further details of specific enforcement policies may be posted separately.
Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the Contributor Covenant, version 1.4, available at http://contributor-covenant.org/version/1/4

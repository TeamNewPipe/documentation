# Prepare everything

Welcome to the NewPipe tutorial. This tutorial will guide you through the process of creating your own NewPipeExtractor
service with which NewPipe will gain support for a dedicated streaming service like YouTube, Vimeo or SournCloud. Let's
dive right. ;D

## Setup your dev environment

First and foremost you need to meet certain conditions in order to write your own service.

### What you need to know

- Basic understanding of __[git](https://try.github.io)__
- Good __[Java](http://whatpixel.com/best-java-books/)__ knowledge
- Good understanding of __[web technology](https://www.w3schools.com/)__
- Basic understanding about __[unit testing](http://www.vogella.com/tutorials/JUnit/article.html)__ and __[JUnit](https://junit.org/)__
- Flawless understanding of how to [contribute](https://github.com/TeamNewPipe/NewPipe/blob/dev/.github/CONTRIBUTING.md#code-contribution) to the __NewPipe project__

### What you need to have

- A dev environment/ide that supports:
    - __[git](https://git-scm.com/downloads/guis)__
    - __[java 8](https://www.java.com/en/download/faq/java8.xml)__
    - __[gradle](https://gradle.org/)__
    - __[unit testing](https://junit.org/junit5/)__
    - I highly recomend [IDEA Community](https://www.jetbrains.com/idea/) since it has everything we need.
- A __[github](https://github.com/)__ account
- A loot of patience and excitement ;D

After making sure all these conditions are provided fork the [NewPipeExtractor](https://github.com/TeamNewPipe/NewPipeExtractor),
using the [fork button](https://github.com/TeamNewPipe/NewPipeExtractor#fork-destination-box).
This way you have your own working repository. Now clone this repository into your local folder in which you want to work in.
Next import the cloned project into your [ide](https://www.jetbrains.com/help/idea/configuring-projects.html#importing-project)
and [run](https://www.jetbrains.com/help/idea/performing-tests.html) it.
If all the checks are green you did everything right, and you are good to go to move on to the next chapter.
![tests passed on idea](img/prepare_tests_passed.png)

# Inclusion criteria for services

After creating you own service you will need to submit it to our [NewPipeExtractor](https://github.com/teamnewpipe/newpipeextractor)
 repository. However in order to include your changes you need to follow these rules:

1. Stick to our [Code contribution guidelines](https://github.com/TeamNewPipe/NewPipe/blob/dev/.github/CONTRIBUTING.md#code-contribution)
2. Do not send services that present content we [don't allow](#not-allowed-content) on NewPipe.
3. You need to be willing to keep on maintaining your service after submission.
4. Be patient and do the requested changes when one of our maintainers rejects your code.

## Allowed Content

- Basically anything except [NOT allowed content](#not-allowed-content).
- Any kind of porn/NSFW that is allowed according to the [US Porn act](https://www.justice.gov/archive/opa/pr/2003/April/03_ag_266.htm).
- Advertisement (may be handled specially tho)

## NOT allowed Content

- NSFL
- Porn that is not allowed according to [US Porn act](https://www.justice.gov/archive/opa/pr/2003/April/03_ag_266.htm).
- Any form of violence
- Child pornography
- Media that harms others
- Media that shows the violation of human rights
- Copyright infringement/pirated media




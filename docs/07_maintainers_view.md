# Maintainers' Section

These are some basic principles that we want maintainers to follow when maintaining NewPipe.


### Keep it Streamlined
NewPipe is a media player for devices on the Android platform, thus it is intended to be used for entertainment. This means it does not have to be some professional
application, and it does not have to be complicated to be used.
However NewPipe might not focus on the casual user completely as there are
some features designed for more experienced users which may require some knowledge about
code, however in essence NewPipe should be easy to use, even for an average Android user.

1. __Don't add too many special
  features.__ NewPipe does not have to be an airplane cockpit. Do not try to fill every single niche that might exist. If people wanted more advanced features, they
  would use professional tools. If you add too much functionality, you add complexity, and complexity scares away the average user. Focus on NewPipe's scope as a **media player** for the end user, and only as such. 
2. __Usability of the user interface should be prioritized.__ Try to make it comply with
  [material design guidelines](https://material.io/design/guidelines-overview/).
  

### Bugfixes

![kde_in_a_nutshell](img/kde_in_a_nutshell.jpg)]

*Disclaimer: This is a meme. Please don't take it personally.*

 __Always prioritize fixing bugs__, as the best application with the best features
   does not help much if it is broken, or annoying to use. Now if a program
   is in an early stage it is quite understandable that many things break. This
   is one reason why NewPipe still has no "1" in the beginning of its version
   number.
   By now, NewPipe is in a stage where there should be a strong focus on
   stability.

1. If there are multiple Pull Requests open, check the ones with bugfixes first.
2. Do not add too many features every version, as every feature will inevitably
    introduce more bugs. It is OK if PRs remain open for a while, but don't leave them open for too long.
3. If there are bugs that are stale, or open for a while bump them from time
   to time, so devs know that there is still something left to fix.
4. Never merge PRs with known issues. From our perception the community does not like to fix bugs, this is why you as a maintainer should
   especially focus on pursuing bugs.


### Features

Features are also something that can cause a headache. You should not blindly
say yes to features, even if they are small, but you should also not immediately say no. If you are not sure, try the feature, look into the
code, speak with the developer, and then make a decision. When considering a feature, ask yourself the following questions:

- Was the feature requested by only a few, or by many?
	- Avoid introducing niche features to satisfy a small handful of users.
- Was the code rushed and messy, and could a cleaner solution be made?	
	- A pull request that adds a frequently requested feature could implement the feature in a messy way. Such PRs should not be merged as it will likely cause problems later down the line, either through problems of extending the feature by introducing many bugs, or simply by breaking the architecture or the philosophy of NewPipe.
- Does the amount of code justify the feature's purpose? 
	- Use critical thinking when considering new features and question
whether that features makes sense, is useful, and if it would benefit NewPipe's users.



### Pull Requests

If a PR contains more than one feature/bugfix, be cautious. The more stuff a PR changes, the longer it will take to be added.
There also might be things that seem to not have any issues, but other things will, and this would prevent you from merging a PR. This is why it is encouraged to keep one change per pull request, and you should insist that contributors divide such PRs into multiple smaller PRs when possible.

### Community

When you talk to the community, stay friendly and respectful with good etiquette.
When you have a bad day, just don't go to GitHub (advice from our experience ;D ).




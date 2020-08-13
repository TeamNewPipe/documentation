# Releasing a New NewPipe Version

This site is meant for those who want to maintain NewPipe, or just want to know how releasing works.

![one does not simply push to master](img/onedoes.jpg)

## Differences Between Regular and Hotfix Releases

NewPipe is a web crawler. That means it does not use a web API, but instead tries to scrape the data from the website,
this however has the disadvantage of the app to break instantly when YouTube changes something.
We do not know when this happen. Therefore, maintainers need to act quickly when it happens, and reduce our downtime as
much as possible. The entire release cycle is therefore designed around this issue.

There is a difference between a release that introduces new features
and a release that fixes an issue that occurred because YouTube, or some other service, changed their website (typically called a shutdown).
Lets have a look at the characteristics of a __regular release__, and then the characteristics of a __hotfix release__.

## Regular Releases

Regular releases are normal releases like they are done in any other app. Releases are always stored on __master__ branch. The latest commit on
__master__ is always equal to the currently released version. No development is done on master. This ensures that we always have one
branch with a stable/releasable version.

### Feature Branching
When developing, the __dev__ branch is used. Pushing to __dev__ directly, however, is not allowed, since QA and testing should be done first before adding something to it.
This ensures that the dev version works as stable a possible.
In order to change something on the app, one may want to __fork__ the dev branch and develop the changes in their own branch (this is called feature branching).

![feature_branching](img/feature_branch.svg)

Make sure that both the dev branches, as well as the master branches of the extractor and the frontend, are compatible with each other.
If a change is done on the API to the extractor, make sure that frontend is compatible, or changed to become compatible, with these changes. If the PR that should make the frontend compatible
again can not be merged, please do not merge the corresponding PR on the extractor either. This should make sure that any developer can run his changes
on the fronted at any time.

### Merging Features/Bugfixes

After finishing a feature, one should open up a __Pull Request__ to the dev branch. From here, a maintainer can do __Code review__ and __Quality Assurance (QA)__.
If you are a maintainer, please take care about the code architecture so __corrosion__ or __code shifting__ can be prevented. Please also prioritize code quality over functionality.
In short: cool function but bad code = no merge. Focus on leaving the code as clean as possible.

![merge_feature_into_dev](img/merge_into_dev.svg)

You, as a maintainer, should build the app and put the signed APK into the description of that new pull request. This way, other people can test the feature/bugfix and help with QA. _You may not need to do this every time. It is enough to do it on bigger pull requests._

After the maintainer merges the new feature into the dev branch, he should add the title of the pull request or a summary of the changes into the [release notes](#release-notes).

### Creating a New Release

Once there are enough features together, and the maintainers believe that NewPipe is ready for a new release, they should create a new release.
Be aware of the rule that a release should never be done on a Friday. For NewPipe, this means: __Don't do a release if you don't have time for it!!!__
Below is a list of things you will want to do:

1. Fork the __dev__ branch into a new __release_x.y.z__ branch.
2. Increase the [version number](#version-nomenclature)
3. Merge [Weblate](https://hosted.weblate.org/projects/newpipe/) changes from the `dev` branch at `https://hosted.weblate.org/git/newpipe/strings/`.
4. Copy the [release notes](#release-notes) from the GitHub version draft into the corresponding fastlane file (see [release notes](#release-notes)).
5. Open up a pull request form the new __release_x.y.z__ branch into the __master__ branch.
6. Create an issue pointing to the new pull request. The reason for opening an issue is that from my perception, people read issues more than pull requests. Put the release-note into this pull request.
7. Build a signed release version of NewPipe using schabis signing keys. This is a release candidate (RC). Name the build apk file `NewPipe_<versionNumber>_RC1.apk`.
   Zip it and post it to the head of the release issue. This way, others can test the release candidate.
8. Test and QA the new version with the help of others.
9. Leave the PR open for a few days and advertise it to help testing.

While being in release phase no new pull requests must be merged into __dev__ branch.

This procedure does not have to be done for the extractor as extractor will be tested together with the fronted.

### Quickfixes

When issuing a new release, you will most likely encounter bugs that might not have existed in previous versions. These are called __regressions__.
If you find a regression during release phase, you are allowed to push fixes directly into the release branch without having to fork a branch away from it.
All maintainers have to be aware that they might be required to fix regressions, so plan your release at a time when
you are available. Do not introduce new features during the release phase.

When you have pushed a quickfix, you will want to update the __release candidate__ you put into the __issue__ corresponding to the __release pull request__.
Increment the version number in the filename of the release candidate. e.g. `NewPipe_<versionNumber>_RC2.apk` etc. _Don't update the actual version number. :P_

![release_branch](img/release_branch.svg)

### Releasing

Once the glorious day of all days has come, and you fulfill the ceremony of releasing.
After going through the release procedure of [creating a new release](#create_a_new_release) and maybe a few [quickfixes](#quickfixes) on the new release,
this is what you should do when releasing:

1. Click "Merge Pull Request".
2. Create a GPG signed tag with the name `v0.x.y`.
3. Merge __dev__ into master on the extractor.
4. Create a GPG signed tag with the name `v0.x.y` on the extractor.
5. Make sure the draft name equals the tag name. ![draft_name](img/draft_name.png)
6. Make sure to not have forgotten anything.
7. Click "Publish Release".
8. Clone [F-Droid / Data](https://gitlab.com/fdroid/fdroiddata).
9. Add the new version in `metadata/org.schabi.newpipe.yml`.
10. Run `fdroid signatures /path/to/newpipe.apk`.
11. Create a MR.
12. Rebase quickfix changes back into __dev__ if quickfixes were made.
13. Temporarily: [Update the changelog for the website](https://github.com/TeamNewPipe/website/blob/master/_includes/release_data.html).

![rebase_back](img/rebase_back_release.svg)

## Hotfix Releases

![this_is_fine](img/could_not_decrypt.png)

As aforementioned, NewPipe is a web crawler and could break at any moment. In order to keep the downtime of NewPipe as low as possible, when such a shutdown happens,
we allow __hotfixes__.



- A hotfix allows work on the master branch instead of the dev branch.
- A hotfix MUST __NOT__ contain any features or unrelated bugfixes.
- A hotfix may only focus on fixing what caused the shutdown.

### Hotfix Branch

Hotfixes work on the master branch. The dev branch has experimental changes that might have not been tested properly enough to be released, if at all. The master branch should always be the latest stable version of NewPipe. If the master branch breaks due to a shutdown, you should fix the master branch.
Of course you are not allowed to push to master directly so you will have to open up a __hotfix__ branch. _If someone else is pushing a hotfix into master, and it works this can be considered as hotfix branch as well._

![hotfix_branch](img/hotfix_branch.svg)

### Releasing

If you fixed the issue and found it to be tested and reviewed well enough, you may release it. You don't need to undergo the full release procedure of a regular release, which takes more time to release.
Keep in mind that if the hotfix might turn out to be broken after release, you should release another hotfix.
It is important to release quickly for the sake of keeping NewPipe alive, and after all, a slightly broken version of NewPipe is better then a non-functional version ¯\\\_(ツ)\_/¯.
Here's what you do when releasing a hotfix:

1. Click "Merge Pull Request"
2. Create a GPG signed tag with the name `v0.x.y`.
3. Merge __dev__ into master on the extractor.
4. Create a GPG signed tag with the name `v0.x.y` on the extractor.
5. Create a new release draft and write the down the fix into the release notes.
6. Copy the [release note](#release-notes) into the fastlane directory of releases.
7. Increment the __small minor__ version number and the `versionCode`.
8. Click "Publish Release".
9. Clone [F-Droid / Data](https://gitlab.com/fdroid/fdroiddata).
10. Add the new version in `metadata/org.schabi.newpipe.yml`.
11. Run `fdroid signatures /path/to/newpipe.apk`.
12. Create a MR.
13. Rebase the hotfix back into __dev__ branch.
14. Temporarily: [Update the changelog for the website](https://github.com/TeamNewPipe/website/blob/master/_includes/release_data.html).

![rebase_back_hotfix](img/rebase_back_hotfix.svg)

## Version Nomenclature

The version nomenclature of NewPipe is simple.

- __Major__: The __major__ version number (the number before the first dot) was 0 for years. The reason for this changed over time. First, I wanted this number to
  switch to 1 once NewPipe was feature complete. Now, I rather think of incrementing this number to 1 once we can ensure that NewPipe runs stable (part of which this documentation should help). After this, well, God knows what happens if we ever reach 1. ¯\\\_(ツ)\_/¯ 
- __Minor__: The __minor__ version number (the number after the first dot) will be incremented if there is a major feature added to the app.
- __Small Minor__: The small minor (the number after the second dot) will be incremented if there are bug fixes or minor features added to the app.


#### Version Nomenclature of the Extractor

The extractor is always released together with the app, therefore the version number of the extractor is identical to the one of NewPipe itself.

#### Version Code
In Android, an app can also have a [versionCode](https://developer.android.com/studio/publish/versioning). This code is a `long integer` and can be incremented by any value to show a device that a new version is there.
For NewPipe, the version code will be incremented by 10 regardless of the change of the major or minor version number. The version codes between the 10 steps
are reserved for our internal F-Droid build server.

## Release Notes
Release notes should tell what was changed in the new version of the app. The release nodes for NewPipe are stored in the [GitHub draft for a new release](https://github.com/TeamNewPipe/NewPipe/releases/tag/v0.14.0). When a maintainer wants to add changes to the release note, but there is no draft for a new version, they should create one.

Changes can be categorized into three types:

- __New__: New features that got added to the app.
- __Improved__: Improvements to the app or existing features
- __Fixes__: Bugfixes

When releasing a new version of NewPipe, before actually clicking "Release", the maintainer should copy the release notes from the draft and put it into a file called
`<versionCode>.txt` (whereas `<versionCode>` needs to be the version code of the incoming release). This file must be stored in the directory [`/fastlane/metadata/android/en-US/changelogs`](https://github.com/teamnewpipe/newpipe/tree/dev/fastlane/metadata/android/en-US/changelogs). This way, F-Droid will be able to show the
changes done to the app.

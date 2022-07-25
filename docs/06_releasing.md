# Releasing a New NewPipe Version

This site is meant for those who want to maintain NewPipe, or just want to know how releasing works.

![one does not simply push to master](img/onedoes.jpg)

## Differences Between Regular and Hotfix Releases

Depending on the service, NewPipe Extractor uses web crawling or internal APIs.
Both are subject to arbitrary changes by the service providers, like  YouTube, SoundCloud or PeerTube.
When they change something, NewPipe Extractor and thus NewPipe break instantly.
Therefore, maintainers need to act quickly when it happens, and reduce our downtime as
much as possible. The entire release cycle is therefore designed around this issue.

There is a difference between a release that introduces new features
and a release that fixes an issue that occurred because YouTube, or some other service,
changed their website (typically called a shutdown).
Let's have a look at the characteristics of a __regular release__,
and then the characteristics of a __hotfix release__.


## Regular Releases

Regular releases are normal releases as they are done in any other app.
Releases are always stored and tagged on __master__ branch. The latest commit on
__master__ is always equal to the currently released version. No development is done on master.
This ensures that we always have one branch with a stable/releasable version.

### Feature Branching
The __dev__ branch is used for development. Pushing to __dev__ directly, however, is not allowed,
since QA and testing should be done _before_ adding something to the branch.
This ensures that the development version works as stable a possible.
In order to change something on the app, one may want to __fork__ the dev branch
and develop the changes in their own branch (this is called feature branching).

![feature_branching](img/feature_branch.svg)

Make sure that both the dev branches, as well as the master branches of the extractor
and the frontend, are compatible with each other.
If the extractor's API is modified, make sure that frontend is compatible,
or changed to become compatible, with these changes.
If the PR that should make the frontend compatible
again can not be merged, please do not merge the corresponding PR on the extractor either.
This should make sure that any developer can run his changes on the fronted at any time.

### Merging Features/Bugfixes

After finishing a feature, one should open up a __Pull Request__ to the dev branch.
From here, a maintainer can do __Code review__ and __Quality Assurance (QA)__.
If you are a maintainer, please take care about the code architecture
so __corrosion__ or __code shifting__ can be prevented.
Please also prioritize code quality over functionality.  
In short: cool function but bad code = no merge. Focus on keeping the code as clean as possible.

![merge_feature_into_dev](img/merge_into_dev.svg)

An APK for __testing__  is provided by GitHub Actions for every PR.
Please ensure that this APK is tested thoroughly to prevent introducing regressions.
Testing features needs to take into account that NewPipe is used on a brought variety
of Android versions from KitKat to the latest, on custom ROMs like Lineage OS, CalyxOS or /e/
and different devices like phones, tablets and TVs.

Sometimes, the content of a PR changes over the time.
Modify the PR's title if it does not represent the introduced changes anymore.
After a maintainer merged the new feature into the dev branch,
they should add the PR's title or a summary of the changes into the [release notes](#release-notes).

### Normal Releases

Once there are enough changes, and the maintainers believe that NewPipe is ready
for a new version, they should prepare a new release.  
Be aware of the rule that a release should never be done on a Friday.
For NewPipe, this means: __Don't do a release if you don't have time for it!!!__

By following the steps listed in [Release instructions](../07_release_instructions), you can publish a stable version of NewPipe.

## Hotfix Releases

![this_is_fine](img/could_not_decrypt.png)

As aforementioned, NewPipe heavily relies on external components and might break at a random point of time.
In order to keep the NewPipe's downtime as low as possible, when such a shutdown happens,
we allow __hotfixes__.


- A hotfix allows work on the master branch instead of the dev branch.
- A hotfix MUST __NOT__ contain any features or unrelated bugfixes.
- A hotfix may only focus on fixing what caused the shutdown.

### Hotfix Branch

Hotfixes work on the master branch.
The dev branch has experimental changes that might have not been tested properly enough to be released,
if at all. The master branch should always be the latest stable version of NewPipe.
If the master branch breaks due to a shutdown, you should fix the master branch.
Of course, you are not allowed to push to master directly,
so you need to create a __hotfix__ branch. 
_If someone else is pushing a hotfix into master, and it works this can be considered as hotfix branch as well._

![hotfix_branch](img/hotfix_branch.svg)

### Releasing

If you fixed the issue and found it to be tested and reviewed well enough, you may publish a new version.
You don't need to undergo the full release procedure of a regular release, which takes too much time.
Keep in mind that if the hotfix might turn out to be broken after release, you should release another hotfix.
It is important to release quickly for the sake of keeping NewPipe alive, and after all,
a slightly broken version of NewPipe is better than a non-functional version ¯\\\_(ツ)\_/¯.
Here's what you do when releasing a hotfix:

1. Merge the corresponding pull request in the extractor.
2. [Publish the new extractor version](#extractor-releases).
3. Update the extractor version in the app's `build.gradle` file.
4. Create a new release draft and put some info on the fix into the [release note](#release-notes).
5. Copy the release notes into the fastlane directory to create a [changelog file](#changelog-file).
6. Increment the __small minor__ version number and the `versionCode`.
7. Generate a release APK (`gradlew assembleRelease`) and sign it (or get it signed by one of the other maintainers).
8. Add the signed APK to the GitHub release notes.
9. Click "Publish Release" .
10. [Publish the new version on F-Droid](#publish-on-f-droid).
11. Merge the changes from __master__ into __dev__.
12. [Update the changelog for the website](https://github.com/TeamNewPipe/website/blob/master/_includes/release_data.html).

![rebase_back_hotfix](img/rebase_back_hotfix.svg)

## Extractor releases
In general, the release process for extractor versions is not that complicated compared to app releases.
The extractor has (in difference to the app) a decent test coverage.
Additionally, the latest extractor version is typically tested in the app's latest __dev__ version.
Therefore, a long test phase is not needed when creating extractor releases.

To create a new [extractor version](#version-nomenclature-of-the-extractor), update the __version__ in the extractor's `build.gradle` file
as well as the version names in the README.
Merge the __dev__ branch into __master__.
The same that applies the app's [release notes](#release-notes) also applies to the extractor's release notes.

When publishing an extractor release via GitHub on the __master__ branch,
a new [JavaDoc version](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/)
is generated and published automatically.
Pleas keep an eye on the GitHub Action which is responsible for that.
If changes in that release introduced invalid JavaDoc, the build fails and needs to be fixed.
For this reason, you should check locally if there are any problems with the JavaDoc generation before publishing the new version.


## Version Nomenclature

The version nomenclature of NewPipe is simple.

- __Major__: The __major__ version number (the number before the first dot) was 0 for years.
  The reason for this changed over time. First, I wanted this number to
  switch to 1 once NewPipe was feature complete.
  Now, I rather think of incrementing this number to 1 once we can ensure that NewPipe runs stable
  (part of which this documentation should help).
  After this, well, God knows what happens if we ever reach 1. ¯\\\_(ツ)\_/¯ 
- __Minor__: The __minor__ version number (the number after the first dot)
  will be incremented if there is a major feature added to the app.
- __Small Minor__: The small minor (the number after the second dot)
  is incremented when bug fixes or minor features are added to the app.


#### Version Nomenclature of the Extractor

Previously, the extractor was released together with the app,
therefore the version number of the extractor was identical to the one of NewPipe itself.

We try to combine efforts to make NewPipe Extractor more independent of the app.
The extractor is used by multiple other applications
and therefore releasing extractor updates should not be coupled to app releases.
However, maintainers need to keep an eye on making the app compatible with extractor changes.

## Release Notes
Release notes should tell what was changed in the new version of the app.
The release notes for NewPipe are stored in the
[GitHub draft for a new release](https://github.com/TeamNewPipe/NewPipe/releases).
When a maintainer wants to add changes to the release notes,
but there is no draft for a new version, they should create one.

Changes can be categorized into five basic types:

- __New__: New features that got added to the app.
- __Improved__: Improvements to the app or existing features
- __Fixed__: Bugfixes
- __Translation__: New translations
- __Development__: Changes which address things "under the hood",
  which do not have any recognizable effect to the user; e.g. dependency updates or changes to the build process

When adding a PR to the release notes, increase the PR counter at the top of the draft
and put the number before the PR summary / title.
This helps the blog post authors to keep easily track of  new PRs.
Remove the numbers before publishing a new version :)

If there is a blog post covering the changes in more detail,
make sure to link it on the top of the release notes.
It would be a pity, if only a few people read the blog post
after our wonderful writers put so much effort into creating it.

### Changelog file

Maintainers need to provide a changelog file for each release.
A changelog file is used by F-Droid to give a quick summary of the most important changes for a release.
This file is placed in the 
[`/fastlane/metadata/android/en-US/changelogs`](https://github.com/teamnewpipe/newpipe/tree/dev/fastlane/metadata/android/en-US/changelogs)
directory and named `<versionCode>.txt` (whereas `<versionCode>` is the version code of the incoming release).
Changelog files *must not* exceed 500 bytes.
Be aware that the changelog is translated into multiple languages.
A changelog written in English which almost hits 500 bytes can hardly be translated completely within this limit.
This causes troubles for translators, because Weblate enforces the 500 bytes limit, too.
For this reason it is recommended to keep the changelog at 400 bytes.

When creating the changelog file be aware of changes which were done in the extractor as well.  
Before pushing the changelog to NewPipe's repo, ask other maintainers to review it.  
After pushing the changelog to NewPipe's GitHub repo, [updating Weblate](../09_maintainers_view#update-weblate) is necessary.
This enables translators to work on localized versions of the changelog before a release is tagged and published.

## Publish on F-Droid

NewPipe is and supports open source software.
For this reason, the preferred way to distribute the app is [F-Droid](https://f-droid.org).
F-Droid is a catalogue of FOSS apps and also comes with an Android client which handles app updates.
There are two ways to install NewPipe via F-Droid.

1. **Through the main F-Droid repository**  
    NewPipe's metadata file can be found in F-Droid's data repository on GitLab:
    [https://gitlab.com/fdroid/fdroiddata/-/blob/master/metadata/org.schabi.newpipe.yml](https://gitlab.com/fdroid/fdroiddata/-/blob/master/metadata/org.schabi.newpipe.yml)  
    This file is automatically updated by a bot when a new release is published on GitHub.
    It can take a few days until all new apps on F-Droid are built, signed and published.  
    [F-Droid also supports reproducible builds](https://f-droid.org/docs/Reproducible_Builds/).
    Reproducible builds or deterministic builds allow someone else to retrieve the exact same binary
    as we get when building the app (except the signing of course).  
    When the reproducible build feature is enabled for an app in F-Droid, they compare their binary to one provided by the author.
    If both are identical, F-Droid does not only publish the binary signed by themselves, but also the one signed by the author.  
    Currently, NewPipe's builds are not deterministic, and we therefore cannot use that feature.
    Once the builds are deterministic again, the following steps need to be done to publish a new version on F-Droid:
    1. [Install `fdroidserver` on your device](https://f-droid.org/docs/Installing_the_Server_and_Repo_Tools/).
    * Clone the F-Droid Data repo from `https://gitlab.com/fdroid/fdroiddata`
    * Add the new version to `metadata/org.schabi.newpipe.yml`
    * Run `fdroid signatures /path/to/newpipe.apk` on the signed APK from within the repo.
    * Create a MR on GitLab.
    An example commit containing all required changes can be found [here](https://gitlab.com/fdroid/fdroiddata/-/commit/393bbb756d5bed4134eb147f411a9d9aa1d47386).
3. **Through NewPipe's F-Droid repository**  
    F-Droid needs 
    NewPipe's own F-Droid repo is available at [https://archive.newpipe.net/fdroid/repo](https://archive.newpipe.net/fdroid/repo/?fingerprint=E2402C78F9B97C6C89E97DB914A2751FDA1D02FE2039CC0897A462BDB57E7501)
    It is updated and maintained by [@TheAssassin](https://github.com/TheAssassin).

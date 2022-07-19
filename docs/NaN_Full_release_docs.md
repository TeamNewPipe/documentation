### Preliminary steps

#### Permissions

- have admin rights on Weblate
    - you should be able to access [Weblate's Maintenance page](https://hosted.weblate.org/projects/newpipe/#repository)
- have at least maintainer rights on the NewPipe and NewPipeExtractor repos

#### Repositories

- have a cloned NewPipe local repository (for the rest of the page, `origin` is assumed to be the remote at `github.com/TeamNewPipe/NewPipe`)
- add the `weblate` remote to the same local repository (the URL used below can be found on the Maintenance page on Weblate)
    - `git remote add weblate https://hosted.weblate.org/git/newpipe/strings/`
- make sure there are no pending changes
    - `git clean -fdx` to **discard** them all (**CAUTION**)
- switch to the `dev` branch and make sure it is up-to-date with the remote:
    - `git checkout dev`
    - `git pull origin dev`

#### Version name and conventions

- find the version code of the next release by looking for `versionCode` in [`app/build.gradle`](https://github.com/TeamNewPipe/NewPipe/blob/dev/app/build.gradle): 1 added to that value (from now on called `NEW_VERSION_CODE`) will be the new value (but do not edit the file yet)
- choose the version number of the next release according to [semantic versioning](http://semver.org/) (from now on called `X.X.X`)

#### Identification

- have `gpg` installed and usable on your PC
- have a GPG key, which can be used to verify that a file is really from you

### Pull changes from Weblate

- go to [Weblate's Maintenance tab](https://hosted.weblate.org/projects/newpipe/#repository)
- press the *Lock* button to prevent translators from translating while you are creating commits; remember to *Unlock* later!
- press the *Update* button to update Weblate with the latest changes on NewPipe's `dev` branch
- press the *Commit* button, if needed, to make sure Weblate creates a commit for translations which had not been committed yet
- now go back to the local git repository
- in case you followed these steps before, delete the `weblate-dev` branch
    - `git branch -D weblate-dev`
- fetch new changes from the `weblate` remote
    - `git fetch weblate`
- create a new branch starting from `weblate/dev`, named `weblate-dev`, and switch to it
    - `git checkout -b weblate-dev weblate/dev`
- if you run `git log --oneline --graph` you should see a Weblate commit on top, and then all of the commits currently on the `dev` branch:
    ```
    * cmt12hash (HEAD -> weblate-dev, weblate/dev) Translated using Weblate (...)
    * cmt89hash (origin/dev, dev) Commit message ...
    ```
- switch back to the `dev` branch
    - `git checkout dev`
- merge `weblate-dev` into `dev`:
    - `git merge weblate-dev`

### Create a changelog

- finalize the draft changelog [kept on GitHub](https://github.com/TeamNewPipe/NewPipe/releases), in case there are still some things to fill in
    - remove the temporary instructions, and the numbers before `-` which keep track of the order in which the PRs were merged, as that info is useful only for the blog post writers
    - before removing that information, you may want to send the original changelog to the blogpost writers
- create a new English changelog in the [`fastlane/metadata/android/en-US/changelogs/`](https://github.com/TeamNewPipe/NewPipe/blob/dev/fastlane/metadata/android/en-US/changelogs/) folder
- the file should be named `NEW_VERSION_CODE.txt`, using the new version code found in the [Preliminary steps](#preliminary-steps)
- the file should have this structure (sections with no points can be removed):
    ```
    New
    • ...

    Improved
    • ...

    Fixed
    • ...
    ```
- make sure you use the `•` for points (it looks nicer than `-`)
- capitalize the first letter in each point
- use English verbs as if you were asking someone to do something, so for example use "Fix abc" and not "Fixed abc"; this allows saving a few characters and using a consistent style
- prepend `[SERVICE]` to service-only changes (e.g. "• \[YouTube\] Add mixes")
- summarize only the most important changes from the draft release [kept on GitHub](https://github.com/TeamNewPipe/NewPipe/releases) (it contains all merged pull requests)
- make sure the file size is **at most 500 bytes**, in order to **fit [F-Droid's changelog size limit](https://f-droid.org/en/docs/All_About_Descriptions_Graphics_and_Screenshots/#fastlane-structure) (!)**
- commit the file on the `dev` branch (try to stick to the provided commit message template)
    - `git add fastlane/metadata/android/en-US/changelogs/NEW_VERSION_CODE.txt`
    - `git commit -m "Add changelog for vX.X.X (NEW_VERSION_CODE)"`

### Push the changelog to Weblate

Now there should be two new commits (the Weblate and changelog ones) on your local `dev` branch, which are not on NewPipe's remote `dev` branch.
- if you are an admin of the NewPipe repo, just push the changes to the remote `dev`
    - `git push origin dev`
    - if you are not an admin, create a pull request normally and ask someone with maintainer access to merge it
- go to [Weblate's Maintenance tab](https://hosted.weblate.org/projects/newpipe/#repository)
- press the *Update* button to update Weblate with the commit you just pushed on NewPipe's `dev` branch
- **press the *Unlock*** button to allow translators to translate the changelog and possibly other components (**do not forget this step!**)
- note that we had to do this process on NewPipe's `dev` branch because:
    - Weblate's components are connected to NewPipe's `dev` branch, and will update changes from there
    - Weblate's git repo is not writable, so there is no way to push commits there manually

### Creating the release branch

- create a new branch starting from `dev`, named `release-X.X.X`, and switch to it
    - `git checkout -b release-X.X.X`
- edit the [`app/build.gradle`](https://github.com/TeamNewPipe/NewPipe/blob/dev/app/build.gradle) file to update the extractor
    - set the NewPipeExtractor dependency version to a suitable one (usually [the last commit in the NewPipeExtractor repo](https://github.com/TeamNewPipe/NewPipeExtractor/commits/dev))
- commit the extractor update (if you used a specific version, append `to VERSION` to the commit message)
    - `git add app/build.gradle`
    - `git commit -m "Update NewPipeExtractor"`
- edit the [`app/build.gradle`](https://github.com/TeamNewPipe/NewPipe/blob/dev/app/build.gradle) file to bump the release
    - set `versionCode` to `NEW_VERSION_CODE`, i.e. increment the value by 1 as described in the [Preliminary steps](#preliminary-steps)
    - set `versionName` to `"X.X.X"`
- commit the version bump (try to stick to the provided commit message template)
    - `git add app/build.gradle`
    - `git commit -m "Release vX.X.X (NEW_VERSION_CODE)"`
- push the newly created branch to the NewPipe repo
    - `git push upstream release-X.X.X`

### Creating the Pull Request

- create a Pull Request (PR) from the new branch you just pushed
    - if you used the correct branch name you should be able to use this url, after changing the X.X.X: https://github.com/TeamNewPipe/NewPipe/pull/new/release-X.X.X
- make sure the PR has `master` as the *base* branch and `release-X.X.X` as the *compare* branch
- the PR title should be "Release vX.X.X (NEW_VERSION_CODE)"
- remove the entire PR template, and instead put these two lines in the description (the `ISSUE_NUMBER` will be replaced later):
    ```
    Do not report regressions here, but rather in the corresponding issue: #ISSUE_NUMBER
    The changelog is also there.
    ```
- once you have created the PR, note down its number (from now on called `PR_NUMBER`)
- in case some issue would be fixed when the release PR is merged, link them using the "Development" tab on the right, or add a "Fixes #...." in the PR description
- *for example, check out [#8231](https://github.com/TeamNewPipe/NewPipe/pull/8231) for reference*

### Creating the issue

- create an issue
    - click [here](https://github.com/TeamNewPipe/NewPipe/issues/new) to open one without a template
- the issue title should be "Release vX.X.X (please TEST!)"
- the issue should have some sections, in the same order as provided below, with `##` before titles
- the `## Testing for regressions` section should contain the following lines; more information about how to obtain the APK are given at [Testing APKs](testing-apks)
    ```
    Debug APK (built by our CI in #PR_NUMBER): ...
    Please report **only regressions** (i.e. new issues) here, not issues that were already present in the previous release!
    ```
- an optional `## TODO` section should contain a list of things that still need to be done before releasing, for example regressions that need to be fixed, or a reminder to merge the Weblate changelogs before releasing (use `- [ ]` to create checkbox lists)
- the `## NewPipeExtractor version` should contain a link to the NewPipeExtractor release this new NewPipe version will ship with (i.e. the one set in [Creating the release branch](#creating-the-release-branch))
- copy the draft Markdown changelog [kept on GitHub](https://github.com/TeamNewPipe/NewPipe/releases) (you finalized it earlier in [Create a changelog](#create-a-changelog)) to the clipboard and paste it under the `## App changelog` section
- once you have created the issue, pin it using the "Pin issue" button on the right
- *for example, check out [#8230](https://github.com/TeamNewPipe/NewPipe/issues/8230) for reference*

### Testing APKs

The first time you open the release issue, and then each time some changes are made to the release PR, you should provide a debug APK in the `## Testing for regressions` section.
- wait for the Continuous Integration (CI) to finish testing the PR, then download the debug APK it will have built from the "Checks" tab
- rename it to `NewPipe_vX.X.X_RC1_debug.apk` where `RC1` should be incremented to `RC2` and so on each time a new APK is provided
- zip it and make sure the `.zip` file has the same name as the `.apk` it contains
- upload it in the issue description, replacing the `...` placeholder used above

Sometimes it might be needed to also provide a release APK. In this case follow the same steps as above, with these differences:
- make sure you are on the `release-X.X.X` branch
- build the **release** APK yourself in Android Studio and sign it with your keys
- make sure it installs correctly on your device
- use this naming scheme: `NewPipe_vX.X.X_RC1_release.apk`
- add a line to the `## Testing for regressions` section, of this form: `Debug APK (built and signed by @YOUR_GITHUB_USERNAME): ...`

### Taking care of regressions

The release issue and pull request should stay open for **roughly one week**, so that people can test the provided APKs and give feedback. If a *regression* is reported by some user, it should possibly be solved before releasing, otherwise the app would become more broken after each release. A *regression* is a bug now present in some code that used to run well in the last release, but was then modified in this release (supposedly to fix something else) and is now broken. So the following do not classify as regressions: some videos stop working because YouTube made some changes; the newly introduced big feature XYZ is still not perfect and has some bugs; a random crash reproducible also on previous versions... You get the point. Before releasing, try to fix any regression that come out, but avoid fixing non-regressions, since those should be treated with the same care and attention as all other issues.

Pull requests fixing regressions should target the `release-X.X.X` branch, not the `dev` branch! When merging those PRs, also provide a new RC APK.

### Finally merging the pull request

Once enough time has passed and all regressions and TODOs have been solved, you can proceed with the actual release. The following points include merging weblate changes again.
- in the local repository, check out the release branch and make sure it is up-to-date with the remote
    - `git checkout release-X.X.X`
    - `git pull origin release-X.X.X`
- go to [Weblate's Maintenance tab](https://hosted.weblate.org/projects/newpipe/#repository)
- press *Lock*; remember to *Unlock* later!
- press *Update*
- press *Commit*, if needed
- now go back to the local git repository
- delete the `weblate-dev` branch, just in case
    - `git branch -D weblate-dev`
- fetch changes from Weblate (in particular you should see the `weblate/dev` remote branch being updated)
    - `git fetch weblate`
- obtain the hash of the last commit on the `weblate/dev` remote branch
    - `git log -n 1 --pretty="format:%H" weblate/dev`
- cherry pick the hash you obtained above into the release branch (the one you are currently on)
    - `git cherry-pick HASH`
- push the changes to the remote branch
    - `git push origin release-X.X.X`
- merge the PR you created before
- delete the GitHub remote branch associated with the PR, i.e. `release-X.X.X` (there should be a button in the PR)
- close the issue you created before
- merge `dev` back into `master` (since the PR merged changes onto `master`)
    - `git checkout master`
    - `git pull origin master`
    - `git checkout dev`
    - `git pull origin dev`
    - `git merge master`
    - `git push origin dev` or create another temporary PR and merge it immediately
- go to [Weblate's Maintenance tab](https://hosted.weblate.org/projects/newpipe/#repository)
- press *Unlock*

### Creating the APK

Now on the remote `master` branch there is the release code which you need to turn into an APK.
- in the local repository, check out the `master` branch and make sure it is up-to-date with the remote
    - `git checkout master`
    - `git pull origin master`
- open the local project in Android Studio
- run the Gradle `clean` task using Android Studio's interface, in order to cleanup temporary/cache files that may interfere with reproducible builds
    - double press Ctrl, type `gradle clean`, press Enter
- make sure leftover files from building RC releases are actually removed, in order to avoid confusion
    - `rm -rf ./app/release`
- run the Gradle `assembleRelease` task using Android Studio's interface: it will start the process of building an unsigned APK
    - double press Ctrl, type `gradle assembleRelease`, press Enter
- after a while you should find the APK under `./app/build/outputs/apk/release/app-release-unsigned.apk`

### Having the APK signed by @TheAssassin

Currently @TheAssassin is the only holder of NewPipe's APK signing keys. Therefore you should send the unsigned APK to him and he will send a signed one back. He will also then publish the signed APK in NewPipe's F-Droid repo.
- rename `app-release-unsigned.apk` to `NewPipe_vX.X.X.apk`
- generate a signature for the APK file
    - `gpg -b NewPipe_vX.X.X.apk` will generate `NewPipe_vX.X.X.apk.sig`
    - it will also output 'using "FINGERPRINT" as default secret key for signing'; keep track of the `FINGERPRINT` part
- send an email to @TheAssassin and attach both `NewPipe_vX.X.X.apk` and `NewPipe_vX.X.X.apk.sig`
- if @TheAssassin does not already know it, send him your PGP key `FINGERPRINT` you obtained before
    - you should send it not using email this time, but another service on which @TheAssassin can be almost sure it is really you (something like 2FA)
    - for example, either just send it on the IRC group, or create a GitHub gist with the fingerprint and then give that link to @TheAssassin
- notify him on IRC that you have sent him an email
- he will send you back the signed APK
- make sure its name is still `NewPipe_vX.X.X.apk` (rename if it's not the case)
- install it on your device to see if everything went well (note that installation will work only if your currently installed version of newpipe comes from NewPipe's F-Droid repo or GitHub)
- tell @TheAssassin to "push the buttons", i.e. publish the signed APK in NewPipe's F-Droid repo.

### Publishing the release

- go to the draft changelog [kept on GitHub](https://github.com/TeamNewPipe/NewPipe/releases)
- set `vX.X.X` as the tag name
- set `vX.X.X` as the release title
- set `dev` as the "Target:" branch
- attach the signed APK @TheAssassin sent you
- publish the release
- profit :-D

### Blog post

> I do not know enough about blog post writing and publishing to fill in this section, I'll leave it to @opusforlife2 and @Poolitzer.

- in order for the blog post to be published, ask @TheAssassin to "press the buttons" again
- once the blog post is ready (which, in optimal cases, should happen before the release is published, but that's not a must), add this block of text on top of the release notes on GitHub:
    ```
    [:arrow_right: :arrow_right: :arrow_right: Read the blog post :arrow_left: :arrow_left: :arrow_left:](LINK_TO_BLOG_POST)
    ```

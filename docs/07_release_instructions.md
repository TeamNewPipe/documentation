# Release instructions for normal releases

This page contains detailed instructions for normal releases. Refer to [Releasing a New NewPipe Version](../06_releasing) for other information about releases.

## Preliminary steps

### Permissions

- Have admin rights on Weblate
    - You should be able to access [Weblate's Maintenance page](https://hosted.weblate.org/projects/newpipe/#repository)
    - Tip: if the correct page does not show up when clicking that url, make sure you are logged in ;-)
- Have at least maintainer rights on the NewPipe and NewPipeExtractor repos

### Repositories

- Have a cloned NewPipe local repository (for the rest of the page, `origin` is assumed to be the remote at `github.com/TeamNewPipe/NewPipe`)
- Add the `weblate` remote to the same local repository (the URL used below can be found on the Maintenance page on Weblate)
    - `git remote add weblate https://hosted.weblate.org/git/newpipe/strings/`
- Make sure there are no pending changes
    - `git clean -fdx` to **discard** them all (**CAUTION**)
- Switch to the `dev` branch and make sure it is up-to-date with the remote:
    - `git checkout dev`
    - `git pull origin dev`

### Version name and conventions

- Find the version code of the next release by looking for `versionCode` in [`app/build.gradle`](https://github.com/TeamNewPipe/NewPipe/blob/dev/app/build.gradle): You will add 1 to that value (from now on called `NEW_VERSION_CODE`) to get the new value (but do not edit the file yet)
- Choose the version number of the next release according to [semantic versioning](https://semver.org/) (from now on called `X.X.X`)

### Identification

- Have `gpg` installed and usable on your PC
- Have a GPG key, which can be used to verify that a file is really from you

## Pull changes from Weblate

- Go to [Weblate's Maintenance tab](https://hosted.weblate.org/projects/newpipe/#repository)
- Press the *Lock* button to prevent translators from translating while you are creating commits; remember to *Unlock* later!
- Press the *Update* button to update Weblate with the latest changes on NewPipe's `dev` branch
- Press the *Commit* button, if needed, to make sure Weblate creates a commit for translations which have not been committed yet
- Now go back to the local git repository
- In case you followed these steps before, delete the `weblate-dev` branch
    - `git branch -D weblate-dev`
- Fetch new changes from the `weblate` remote
    - `git fetch weblate`
- Create a new branch starting from `weblate/dev`, named `weblate-dev`, and switch to it
    - `git checkout -b weblate-dev weblate/dev`
- If you run `git log --oneline --graph` you should see a Weblate commit on top, and then all of the commits currently on the `dev` branch:
```md
* cmt12hash (HEAD -> weblate-dev, weblate/dev) Translated using Weblate (...)
* cmt89hash (origin/dev, dev) Commit message ...
```
- Switch back to the `dev` branch
    - `git checkout dev`
- Merge `weblate-dev` into `dev`:
    - `git merge weblate-dev`

## Create a changelog

- Finalize the draft changelog [kept on GitHub](https://github.com/TeamNewPipe/NewPipe/releases), in case there are still some things to fill in
    - Remove the temporary instructions, and the numbers before `-` which keep track of the order in which the PRs were merged, as that info is useful only for the blog post writers
    - Before removing that information, you may want to send the original changelog to the blogpost writers
- Create a new English changelog in the [`fastlane/metadata/android/en-US/changelogs/`](https://github.com/TeamNewPipe/NewPipe/blob/dev/fastlane/metadata/android/en-US/changelogs/) folder
- The file should be named `NEW_VERSION_CODE.txt`, using the new version code found in the [Preliminary steps](#preliminary-steps)
- The file should have this structure (sections with no points can be removed):
```txt
New
• ...

Improved
• ...

Fixed
• ...
```
- Make sure you use the `•` for points (it looks nicer than `-`)
- Capitalize the first letter in each point
- Use English verbs as if you were asking someone to do something, so for example use "Fix abc" and not "Fixed abc"; this allows saving a few characters and using a consistent style
- Prepend `[SERVICE]` to service-only changes (e.g. "• \[YouTube\] Add mixes")
- Summarize only the most important changes from the draft release [kept on GitHub](https://github.com/TeamNewPipe/NewPipe/releases) (it contains all merged pull requests)
- Make sure the file size is **at most 500 bytes**, in order to **fit [F-Droid's changelog size limit](https://f-droid.org/en/docs/All_About_Descriptions_Graphics_and_Screenshots/#fastlane-structure) (!)**
    - Tip: removing the newline at the end of the file saves 1 byte ;-)
- Commit the file on the `dev` branch (try to stick to the provided commit message template)
    - `git add fastlane/metadata/android/en-US/changelogs/NEW_VERSION_CODE.txt`
    - `git commit -m "Add changelog for vX.X.X (NEW_VERSION_CODE)"`

## Push the changelog to Weblate

Now there should be two new commits (the Weblate and changelog ones) on your local `dev` branch, which are not on NewPipe's remote `dev` branch.

- If you are an admin of the NewPipe repo, just push the changes to the remote `dev`
    - `git push origin dev`
    - If you are not an admin, create a pull request normally and ask someone with maintainer access to merge it
- Go to [Weblate's Maintenance tab](https://hosted.weblate.org/projects/newpipe/#repository)
- Press the *Update* button to update Weblate with the commit you just pushed on NewPipe's `dev` branch
- **Press the *Unlock*** button to allow translators to translate the changelog and possibly other components (**do not forget this step!**)
- Note that we had to do this process on NewPipe's `dev` branch because:
    - Weblate's components are connected to NewPipe's `dev` branch, and will update changes from there
    - Weblate's git repo is not writable, so there is no way to push commits there manually

## Creating the release branch

- Create a new branch starting from `dev`, named `release-X.X.X`, and switch to it
    - `git checkout dev`
    - `git checkout -b release-X.X.X`
- Edit the [`app/build.gradle`](https://github.com/TeamNewPipe/NewPipe/blob/dev/app/build.gradle) file to update the extractor
    - Set the NewPipeExtractor dependency version to a suitable one (usually [the last commit in the NewPipeExtractor repo](https://github.com/TeamNewPipe/NewPipeExtractor/commits/dev))
- Commit the extractor update (if you used a specific version, append `to VERSION` to the commit message)
    - `git add app/build.gradle`
    - `git commit -m "Update NewPipeExtractor"`
- Edit the [`app/build.gradle`](https://github.com/TeamNewPipe/NewPipe/blob/dev/app/build.gradle) file to bump the release
    - Set `versionCode` to `NEW_VERSION_CODE`, i.e. increment the value by 1 as described in the [Preliminary steps](#preliminary-steps)
    - Set `versionName` to `"X.X.X"`
- Commit the version bump (try to stick to the provided commit message template)
    - `git add app/build.gradle`
    - `git commit -m "Release vX.X.X (NEW_VERSION_CODE)"`
- Push the newly created branch to the NewPipe repo
    - `git push origin release-X.X.X`

## Creating the Pull Request

- Create a Pull Request (PR) from the new branch you just pushed
    - If you used the correct branch name you should be able to use this URL, after changing the X.X.X: `https://github.com/TeamNewPipe/NewPipe/pull/new/release-X.X.X`
- Make sure the PR has `master` as the *base* branch and `release-X.X.X` as the *compare* branch
- The PR title should be "Release vX.X.X (NEW_VERSION_CODE)"
- Remove the entire PR template, and instead put these two lines in the description (the `ISSUE_NUMBER` will be replaced later):
```md
Do **not** report regressions here, but rather in the corresponding issue: #ISSUE_NUMBER
The changelog is also there.
```
- Once you have created the PR, note down its number (from now on called `PR_NUMBER`)
- In case some issue would be fixed when the release PR is merged, link them using the "Development" tab on the right, or add a "Fixes #...." in the PR description
- *Check out [#8231](https://github.com/TeamNewPipe/NewPipe/pull/8231) for reference*

## Creating the issue

- Create an issue
    - Click [here](https://github.com/TeamNewPipe/NewPipe/issues/new) to open one without a template
- The issue title should be "Release vX.X.X (please TEST!)"
- The issue should have some sections, in the same order as provided below, with `##` before titles
- The `## Testing for regressions` section should contain the following lines; more information about how to obtain the APK are given at [Testing APKs](#testing-apks)
```md
Debug APK (built by our CI in #PR_NUMBER): ...
Please report **only regressions** (i.e. new issues) here, not issues that were already present in previous releases!
```
- An optional `## TODO` section should contain a list of things that still need to be done before releasing, for example regressions that need to be fixed, or a reminder to merge the Weblate changelogs before releasing (use `- [ ]` to create checkbox lists)
- The `## NewPipeExtractor version` section should contain a link to the NewPipeExtractor release this new NewPipe version will ship with (i.e. the one set in [Creating the release branch](#creating-the-release-branch)); choose one of these lines as a template
```md
This version of NewPipe will ship with [NewPipeExtractor version NPE_VERSION](https://github.com/TeamNewPipe/NewPipeExtractor/releases/tag/NPE_VERSION)
This version of NewPipe will ship with [NewPipeExtractor commit FIRST_7_DIGITS_OF_NPE_COMMIT](https://github.com/TeamNewPipe/NewPipeExtractor/commit/NPE_COMMIT)
```
- Create the `App changelog` section using the template below. Copy the draft Markdown changelog [kept on GitHub](https://github.com/TeamNewPipe/NewPipe/releases) (you finalized it earlier in [Create a changelog](#create-a-changelog)) to the clipboard and paste it where specified below (make sure to leave a newline above, otherwise Markdown breaks):
```md
<details><summary><h2>App changelog </h2></summary><p>

INSERT_COPIED_CHANGELOG_HERE
</details>
```
- Once you have created the issue, pin it using the "Pin issue" button on the right
- Update the `ISSUE_NUMBER` in the pull request description
- *Check out [#8230](https://github.com/TeamNewPipe/NewPipe/issues/8230) for reference*

## Testing APKs

The first time you open the release issue, and then each time some changes are made to the release PR, you should provide a debug APK in the `## Testing for regressions` section.

- Wait for the Continuous Integration (CI) to finish testing the PR, then download the resulting debug APK artifact from the "Checks" tab
- Rename it to `NewPipe_vX.X.X_RC1_debug.apk` where `RC1` should be incremented to `RC2` and so on each time a new APK is provided
- Zip it and make sure the `.zip` file has the same name as the `.apk` it contains
- Upload it in the issue description, replacing the `...` placeholder used above

Sometimes it might be needed to also provide a release APK. In this case follow the same steps as above, with these differences:

- Make sure you are on the `release-X.X.X` branch
- Build the **release** APK yourself in Android Studio and sign it with your keys
    - *Temporarily* edit the `app/build.gradle` file and add `System.properties.put("packageSuffix", "vX_X_X")` at the top of the `android -> buildTypes -> release` block, which ensures that the application has a different package name than the official one
    - Build and sign an APK via "Build -> Generate Signed Bundle / APK..."
- Make sure it installs correctly on your device
- Use this naming scheme: `NewPipe_vX.X.X_RC1_release.apk`
- Add a line to the `## Testing for regressions` section, of this form: `Release APK (built and signed by @YOUR_GITHUB_USERNAME): ...`

## Taking care of regressions (quickfixes)

The release issue and pull request should stay open for **roughly one week**, so that people can test the provided APKs and give feedback. If a *regression* is reported by some user, it should possibly be solved before releasing, otherwise the app would become more broken after each release. A *regression* is a bug now present in some code that used to run well in the last release, but was then modified in this release (supposedly to fix something else) and is now broken. So the following do not classify as regressions: some videos stop working because YouTube made some changes; the newly introduced big feature XYZ is still not perfect and has some bugs; a random crash reproducible also on previous versions... You get the point. Before releasing, try to fix any regressions that are reported, but avoid fixing non-regressions, since those should be treated with the same care and attention as all other issues. As a Release Manager, you might be required to fix regressions, so plan your release at a time when you are available.

Pull requests fixing regressions should target the `release-X.X.X` branch, not the `dev` branch! When merging those PRs, also provide a new Release Candidate APK.

## Finally merging the pull request

Once enough time has passed and all regressions and TODOs have been solved, you can proceed with the actual release. The following points include merging weblate changes again.

- In the local repository, check out the release branch and make sure it is up-to-date with the remote
    - `git checkout release-X.X.X`
    - `git pull origin release-X.X.X`
- Go to [Weblate's Maintenance tab](https://hosted.weblate.org/projects/newpipe/#repository)
- Press *Lock*; remember to *Unlock* later!
- Press *Update*
- Press *Commit*, if needed
- Now go back to the local git repository
- Delete the `weblate-dev` branch, just in case
    - `git branch -D weblate-dev`
- Fetch changes from Weblate (in particular you should see the `weblate/dev` remote branch being updated)
    - `git fetch weblate`
- Obtain the hash of the last commit on the `weblate/dev` remote branch
    - `git log -n 1 --pretty="format:%H" weblate/dev`
- Cherry pick the hash you obtained above into the release branch (the one you are currently on)
    - `git cherry-pick HASH`
- Push the changes to the remote branch
    - `git push origin release-X.X.X`
- Merge the PR you created before
- Delete the GitHub remote branch associated with the PR, i.e. `release-X.X.X` (there should be a button in the PR)
- Close the issue you created before
- Merge `dev` back into `master` (since the PR merged changes onto `master`)
    - `git checkout master`
    - `git pull origin master`
    - `git checkout dev`
    - `git pull origin dev`
    - `git merge master`
    - `git push origin dev` or create another temporary PR and merge it immediately
- Go to [Weblate's Maintenance tab](https://hosted.weblate.org/projects/newpipe/#repository)
- **Press *Unlock***

## Creating the APK

Now on the remote `master` branch there is the release code which you need to turn into an APK.

- In the local repository, check out the `master` branch and make sure it is up-to-date with the remote
    - `git checkout master`
    - `git pull origin master`
- Open the local project in Android Studio
- Run the Gradle `clean` task using Android Studio's interface, in order to clean up temporary/cache files that may interfere with reproducible builds
    - Double press Ctrl, type `gradle clean`, press Enter
- Make sure leftover files from building RC releases are actually removed, in order to avoid confusion
    - `rm -rf ./app/release`
- Run the Gradle `assembleRelease` task using Android Studio's interface: it will start the process of building an unsigned APK
    - Double press Ctrl, type `gradle assembleRelease`, press Enter
- After a while you should find the APK under `./app/build/outputs/apk/release/app-release-unsigned.apk`

## Having the APK signed by @TheAssassin

Currently @TheAssassin is the only holder of NewPipe's APK signing keys. Therefore you should send the unsigned APK to him, after which he will sign it and send it back to you. He will also then publish the signed APK in NewPipe's F-Droid repo.

- Rename `app-release-unsigned.apk` to `NewPipe_vX.X.X.apk`
- Generate a signature for the APK file
    - `gpg -b NewPipe_vX.X.X.apk` will generate `NewPipe_vX.X.X.apk.sig`
    - It will also output 'using "FINGERPRINT" as default secret key for signing'; keep track of the `FINGERPRINT` part
- Send an email to @TheAssassin and attach both `NewPipe_vX.X.X.apk` and `NewPipe_vX.X.X.apk.sig`
- If @TheAssassin does not already know it, send him your PGP key `FINGERPRINT` you obtained before
    - You should not send it using email this time, but using another service through which @TheAssassin can be almost sure it is really you (this is a sort of 2FA)
    - For example, you can send it on the IRC group, or create a GitHub gist with the fingerprint and then give that link to @TheAssassin
- Notify him on IRC that you have sent him an email
- He will send you back the signed APK
- Make sure its name is still `NewPipe_vX.X.X.apk` (rename if it's not the case)
- Install it on your device to see if everything went well (note that installation will work only if your currently installed version of newpipe comes from NewPipe's F-Droid repo or GitHub)
- Tell @TheAssassin to "push the buttons", i.e. publish the signed APK in NewPipe's F-Droid repo.

## Publishing the release

- Go to the draft changelog [kept on GitHub](https://github.com/TeamNewPipe/NewPipe/releases)
- Set `vX.X.X` as the tag name
- Set `vX.X.X` as the release title
- Set `master` as the "Target:" branch
- Attach the signed APK @TheAssassin sent you
- Publish the release
- Profit :-D

## Blog post

The blog post writers need an up-to-date list of merged PRs numbered in chronological order. This is so that they can keep track of what changes have already been detailed in the draft blog post, and which ones still need to be added. So make sure that there is always at least one up-to-date "master copy" of the draft release notes available for them to review.

The blog post should ideally be published before the GitHub release is made (so that the link to it works!), but in case of some delay, it is fine to let the blog post come later. It is far more important to get the release into users' hands sooner.

- In order for the blog post to be published, ask @TheAssassin to "press the buttons" again
- Once the blog post is ready, add this block of text on top of the release notes on GitHub:
    ```
    [:arrow_right: :arrow_right: :arrow_right: Read the blog post :arrow_left: :arrow_left: :arrow_left:](LINK_TO_BLOG_POST)
    ```

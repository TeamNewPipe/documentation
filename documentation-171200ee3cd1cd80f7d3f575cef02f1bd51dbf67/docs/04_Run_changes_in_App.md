# Testing Your Changes in the App

You should develop and test your changes with the JUnit environment that is
provided by the NewPipe Extractor and IDEA. If you want to try it with
the actual fronted, you need to follow these steps.

### Setup Android Studio

First, you'll want to set up a working Android Studio environment. To do this,
download Studio from [developer.android.com](https://developer.android.com/studio/),
and follow the [instructions](https://developer.android.com/studio/install) on how to set it up.

### Get the NewPipe Code and Run it.

In order to get it, you simply clone or download it from the current `dev` branch
[github.com/TeamNewPipe/NewPipe.git](https://github.com/TeamNewPipe/NewPipe/archive/dev.zip).
You can then build and run it following [these instructions](https://developer.android.com/studio/run/).
Also, make sure you are comfortable with [adb](https://en.droidwiki.org/wiki/Android_Debug_Bridge) since
you might experience some trouble running your compiled app on a real device, especially under Linux, where you
sometimes have to adjust the udev rules in order to
[make your device accessible](https://www.janosgyerik.com/adding-udev-rules-for-usb-debugging-android-devices/).

### Run Your Changes on the Extractor

In order to use the extractor in our app, we use [jitpack](https://jitpack.io). This is a build service that can build
maven *.jar packages for Android and Java based on GitHub or GitLab repositories. 

To use the extractor through jitpack, you need to push it to your online repository of
your copy that you host either on [GitHub](https://github.com) or [GitLab](https://gitlab.com). It's important to host
it on one of both. To copy your repository URL in HTTP format, go to [jitpack](https://jitpack.io/) and paste it there.
From here, you can grab the latest commit via `GET IT` button.
I recomend not to use a SNAPSHOT, since I am not sure when snapshot is built. An "implementation" string will be generated
for you. Copy this string and replace the `implementation 'com.github.TeamNewPipe:NewPipeExtractor:<commit>'` line in
the file [/app/build.gradle](https://github.com/TeamNewPipe/NewPipe/blob/dev/app/build.gradle#L58) with it.

<video width="600" controls>
  <source src="../media/how_to_jitpack.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

If everything synced well, then you should only see a screen with OK signs. Now you can compile and run NewPipe
with the new extractor.

![image_sync_ok](img/sync_ok.png)

### Troubleshooting

If something went wrong on jitpack site, you can check their build log, by selecting the commit you tried to build and
click on that little paper symbol next to the `GET IT` button. If it's red, it means that the build failed.
![jitpack failed to build](img/jitpack_fail.png)

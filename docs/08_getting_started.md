# Getting Started
This section provides you with the steps that are required to use the extractor in your android app.


## Configure project.
### Add dependencies to gradle:

1. **project** `settings.gradle`:

```gradle
...
buildscript {
    repositories {
        ...
        maven { url 'https://jitpack.io' }
    }
    ...
}
```



2. module/app build.gradle:

```gradle
// NewPipe Libraries
implementation 'com.github.TeamNewPipe:NewPipeExtractor:0.21.12'
implementation 'com.github.TeamNewPipe:nanojson:1d9e1aea9049fc9f85e68b43ba39fe7be1c1f751'


// HTTP client
implementation "com.squareup.okhttp3:okhttp:3.12.13"
```

Note that you could use any http client other then okhttp, but it used here for more simplicity.


### Make sure you use Java 11

Change this in your module `build.gradle`:

```gradle
android {
    ...
    compileOptions {
        // enabling desugaring seems required.
        coreLibraryDesugaringEnabled true

        // java version:
        sourceCompatibility JavaVersion.VERSION_11
        targetCompatibility JavaVersion.VERSION_11
    }

    // if you are using kotlin:
    kotlinOptions {
        jvmTarget = JavaVersion.VERSION_11
        useIR = true
    }
}

dependencies {
    ...

    // desugar
    coreLibraryDesugaring 'com.android.tools:desugar_jdk_libs:1.1.5'
}
```


### Proguard rules

If you've `minifyEnabled` to `true` you should enable this rules:

```pro
# ....
# For NewPipeExtractor
-dontobfuscate
-keep class org.schabi.newpipe.extractor.timeago.patterns.** { *; }
-keep class org.ocpsoft.prettytime.i18n.** { *; }

-keep class org.mozilla.javascript.** { *; }

-keep class org.mozilla.classfile.ClassFileWriter
-keep class com.google.android.exoplayer2.** { *; }

-dontwarn org.mozilla.javascript.tools.**
-dontwarn android.arch.util.paging.CountedDataSource
-dontwarn android.arch.persistence.room.paging.LimitOffsetDataSource



# Rules for OkHttp. Copy paste from https://github.com/square/okhttp
-dontwarn okhttp3.**
-dontwarn okio.**
-dontwarn javax.annotation.**
# A resource is loaded with a relative path so the package of this class must be preserved.
-keepnames class okhttp3.internal.publicsuffix.PublicSuffixDatabase
-keepclassmembers class * implements java.io.Serializable {
    static final long serialVersionUID;
    !static !transient <fields>;
    private void writeObject(java.io.ObjectOutputStream);
    private void readObject(java.io.ObjectInputStream);
}
```


## Implement a Downloader

The extractor needs to fetch websites and JSON files.
Its entire network activity is going through the downloader you pass to it.  
We have predefined some methods which need to be implemented.
To get started, create a class extending
[`Downloader`](https://github.com/TeamNewPipe/NewPipeExtractor/blob/master/extractor/src/main/java/org/schabi/newpipe/extractor/downloader/Downloader.java).
We will call that class `DownloaderImpl` in this example.

``` Java

import org.schabi.newpipe.extractor.downloader.Downloader;

public class DownloaderImpl extends Downloader {

    public DownloaderImpl() {

    }

}

```
Your IDE will prompt you to implement at least one method:

``` Java
/**
 * Do a request using the specified {@link Request} object.
 *
 * @return the result of the request
 */
public Response execute(@Nonnull Request request) throws IOException, ReCaptchaException {
    // your code goes here
}
```

<details>
<summary>simple implementation</summary>

Here is a simple implementation for the `Downloader`, assumes that you are using `okhttp`.

```java
package gh.cloneconf.newpipe_android_example;

import org.schabi.newpipe.extractor.downloader.Downloader;
import org.schabi.newpipe.extractor.downloader.Request;
import org.schabi.newpipe.extractor.downloader.Response;
import org.schabi.newpipe.extractor.exceptions.ReCaptchaException;

import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeUnit;

import okhttp3.OkHttpClient;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;

public final class DownloaderImpl extends Downloader {
    private static final String USER_AGENT
            = "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0";

    private final OkHttpClient okhttp;

    public DownloaderImpl() {
        okhttp = new OkHttpClient.Builder()
                .readTimeout(30, TimeUnit.SECONDS)
                .build();
    }

    @Override
    public Response execute(final Request request)
            throws IOException, ReCaptchaException {
        final String httpMethod = request.httpMethod();
        final String url = request.url();
        final Map<String, List<String>> headers = request.headers();
        final byte[] dataToSend = request.dataToSend();

        RequestBody requestBody = null;
        if (dataToSend != null) {
            requestBody = RequestBody.create(null, dataToSend);
        }

        final okhttp3.Request.Builder requestBuilder = new okhttp3.Request.Builder()
                .method(httpMethod, requestBody).url(url)
                .addHeader("User-Agent", USER_AGENT);

        for (Map.Entry<String, List<String>> pair : headers.entrySet()) {
            final String headerName = pair.getKey();
            final List<String> headerValueList = pair.getValue();

            if (headerValueList.size() > 1) {
                requestBuilder.removeHeader(headerName);
                for (String headerValue : headerValueList) {
                    requestBuilder.addHeader(headerName, headerValue);
                }
            } else if (headerValueList.size() == 1) {
                requestBuilder.header(headerName, headerValueList.get(0));
            }

        }

        final okhttp3.Response response = okhttp.newCall(requestBuilder.build()).execute();

        if (response.code() == 429) {
            response.close();

            throw new ReCaptchaException("reCaptcha Challenge requested", url);
        }

        final ResponseBody body = response.body();
        String responseBodyToReturn = null;

        if (body != null) {
            responseBodyToReturn = body.string();
        }

        final String latestUrl = response.request().url().toString();
        return new Response(response.code(), response.message(), response.headers().toMultimap(),
                responseBodyToReturn, latestUrl);
    }
}


```

</details>


You can find two example implementations of the Downloader below.
Both use an old OkHttp version (version 3) to support Android 4. However, you do not need to use OkHttp.
In case you want to use it and do not need to support old Android versions,
we recommend using a newer OkHttp version, because the version used in the example will only receive security updates until December 2021.

- [Downloader implementation for NewPipe Extractor tests](https://github.com/TeamNewPipe/NewPipeExtractor/blob/master/extractor/src/test/java/org/schabi/newpipe/downloader/DownloaderTestImpl.java)
- [Downloader implementation of the NewPipe app](https://github.com/TeamNewPipe/NewPipe/blob/master/app/src/main/java/org/schabi/newpipe/DownloaderImpl.java)  
Note: This implementation contains some additional methods which are not necessary for general use cases.


Depending on your use case and your downloader implementation, we suggest you to make use of the singleton pattern.

#### Browser Agent

When making requests to websites, you should define a user agent for the request headers. We have build our tests on
```
Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0
```
For this reason, we strongly recommend using that agent or any other that is used in the [testimplementation in NewPipe Extractor](https://github.com/TeamNewPipe/NewPipeExtractor/blob/master/extractor/src/test/java/org/schabi/newpipe/downloader/DownloaderTestImpl.java).  
However, a service might want to override the default user agent.
This is sometimes necessary to get special versions of a website (e.g. mobile or legacy version).
Please respect that when implementing the `execute(@Nonnull Request request)` method.

## Initialize NewPipe

``` Java
NewPipe.init(
    /* 
      New instance of your downloader implementation.
      If you implemented the singleton pattern, use DownlaoderImpl.getInstance() instead.
    */
    new DownloaderImpl()
);
```
You can also set a default localization 
``` Java
NewPipe.init(
    new DownloaderImpl(),
    new Localization("EN", "US")
);
```
and a default content country. However, not all services support those, yet.
``` Java
NewPipe.init(
    new DownloaderImpl(),
    new Localization("EN", "US"),
    new ContentCountry("EN-US")
);
```



## Using Service

We can any service that NewPipe supports from `ServiceList`.

```java
YoutubeService youtube = ServiceList.YouTube;
// SoundcloudService soundCloud = ServiceList.SoundCloud;
// ...
```

### Some examples for **youtube** service:


- Suggestions

```java
youtube.getSuggestionExtractor().suggestionList("Hello");
```

- Search results

```java
SearchExtractor page = youtube.getSearchExtractor("Hello");
page.fetchPage();

// results list
page.getInitialPage().getItems();
```


- get video stream links:

```java
StreamExtractor page = youtube.getStreamExtractor("https://www.youtube.com/watch?v=1YGCQRTSOSI");
page.fetchPage();

// list of streams
page.getVideoStreams();
```

## Examples:
- [Android example](https://github.com/cloneconf/newpipe-android-example) by @cloneconf.
- [Java example](https://github.com/cloneconf/newpipe-java-example) by @cloneconf.
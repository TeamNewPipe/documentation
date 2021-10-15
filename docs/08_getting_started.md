# Getting Started
This section provides you with the steps that are required to use the extractor.

### Implement a Downloader

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



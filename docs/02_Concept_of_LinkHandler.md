# Concept of LinkHandler

[LinkHandler](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/LinkHandler.html)
represent Links to resources like videos, search requests, channels, etc.
The idea behind them is that a video can have multiple links pointig to it, but it has
one unique id that represents it, like this example:

[oHg5SJYRHA0](https://www.youtube.com/watch?v=oHg5SJYRHA0) can be represented as:

- https://www.youtube.com/watch?v=oHg5SJYRHA0 (default url for youtube)
- https://youtu.be/oHg5SJYRHA0
- https://m.youtube.com/watch?v=oHg5SJYRHA0

### Importand notes about LinkHandler: 
- A simple `LinkHandler` will contain the default URL, the ID and the original url.
- `LinkHandler` are ReadOnly
- LinkHandler are also used to determine which part of the extractor can handle a certain link.
- In order to get one you must either call
[fromUrl()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/LinkHandlerFactory.html#fromUrl-java.lang.String-) or [fromId()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/LinkHandlerFactory.html#fromId-java.lang.String-) of the the coresponding `LinkHandlerFactory`.
- Every type of Type of Resource has its own LinkHandlerFactory. Eg. YoutubeStreamLinkHandler, YoutubeChannelLinkHandler, etc.

### Usage

So the typical Usage for getting a LinkHandler would look like this.
```java
LinkHandlerFactory myLinkHandlerFactory = new MyStreamLinkHandlerFactory();
LinkHandler myVideo = myLinkHandlerFactory.fromUrl("https://my.service.com/the_video");
```

### Implementation

In order to Use LinkHandler for your service you must override the apropriate LinkHandlerFactory. eg:

```java
class MyStreamLinkHandlerFactory extends LinkHandlerFactory {
    
    @Override
    public String getId(String url) throws ParsingException {
        // Return the ID based on the url.
    }

    @Override
    public String getUrl(String id) throws ParsingException {
        // Return the url based on the id given.
    }

    @Override
    public boolean onAcceptUrl(String url) throws ParsingException {
        // Return true if this LinkHanlderFactory can handle this type of link
    }
}
```

### ListLinkHandler and QueryLinkHandler

List based resources like channels and playlists can be sorted, for example by date, name, or by a certain name.
Therefore these type of resources don't just use a LinkHandler, but an extention called
[ListLinkHandler](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandler.html)







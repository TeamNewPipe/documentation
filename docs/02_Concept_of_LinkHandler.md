# Concept of LinkHandler

[LinkHandler](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/LinkHandler.html)
represent Links to resources like videos, search requests, channels, etc.
The idea behind them is that a video can have multiple links pointing to it, but it has
one unique ID that represents it, like this example:

[oHg5SJYRHA0](https://www.youtube.com/watch?v=oHg5SJYRHA0) can be represented as:

- https://www.youtube.com/watch?v=oHg5SJYRHA0 (default URL for YouTube)
- https://youtu.be/oHg5SJYRHA0
- https://m.youtube.com/watch?v=oHg5SJYRHA0

### Importand notes about LinkHandler: 
- A simple `LinkHandler` will contain the default URL, the ID and the original URL.
- `LinkHandler`s are ReadOnly
- `LinkHandler`s are also used to determine which part of the extractor can handle a certain link.
- In order to get one you must either call
[fromUrl()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/LinkHandlerFactory.html#fromUrl-java.lang.String-) or [fromId()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/LinkHandlerFactory.html#fromId-java.lang.String-) of the the corresponding `LinkHandlerFactory`.
- Every type of Type of Resource has its own `LinkHandlerFactory`. Eg. YoutubeStreamLinkHandler, YoutubeChannelLinkHandler, etc.

### Usage

So the typical usage for getting a LinkHandler would look like this.
```java
LinkHandlerFactory myLinkHandlerFactory = new MyStreamLinkHandlerFactory();
LinkHandler myVideo = myLinkHandlerFactory.fromUrl("https://my.service.com/the_video");
```

### Implementation

In order to Use LinkHandler for your service you must override the appropriate LinkHandlerFactory. eg:

```java
class MyStreamLinkHandlerFactory extends LinkHandlerFactory {
    
    @Override
    public String getId(String url) throws ParsingException {
        // Return the ID based on the URL.
    }

    @Override
    public String getUrl(String id) throws ParsingException {
        // Return the URL based on the ID given.
    }

    @Override
    public boolean onAcceptUrl(String url) throws ParsingException {
        // Return true if this LinkHanlderFactory can handle this type of link
    }
}
```

### ListLinkHandler and SearchQueryHandler

List based resources like channels and playlists can be sorted, and filtered.
Therefore these type of resources don't just use a LinkHandler, but a class called
[ListLinkHandler](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandler.html)
which inherits from LinkHandler and adds the fields [ContentFilter](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandler.html#contentFilters)
which is used to filter by resource type like stream or playlist, and
[SortFilter](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandler.html#sortFilter)
which is used to sort by name, date or view count.

ListLinkHandler are also created by overriding the [ListLinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html)
additionally to the abstract methods this factory inherits from the LinkHandlerFactory you can override
[getAvailableContentFilter()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html#getAvailableContentFilter--)
and [getAvailableSortFilter()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html#getAvailableSortFilter--).
Through these you can tell the front end which kind of filter your service supports.


#### SearchQueryHandler

You cannot point to a search request with an ID like you point to a playlist or a channel, simply because one and the
same search request might have a different outcome depending on the country or the time you send the request. This is
why the idea of an "ID" is replaced by a "SearchString" in the [SearchQueryHandler](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/SearchQueryHandler.html)
These work like regular ListLinkHandler, except that you don't have to implement the methods `onAcceptUrl()`
and `getId()` when overriding [SearchQueryHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/SearchQueryHandlerFactory.html).









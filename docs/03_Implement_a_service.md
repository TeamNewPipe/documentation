# Implementing a Service

Services, or better service connectors, are the parts of NewPipe which communicate with an actual service like YouTube.
This page will describe how you can implement and add your own services to the extractor. Please make sure you read and understand the
[Concept of Extractors](https://teamnewpipe.github.io/documentation/01_Concept_of_the_extractor/)
and the [Concept of LinkHandler](https://teamnewpipe.github.io/documentation/02_Concept_of_LinkHandler/)
before continuing.

### Required and Optional Parts
Your service does not have to implement everything; some parts are optional.
This is because not all services support every feature other services support. For example, it might be that a certain
service does not support channels. If so, you can leave out the implementation of channels, and make the corresponding
factory method of the your __StreamingService__ implementation return __null__. The frontend will handle the lack of
having channels.

However, if you start to implement one of the optional parts of the list below, you will have to implement all of its parts/classes. NewPipe will crash if you only implement the extractor for the list item of a channel, but not the channel extractor itself.

__The Parts of a Service:__

- [Head of Service](#head-of-service)
- [Stream](#stream)
- [Search](#search)
- [Playlist](#playlist) _(optional)_
- [Channel](#channel) _(optional)_
- [Kiosk](#kiosk) _(optional)_

### Allowed Libraries

The NewPipe Extractor already includes a lot of usable tools and external libraries that should make extracting easy.
For some specific (tiny) tasks, Regex is allowed. Here you can take a look at the
[Parser](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/utils/Parser.html),
which will give you a little help with that. __Use Regex with care!!!__ Avoid it as often as possible. It's better to
ask us to introduce a new library than start using Regex to often.

- Html/XML Parsing: [jsoup](https://jsoup.org/apidocs/overview-summary.html)
- JSON Parsing: [nanojson](https://github.com/mmastrac/nanojson#parser-example)
- JavaScript Parsing/Execution: [Mozilla Rhino](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino/Documentation)
- Link detection in strings: [AutoLink](https://github.com/robinst/autolink-java)

If you need to introduce new libraries, please tell us before you do so.

### Head of Service

First of all, if you want to create a new service, you should create a new package below `org.schabi.newpipe.services`
, with the name of your service as package name.

__Parts Required to be Implemented:__

- [StreamingService](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.html)
- [ServiceInfo](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.ServiceInfo.html)

[StreamingService](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.html)
is a factory class that will return objects of all important parts of your service.
Every extractor, handler, and info type you add and should be part of your implementation, must be instantiated using an
instance of this class. You can see it as a factory for all objects of your implementation.

[ServiceInfo](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.ServiceInfo.html)
will return some metadata about your service such as the name, capabilities, the author's name, and their 
email address for further notice and maintenance issues. Remember, after extending this class, you need to return an
instance of it by through your implementation of
[`StreamingService.getServiceInfo()`](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.html#getServiceInfo--).

When these two classes are extended by you, you need to add your `StreamingService` to the
[ServiceList](https://github.com/TeamNewPipe/NewPipeExtractor/blob/49c2eb51859a58e4bb5ead2d9d0771408f7d59d6/extractor/src/main/java/org/schabi/newpipe/extractor/ServiceList.java#L23)
of NewPipe. This way, your service will become an official part of the NewPipe Extractor.
Every service has an ID, which will be set when this list gets created. You need to set this ID by entering it in the constructor.
So when adding your service just give it the ID of the previously last service in the list incremented by one.

### Stream

Streams are considered single entities of video or audio. They have metadata like a title, a description,
next/related videos, a thumbnail and comments. To obtain the URL to the actual stream data, as well as its metadata,
StreamExtractor is used. The LinkHandlerFactory will represent a link to such a stream. StreamInfoItemExtractor will
extract one item in a list of items representing such streams, like a search result or a playlist.
Since every streaming service (obviously) provides streams, this is required to implement. Otherwise, your service was
pretty useless :)

__Parts Required to be Implemented:__

- [StreamExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/stream/StreamExtractor.html)
- [StreamInfoItemExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/stream/StreamInfoItemExtractor.html)
- [LinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/LinkHandlerFactory.html)

### Search
The SearchExtractor is also required to be implemented. It will take a search query represented as
[SearchQueryHandler](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/SearchQueryHandler.html)
and return a list of search results. Since many services support suggestions as you type, you will also want to implement
a __SuggestionExtractor__. This will make it possible for the frontend to also display a suggestion while typing.

__Parts Required to be Implemented:__

- [SearchExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/search/SearchExtractor.html)
- [SearchQueryHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/SearchQueryHandlerFactory.html)
- [SuggestionExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/SuggestionExtractor.html) _(optional)_

### Playlist
Playlists are lists of streams provided by the service (you might not have to be concerned over locally saved playlists, those will be handled by the frontend).
A playlist may only contain __StreamInfoItems__, but no other __InfoItem__ types.

__Parts Required to be Implemented:__

- [PlaylistExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/playlist/PlaylistExtractor.html)
- [PlayListInfoItemExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/playlist/PlaylistExtractor.html)
- [ListLinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html)

### Channel
A Channel is mostly a [Playlist](#playlist), the only difference is that it does not only represent a simple list of streams, but also a
user, a channel, or any entity that could be represented as a user. This is why the metadata supported by the ChannelExtractor
differs from the one of a playlist.

__Parts Required to be Implemented:__

- [ChannelExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/channel/ChannelExtractor.html)
- [ChannelInfoItemExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/channel/ChannelExtractor.html)
- [ListLinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html)

### Kiosk
A kiosk is a list of __InfoItems__ which will be displayed on the main page of NewPipe. A kiosk is mostly similar to the content
displayed on the main page of a video platform. A kiosk could be something like "Top 20", "Charts", "News", "Creators Selection" etc.
Kiosks are controversial; many people may not like them. If you also don't like them, please consider your users and refrain from denying support for them.
Your service would look pretty empty if you select it and no video is being displayed. Also, you should not override the preference of the user,
since users of NewPipe can decide by the settings whether they want to see the kiosk page or not.

#### Multiple Kiosks
Most services will implement more than one kiosk, so a service might have a "Top 20" for different categories like "Country Music", "Techno", etc.
This is why the extractor will let you implement multiple __KioskExtractors__. Since different kiosk pages might also differ 
with their HTML structure, every page you want to support has to be implemented as its own __KioskExtractor__.
However, if the pages are similar, you can use the same implementation, but set the page type when you instantiate your __KioskExtractor__
through the __KioskList.KioskExtractorFactory__.

Every kiosk you implement needs to be added to your __KioskList__ which you return with your
__StreamingService__ implementation.

It is also important to set the default kiosk. This will be the kiosk that will be shown by the first start of your service.

An example implementation of the
[getKioskList()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.html)
could look like this:
```java
@Override
public KioskList getKioskList() throws ExtractionException {
    KioskList list = new KioskList(getServiceId());

    list.addKioskEntry(new KioskList.KioskExtractorFactory() {
        @Override
        public KioskExtractor createNewKiosk(StreamingService streamingService,
                                             String url,
                                             String id,
                                             Localization local)
        throws ExtractionException {
            return new YoutubeTrendingExtractor(YoutubeService.this,
                    new YoutubeTrendingLinkHandlerFactory().fromUrl(url), id, local);
        }
    }, new YoutubeTrendingLinkHandlerFactory(), "Trending");

    list.setDefaultKiosk("Trending");
    return list;
}

```

__Parts Required to be Implemented:__

- [KioskList.KioskExtractorFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/kiosk/KioskList.KioskExtractorFactory.html)
- [KioskExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/kiosk/KioskExtractor.html)
- [ListLinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html)

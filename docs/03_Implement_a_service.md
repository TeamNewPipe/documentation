# Implement a service

Services or better service connectors are the parts of NewPipe which communicative with an actual service like YouTube.
This Page will describe how you can implement and add your own to the extractor. Please make sure you read and understand the
[Concept of Extractors](https://teamnewpipe.github.io/documentation/01_Concept_of_the_extractor/)
and the [Concept of LinkHandler](https://teamnewpipe.github.io/documentation/02_Concept_of_LinkHandler/)
before doing this.

### Required and optional parts
Please be aware that your extractor has to implement certain parts, but does not have to implement all.
This is because not all services support every feature other services support. For example, it might be that a certain
service does not support channels. If so, you can leve out the implementation of channels, and make the corresponding
factory methode of the your __StreamingService__ implementation return __null__. The forntend will then automatically
leave out these parts.

However if you start to implement one of the optional parts of the list below, you have to implement all parts/classes
of it. NewPipe will crash if you only implement the extractor for the list item of a channel, but not the channel extractor itself.

__The parts of a service:__

- [Head of Service](#head-of-service)
- [Stream](#stream)
- [Search](#search)
- [Playlist](#playlist) _(optional)_
- [Channel](#channel) _(optional)_
- [Kiosk](#kiosk) _(optional)_

### Allowed Libraries

The NewPipe Extractor already comes along with a lot of usable tools and external libraries that should make extracting easy.
For some specific (tiny) tasks regex is allowed. Here you can take a look at the
[Parser](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/utils/Parser.html),
which will give you a little help with that. __Use Regex with care!!!__ Avoid it as often as possible. It's better to
ask us to introduce a new library than start using regex to often.

- Html/XML Parsing: [jsoup](https://jsoup.org/apidocs/overview-summary.html)
- JSON Parsiong: [nanojson](https://github.com/mmastrac/nanojson#parser-example)
- JavaScript Parsing/Execution: [Mozilla Rhino](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino/Documentation)
- Link dectection in strings: [AutoLink](https://github.com/robinst/autolink-java)

If you need to introduce new libraries please tell us before you do it.

### Head of Service

First of all if you want to create a new service you should create a new package below `org.schabi.newpipe.services`
, with the name of your service as package name. Here you must put an implementation of these two classes:

- [StreamingService](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.html)
- [ServiceInfo](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.ServiceInfo.html)

[StreamingService](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.html)
is a factory class that will return objects of all important parts of your service.
Every extractor, handler, and info type you add, and which should be part of your implementation, must be instantiated using an
instance of this class. You can see it as a factory for all objects of your implementation.

[ServiceInfo](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.ServiceInfo.html)
will return some meta information about your service. Such as the name, the capabilities, and your name as well as your 
email address for further notice and maintenance issues. Remember, after extending this class you need to return an
instance of it by through your implementation of
[`StreamingService.getServiceInfo()`](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.html#getServiceInfo--).

When these two classes are extended by you, you need to add your `StreamingService` to the
[ServiceList](https://github.com/TeamNewPipe/NewPipeExtractor/blob/49c2eb51859a58e4bb5ead2d9d0771408f7d59d6/extractor/src/main/java/org/schabi/newpipe/extractor/ServiceList.java#L23)
of NewPipe. This way your service will become an official part of the NewPipe Extractor.
Every service has an ID, which will be set when this list gets created. You need to set this ID by entering it in the constructor.
So when adding your service just give it the ID of the previously last service in the list incremented by one.

### Stream

Streams are considered single entities of video or audio, the come along with metainformation like a title, a description,
next/related videos, thumbnail and commends. For getting the url to the actual stream data as well as this metainformation
StreamExtractor is used. The LinkHandlerFactory will represent a link to such a stream. StreamInfoItemExtractor will
extract one item in a list of items representing such Streams, like a search result or a playlist.
Since every Streaming service (obviously) provides streams this is required to implement. Otherwise your service was
pretty useless :)

- [StreamExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/stream/StreamExtractor.html)
- [StreamInfoItemExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/stream/StreamInfoItemExtractor.html)
- [LinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/LinkHandlerFactory.html)

### Search
The SearchExtractor is also required to be implemented. It will take a search query represented as [SearchQueryHandler](link here),
and return a list of search results. Since many services support a suggestion popup while you type you will also want to implement
a __SuggestionExtractor__. This will make it possible for the frontend to as well display a suggestion while typing.

- [SearchExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/search/SearchExtractor.html)
- [SearchQueryHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/SearchQueryHandlerFactory.html)
- [SuggestionExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/SuggestionExtractor.html) _(optional)_

### Playlist
Playlists are lists of streams provided by the service (you may not have to take care about locally saved playlists. This will be handled by the frontend).
A playlist may only contains __StreamItems__, but no other __InfoItem__ types.

- [PlaylistExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/playlist/PlaylistExtractor.html)
- [PlayListInfoItemExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/playlist/PlaylistExtractor.html)
- [ListLinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html)

### Channel
A Channel is mostly a [Playlist](#playlist), the only diferens is that it does not represent a simple list of streams, but a
user, a channel, or any entity that could be represented as a user. This is why the metadata supported by the channel extractor
differs form the one of a playlist.

- [ChannelExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/channel/ChannelExtractor.html)
- [ChannelInfoItemExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/channel/ChannelExtractor.html)
- [ListLinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html)

### Kiosk
- [KioskExtractorFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/kiosk/KioskList.KioskExtractorFactory.html)
- [KioskExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/kiosk/KioskExtractor.html)
- [ListLinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html)

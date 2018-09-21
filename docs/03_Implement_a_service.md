# Implement a service

Services or better service connectors are the parts of NewPipe which communicative with an actual service like YouTube.
This Page will describe how you can implement and add your own. Please make sure you red and understand the
[Concept of Extractors](https://teamnewpipe.github.io/documentation/01_Concept_of_the_extractor/)
and the [Concept of LinkHandler](https://teamnewpipe.github.io/documentation/02_Concept_of_LinkHandler/)
before implementing your own Service.

### Allowed Libraries

The NewPipe Extractor already comes a long with a lot of usable tools and external libraries that should make extracting easy.
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
Every extractor Kisok, Info type you add, and which should be part of your implementation must be instantiated using an
instance of this class.

[ServiceInfo](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.ServiceInfo.html)
will return some meta information about your service. Such as the name, the capabilities, and your name as well as your 
email address for further notice and maintenance issues. Remember, after extending this class you need to return an
instance of it by through your implementation of
[`StreamingService.getServiceInfo()`](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.html#getServiceInfo--).

When these two classes are extended by you, you need to add them to the
[ServiceList](https://github.com/TeamNewPipe/NewPipeExtractor/blob/49c2eb51859a58e4bb5ead2d9d0771408f7d59d6/extractor/src/main/java/org/schabi/newpipe/extractor/ServiceList.java#L23)
of NewPipe. This way the will become an official part of the NewPipe Extractor.
Every service has an ID, which will be set when this list gets created. You set this Id by entering it in the constructor.
So when adding your service just give it the ID of the previously last service in the list incremented by one.

### Search
- [SearchExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/search/SearchExtractor.html)
- [SearchQueryHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/SearchQueryHandlerFactory.html)

### Stream
- [StreamExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/stream/StreamExtractor.html)
- [StreamInfoItemExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/stream/StreamInfoItemExtractor.html)
- [LinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/LinkHandlerFactory.html)

### Channel
- [ChannelExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/channel/ChannelExtractor.html)
- [ChannelInfoItemExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/channel/ChannelExtractor.html)
- [ListLinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html)

### Playlist
- [PlaylistExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/playlist/PlaylistExtractor.html)
- [PlayListInfoItemExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/playlist/PlaylistExtractor.html)
- [ListLinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html)

### Kiosk
- [KioskExtractorFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/kiosk/KioskList.KioskExtractorFactory.html)
- [KioskExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/kiosk/KioskExtractor.html)
- [ListLinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/ListLinkHandlerFactory.html)

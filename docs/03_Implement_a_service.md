# Implement a service

Services or better service connectors are the parts of NewPipe which communicative with an actual service like YouTube.
This Page will describe how you can implement and add your own. Please make sure you red and understand the
[Concept of Extractors](https://teamnewpipe.github.io/documentation/01_Concept_of_the_extractor/)
and the [Concept of LinkHandler](https://teamnewpipe.github.io/documentation/02_Concept_of_LinkHandler/)
before implementing your own Service.

## The service

- [ServiceList](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/ServiceList.html)
- [StreamingService](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.html)
- [ServiceInfo](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/StreamingService.ServiceInfo.html)

__The parts of a service:__

- [Stream](#stream)
- [Search](#search)
- [Channel](#channel) _(optional)_
- [Playlist](#playlist) _(optional)_
- [Kiosk](#kiosk) _(optional)_

### Stream
- [StreamExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/stream/StreamExtractor.html)
- [StreamInfoItemExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/stream/StreamInfoItemExtractor.html)
- [LinkHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/LinkHandlerFactory.html)

### Search
- [SearchExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/search/SearchExtractor.html)
- [SearchQueryHandlerFactory](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/linkhandler/SearchQueryHandlerFactory.html)
- [SuggestionExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/SuggestionExtractor.html) _(optional)_

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

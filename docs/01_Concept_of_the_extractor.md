# Concept of the Extractor

## The Collector/Extractor Pattern

Before you start coding your own service, you need to understand the basic concept of the extractor itself. There is a pattern
you will find all over the code, called the __extractor/collector__ pattern. The idea behind it is that
the [extractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/Extractor.html)
would produce fragments of data, and the collector would collect them and assemble that data into a readable format for the front end.
The collector also controls the parsing process, and takes care of error handling. So, if the extractor fails at any
point, the collector will decide whether or not it should continue parsing. This requires the extractor to be made out of
multiple methods, one method for every data field the collector wants to have. The collectors are provided by NewPipe.
You need to take care of the extractors.

### Usage in the Front End

A typical call for retrieving data from a website would look like this:
``` java
Info info;
try {
    // Create a new Extractor with a given context provided as parameter.
    Extractor extractor = new Extractor(some_meta_info);
    // Retrieves the data form extractor and builds info package.
    info = Info.getInfo(extractor);
} catch(Exception e) {
    // handle errors when collector decided to break up extraction
}
```

### Typical Implementation of a Single Data Extractor

The typical implementation of a single data extractor, on the other hand, would look like this:
``` java
class MyExtractor extends FutureExtractor {

    public MyExtractor(RequiredInfo requiredInfo, ForExtraction forExtraction) {
        super(requiredInfo, forExtraction);

        ...
    }

    @Override
    public void fetch() {
        // Actually fetch the page data here
    }

    @Override
    public String someDataFiled() 
        throws ExtractionException {    //The exception needs to be thrown if someting failed
        // get piece of information and return it
    }

    ...                                 // More datafields
}
```

## Collector/Extractor Pattern for Lists

Information can be represented as a list. In NewPipe, a list is represented by a
[InfoItemsCollector](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/InfoItemsCollector.html).
A InfoItemsCollector will collect and assemble a list of [InfoItem](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/InfoItem.html).
For each item that should be extracted, a new Extractor must be created, and given to the InfoItemsCollector via [commit()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/InfoItemsCollector.html#commit-E-).

![InfoItemsCollector_objectdiagram.svg](img/InfoItemsCollector_objectdiagram.svg)

If you are implementing a list in your service you need to implement an [InfoItemExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/Extractor.html),
that will be able to retrieve data for one and only one InfoItem. This extractor will then be _comitted_ to the __InfoItemsCollector__ that can collect the type of InfoItems you want to generate.

A common implementation would look like this:
```
private SomeInfoItemCollector collectInfoItemsFromElement(Element e) {
    // See *Some* as something like Stream or Channel
    // e.g. StreamInfoItemsCollector, and ChannelInfoItemsCollector are provided by NP
    SomeInfoItemCollector collector = new SomeInfoItemCollector(getServiceId());

    for(final Element li : element.children()) {
        collector.commit(new InfoItemExtractor() {
            @Override
            public String getName() throws ParsingException {
                ...
            }

            @Override
            public String getUrl() throws ParsingException {
                ...
            }
            
            ...
    }
    return collector;
}

```

## ListExtractor

There is more to know about lists:

1. When a streaming site shows a list of items, it usually offers some additional information about that list like its title, a thumbnail,
and its creator. Such info can be called __list header__.

2. When a website shows a long list of items it usually does not load the whole list, but only a part of it. In order to get more items you may have to click on a next page button, or scroll down.

Both of these Problems are fixed by the [ListExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/ListExtractor.html) which takes care about extracting additional metadata about the list,
and by chopping down lists into several pages, so called [InfoItemsPage](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/ListExtractor.InfoItemsPage.html)s.
Each page has its own URL, and needs to be extracted separately.


For extracting list header information a `ListExtractor` behaves like a regular extractor. For handling `InfoItemsPages` it adds methods
such as:

 - [getInitialPage()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/ListExtractor.html#getInitialPage--)
   which will return the first page of InfoItems.
 - [getNextPageUrl()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/ListExtractor.html#getNextPageUrl--)
   If a second Page of InfoItems is available this will return the URL pointing to them.
 - [getPage()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/ListExtractor.html#getPage-java.lang.String-)
   returns a ListExtractor.InfoItemsPage by its URL which was retrieved by the `getNextPageUrl()` method of the previous page.


The reason why the first page is handled special is because many Websites such as YouTube will load the first page of
items like a regular web page, but all the others as an AJAX request.

An InfoItemsPage itself has two constructors which take these parameters:
- The __InfoitemsCollector__ of the list that the page should represent
- A __nextPageUrl__ which represents the url of the following page (may be null if not page follows).
- Optionally __errors__ which is a list of Exceptions that may have happened during extracton.

Here is a simplified reference implementation of a list extractor that only extracts pages, but not metadata:

```
class MyListExtractor extends ListExtractor {
    ...
    private Document document;

    ...

    public InfoItemsPage<SomeInfoItem> getPage(pageUrl)
        throws ExtractionException {
        SomeInfoItemCollector collector = new SomeInfoItemCollector(getServiceId());
        document = myFunctionToGetThePageHTMLWhatever(pageUrl);

        //remember this part from the simple list extraction
        for(final Element li : document.children()) {
            collector.commit(new InfoItemExtractor() {
                @Override
                public String getName() throws ParsingException {
                    ...
                }

                @Override
                public String getUrl() throws ParsingException {
                    ...
                }
                ...
        }
        return new InfoItemsPage<SomeInfoItem>(collector, myFunctionToGetTheNextPageUrl(document));
    }

    public InfoItemsPage<SomeInfoItem> getInitialPage() {
        //document here got initialzied by the fetch() function.
        return getPage(getTheCurrentPageUrl(document));
    }
    ... 
}
```

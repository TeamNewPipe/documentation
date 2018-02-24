# Concept of the Extractor

## Collector/Extractor pattern

Before we can start coding our own service we need to understand the basic concept of the extractor. There is a pattern
you will find all over the code. It is called the __extractor/collector__ pattern. The idea behind this pattern is that
the [extractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/Extractor.html)
would produce single peaces of data, and the collector would take it and form usable data for the front end out of it.
The collector also controls the parsing process, and takes care about error handling. So if the extractor fails at any
point the collector will decide whether it should continue parsing or not. This requires the extractor to be made out of
many small methods. One method for every data field the collector wants to have. The collectors are provided by NewPipe.
You need to take care of the extractors.

### Usage in the front end

So typical call for retrieving data from a website would look like this:
```java
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

### Typical implementation of a single data extractor

The typical implementation of a single data extractor on the other hand would look like this:
```java
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

## Collector/Extractor pattern for lists

Sometimes information can not be represented as a structure, but as a list. In NewPipe an item of a list is called
[InfoItem](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/InfoItem.html). In order
to get such items a [InfoItemsCollector](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/InfoItemsCollector.html)
is used. For each item that should be extracted a new Extractor will be given to the InfoItemCollector via [commit()](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/InfoItemsCollector.html#commit-E-).

![InfoItemsCollector_objectdiagram.svg](img/InfoItemsCollector_objectdiagram.svg)

When a streaming site shows a list it usually offers some additional information about that list, like it's title, a thumbnail
or its creator. Such info can be called __list header__.

Also if you open a list in a web browser the website usually does not load the whole list, but only a part
of it. In order to get more you may have to click on a next page button, or scroll down. This is why a list in
NewPipe is coped down into [InfoItemPage](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/ListExtractor.InfoItemPage.html)s. Each Page has its own URL, and needs to be extracted separately.

List header information and extracting multiple pages of an InfoItem list can be handled by a
[ListExtractor](https://teamnewpipe.github.io/NewPipeExtractor/javadoc/org/schabi/newpipe/extractor/ListExtractor.html)







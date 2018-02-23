# Basic Concept of the Extractor

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
    Extractor extractor = new Extractor(ome_meta_info);
    // Retrieves the data form extractor and builds info package.
    info = Info.getInfo(extractor);
} catch(Exception e) {
    // handle errors when collector decided to break up extraction
}
```









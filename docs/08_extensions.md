# NewPipe extensions

## File format

A NewPipe extension is a signed JAR file containing the following files:

### `about.json`

This is a JSON file describing things about the extension. It should have the following fields:

- `name`: This should be the name of the extension. It should be exactly the same as the name returned by `StreamingService$ServiceInfo#getName()`. If the extension replaces a built-in service, its name should be exactly the same as the name of the built-in service.
- `author`: This should be the name(s) of the author(s) of the extension.
- `class`: This should be the fully qualified name of the class that extends `StreamingService`. It should be located in a subpackage of `org.schabi.newpipe.extractor.extensions.services`.
- `major_version`: The major internal version of NewPipe Extractor that this extension is compatible with.
- `minor_version`: The minor internal version of NewPipe Extractor that this extension is compatible with. It will also work on later minor internal versions of NewPipe Extractor.
- `replaces` (optional): The ID of the service that this extension replaces.

### `classes.dex`

This is the Dalvik Executable compiled from your Java code.

### `icon.png`

This is a PNG with a resolution of 512x512 containing the logo of the service in white on a transparent background.

## Runtime environment

You could add the following compile-only dependencies to your project:

- `com.github.TeamNewPipe:NewPipeExtractor`
- `com.github.TeamNewPipe:nanojson`
- `org.jsoup:jsoup`
- `com.github.spotbugs:spotbugs-annotations`

For versions, please check the `build.gradle` of the version of NewPipe Extractor you want to target.

For security reasons, only a limited amount of classes could be used.

### Allowed classes

- `dalvik.annotation.*`
- `javax.annotation.*`
- `java.lang.*`
- `java.util.*`
- `java.text.*`
- `com.grack.nanojson.*`
- `org.schabi.newpipe.extractor.*`
- `java.io.IOException`
- `java.io.UnsupportedEncodingException`
- `java.io.InputStream`
- `java.net.URL`
- `java.net.MalformedURLException`
- `java.net.URLEncoder`
- `java.net.URLDecoder`
- `java.net.URI`
- `java.net.URISyntaxException`
- `org.jsoup.Jsoup`
- `org.jsoup.nodes.Document`
- `org.jsoup.nodes.Element`
- `org.jsoup.parser.Parser`
- `org.jsoup.select.Elements`

### Disallowed classes

- `java.lang.reflect.*`
- `org.schabi.newpipe.extractor.services.*`
- `java.lang.Class` (this unfortunately means you can't define `enum`s)
- `java.lang.ClassLoader`
- `org.schabi.newpipe.extractor.ServiceList`

# Book Notes on JavaScript for Web Developers

## What is JavaScript?

**JavaScript** is a scripting language designed to interact with web pages.

######3 distinct parts:
- ECMAScript - defined in ECMA-262 and provides the core functionality
- Document Object Model (DOM) - provides methods and interfaces for working with
the content of a web page
- Browser Object Model (BOM) - provides methods and interfaces for interacting with
the browser

######Browser compatibility:
- ECMAScript - good across all browsers
- DOM - varies widely
- BOM - no standard, some commonalities

## JavaScript in HTML

- Insert JavaScript to HTML in two ways: **inline** or from **external file**.
- Declare `type` attribute as "text/javascript".
- Set `src` to the URL of the file.

*inline JavaScript*
```
<script type="text/javascript" src="jquery.min.js"><script>
```
*JavaScript from external file*
```
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
```

- All `<script>` elements are interpreted in the order in which they occur on the page.
- `<script>` elements are usually included toward the end of the page, just before the closing `</body>` tag.
- Defer a script’s execution until after the document has rendered by using the `defer` attribute (for IE only).
- Use `<noscript>` to specify that content is to be shown only if scripting support isn’t available on the browser.

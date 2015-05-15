# Book Notes on JavaScript for Web Developers

## 1. What is JavaScript?

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

## 2. JavaScript in HTML

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

## 3. Language Basics

#### On Syntax
1. Case-sensitivity - `typeof` != `typeOf`
2. Identifiers - starts with a letter, `_`, or `$`; functions are in camelCase
3. Comments - use `//comment` for single line, and `/* comment */` for multi line
4. Statements - use semicolons `;` for single lines, and code blocks `{ }`for multiple & control statements

#### Variables
- loosely-typed (can hold any type of data, though not best to switch from one to another)
- `var` to define a variable in local scope e.g.`var name='Nadine';`
- no `var` to define a variable globally (not recommended) e.g. `name='Nadine';`
- define multiple variables e.g. `var message='hi', name='nadine', age='23';`

#### Data Types

###### Primitive types
1. Undefined - any uninitialized variable
2. Null - empty object pointer
3. Boolean - `true` or `false` (distinct from `1` and `0`)
4. Number - convert to number using `Number()`, `parseInt()`, `parseFloat()`; `NaN` when not a number
5. String - convert to string using `toString()`, `String()`

###### Complex type
6. Object (unordered list of name-value pairs)

Determine data type with `typeof` operator. e.g. `alert(typeof 23);`

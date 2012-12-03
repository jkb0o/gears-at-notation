Gears @ notation
=================
Specify requirements using @require notation.

It is stricted notation. No attemt to determine file extention.
No need to depend on same filetype.

Usage
-----

If you use pure gears:
```python
environment.preprocessor.register('text/css', AtDirectivesProcessor.as_handler())
environment.preprocessor.register('application/javascript', AtDirectivesProcessor.as_handler())
```

For django:
```python
GEARS_PREPROCESSORS = {
    'text/css': 'gears_at_notation.processor.AtDirectivesProcessor',
    'application/javascript': 'gears_at_notation.processor.AtDirectivesProcessor',
}
```

Now you can specify dependencies in different way:
```
// file style.css
// @require "main.css"
// @require "application.less"
// @require "modules.styl"
```


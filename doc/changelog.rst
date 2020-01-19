Changelog
=========

Version 0.1.6
-------------

To be released.

- New option ``label`` to add a label/anchor that can be referenced with ``:ref:``.


Version 0.1.5
-------------

Released on May 15, 2018.

- New ``:groups:`` option to render argument groups. [by Lukas Atkinson]


Version 0.1.4
-------------

Released on February 27, 2018.

- Fixed a :rst:dir`.. autoprogram::` bug that raises :exc:`AttributeError`
  during build without ``:no_usage_codeblock:`` option on Python 2.
  [:bbissue:`168`, :bbissue:`169`]
- Fixed an issue with Sphinx 1.7 which removed ``sphinx.util.compat``.
  [:issue:`1`, :issue:`2` by Zach Riggle]


Version 0.1.3
-------------

Released on October 7, 2016.

- Fixed a bug that descriptions with :class:`~argparse.RawTextHelpFormatter`
  had been incorrectly formatted.  [:bbpull:`123` by Aaron Meurer]
- Fixed crash when metavars is a tuple (i.e. for ``nargs > 1``).
  [:bbpull:`112` by Alex Honeywell]
- Fixed usage string for subcommands (subcommands were previously showing
  the top-level command usage).  [:bbpull:`112` by Alex Honeywell]
- Added :ref:`new options <autoprogram-options>` to :rst:dir:`.. autoprogram::`
  directive:  [:bbpull:`112` by Alex Honeywell]
    
  - ``maxdepth``
  - ``no_usage_codeblock``
  - ``start_command``
  - ``strip_usage``

- Fixed suppressed arguments (using :const:`argparse.SUPPRESS` flag)
  to become ignored.  [:bbissue:`166`]


Version 0.1.2
-------------

Released on August 18, 2015.

- Fixed crash with empty fields.  [:bbissue:`110`]
- Fixed :exc:`ImportError` with non-module Python scripts (i.e. files not
  ending with :file:`.py`).  [:bbpull:`101` by Matteo Bachetti]


Version 0.1.1
-------------

Released on April 22, 2014.

- Omit metavars of ``store_const``/``store_true``/``store_false`` options.
- Sort subcommands in alphabetical order if Python 2.6 which doesn't have
  :class:`collections.OrderedDict`.


Version 0.1.0
-------------

Released on March 2, 2014.  The first release.

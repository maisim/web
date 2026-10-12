The new periods are offered in the date filter of every search panel, next to the ones of the
client. They behave as follows:

- the day and week periods are complete on their own: they do not select a year, and removing a year
  does not drop them. The periods of the client (months, quarters) cannot be used without a year:
  the client selects one automatically for them;
- a sliding window covers exactly its number of days, the current day included;
- once a period is compared ("Previous Period"), a sliding window is compared to the window of the
  same width just before it, and a week is described by its ISO week number and year.

The periods are added to the search panel of the client. The legacy control panel, which a few old
views still use, keeps its own list of periods and is not extended by this module.

The periods are active as soon as the module is installed: they change the list of the date filter
for every user. The QUnit test of the client which checks that exact list
(`web/static/tests/search/filter_menu_tests.js`) has to be adapted accordingly; it is not run by the
CI of this repository.

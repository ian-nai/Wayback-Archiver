# Simple-Web-Archiver
Simple web archiving scripts using Python. These scripts use [savepagenow](https://github.com/pastpages/savepagenow) and [requests](https://requests.readthedocs.io/en/master/) to archive webpages using the Internet Archive's [Wayback Machine](https://archive.org/web/).

## [wayback_archiver.py](https://github.com/ian-nai/Simple-Web-Archiver/blob/master/wayback_archiver.py)
This script archives all of the urls included in a 'urls.txt' file provided by the user, then outputs the new urls for the archived versions of the pages. This could be used to archive pages on a regular schedule, using either [Windows Scheduler](https://datatofish.com/python-script-windows-scheduler/) or [launchd](https://nathangrigg.com/2012/07/schedule-jobs-using-launchd) for Mac.

## [archive_uncaptured_pages.py](https://github.com/ian-nai/Simple-Web-Archiver/blob/master/archive_uncaptured_pages.py)
This script detects whether a page has been archived already, and if it hasn't it archives the page and saves the url where the archived version is located. It also outputs the archived urls for pages that have already been captured.

=======
fileorg
=======

Utility functions for corpus and experiment file management in Python.

============
Installation
============

pip install git+https://github.com/phonetics-projects/file-organization

=============
Documentation
=============

========
Examples
========

.. code-block:: Python

  from fileorg import dir_to_df, today_YYYYMMDD, timestamp_now, cp_backup

  # Get all files in `mypath` as a dataframe
  df = dir_to_df(mypath)

  # Get all `.wav` files in `mypath` as a dataframe
  df = dir_to_df(mypath, fnpat=r'\.wav$')

  # Get all `.wav` files in `mypath` and extract named captures as
  # categorical `subj` and `token` columns
  df = dir_to_df(
      mypath,
      fnpat=r'(?P<subj>[A-Z]+\d+)-(?P<token>\d+)\.wav$'
  )

  # Get today's date in YYYYMMDD format
  todaystr = today_YYYYMMDD()

  # Get timestamp as YYYY-MM-DDTHHMMSS string and UTC offset for current
  # the current datetime
  tstamp, utcoffset = timestamp_now()

  # Copy a file to a backup directory with a version number
  copyname = cp_backup(origfile, backupdir)

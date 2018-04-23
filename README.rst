======
Task 1
======

Short version, typed by user in a console:

.. code-block:: bash

    cat /etc/passwd | grep -v nologin | grep -v false | cut -d ":" -f 1,7 | tr ":" "\t"


Long version, bash script **bin/task1-show-allowed-users**. This version is improved,
will check for example if the login shell is either valid or not. Use properly
tools get file contents instead of just reading it raw way.

.. code-block:: bash

    #!/bin/bash

    for uid in $(getent passwd | cut -f3 -d:);
    do
        shell=$(getent passwd $uid | cut -f7 -d:);
        if grep -q $shell /etc/shells; then
            user=$(getent passwd $uid | cut -f1);
            echo "$user\t$shell";
        fi
    done


======
Task 2
======

This application is framework agnostic. The application is decoupled and
doesn't depends a specific framework.

The application code is available at **task2/app.py**.


Tests
=====

The tests aren't written using **pytest** style but the discovery is made by it
with some *fancy plugins*.

Tests for HTTP API calls unavailable.


Request Logs
============

The request logs aren't being logged as database entries, but using the classic
logging system on **task2.app** package.


Caching Layer
=============

The cache layer is available at **task2/cache.py**.  There is no sharing
persistence across running instances but the basic funcionally is there.
(Connect to a memcached server doesn't looks like a problem).

NO BENCHMARKS available.


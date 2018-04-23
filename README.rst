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


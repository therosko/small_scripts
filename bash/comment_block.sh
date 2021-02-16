#!/bin/bash

echo This will be echoed
: <<'END'
This here
will not
END
echo This also will be echoed
Flask Web Server with Teradata query
=============

Runs a Teradata query and prints results to log, then returns results in HTTP request

To use:

* Add config to udaexec.ini
* Update connection params in /query function
* Encode return value as JSON

Uses the Anaconda Teradata and Unixodbc driver packages (see environment.yml)

Runtime uses Python Conda

# Ref: http://developer.teradata.com/tools/reference/teradata-python-module
# Ref: https://developer.teradata.com/tools/reference/teradata-python-module#UdaExec Parameters

@echo off

%~d0
cd %~d0%~p0

set sikuli_jar=%sikuli_home%sikuli-script.jar
set CLASSPATH=%sikuli_jar%
set JYTHONPATH=%sikuli_jar%/Lib

call jybot --pythonpath=TestLib ^
      --outputdir=results ^
      --loglevel=TRACE ^
      --output "%~d0%~p0results\output.xml" ^
      --log "%~d0%~p0results\log.html" ^
      --report "%~d0%~p0results\report.html" ^
      testsuite

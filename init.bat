@echo off
:: Copyright (c) 2019 TECNALIA Research & Innovation. All rights reserved.
::
:: OPERATING SYSTEM:   Microsoft Windows 7 Professional Service Pack 1
:: LANGUAGE:           Windows batch script
:: IDE:                notepad++
:: DATE:               2019/02/19
:: AUTHOR:             sandra.riano@tecnalia.com
::
:: PROJECT:            skel_console
:: FILE:               init.bat
:: DESCRIPTION:
::     This file defines a MS Windows batch script for setting environmental
::     variables.
::     It defines:
::         - GIT_HOME: Directory of GIT
::         - GNU_HOME: Directory of GNU tools (optional)
::         - PYTHON_HOME: Directory of Python distribution to use (optional)
::         - _REPO_SOURCE: Directory of source repo (input data). Maybe in T:
::         - _REPO_DESTINY: Directory of local code folder (thePath\repo\raw)
::     It adds:
::         - All HOME variables to local PATH
::         - The content of _REPO_SOURCE to _REPO_DESTINY if the 2nd is empty
::     Environment variable requisites:
::         - None
::------------------------------------------------------------------------------

:: -- Print an empty line ------------------------------------------------------
echo.

:: -- Set environment variables ------------------------------------------------
:: -- NOTE: these directories must be modified for each case
set GIT_HOME=D:\Aplic\PortableGit\bin
set GNU_HOME=D:\Aplic\UnxUtils\usr\local\wbin
set PYTHON_HOME=D:\Aplic\Python\Python37

set _REPO_SOURCE=
set _REPO_DESTINY=


:: -- Check if file has been edited --------------------------------------------
IF "%GIT_HOME%"=="" goto :errorChangeDirectories
IF "%GIT_HOME%"=="D:\Aplic\PortableGit\bin" goto :errorChangeDirectories
IF "%_REPO_SOURCE%"=="" goto :errorChangeDirectories
IF "%_REPO_DESTINY%"=="" goto :errorChangeDirectories


:: -- Add local path -----------------------------------------------------------
set PATH=%GIT_HOME%;%PATH%
set PATH=%GNU_HOME%;%PATH%
set PATH=%PYTHON_HOME%;%PATH%
set PATH=%PYTHON_HOME%\Scripts;%PATH%


:: -- Show environment ---------------------------------------------------------
echo ---------------------------------------------------------------------------
echo Defined GIT_HOME: %GIT_HOME%
echo Defined GNU_HOME: %GNU_HOME%
echo Defined PYTHON_HOME: %PYTHON_HOME%
echo Use %%PYTHON_HOME%%\python
echo.
echo Added GIT directory to path
echo Added GNU tools directory to path
echo Added Python directory to path
echo ---------------------------------------------------------------------------
echo.

:: -- Add content from _REPO_SOURCE----------------------------------------------
:: Check if folder is empty before copy from source repository
set _TMP=
for /f "delims=" %%a in ('dir /b "%_REPO_DESTINY%"') do set _TMP="%%a"
IF {%_TMP%}=={} (
	goto :copyRepoSource
) ELSE (
   	goto :alreadyCopied
)

:copyRepoSource
echo ---------------------------------------------------------------------------
echo Copying repo files from %_REPO_SOURCE%
xcopy %_REPO_SOURCE% %_REPO_DESTINY% /E
echo ---------------------------------------------------------------------------
echo.
goto :cleanup

:alreadyCopied
echo ---------------------------------------------------------------------------
echo %_REPO_DESTINY% already contains data. 
echo No files have been added. If it should be updated, please do it manually
echo ---------------------------------------------------------------------------
echo.
goto :cleanup

:: ----- Error: Paths need to be changed  -----------------------------------
:errorChangeDirectories
echo ---------------------------------------------------------------------------
echo ERROR in execution
echo Check environment variables defined in section "Set environment variables"
echo  of init.bat file. Please insert the suitable values for your project.
echo ---------------------------------------------------------------------------
goto :cleanup

:: ----- Restore Environment Variables --------------------------------------
:cleanup
set _REPO_SOURCE=
set _REPO_DESTINY=
set _TMP=
set GIT_HOME=
set GNU_HOME=
set PYTHON_HOME=


:finish


:: Copyright (c) 2019 TECNALIA Research & Innovation. All rights reserved.
::
:: OPERATING SYSTEM:   Microsoft Windows 7 Professional Service Pack 1
:: LANGUAGE:           Windows batch script
:: IDE:                notepad++
:: DATE:               2019/04/08
:: AUTHOR:             sandra.riano@tecnalia.com
::
:: PROJECT:            skel_console_python
:: FILE:               copyRepo.bat
:: DESCRIPTION:
::     This file defines a MS Windows batch script for copying the repo
::     data (in T: or similar path) to the working directory of the project
::		(./repo/raw)
::     It defines the following environmental variables:
::         - INPUT_REPO: Directory where input data are. Maybe in T:
::		   - WORKING_REPO: Raw repository of working directory (.\repo\raw)
::     It adds:
::         - All environmental variables to local PATH
::         - The content of INPUT_REPO to WORKING_REPO (.\repo\raw)
::     Environment variable requisites:
::         - None
::------------------------------------------------------------------------------
@echo off
:: -- Print an empty line ------------------------------------------------------
echo.

:: -- Set environment variables ------------------------------------------------
:: -- NOTE: INPUT_REPO must be modified for each case
set INPUT_REPO=
set WORKING_REPO=.\repo\raw

:: -- Check if file has been edited --------------------------------------------
IF "%INPUT_REPO%"=="" goto :errorChangeDirectories
IF "%WORKING_REPO%"=="" goto :errorChangeDirectories

:: -- Add local path -----------------------------------------------------------
set PATH=%INPUT_REPO%;%PATH%
set PATH=%WORKING_REPO%;%PATH%

:: -- Show environment ---------------------------------------------------------
echo ---------------------------------------------------------------------------
echo Defined INPUT_REPO: %INPUT_REPO%
echo Defined WORKING_REPO: %WORKING_REPO%
echo.
echo Added INPUT_REPO to path
echo Added WORKING_REPO to path
echo ---------------------------------------------------------------------------
echo.

:copyRepoSource
echo ---------------------------------------------------------------------------
echo Copying repo files from %INPUT_REPO%
xcopy %INPUT_REPO% %WORKING_REPO% /E
echo ---------------------------------------------------------------------------
echo.
goto :cleanup

:: ----- Error: Paths need to be changed  -----------------------------------
:errorChangeDirectories
color C
echo ---------------------------------------------------------------------------
echo ERROR in execution
echo Check environment variables defined in section "Set environment variables"
echo  of copyRepo.bat file. Please insert the suitable values for your project.
echo ---------------------------------------------------------------------------
goto :cleanup

:: ----- Restore Environment Variables --------------------------------------
:cleanup
set INPUT_REPO=
set WORKING_REPO=
set _TMP=


:finish


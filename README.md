# Visadore
A plug-in manager for modules that implement complex pyvisa resource interactions.
Visadore is built on top of the stevedore package module that provides a driver interface to plug-in modules.
Each plug-in module is registered in setuptool's entry point registry.

#Invoking Visadore
Invoking Visadore is easy...

    Python 3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from visadore import get
    >>> instrument = get("TCPIP::192.168.1.100::INSTR")

When invoked, the get() method queries the IDN string from the specified instrument.
The instrument is specified using the standard VISA resource name syntax.
Using the IDN string, Visadore searches for setuptools entry points that matches the instrument's manufacturer and model number.
The is an unique entry point for each feature.
When one or more matching entry points are found, Visadore dynamically creates a new class for that instrument.
The new class includes all of the features identified during the entry point search.

#Features Implemented by Visadore

Visadore does not implement any actual instrument features.
Instrument features must implemented by other package modules which import visadore and register the features as setuptools entry points.

*Actually, there are a few features implemented in a "mock instrument" that is used solely by Visadore test code.*

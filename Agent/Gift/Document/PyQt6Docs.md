# Reference Guide — PyQt Documentation v6.11.0

**源 URL:** https://www.riverbankcomputing.com/static/Docs/PyQt6/
**生成日期:** 2026-05-16 15:20
**页面数:** 44

---

## 目录

- [Reference Guide — PyQt Documentation v6.11.0](#reference-guide--pyqt-documentation-v6110)
- [Introduction](#introduction)
- [Contributing to this Documentation](#contributing-to-this-documentation)
- [Support for Old Versions of Python](#support-for-old-versions-of-python)
- [Installing PyQt6](#installing-pyqt6)
- [Differences Between PyQt6 and PyQt5](#differences-between-pyqt6-and-pyqt5)
- [Support for Signals and Slots](#support-for-signals-and-slots)
- [Support for Qt Properties](#support-for-qt-properties)
- [Other Support for Dynamic Meta-objects](#other-support-for-dynamic-meta-objects)
- [Support for Qt Interfaces](#support-for-qt-interfaces)
- [Support for QVariant](#support-for-qvariant)
- [Support for QSettings](#support-for-qsettings)
- [Integrating Python and QML](#integrating-python-and-qml)
  - [qmlRegisterType()](#qmlregistertype)
  - [qmlAttachedPropertiesObject()](#qmlattachedpropertiesobject)
  - [qmlRegisterType()](#qmlregistertype)
  - [qmlAttachedPropertiesObject()](#qmlattachedpropertiesobject)
- [Support for Cooperative Multi-inheritance](#support-for-cooperative-multi-inheritance)
- [Things to be Aware Of](#things-to-be-aware-of)
- [Using Qt Designer](#using-qt-designer)
  - [QObject](#qobject)
  - [QPyDesignerCustomWidgetPlugin](#qpydesignercustomwidgetplugin)
  - [QPyDesignerCustomWidgetPlugin](#qpydesignercustomwidgetplugin)
  - [pyqtSlot()](#pyqtslot)
- [Support for Pickling](#support-for-pickling)
  - [QByteArray](#qbytearray)
  - [QColor](#qcolor)
  - [QDate](#qdate)
  - [QDateTime](#qdatetime)
  - [QKeySequence](#qkeysequence)
  - [QLine](#qline)
  - [QLineF](#qlinef)
  - [QPoint](#qpoint)
  - [QPointF](#qpointf)
  - [QPolygon](#qpolygon)
  - [QRect](#qrect)
  - [QRectF](#qrectf)
  - [QSize](#qsize)
  - [QSizeF](#qsizef)
  - [QTime](#qtime)
- [Using PyQt6 from the Python Shell](#using-pyqt6-from-the-python-shell)
- [Internationalisation of PyQt6 Applications](#internationalisation-of-pyqt6-applications)
- [DBus Support](#dbus-support)
- [The PyQt6 Extension API](#the-pyqt6-extension-api)

---



---


### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* PyQt Documentation v6.11.0 »
* Reference Guide

# Reference Guide[¶](#reference-guide "Link to this heading")

* [Introduction](introduction.html)
  + [License](introduction.html#license)
  + [PyQt6 Components](introduction.html#pyqt6-components)
* [Contributing to this Documentation](contributing.html)
  + [Repository Structure](contributing.html#repository-structure)
  + [Description Files](contributing.html#description-files)
  + [Contributing Changes](contributing.html#contributing-changes)
* [Support for Old Versions of Python](eol_policy.html)
* [Installing PyQt6](installation.html)
  + [Understanding the Correct Version to Install](installation.html#understanding-the-correct-version-to-install)
  + [Installing from Wheels](installation.html#installing-from-wheels)
  + [Building and Installing from Source](installation.html#building-and-installing-from-source)
* [Differences Between PyQt6 and PyQt5](pyqt5_differences.html)
* [Support for Signals and Slots](signals_slots.html)
  + [Unbound and Bound Signals](signals_slots.html#unbound-and-bound-signals)
  + [Defining New Signals with pyqtSignal](signals_slots.html#defining-new-signals-with-pyqtsignal)
  + [Connecting, Disconnecting and Emitting Signals](signals_slots.html#connecting-disconnecting-and-emitting-signals)
  + [Connecting Signals Using Keyword Arguments](signals_slots.html#connecting-signals-using-keyword-arguments)
  + [The pyqtSlot Decorator](signals_slots.html#the-pyqtslot-decorator)
  + [The `PyQt_PyObject` Signal Argument Type](signals_slots.html#the-pyqt-pyobject-signal-argument-type)
  + [Connecting Slots By Name](signals_slots.html#connecting-slots-by-name)
* [Support for Qt Properties](qt_properties.html)
  + [Defining New Qt Properties](qt_properties.html#defining-new-qt-properties)
* [Other Support for Dynamic Meta-objects](metaobjects.html)
  + [pyqtEnum](metaobjects.html#pyqtenum)
  + [pyqtClassInfo](metaobjects.html#pyqtclassinfo)
* [Support for Qt Interfaces](qt_interfaces.html)
* [Support for QVariant](pyqt_qvariant.html)
* [Support for QSettings](pyqt_qsettings.html)
* [Integrating Python and QML](qml.html)
  + [Registering Python Types](qml.html#registering-python-types)
  + [A Simple Example](qml.html#a-simple-example)
  + [Using QQmlListProperty](qml.html#using-qqmllistproperty)
  + [Using Attached Properties](qml.html#using-attached-properties)
  + [Using Property Value Sources](qml.html#using-property-value-sources)
  + [Using QQmlParserStatus](qml.html#using-qqmlparserstatus)
  + [Writing Python Plugins for **qmlscene**](qml.html#writing-python-plugins-for-qmlscene)
* [Support for Cooperative Multi-inheritance](multiinheritance.html)
* [Things to be Aware Of](gotchas.html)
  + [TLS Support](gotchas.html#tls-support)
  + [Crashes On Exit](gotchas.html#crashes-on-exit)
  + [Keyword Arguments](gotchas.html#keyword-arguments)
  + [Garbage Collection](gotchas.html#garbage-collection)
  + [Multiple Inheritance](gotchas.html#multiple-inheritance)
  + [Access to Protected Member Functions](gotchas.html#access-to-protected-member-functions)
  + [`None` and `NULL`](gotchas.html#none-and-null)
  + [Support for `void *`](gotchas.html#support-for-void)
* [Using Qt Designer](designer.html)
  + [Using the Generated Code](designer.html#using-the-generated-code)
  + [**pyuic6**](designer.html#pyuic6)
  + [Writing Qt Designer Plugins](designer.html#writing-qt-designer-plugins)
* [Support for Pickling](pickle.html)
* [Using PyQt6 from the Python Shell](python_shell.html)
* [Internationalisation of PyQt6 Applications](i18n.html)
  + [**pylupdate6**](i18n.html#pylupdate6)
  + [Differences Between PyQt6 and Qt](i18n.html#differences-between-pyqt6-and-qt)
  + [Support for Translator Comments](i18n.html#support-for-translator-comments)
* [DBus Support](dbus.html)
  + [QtDBus](dbus.html#qtdbus)
  + [dbus.mainloop.pyqt6](dbus.html#dbus-mainloop-pyqt6)
* [The PyQt6 Extension API](extension_api.html)
  + [C++ API](extension_api.html#c-api)

#### Next topic

[Introduction](introduction.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* PyQt Documentation v6.11.0 »
* Reference Guide

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Introduction {#introduction}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Introduction

# Introduction[¶](#introduction "Link to this heading")

This is the reference guide for PyQt6 v6.11. PyQt6 is a set of [Python](https://www.python.org) bindings for v6 of the Qt application framework
from [The Qt Company](https://www.qt.io).

Qt is a set of C++ libraries and development tools that includes platform
independent abstractions for graphical user interfaces, networking, threads,
regular expressions, SQL databases, SVG, OpenGL, XML, user and application
settings, positioning and location services, short range communications (NFC
and Bluetooth), web browsing, 3D animation, charts and 3D data visualisation.

PyQt6 comprises PyQt6 itself and a number of add-ons that correspond to Qt’s
additional libraries. At the moment these are PyQt6-3D, PyQt6-Charts,
PyQt6-DataVisualization, PyQt6-Graphs, PyQt6-NetworkAuth and PyQt6-WebEngine.
Each is provided as a source distribution (*sdist*) and binary wheels for
Windows (Intel and ARM), Linux (Intel and ARM) and macOS (Intel and ARM).

PyQt6 requires Python v3.9 or later.

The homepage for PyQt6 is <https://www.riverbankcomputing.com/software/pyqt/>.
Here you will always find the latest stable version and current development
snapshots.

## License[¶](#license "Link to this heading")

PyQt6 is dual licensed on all platforms under the Riverbank Commercial License
and the GPL v3. Your PyQt6 license must be compatible with your Qt license.
If you use the GPL version then your own code must also use a compatible
license.

PyQt6, unlike most of Qt, is not available under the LGPL.

You can find the answers to questions about licensing [here](https://www.riverbankcomputing.com/commercial/license-faq).

You can purchase a commercial PyQt6 license [here](https://www.riverbankcomputing.com/commercial/buy).

## PyQt6 Components[¶](#pyqt6-components "Link to this heading")

PyQt6 comprises a number of different components. First of all there are a
number of Python extension modules. These are all installed in the
`PyQt6` Python package and are described in the
[list of modules](module_index.html#ref-module-index).

Each extension module has a corresponding [PEP 484](https://www.python.org/dev/peps/pep-0484) defined stub file containing type
hints for the module’s API. This can be used by static type checkers such as
[mypy](http://www.mypy-lang.org).

PyQt6 contains plugins that enable Qt Designer and **qmlscene** to be
extended using Python code. See [Writing Qt Designer Plugins](designer.html#ref-designer-plugins) and
[Integrating Python and QML](qml.html#ref-integrating-qml) respectively for the details. (Note that these are
not included in the binary wheels.)

PyQt6 also contains a couple of utility programs.

* **pyuic6** corresponds to the Qt **uic** utility. It converts
  [QtWidgets](api/qtwidgets/qtwidgets-module.html) based GUIs created using Qt Designer to Python
  code.
* **pylupdate6** corresponds to the Qt **lupdate** utility. It
  extracts all of the translatable strings from Python code and creates or
  updates `.ts` translation files. These are then used by Qt Linguist to
  manage the translation of those strings.

The [DBus](http://www.freedesktop.org/wiki/Software/DBusBindings) support
module is installed as `dbus.mainloop.pyqt6`. This module provides support
for the Qt event loop in the same way that the `dbus.mainloop.glib` included
with the standard `dbus-python` bindings package provides support for the
GLib event loop. The API is described in [DBus Support](dbus.html#ref-dbus). It is only
available if the `dbus-python` v0.80 (or later) bindings package is
installed. The [QtDBus](api/qtdbus/qtdbus-module.html) module provides a more Qt-like
interface to DBus.

PyQt6 includes a large number of examples. These are ports to Python of many
of the C++ examples provided with Qt. They can be found in the
`examples` directory of the sdist.

Finally, PyQt6 contains the specification files that allow bindings for other
Qt based class libraries that further extend PyQt6 to be developed and
installed.

### [Table of Contents](index.html)

* Introduction
  + [License](#license)
  + [PyQt6 Components](#pyqt6-components)

#### Previous topic

[Reference Guide](index.html "previous chapter")

#### Next topic

[Contributing to this Documentation](contributing.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Introduction

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Contributing to this Documentation {#contributing-to-this-documentation}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Contributing to this Documentation

# Contributing to this Documentation[¶](#contributing-to-this-documentation "Link to this heading")

The reference section of this documentation describes each element of the PyQt6
API. It is based on the original Qt documentation which, of course, contains
many references to C++. The intention is that, over time, the documentation
will be updated to replace all of the C++ idioms with their Python equivalents.
However, given the size of the API, it is unlikely that this task will ever be
complete.

The system used to create the documentation has been designed to make it easy
for users to contribute patches converting it from C++ to Python a bit at a
time. This is done in such as a way as to ensure that the documentation can be
updated with new releases of both PyQt6 and Qt without losing any
user-contributed modifications.

The documentation itself is written as reStructuredText and generated using
[Sphinx](https://www.sphinx-doc.org).

The documentation source is hosted at
[GitHub](https://github.com/Python-PyQt/PyQt6-Docs). The repository can be
cloned using the following command:

```
git clone git@github.com:Python-PyQt/PyQt6-Docs
```

The latest stable version will always be on the `main` branch.

## Repository Structure[¶](#repository-structure "Link to this heading")

The `docs` directory contains the handwritten overview documentation.

The `docs/api` directory contains the stuctured skeleton of the API
documentation. It is automatically generated from the PyQt6 `.sip` files and
are updated with every new release of PyQt6. They include information on all
elements of the API, including method arguments and types, but do not contain
any descriptions of those elements. They must not be modified by hand.

The `descriptions` directory contains a file for every individual element of
the PyQt6 API - even down to individual enum members. Amongst other things,
a file contains the reStructuredText describing the API element and a
`:status:` field describing the status of the description. It is this
`:status:` field than ensures that any user contributed modifications cannot
be subsequently overwritten. Description files are initially created when a
new release of PyQt6 introduces new elements to the API. Those description
files that haven’t been modified will be overwritten with every new release of
Qt.

The `images` directory contains the images that are referered to in
description files. Originally they were copied from the Qt documentation and
may be replaced by more Python-centric alternatives.

The `snippets` directory contains the code snippets that are referered to in
description files. Originally they were copied from the Qt documentation but
with every line of C++ code turned into a Python comment.

The `sphinx` directory contains a Sphinx extension and theme that implements
the documentation system.

The `sip2rst.py` script is run whenever a new release of PyQt6 is made. It
updates the `docs/api` and `descriptions` directories.

The `webxml2rst.py` script is run whenever a new release of Qt is made. It
updates the `descriptions`, `images` and `snippets` directories.

Note

The naming convention used for description files requires that the
repository is cloned to a case sensitive filesystem.

## Description Files[¶](#description-files "Link to this heading")

Most contributions to the documentation will be patches to description files.
The description files for each module are placed in a module-specific
sub-directory of `descriptions`. The name of a description file is derived
from the fully qualified name of the API element being described, a type tag,
an optional unique identifier, and a `.rst` extension.

For example the description file for the [QObject](api/qtcore/qobject.html) class
is `descriptions/QtCore/QObject-c.rst`. Here the type tag `c` denotes a
class. The complete set of type tags is shown in the table below.

|  |  |
| --- | --- |
| a | an attribute |
| c | a class |
| e | an enum |
| f | a function or method |
| m | a module |
| s | a signal |
| v | an enum member |

A function, method or signal may have overloads. Each overload is described in
a separate file. In these cases the name of each file also includes a unique
numerical identifer. You must look at the `:realsig:` field within the
description file to determine which of the overloads the file describes.

Apart from the reST description itself, the only part of the description file
that should be modified is the `:status:` field. The possible values of this
field are described below.

**todo**
:   The description is that extracted from the last release of Qt (or a stub if
    nothing was extracted) and has not been subsequently modified. It will be
    replaced when the next release of Qt is made.

**done**
:   The description has been modified and will not be overwritten by the next
    release of Qt.

**review**
:   The description has been modified. However the original description in the
    Qt document has itself been updated since the modifications were made.
    Therefore the changes to the Qt documentation should be reviewed to see if
    corresponding changes should be made to the description.

It follows from the above that any contributed change to a description file
should set the `:status:` field to `done`.

Any other fields in a description file must not be modified.

The description itself may use any of the normal Sphinx and docutils domains,
directives and roles. The only exception is that all cross-references to any
element of the PyQt6 API should use the `:sip:ref` role. For example, a
reference to the [QObject](api/qtcore/qobject.html) class should be specified as
`` :sip:ref:`~PyQt6.QtCore.QObject` ``.

## Contributing Changes[¶](#contributing-changes "Link to this heading")

User contributed changes can cover any of the following:

* `descriptions`
* `docs`
* `images`
* `snippets`
* `sphinx/riverbank/static/riverbank.css`.

### [Table of Contents](index.html)

* Contributing to this Documentation
  + [Repository Structure](#repository-structure)
  + [Description Files](#description-files)
  + [Contributing Changes](#contributing-changes)

#### Previous topic

[Introduction](introduction.html "previous chapter")

#### Next topic

[Support for Old Versions of Python](eol_policy.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Contributing to this Documentation

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Support for Old Versions of Python {#support-for-old-versions-of-python}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Old Versions of Python

# Support for Old Versions of Python[¶](#support-for-old-versions-of-python "Link to this heading")

When a Python version reaches it’s end-of-life, support for it will be removed
in the next minor release of PyQt6. For example, if the current version of
PyQt6 is v6.x.y then the support will be removed in v6.x+1.0.

On this basis support for Python v3.10 will be removed in the first minor
release after October 2026.

#### Previous topic

[Contributing to this Documentation](contributing.html "previous chapter")

#### Next topic

[Installing PyQt6](installation.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Old Versions of Python

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Installing PyQt6 {#installing-pyqt6}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Installing PyQt6

# Installing PyQt6[¶](#installing-pyqt6 "Link to this heading")

Both the GPL and commercial versions of PyQt6 can be built from sdists or
installed from binary wheels. Although this section concentrates on PyQt6
itself it applies equally to the add-on projects (e.g. PyQt6-3D,
PyQt6-NetworkAuth etc.).

## Understanding the Correct Version to Install[¶](#understanding-the-correct-version-to-install "Link to this heading")

People sometimes mistakenly believe that support for a particular version of Qt
requires a matching version of PyQt.

Qt uses [semantic versioning](https://semver.org/spec/v2.0.0.html) when
deciding on the version number of a release. In summary the major version is
increased when a release includes incompatible changes, the minor version is
increased when a release includes compatible changes, and the patch version is
increased when a release includes no user-visible changes.

With PyQt6 the version number of PyQt6 is tied, to a certain extent, to the
version of Qt v6 so that:

* The major version will always be **6**.
* For a particular minor version *n* it will build against any version of Qt
  v6. It will not support any new features introduced in Qt v6.*n+1* or
  later.
* It will support all the features of supported modules of Qt v6.*n* or
  earlier.
* Support for new modules may be added to PyQt6 at any time. This would result
  in a change of patch version only.
* The major and minor versions of the latest release of PyQt6 will be the same
  as the latest release of Qt v6.
* The patch versions of PyQt6 and Qt v6 are entirely unrelated to each other.

So, for example, PyQt6 v6.1 will build against Qt v6.2 but will not support any
new features introduced in Qt v6.2. PyQt6 v6.1 will support all the features
of supported modules of Qt v6.0 and those new features introduced in Qt v6.1.

In summary, you should always try and use the latest version of PyQt6 no matter
what version of Qt v6 you are using.

## Installing from Wheels[¶](#installing-from-wheels "Link to this heading")

Wheels are the standard Python packaging format for pure Python or binary
extension modules such as PyQt6. Wheels are provided for 64-bit Windows (Intel
and ARM), 64-bit macOS (Intel and ARM) and 64-bit Linux (Intel and ARM). These
correspond to the platforms for which The Qt Company provides binary
installers.

Wheels are installed using Python’s **pip** program.

### Installing the GPL Version[¶](#installing-the-gpl-version "Link to this heading")

To install the wheel for the GPL version of PyQt6, run:

```
pip install PyQt6
```

This will attempt to install the wheel for your platform and your version of
Python (assuming both are supported). The wheel will be automatically
downloaded from [PyPI](https://pypi.org/project/PyQt6/).

You may find that **pip** doesn’t download a wheel but instead downloads
the sdist and tries to build PyQt6 from source. If it does then the build will
probably fail with a cryptic error message. There are a number of reasons for
this:

* there is no wheel available for your platform and version of Python
* your version of Python is unsupported
* your version of **pip** is too old and doesn’t support the current
  standards for naming wheels
* in order for **pip** to build from source additional options must be
  specified.

When using **pip** to build from source then a command line similar to
the following should be used:

```
pip -v install --config-settings --confirm-license= --config-settings --qmake=/path/to/qmake PyQt6
```

The `-v` option is not required but is recommended. The **qmake**
location does not need to specified if it is on `PATH`.

**pip** will also automatically install any dependencies that are
required. In the case of PyQt6 itself this will be the PyQt6-Qt6 and PyQt6-sip
projects. The PyQt6-Qt6 project contains the parts of a standard LGPL Qt
installation required by PyQt6. The PyQt6-sip project contains the
[sip](api/sip/sip-module.html) module.

Note

If you want PyQt6 to use a copy of Qt that you already have installed then
you need to build it from source.

To uninstall the GPL version, run:

```
pip uninstall PyQt6
```

Note

The Qt libraries in the Linux wheel of the PyQt6-Qt6 project require
OpenSSL v1.1 however some Linux distributions (specifically Ubuntu 22.04 at
the time of writing) include the incompatible OpenSSL v3.

The required version of OpenSSL can be downloaded from the Ubuntu 20.04
repository by clicking [here](http://security.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.16_amd64.deb).

The downloaded `.deb` file can then be installed by running:

```
sudo apt install /path/to/libssl1.1_1.1.1f-1ubuntu2.16_amd64.deb
```

### Installing the Commercial Version[¶](#installing-the-commercial-version "Link to this heading")

Wheels are also provided for the commercial version of PyQt6 but they must be
downloaded from your account on the Riverbank Computing website. Before you
install the downloaded wheel using **pip** you must ensure you have an
appropriate Qt license and have decided how you want to distribute your PyQt6
wheels to your developers.

By default, installing the commercial PyQt6 wheel will do the same as
installing the GPL wheel, i.e. it will automatically download and install the
required parts of a standard LGPL Qt installation from PyPI. There are a
number of reasons why you might not want to do this:

* you have a commercial Qt license and need to make sure that is used with
  PyQt6
* you don’t allow your developers access to PyPI
* you want to minimise the number of wheels you need to distribute to your
  developers.

Note

Some Qt libraries are licensed under the GPL rather than the LGPL. If your
own application license is compatibile with the LGPL but is incompatible
with the GPL then you must make sure you do not use the corresponding PyQt
modules (even though you have a commercial PyQt license).

The solution to all these issues is to use the **pyqt-bundle** program
to bundle a copy of your own Qt installation with your commercial PyQt6. This
will produce a new wheel that you can distribute easily to your developers.

**pyqt-bundle** is part of [PyQt-builder](https://pypi.org/project/PyQt-builder/). To install it, run:

```
pip install PyQt-builder
```

The documentation can be found [here](https://pyqt-builder.readthedocs.io/en/stable/pyqtbundle.html).

To uninstall the commercial version, run:

```
pip uninstall PyQt6-commercial
```

## Building and Installing from Source[¶](#building-and-installing-from-source "Link to this heading")

As described above **pip** can be used to download, build and
install the GPL source packages from the [PyQt6](https://pypi.org/project/PyQt6/) project at PyPI. However doing so is not
recommended as it is not easy to configure the installation or diagnose any
problems.

PyQt6 is built using [PyQt-builder](https://pypi.org/project/PyQt-builder/).
To install it, run:

```
pip install PyQt-builder
```

PyQt-builder is an extension to the [SIP](https://pypi.org/project/sip/)
bindings generator which will be installed automatically.

The rest of these instructions assume that you have downloaded the PyQt6 sdist
from [PyPI](https://pypi.org/project/PyQt6/) and will used SIP’s
**sip-install** command line tool to do the build and installation.

If you are using the commercial version of PyQt6 then you should use the
download instructions which were sent to you when you made your purchase. You
must also download your `pyqt-commercial.sip` license file.

PyQt-builder extends SIP’s build system by adding [options](https://pyqt-builder.readthedocs.io/en/stable/command_line_tools.html)
to SIP’s [command line tools](https://python-sip.readthedocs.io/en/stable/command_line_tools.html).

PyQt6 further extends the build system by adding the following options to SIP’s
command line tools.

--confirm-license[¶](#cmdoption-confirm-license "Link to this definition")
:   Using this confirms that you accept the terms of the PyQt license. If it
    is omitted then you will be asked for confirmation during configuration.

--dbus DIR[¶](#cmdoption-dbus "Link to this definition")
:   The directory containing the `dbus/dbus-python.h` header file of the
    dbus-python package can be found in the directory `DIR`.

--license-dir DIR[¶](#cmdoption-license-dir "Link to this definition")
:   The `pyqt-commercial,sip` license file needed by the commercial
    version of PyQt6 can be found in the directory `DIR`. By default it is
    assumed that you have copied it to the `sip` sub-directory of the
    unpacked sdist.

--no-dbus-python[¶](#cmdoption-no-dbus-python "Link to this definition")
:   The Qt support for the dbus-python package will not be built.

--no-designer-plugin[¶](#cmdoption-no-designer-plugin "Link to this definition")
:   The Qt Designer plugin will not be built.

--no-qml-plugin[¶](#cmdoption-no-qml-plugin "Link to this definition")
:   The **qmlscene** plugin will not be built.

--no-tools[¶](#cmdoption-no-tools "Link to this definition")
:   The **pyuic6** and **pylupdate6** tools will not be built.

--qt-shared[¶](#cmdoption-qt-shared "Link to this definition")
:   Normally Qt is checked to see if it has been built as shared libraries.
    Some Linux distributions configure their Qt builds to make this check
    unreliable. This option ignores the result of the check and assumes that
    Qt has been built as shared libraries.

### Building the [sip](api/sip/sip-module.html) Module[¶](#building-the-sip-module "Link to this heading")

It is not necessary to install the [PyQt6.sip](api/sip/sip-module.html) module before building
PyQt6 but it must be installed before PyQt6 can be used.

The module is built using `setuptools` and is available from the
[PyQt6-sip](https://pypi.org/project/PyQt6-sip/) project at PyPI. It uses
`setuptools` as its build system and can be installed by **pip**
or you can also unpack the sdist and install it by running its
**setup.py** script.

### Building PyQt6[¶](#building-pyqt6 "Link to this heading")

Once you have downloaded the sdist from PyPI, unpack it and change directory to
its top level directory (i.e. the one containing the `pyproject.toml`
file.

If you are building the commercial version of PyQt6 then copy the
`pyqt-commercial.sip` license file to the `sip` sub-directory.

To build and install PyQt6, run:

```
sip-install
```

In order to see all the available command line options, run:

```
sip-install -h
```

If you want to run **make** seperately then instead run:

```
sip-build --no-make
make
make install
```

### Building PyQt6 Add-on Projects[¶](#building-pyqt6-add-on-projects "Link to this heading")

The add-on PyQt6 projects are built and installed in exactly the same way as
PyQt6 itself. PyQt6 must be built and installed first.

### [Table of Contents](index.html)

* Installing PyQt6
  + [Understanding the Correct Version to Install](#understanding-the-correct-version-to-install)
  + [Installing from Wheels](#installing-from-wheels)
    - [Installing the GPL Version](#installing-the-gpl-version)
    - [Installing the Commercial Version](#installing-the-commercial-version)
  + [Building and Installing from Source](#building-and-installing-from-source)
    - [Building the sip Module](#building-the-sip-module)
    - [Building PyQt6](#building-pyqt6)
    - [Building PyQt6 Add-on Projects](#building-pyqt6-add-on-projects)

#### Previous topic

[Support for Old Versions of Python](eol_policy.html "previous chapter")

#### Next topic

[Differences Between PyQt6 and PyQt5](pyqt5_differences.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Installing PyQt6

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Differences Between PyQt6 and PyQt5 {#differences-between-pyqt6-and-pyqt5}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Differences Between PyQt6 and PyQt5

# Differences Between PyQt6 and PyQt5[¶](#differences-between-pyqt6-and-pyqt5 "Link to this heading")

In this section we give an overview of the differences between PyQt6 and PyQt5.
This is not an exhaustive list and does not go into the detail of the
differences between the Qt v6 and Qt v5 APIs.

* All named enums are now implemented as a sub-class of the standard Python
  [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.14)") class. (PyQt5 used [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "(in Python v3.14)") for
  scoped enums and a custom type for traditional named enums).
* Qt provides the `QFlags` template class as a type-safe way of
  using enum values that can be combined as a set of flags. The name of the
  class is often the plural form of the name of the enum. PyQt5 implements
  both of these as separate types. PyQt6 instead combines them as a single
  type, using the name of the enum, as a sub-class of [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "(in Python v3.14)").
* `Q_CLASSINFO()` has been replaced by the
  [pyqtClassInfo()](api/qtcore/qtcore-module.html#pyqtClassInfo) class decorator.
* `Q_ENUM()`, `Q_ENUMS()`,
  `Q_FLAG()` and `Q_FLAGS()` have
  been replaced by the [pyqtEnum()](api/qtcore/qtcore-module.html#pyqtEnum) class decorator.
* All `exec_()` and `print_()` methods have been removed.
* `qApp` has been removed.
* The `PYQT_CONFIGURATION` dict has been removed.
* The `Qt` module has been removed.
* The bindings for the (GPL licensed) Qt classes that implement support for
  network authorisation have moved out to a separate add-on project
  `PyQt6-NetworkAuth`. This means that all of the libraries wrapped by PyQt6
  itself are licensed under the LGPL.
* **pylupdate6** is a completely new pure-Python implementation. It can
  no longer read a `.pro` file in order to determine the names of `.py`
  files to translate.
* Support for Qt’s resource system has been removed (i.e. there is no
  `pyrcc6`).

Qt v6 implements a number of functions from Qt v5 that are now marked as being
deprecated. These are not supported in PyQt6.

#### Previous topic

[Installing PyQt6](installation.html "previous chapter")

#### Next topic

[Support for Signals and Slots](signals_slots.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Differences Between PyQt6 and PyQt5

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Support for Signals and Slots {#support-for-signals-and-slots}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Signals and Slots

# Support for Signals and Slots[¶](#support-for-signals-and-slots "Link to this heading")

One of the key features of Qt is its use of signals and slots to communicate
between objects. Their use encourages the development of reusable components.

A signal is emitted when something of potential interest happens. A slot is a
Python callable. If a signal is connected to a slot then the slot is called
when the signal is emitted. If a signal isn’t connected then nothing happens.
The code (or component) that emits the signal does not know or care if the
signal is being used.

The signal/slot mechanism has the following features.

* A signal may be connected to many slots.
* A signal may also be connected to another signal.
* Signal arguments may be any Python type.
* A slot may be connected to many signals.
* Connections may be direct (ie. synchronous) or queued (ie. asynchronous).
* Connections may be made across threads.
* Signals may be disconnected.

## Unbound and Bound Signals[¶](#unbound-and-bound-signals "Link to this heading")

A signal (specifically an unbound signal) is a class attribute. When a signal
is referenced as an attribute of an instance of the class then PyQt6
automatically binds the instance to the signal in order to create a *bound
signal*. This is the same mechanism that Python itself uses to create bound
methods from class functions.

A bound signal has `connect()`, `disconnect()` and `emit()` methods that
implement the associated functionality. It also has a `signal` attribute
that is the signature of the signal that would be returned by Qt’s `SIGNAL()`
macro.

A signal may be overloaded, ie. a signal with a particular name may support
more than one signature. A signal may be indexed with a signature in order to
select the one required. A signature is a sequence of types. A type is either
a Python type object or a string that is the name of a C++ type. The name of a
C++ type is automatically normalised so that, for example, `QVariant` can be
used instead of the non-normalised `const QVariant &`.

If a signal is overloaded then it will have a default that will be used if no
index is given.

When a signal is emitted then any arguments are converted to C++ types if
possible. If an argument doesn’t have a corresponding C++ type then it is
wrapped in a special C++ type that allows it to be passed around Qt’s meta-type
system while ensuring that its reference count is properly maintained.

## Defining New Signals with pyqtSignal[¶](#defining-new-signals-with-pyqtsignal "Link to this heading")

PyQt6 automatically defines signals for all Qt’s built-in signals. New signals
can be defined as class attributes using the
pyqtSignal factory.

PyQt6.QtCore.pyqtSignal(*types*[, *name*[, *revision=0*[, *arguments=[]*]]])[¶](#PyQt6.QtCore.pyqtSignal "Link to this definition")
:   Create one or more overloaded unbound signals as a class attribute.

    Parameters:
    :   * **types** – the types that define the C++ signature of the signal. Each type may
          be a Python type object or a string that is the name of a C++ type.
          Alternatively each may be a sequence of type arguments. In this case
          each sequence defines the signature of a different signal overload.
          The first overload will be the default.
        * **name** – the name of the signal. If it is omitted then the name of the class
          attribute is used. This may only be given as a keyword argument.
        * **revision** – the revision of the signal that is exported to QML. This may only be
          given as a keyword argument.
        * **arguments** – the sequence of the names of the signal’s arguments that is exported to
          QML. This may only be given as a keyword argument.

    Return type:
    :   an unbound signal

The following example shows the definition of a number of new signals:

```
from PyQt6.QtCore import QObject, pyqtSignal

class Foo(QObject):

    # This defines a signal called 'closed' that takes no arguments.
    closed = pyqtSignal()

    # This defines a signal called 'rangeChanged' that takes two
    # integer arguments.
    range_changed = pyqtSignal(int, int, name='rangeChanged')

    # This defines a signal called 'valueChanged' that has two overloads,
    # one that takes an integer argument and one that takes a QString
    # argument.  Note that because we use a string to specify the type of
    # the QString argument then this code will run under Python v2 and v3.
    valueChanged = pyqtSignal([int], ['QString'])
```

New signals should only be defined in sub-classes of
[QObject](api/qtcore/qobject.html). They must be part of the class definition
and cannot be dynamically added as class attributes after the class has been
defined.

New signals defined in this way will be automatically added to the class’s
[QMetaObject](api/qtcore/qmetaobject.html). This means that they will appear in Qt
Designer and can be introspected using the
[QMetaObject](api/qtcore/qmetaobject.html) API.

Overloaded signals should be used with care when an argument has a Python type
that has no corresponding C++ type. PyQt6 uses the same internal C++ class to
represent such objects and so it is possible to have overloaded signals with
different Python signatures that are implemented with identical C++ signatures
with unexpected results. The following is an example of this:

```
class Foo(QObject):

    # This will cause problems because each has the same C++ signature.
    valueChanged = pyqtSignal([dict], [list])
```

## Connecting, Disconnecting and Emitting Signals[¶](#connecting-disconnecting-and-emitting-signals "Link to this heading")

Signals are connected to slots using the [`connect()`](#connect "connect") method of a bound
signal.

connect(*slot*[, *type=PyQt6.QtCore.Qt.AutoConnection*[, *no\_receiver\_check=False*]]) → PyQt6.QtCore.QMetaObject.Connection[¶](#connect "Link to this definition")
:   Connect a signal to a slot. An exception will be raised if the connection
    failed.

    Parameters:
    :   * **slot** – the slot to connect to, either a Python callable or another bound
          signal.
        * **type** – the type of the connection to make.
        * **no\_receiver\_check** – suppress the check that the underlying C++ receiver instance still
          exists and deliver the signal anyway.

    Returns:
    :   a [Connection](api/qtcore/qmetaobject-connection.html) object which can be
        passed to [`disconnect()`](#disconnect "disconnect"). This is the only way to disconnect a
        connection to a lambda function.

Signals are disconnected from slots using the [`disconnect()`](#disconnect "disconnect") method of a
bound signal.

disconnect([*slot*])[¶](#disconnect "Link to this definition")
:   Disconnect one or more slots from a signal. An exception will be raised if
    the slot is not connected to the signal or if the signal has no connections
    at all.

    Parameters:
    :   **slot** – the optional slot to disconnect from, either a
        [Connection](api/qtcore/qmetaobject-connection.html) object returned by
        [`connect()`](#connect "connect"), a Python callable or another bound signal. If it is
        omitted then all slots connected to the signal are disconnected.

Signals are emitted from using the [`emit()`](#emit "emit") method of a bound signal.

emit(*\\*args*)[¶](#emit "Link to this definition")
:   Emit a signal.

    Parameters:
    :   **args** – the optional sequence of arguments to pass to any connected slots.

The following code demonstrates the definition, connection and emit of a
signal without arguments:

```
from PyQt6.QtCore import QObject, pyqtSignal

class Foo(QObject):

    # Define a new signal called 'trigger' that has no arguments.
    trigger = pyqtSignal()

    def connect_and_emit_trigger(self):
        # Connect the trigger signal to a slot.
        self.trigger.connect(self.handle_trigger)

        # Emit the signal.
        self.trigger.emit()

    def handle_trigger(self):
        # Show that the slot has been called.

        print "trigger signal received"
```

The following code demonstrates the connection of overloaded signals:

```
from PyQt6.QtWidgets import QComboBox

class Bar(QComboBox):

    def connect_activated(self):
        # The PyQt6 documentation will define what the default overload is.
        # In this case it is the overload with the single integer argument.
        self.activated.connect(self.handle_int)

        # For non-default overloads we have to specify which we want to
        # connect.  In this case the one with the single string argument.
        # (Note that we could also explicitly specify the default if we
        # wanted to.)
        self.activated[str].connect(self.handle_string)

    def handle_int(self, index):
        print "activated signal passed integer", index

    def handle_string(self, text):
        print "activated signal passed QString", text
```

## Connecting Signals Using Keyword Arguments[¶](#connecting-signals-using-keyword-arguments "Link to this heading")

It is also possible to connect signals by passing a slot as a keyword argument
corresponding to the name of the signal when creating an object, or using the
`pyqtConfigure()` method. For example the following
three fragments are equivalent:

```
act = QAction("Action", self)
act.triggered.connect(self.on_triggered)

act = QAction("Action", self, triggered=self.on_triggered)

act = QAction("Action", self)
act.pyqtConfigure(triggered=self.on_triggered)
```

## The [pyqtSlot()](api/qtcore/qtcore-module.html#pyqtSlot) Decorator[¶](#the-pyqtslot-decorator "Link to this heading")

Although PyQt6 allows any Python callable to be used as a slot when connecting
signals, it is sometimes necessary to explicitly mark a Python method as being
a Qt slot and to provide a C++ signature for it. PyQt6 provides the
[pyqtSlot()](api/qtcore/qtcore-module.html#pyqtSlot) function decorator to do this.

PyQt6.QtCore.pyqtSlot(*types*[, *name*[, *result*[, *revision=0*]]])[¶](#PyQt6.QtCore.pyqtSlot "Link to this definition")
:   Decorate a Python method to create a Qt slot.

    Parameters:
    :   * **types** – the types that define the C++ signature of the slot. Each type may be
          a Python type object or a string that is the name of a C++ type.
        * **name** – the name of the slot that will be seen by C++. If omitted the name of
          the Python method being decorated will be used. This may only be given
          as a keyword argument.
        * **revision** – the revision of the slot that is exported to QML. This may only be
          given as a keyword argument.
        * **result** – the type of the result and may be a Python type object or a string that
          specifies a C++ type. This may only be given as a keyword argument.

Connecting a signal to a decorated Python method also has the advantage of
reducing the amount of memory used and is slightly faster.

For example:

```
from PyQt6.QtCore import QObject, pyqtSlot

class Foo(QObject):

    @pyqtSlot()
    def foo(self):
        """ C++: void foo() """

    @pyqtSlot(int, str)
    def foo(self, arg1, arg2):
        """ C++: void foo(int, QString) """

    @pyqtSlot(int, name='bar')
    def foo(self, arg1):
        """ C++: void bar(int) """

    @pyqtSlot(int, result=int)
    def foo(self, arg1):
        """ C++: int foo(int) """

    @pyqtSlot(int, QObject)
    def foo(self, arg1):
        """ C++: int foo(int, QObject *) """
```

It is also possible to chain the decorators in order to define a Python method
several times with different signatures. For example:

```
from PyQt6.QtCore import QObject, pyqtSlot

class Foo(QObject):

    @pyqtSlot(int)
    @pyqtSlot('QString')
    def valueChanged(self, value):
        """ Two slots will be defined in the QMetaObject. """
```

## The `PyQt_PyObject` Signal Argument Type[¶](#the-pyqt-pyobject-signal-argument-type "Link to this heading")

It is possible to pass any Python object as a signal argument by specifying
`PyQt_PyObject` as the type of the argument in the signature. For example:

```
finished = pyqtSignal('PyQt_PyObject')
```

This would normally be used for passing objects where the actual Python type
isn’t known. It can also be used to pass an integer, for example, so that the
normal conversions from a Python object to a C++ integer and back again are not
required.

The reference count of the object being passed is maintained automatically.
There is no need for the emitter of a signal to keep a reference to the object
after the call to `finished.emit()`, even if a connection is queued.

## Connecting Slots By Name[¶](#connecting-slots-by-name "Link to this heading")

PyQt6 supports the `connectSlotsByName()` function
that is most commonly used by **pyuic6** generated Python code to
automatically connect signals to slots that conform to a simple naming
convention. However, where a class has overloaded Qt signals (ie. with the
same name but with different arguments) PyQt6 needs additional information in
order to automatically connect the correct signal.

For example the [QSpinBox](api/qtwidgets/qspinbox.html) class has the following
signals:

```
void valueChanged(int i);
void valueChanged(const QString &text);
```

When the value of the spin box changes both of these signals will be emitted.
If you have implemented a slot called `on_spinbox_valueChanged` (which
assumes that you have given the QSpinBox instance
the name `spinbox`) then it will be connected to both variations of the
signal. Therefore, when the user changes the value, your slot will be called
twice - once with an integer argument, and once with a string argument.

The [pyqtSlot()](api/qtcore/qtcore-module.html#pyqtSlot) decorator can be used to specify which of
the signals should be connected to the slot.

For example, if you were only interested in the integer variant of the signal
then your slot definition would look like the following:

```
@pyqtSlot(int)
def on_spinbox_valueChanged(self, i):
    # i will be an integer.
    pass
```

If you wanted to handle both variants of the signal, but with different Python
methods, then your slot definitions might look like the following:

```
@pyqtSlot(int, name='on_spinbox_valueChanged')
def spinbox_int_value(self, i):
    # i will be an integer.
    pass

@pyqtSlot(str, name='on_spinbox_valueChanged')
def spinbox_qstring_value(self, s):
    # s will be a Python string object (or a QString if they are enabled).
    pass
```

### [Table of Contents](index.html)

* Support for Signals and Slots
  + [Unbound and Bound Signals](#unbound-and-bound-signals)
  + [Defining New Signals with pyqtSignal](#defining-new-signals-with-pyqtsignal)
    - [`PyQt6.QtCore.pyqtSignal()`](#PyQt6.QtCore.pyqtSignal)
  + [Connecting, Disconnecting and Emitting Signals](#connecting-disconnecting-and-emitting-signals)
    - [`connect()`](#connect)
    - [`disconnect()`](#disconnect)
    - [`emit()`](#emit)
  + [Connecting Signals Using Keyword Arguments](#connecting-signals-using-keyword-arguments)
  + [The pyqtSlot Decorator](#the-pyqtslot-decorator)
    - [`PyQt6.QtCore.pyqtSlot()`](#PyQt6.QtCore.pyqtSlot)
  + [The `PyQt_PyObject` Signal Argument Type](#the-pyqt-pyobject-signal-argument-type)
  + [Connecting Slots By Name](#connecting-slots-by-name)

#### Previous topic

[Differences Between PyQt6 and PyQt5](pyqt5_differences.html "previous chapter")

#### Next topic

[Support for Qt Properties](qt_properties.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Signals and Slots

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Support for Qt Properties {#support-for-qt-properties}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Qt Properties

# Support for Qt Properties[¶](#support-for-qt-properties "Link to this heading")

PyQt6 does not support the setting and getting of Qt properties as if they were
normal instance attributes. This is because the name of a property often
conflicts with the name of the property’s getter method.

However, PyQt6 does support the initial setting of properties using keyword
arguments passed when an instance is created. For example:

```
act = QAction("&Save", self, shortcut=QKeySequence.StandardKey.Save,
        statusTip="Save the document to disk", triggered=self.save)
```

The example also demonstrates the use of a keyword argument to connect a
signal to a slot.

PyQt6 also supports setting the values of properties (and connecting a signal
to a slot) using the `pyqtConfigure()` method. For
example, the following gives the same results as above:

```
act = QAction("&Save", self)
act.pyqtConfigure(shortcut=QKeySequence.StandardKey.Save,
        statusTip="Save the document to disk", triggered=self.save)
```

## Defining New Qt Properties[¶](#defining-new-qt-properties "Link to this heading")

A new Qt property may be defined using the
pyqtProperty function. It is used in the same way as
the standard Python `property()` function. In fact, Qt properties defined in
this way also behave as Python properties.

PyQt6.QtCore.pyqtProperty(*type*[, *fget=None*[, *fset=None*[, *freset=None*[, *fdel=None*[, *doc=None*[, *designable=True*[, *scriptable=True*[, *stored=True*[, *user=False*[, *constant=False*[, *final=False*[, *notify=None*[, *revision=0*]]]]]]]]]]]]])[¶](#PyQt6.QtCore.pyqtProperty "Link to this definition")
:   Create a property that behaves as both a Python property and a Qt property.

    Parameters:
    :   * **type** – the type of the property. It is either a Python type object or a
          string that is the name of a C++ type.
        * **fget** – the optional callable used to get the value of the property.
        * **fset** – the optional callable used to set the value of the property.
        * **freset** – the optional callable used to reset the value of the property to its
          default value.
        * **fdel** – the optional callable used to delete the property.
        * **doc** – the optional docstring of the property.
        * **designable** – optionally sets the Qt `DESIGNABLE` flag.
        * **scriptable** – optionally sets the Qt `SCRIPTABLE` flag.
        * **stored** – optionally sets the Qt `STORED` flag.
        * **user** – optionally sets the Qt `USER` flag.
        * **constant** – optionally sets the Qt `CONSTANT` flag.
        * **final** – optionally sets the Qt `FINAL` flag.
        * **notify** – the optional unbound notify signal.
        * **revision** – the revision exported to QML.

    Return type:
    :   the property object.

It is also possible to use pyqtProperty as a decorator
in the same way as the standard Python `property()` function. The following
example shows how to define an `int` property with a getter and setter:

```
from PyQt6.QtCore import QObject, pyqtProperty

class Foo(QObject):

    def __init__(self):
        QObject.__init__(self)

        self._total = 0

    @pyqtProperty(int)
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value
```

If you prefer the Qt terminology you may also use `write` instead of
`setter` (and `read` instead of `getter`).

### [Table of Contents](index.html)

* Support for Qt Properties
  + [Defining New Qt Properties](#defining-new-qt-properties)
    - [`PyQt6.QtCore.pyqtProperty()`](#PyQt6.QtCore.pyqtProperty)

#### Previous topic

[Support for Signals and Slots](signals_slots.html "previous chapter")

#### Next topic

[Other Support for Dynamic Meta-objects](metaobjects.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Qt Properties

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Other Support for Dynamic Meta-objects {#other-support-for-dynamic-meta-objects}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Other Support for Dynamic Meta-objects

# Other Support for Dynamic Meta-objects[¶](#other-support-for-dynamic-meta-objects "Link to this heading")

PyQt6 creates a [QMetaObject](api/qtcore/qmetaobject.html) instance for any Python
sub-class of [QObject](api/qtcore/qobject.html) without the need for the
equivalent of Qt’s `Q_OBJECT` macro. Most of a
[QMetaObject](api/qtcore/qmetaobject.html) is populated automatically by defining
signals, slots and properties as described in previous sections. In this
section we cover the ways in which the remaining parts of a
[QMetaObject](api/qtcore/qmetaobject.html) are populated.

## [pyqtEnum()](api/qtcore/qtcore-module.html#pyqtEnum)[¶](#pyqtenum "Link to this heading")

The [pyqtEnum()](api/qtcore/qtcore-module.html#pyqtEnum) class decorator is used to decorate
sub-classes of the Python [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "(in Python v3.14)") class so that they are
published in the [QMetaObject](api/qtcore/qmetaobject.html). The typical use in
PyQt6 is to declare symbolic constants that can be used by QML, and as the type
of properties that can be set in Qt Designer. For example:

```
from enum import Enum, Flag

from PyQt6.QtCore import pyqtEnum, QObject

class Instruction(QObject):

    @pyqtEnum
    class Direction(Enum):
        Up, Down, Left, Right = range(4)

    @pyqtEnum
    class Status(Flag):
        Null = 0x00
        Urgent = 0x01
        Acknowledged = 0x02
        Completed = 0x04
```

## [pyqtClassInfo()](api/qtcore/qtcore-module.html#pyqtClassInfo)[¶](#pyqtclassinfo "Link to this heading")

The [pyqtClassInfo()](api/qtcore/qtcore-module.html#pyqtClassInfo) class decorator is used to specify a
a name/value pair that is placed in the class’s
[QMetaObject](api/qtcore/qmetaobject.html). It is the equivalent of Qt’s
`Q_CLASSINFO` macro.

For example it is used by QML to define the default property of a class:

```
from PyQt6.QtCore import pyqtClassInfo, QObject

@pyqtClassInfo('DefaultProperty', 'guests')
class BirthdayParty(QObject):

    pass
```

The decorator may be chained to define multiple name/value pairs.

### [Table of Contents](index.html)

* Other Support for Dynamic Meta-objects
  + [pyqtEnum](#pyqtenum)
  + [pyqtClassInfo](#pyqtclassinfo)

#### Previous topic

[Support for Qt Properties](qt_properties.html "previous chapter")

#### Next topic

[Support for Qt Interfaces](qt_interfaces.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Other Support for Dynamic Meta-objects

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Support for Qt Interfaces {#support-for-qt-interfaces}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Qt Interfaces

# Support for Qt Interfaces[¶](#support-for-qt-interfaces "Link to this heading")

PyQt6 does not, generally, support defining a class that inherits from more
than one Qt class. The exception is when inheriting from classes that Qt
defines as *interfaces*, for example
[QTextObjectInterface](api/qtgui/qtextobjectinterface.html).

A Qt interface is an abstract class contains only pure virtual methods and is
used as a mixin with (normally) a [QObject](api/qtcore/qobject.html) sub-class.
It is often used to define the interface that a plugin must implement.

Note that PyQt6 does not need an equivalent of Qt’s `Q_INTERFACES`
macro in order to use an interface class.

The `textobject.py` example included with PyQt6 demonstrates the use of an
interface.

#### Previous topic

[Other Support for Dynamic Meta-objects](metaobjects.html "previous chapter")

#### Next topic

[Support for QVariant](pyqt_qvariant.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Qt Interfaces

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Support for QVariant {#support-for-qvariant}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for QVariant

# Support for [QVariant](api/qtcore/qvariant.html)[¶](#support-for-qvariant "Link to this heading")

PyQt6 can convert any Python object to a [QVariant](api/qtcore/qvariant.html) and
back again. Normally this is done automatically and transparently so you don’t
even need to know of the existence of [QVariant](api/qtcore/qvariant.html).

An invalid [QVariant](api/qtcore/qvariant.html) is automatically converted to
`None` and vice versa.

However there are some situations where you might need to exert more control.
For example you might want to distinguish between a
[QVariant](api/qtcore/qvariant.html) containing a C++ float value and one
containing a C++ double value.

However it is possible to temporarily suppress the automatic conversion of a
C++ [QVariant](api/qtcore/qvariant.html) to a Python object and to return a
wrapped Python [QVariant](api/qtcore/qvariant.html) instead
by calling the [`enableautoconversion()`](api/sip/sip-module.html#PyQt6.sip.enableautoconversion "PyQt6.sip.enableautoconversion") function.

The actual value of a wrapped Python [QVariant](api/qtcore/qvariant.html) is
obtained by calling its [value()](api/qtcore/qvariant.html#value) method.

#### Previous topic

[Support for Qt Interfaces](qt_interfaces.html "previous chapter")

#### Next topic

[Support for QSettings](pyqt_qsettings.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for QVariant

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Support for QSettings {#support-for-qsettings}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for QSettings

# Support for [QSettings](api/qtcore/qsettings.html)[¶](#support-for-qsettings "Link to this heading")

Qt provies the [QSettings](api/qtcore/qsettings.html) class as a platform
independent API for the persistent storage and retrieval of application
settings. Settings are retrieved using the
`value()` method. However the type of the value
returned may not be what is expected. Some platforms only ever store string
values which means that the type of the original value is lost. Therefore a
setting with an integer value of `42` may be retrieved (on some platforms) as
a string value of `'42'`.

As a solution to this problem PyQt6’s implementation takes an optional third
argument called `type`. This is either a Python type object, e.g. `int`,
or a string that is the name of a C++ type, e.g. `'QStringList'`. The value
returned will be an object of the requested type.

For example:

```
from PyQt6.QtCore import QSettings, QPoint

settings = QSettings('foo', 'foo')

settings.setValue('int_value', 42)
settings.setValue('point_value', QPoint(10, 12))

# This will write the setting to the platform specific storage.
del settings

settings = QSettings('foo', 'foo')

int_value = settings.value('int_value', type=int)
print("int_value: %s" % repr(int_value))

point_value = settings.value('point_value', type=QPoint)
print("point_value: %s" % repr(point_value))
```

When this is executed then the following will be displayed for all platforms:

```
int_value: 42
point_value: PyQt6.QtCore.QPoint(10, 20)
```

If the value of the setting is a container (corresponding to either
`QVariantList`, `QVariantMap` or `QVariantHash`) then the type is applied
to the contents of the container.

For example:

```
from PyQt6.QtCore import QSettings

settings = QSettings('foo', 'foo')

settings.setValue('list_value', [1, 2, 3])
settings.setValue('dict_value', {'one': 1, 'two': 2})

# This will write the setting to the platform specific storage.
del settings

settings = QSettings('foo', 'foo')

list_value = settings.value('list_value', type=int)
print("list_value: %s" % repr(list_value))

dict_value = settings.value('dict_value', type=int)
print("dict_value: %s" % repr(dict_value))
```

When this is executed then the following will be displayed for all platforms:

```
list_value: [1, 2, 3]
dict_value: {'one': 1, 'two': 2}
```

#### Previous topic

[Support for QVariant](pyqt_qvariant.html "previous chapter")

#### Next topic

[Integrating Python and QML](qml.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for QSettings

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Integrating Python and QML {#integrating-python-and-qml}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Integrating Python and QML

# Integrating Python and QML[¶](#integrating-python-and-qml "Link to this heading")

Qt includes QML as a means of declaratively describing a user interface and
using JavaScript as a scripting language within it. It is possible to write
complete standalone QML applications, or to combine them with C++. PyQt6
allows QML to be integrated with Python in exactly the same way. In
particular:

* Python types that are sub-classed from [QObject](api/qtcore/qobject.html) can
  be registered with QML.
* Instances of registered Python types can be created and made available to QML
  scripts.
* Instances of registered Python types can be created by QML scripts.
* Singleton instances of registered Python types can be created automatically
  by a QML engine and made available to QML scripts.
* QML scripts interact with Python objects through their properties, signals
  and slots.
* Python properties, signals and slots can be given revision numbers that only
  those implemented by a specific version are made available to QML.

Note

The PyQt support for QML requires knowledge of the internals of the C++
code that implements QML. This can (and does) change between Qt versions
and may mean that some features only work with specific Qt versions and may
not work at all with some future version of Qt.

It is recommended that, in an MVC architecture, QML should only be used to
implement the view. The model and controller should be implemented in
Python.

## Registering Python Types[¶](#registering-python-types "Link to this heading")

Registering Python types with QML is done in the same way is it is done with
C++ classes, i.e. using the [qmlRegisterType()](api/qtqml/qtqml-module.html#qmlRegisterType),
[qmlRegisterSingletonType()](api/qtqml/qtqml-module.html#qmlRegisterSingletonType),
[qmlRegisterUncreatableType()](api/qtqml/qtqml-module.html#qmlRegisterUncreatableType) and
[qmlRegisterRevision()](api/qtqml/qtqml-module.html#qmlRegisterRevision) functions.

In C++ these are template based functions that take the C++ class, and
sometimes a revision, as template arguments. In the Python implementation
these are simply passed as the first arguments to the respective functions.

## A Simple Example[¶](#a-simple-example "Link to this heading")

The following simple example demonstates the implementation of a Python class
that is registered with QML. The class defines two properties. A QML script
is executed which creates an instance of the class and sets the values of the
properties. That instance is then returned to Python which then prints the
values of those properties.

Hopefully the comments are self explanatory:

```
import sys

from PyQt6.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl
from PyQt6.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine

# This is the type that will be registered with QML.  It must be a
# sub-class of QObject.
class Person(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialise the value of the properties.
        self._name = ''
        self._shoeSize = 0

    # Define the getter of the 'name' property.  The C++ type of the
    # property is QString which Python will convert to and from a string.
    @pyqtProperty('QString')
    def name(self):
        return self._name

    # Define the setter of the 'name' property.
    @name.setter
    def name(self, name):
        self._name = name

    # Define the getter of the 'shoeSize' property.  The C++ type and
    # Python type of the property is int.
    @pyqtProperty(int)
    def shoeSize(self):
        return self._shoeSize

    # Define the setter of the 'shoeSize' property.
    @shoeSize.setter
    def shoeSize(self, shoeSize):
        self._shoeSize = shoeSize

# Create the application instance.
app = QCoreApplication(sys.argv)

# Register the Python type.  Its URI is 'People', it's v1.0 and the type
# will be called 'Person' in QML.
qmlRegisterType(Person, 'People', 1, 0, 'Person')

# Create a QML engine.
engine = QQmlEngine()

# Create a component factory and load the QML script.
component = QQmlComponent(engine)
component.loadUrl(QUrl.fromLocalFile('example.qml'))

# Create an instance of the component.
person = component.create()

if person is not None:
    # Print the value of the properties.
    print("The person's name is %s." % person.name)
    print("They wear a size %d shoe." % person.shoeSize)
else:
    # Print all errors that occurred.
    for error in component.errors():
        print(error.toString())
```

The following is the `example.qml` QML script that is executed:

```
import People 1.0

Person {
    name: "Bob Jones"
    shoeSize: 12
}
```

## Using QQmlListProperty[¶](#using-qqmllistproperty "Link to this heading")

Defining list-based properties in Python that can be updated from QML is done
using the QQmlListProperty class. However the way it
is used in Python is slightly different to the way it is used in C++.

In the simple case QQmlListProperty wraps a Python
list that is usually an instance sttribute, for example:

```
class BirthdayParty(QObject):

    def __init__(self, parent=None):
        super().__init__(parent)

        # The list which will be accessible from QML.
        self._guests = []

    @pyqtProperty(QQmlListProperty)
    def guests(self):
        return QQmlListProperty(Person, self, self._guests)
```

QML can now manipulate the Python list of `Person` instances.
QQmlListProperty also acts as a proxy for the Python
list so that the following can be written:

```
for guest in party.guests:
    print("Guest:", guest.name)
```

QQmlListProperty can also be used to wrap a *virtual*
list. The following code fragment is taken from the
`chapter5-listproperties.py` example included with PyQt6:

```
class PieChart(QQuickItem):

    @pyqtProperty(QQmlListProperty)
    def slices(self):
        return QQmlListProperty(PieSlice, self,
                append=lambda pie_ch, pie_sl: pie_sl.setParentItem(pie_ch))
```

`PieChart` and `PieSlice` are Quick items that are registered using
[qmlRegisterType()](api/qtqml/qtqml-module.html#qmlRegisterType). Instances of both can be created from
QML. `slices` is a property of `PieChart` that, as far as QML is
concerned, is a list of `PieSlice` instances.

The pyqtProperty decorator specifies that the property
is a QQmlListProperty, that its name is `slices` and
that the `slices()` function is its getter.

The getter returns an instance of QQmlListProperty.
This specifies that elements of the list should be of type `PieSlice`, that
the `PieChart` instance (i.e. `self`) has the property, and defines the
callable that will be invoked in order to append a new element to the list.

The `append` callable is passed two arguments: the object whose property is
to be updated (i.e. the `PyChart` instance), and the element to be appended
(i.e. a `PieSlice` instance). Here we simply set the chart as the slice’s
parent item. Note that there isn’t actually a list anywhere - this is because,
in this particular example, one isn’t needed.

The signature of the `append` callable is slightly different to that of the
corresponding C++ function. In C++ the first argument is the
QQmlListProperty instance rather than the `PyChart`
instance. The signatures of the `at`, `clear` and `count` callables are
different in the same way.

## Using Attached Properties[¶](#using-attached-properties "Link to this heading")

In order to use attached properties in C++, three steps need to be taken.

* A type that has attached properties must implement a static function called
  `qmlAttachedProperties`. This is a factory that creates an instance of the
  properties object to attach.
* A type that has attached properties needs to be defined as such using the
  `QML_ATTACHED` macro.
* The instance of an attached properties object is retrieved using the
  `qmlAttachedPropertiesObject()` template function. The template type is
  the type that has the attached properties.

PyQt6 uses similar, but slightly simpler steps to achieve the same thing.

* When calling [qmlRegisterType()](api/qtqml/qtqml-module.html#qmlRegisterType) to register a type that
  has attached properties the type of the properties object is passed as the
  `attachedProperties` argument. This type will be used as the factory for
  creating an instance of the properties object.
* The instance of an attached properties object is retrieved using the
  [qmlAttachedPropertiesObject()](api/qtqml/qtqml-module.html#qmlAttachedPropertiesObject) function in the same way
  that you would from C++. Just like [qmlRegisterType()](api/qtqml/qtqml-module.html#qmlRegisterType),
  [qmlAttachedPropertiesObject()](api/qtqml/qtqml-module.html#qmlAttachedPropertiesObject) takes an additional first
  argument that is the type that, in C++, would be the template argument.

See the `attach.py` example included with PyQt6 for a complete example
showing the use of attached properties.

## Using Property Value Sources[¶](#using-property-value-sources "Link to this heading")

Property values sources are implemented in PyQt6 in the same way as they are
implemented in C++. Simply sub-class from both
[QObject](api/qtcore/qobject.html) and
[QQmlPropertyValueSource](api/qtqml/qqmlpropertyvaluesource.html) and provide an implementation
of the [setTarget()](api/qtqml/qqmlpropertyvaluesource.html#setTarget) method.

## Using [QQmlParserStatus](api/qtqml/qqmlparserstatus.html)[¶](#using-qqmlparserstatus "Link to this heading")

Monitoring the QML parser status is implemented in PyQt6 in the same way as it
is implemented in C++. Simply sub-class from both
[QObject](api/qtcore/qobject.html) and
[QQmlParserStatus](api/qtqml/qqmlparserstatus.html) and provide implementations of the
[classBegin()](api/qtqml/qqmlparserstatus.html#classBegin) and
[componentComplete()](api/qtqml/qqmlparserstatus.html#componentComplete) methods.

## Writing Python Plugins for **qmlscene**[¶](#writing-python-plugins-for-qmlscene "Link to this heading")

Qt allows plugins that implement QML modules to be written that can be
dynamically loaded by a C++ application (e.g. **qmlscene**). These
plugins are sub-classes of [QQmlExtensionPlugin](api/qtqml/qqmlextensionplugin.html). PyQt6
supports exactly the same thing and allows those plugin to be written in
Python. In other words it is possible to provide QML extensions written in
Python to a C++ application, and to provide QML extensions written in C++ to a
Python application.

PyQt6 provides a QML plugin called `pyqt6qmlplugin`. This acts as a wrapper
around the Python code that implements the plugin. It handles the loading of
the Python interpreter, locating and importing the Python module that contains
the implementation of [QQmlExtensionPlugin](api/qtqml/qqmlextensionplugin.html), creating
an instance of that class, and calling the instance’s
[registerTypes()](api/qtqml/qqmlextensionplugin.html#registerTypes) method. By default
the `pyqt6qmlplugin` is installed in the `PyQt6` sub-directory of your Qt
installation’s `plugin` directory.

Note

`pyqt6qmlplugin` is the name of the plugin as seen by QML. Its actual
filename will be different and operating system dependent.

A QML extension module is a directory containing a file called `qmldir`. The
file contains the name of the module and the name of the plugin that implements
the module. It may also specify the directory containing the plugin. Usually
this isn’t needed because the plugin is installed in the same directory.

Therefore, for a QML extension module called `Charts`, the contents of the
`qmldir` file might be:

```
module Charts
plugin pyqt6qmlplugin /path/to/qt/plugins/PyQt6
```

The `pyqt6qmlplugin` expects to find a Python module in the same directory
with a filename ending with `plugin.py` or `plugin.pyw`. In this case the
name `chartsplugin.py` would be a sensible choice. Before importing this
module `pyqt6qmlplugin` first places the name of the directory at the start
of `sys.path`.

Note

`pyqt6qmlplugin` has to locate the directory containing the `qmldir`
file itself. It does this using the same algorithm used by QML, i.e. it
searches some standard locations and locations specified by the
`QML2_IMPORT_PATH` environment variable. When using
**qmlscene**, `pyqt6qmlplugin` will not know about any additional
locations specified by its `-I` option. Therefore,
`QML2_IMPORT_PATH` should always be used to specify additional
locations to search.

Due to a limitation in QML it is not possible for multiple QML modules to use
the same C++ plugin. In C++ this is not a problem as there is a one-to-one
relationship between a module and the plugin. However, when using Python,
`pyqt6qmlplugin` is used by every module. There are two solutions to this:

* on operating systems that support it, place a symbolic link in the directory
  containing the `qmldir` file that points to the actual `pyqt6qmlplugin`
* make a copy of `pyqt6qmlplugin` in the directory containing the `qmldir`
  file.

In both cases the contents of the `qmldir` file can be simplifed to:

```
module Charts
plugin pyqt6qmlplugin
```

PyQt6 provides an example that can be run as follows:

```
cd /path/to/examples/quick/tutorials/extending/chapter6-plugins
QML2_IMPORT_PATH=. /path/to/qmlscene app.qml
```

On Linux you may also need to set a value for the `LD_LIBRARY_PATH`
environment variable.

### [Table of Contents](index.html)

* Integrating Python and QML
  + [Registering Python Types](#registering-python-types)
  + [A Simple Example](#a-simple-example)
  + [Using QQmlListProperty](#using-qqmllistproperty)
  + [Using Attached Properties](#using-attached-properties)
  + [Using Property Value Sources](#using-property-value-sources)
  + [Using QQmlParserStatus](#using-qqmlparserstatus)
  + [Writing Python Plugins for **qmlscene**](#writing-python-plugins-for-qmlscene)

#### Previous topic

[Support for QSettings](pyqt_qsettings.html "previous chapter")

#### Next topic

[Support for Cooperative Multi-inheritance](multiinheritance.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Integrating Python and QML

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## qmlRegisterType() {#qmlregistertype}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QtQml

# QtQml[¶](#qtqml "Link to this heading")

The QtQml module contains classes to allow applications to
integrate support for QML and JavaScript. Python objects can be exported to
QML or be created from QML in the same way that Qt allows the same with C++
instances. See [Integrating Python and QML](../../qml.html#ref-integrating-qml) for a fuller description of how to
do this.

## Classes[¶](#classes "Link to this heading")

|  |  |  |  |
| --- | --- | --- | --- |
| [QJSEngine](qjsengine.html) | [QQmlAbstractUrlInterceptor](qqmlabstracturlinterceptor.html) | [QQmlExpression](qqmlexpression.html) | [QQmlNetworkAccessManagerFactory](qqmlnetworkaccessmanagerfactory.html) |
| [QJSManagedValue](qjsmanagedvalue.html) | [QQmlApplicationEngine](qqmlapplicationengine.html) | [QQmlExtensionPlugin](qqmlextensionplugin.html) | [QQmlParserStatus](qqmlparserstatus.html) |
| [QJSPrimitiveNull](qjsprimitivenull.html) | [QQmlComponent](qqmlcomponent.html) | [QQmlFileSelector](qqmlfileselector.html) | [QQmlProperty](qqmlproperty.html) |
| [QJSPrimitiveUndefined](qjsprimitiveundefined.html) | [QQmlContext](qqmlcontext.html) | [QQmlImageProviderBase](qqmlimageproviderbase.html) | [QQmlPropertyMap](qqmlpropertymap.html) |
| [QJSPrimitiveValue](qjsprimitivevalue.html) | [QQmlEngine](qqmlengine.html) | [QQmlIncubationController](qqmlincubationcontroller.html) | [QQmlPropertyValueSource](qqmlpropertyvaluesource.html) |
| [QJSValue](qjsvalue.html) | [QQmlEngineExtensionPlugin](qqmlengineextensionplugin.html) | [QQmlIncubator](qqmlincubator.html) | [QQmlScriptString](qqmlscriptstring.html) |
| [QJSValueIterator](qjsvalueiterator.html) | [QQmlError](qqmlerror.html) | [QQmlListReference](qqmllistreference.html) |

## Functions[¶](#functions "Link to this heading")

qjsEngine([QObject](../qtcore/qobject.html)) → [QJSEngine](qjsengine.html)
:   Returns the [QJSEngine](qjsengine.html) associated with *object*, if any.

    This function is useful if you have exposed a [QObject](../qtcore/qobject.html) to the JavaScript environment and later in your program would like to regain access. It does not require you to keep the wrapper around that was returned from [newQObject()](qjsengine.html#newQObject).

---

qmlAttachedPropertiesObject(type, [QObject](../qtcore/qobject.html), create: bool = True) → [QObject](../qtcore/qobject.html)
:   TODO

---

qmlClearTypeRegistrations()
:   Clears all stored type registrations, such as those produced with [qmlRegisterType()](#qmlRegisterType).

    Do not call this function while a [QQmlEngine](qqmlengine.html) exists or behavior will be undefined. Any existing QQmlEngines must be deleted before calling this function. This function only affects the application global cache. Delete the [QQmlEngine](qqmlengine.html) to clear all cached data relating to that engine.

---

qmlContext([QObject](../qtcore/qobject.html)) → [QQmlContext](qqmlcontext.html)
:   Returns the [QQmlContext](qqmlcontext.html) associated with *object*, if any. This is equivalent to [contextForObject()](qqmlengine.html#contextForObject)(object).

    **Note:** Add `#include <QtQml>` to use this function.

    See also

    [contextForObject()](qqmlengine.html#contextForObject), [qmlEngine()](#qmlEngine).

---

qmlEngine([QObject](../qtcore/qobject.html)) → [QQmlEngine](qqmlengine.html)
:   Returns the [QQmlEngine](qqmlengine.html) associated with *object*, if any. This is equivalent to [contextForObject()](qqmlengine.html#contextForObject)(object)->engine(), but more efficient.

    **Note:** Add `#include <QtQml>` to use this function.

    See also

    [contextForObject()](qqmlengine.html#contextForObject), [qmlContext()](#qmlContext).

---

qmlProtectModule(str, int) → bool
:   This function protects a module from further modification. This can be used to prevent other plugins from injecting types into your module. It can also be a performance improvement, as it allows the engine to skip checking for the possibility of new types or plugins when this import is reached.

    Once qmlProtectModule has been called, a QML engine will not search for a new `qmldir` file to load the module anymore. It will re-use any `qmldir` files it has loaded before, though. Therefore, types present at this point continue to work. Mind that different QML engines may load different modules. The module protection, however, is global and affects all engines. The overhead of locating `qmldir` files and loading plugins may be noticeable with slow file systems. Therefore, protecting a module once you are sure you won’t need to load it anymore can be a good optimization. Mind also that the module lock not only affects plugins but also any other qmldir directives, like `import` or `prefer`, as well as any composite types or scripts declared in a `qmldir` file.

    In addition, after this function is called, any attempt to register C++ types into this uri, major version combination will lead to a runtime error.

    Returns true if the module with *uri* as a [module identifier](https://doc.qt.io/qt-6/qtqml-modules-identifiedmodules.html) and *majVersion* as a major version number was found and locked, otherwise returns false. The module must contain exported types in order to be found.

---

qmlRegisterAnonymousType(type, str, int) → int
:   TODO

---

qmlRegisterModule(str, int, int)
:   This function registers a module in a particular *uri* with a version specified in *versionMajor* and *versionMinor*.

    This can be used to make a certain module version available, even if no types are registered for that version. This is particularly useful for keeping the versions of related modules in sync.

---

qmlRegisterRevision(type, str, int, int, attachedProperties: type = None) → int
:   TODO

---

qmlRegisterSingletonInstance(str, int, int, str, [QObject](../qtcore/qobject.html)) → int
:   This function is used to register a singleton object *cppObject*, with a particular *uri* and *typeName*. Its version is a combination of *versionMajor* and *versionMinor*.

    Installing a singleton type into a URI allows you to provide arbitrary functionality (methods and properties) to QML code without requiring individual instances of the type to be instantiated by the client.

    Use this function to register an object of the given type T as a singleton type.

    A [QObject](../qtcore/qobject.html) singleton type may be referenced via the type name with which it was registered; in turn this type name may be used as the target in a [Connections](https://doc.qt.io/qt-6/qml-qtqml-connections.html) type, or like any other type ID. However, there’s one exception: a [QObject](../qtcore/qobject.html) singleton type property can’t be aliased because the singleton type name does not identify an object within the same component as any other item.

    **Note:** *cppObject* must outlive the QML engine in which it is used. Moreover, cppObject must have the same thread affinity as the engine. If you want separate singleton instances for multiple engines, you need to use [qmlRegisterSingletonType()](#qmlRegisterSingletonType). See Threads and QObjects for more information about thread safety.

    **NOTE:** qmlRegisterSingleton can only be used when all types of that module are registered procedurally.

    Usage:

    ```
    // First, define your QObject which provides the functionality.
    class SingletonTypeExample : public QObject
    {
        Q_OBJECT
        Q_PROPERTY(int someProperty READ someProperty WRITE setSomeProperty NOTIFY somePropertyChanged)

    public:
        explicit SingletonTypeExample(QObject* parent = nullptr) : QObject(parent) {}

        Q_INVOKABLE int doSomething()
        {
            setSomeProperty(5);
            return m_someProperty;
        }

        int someProperty() const { return m_someProperty; }
        void setSomeProperty(int val) {
            if (m_someProperty != val) {
                m_someProperty = val;
                emit somePropertyChanged(val);
            }
        }

    signals:
        void somePropertyChanged(int newValue);

    private:
        int m_someProperty = 0;
    };
    ```

    ```
    // Second, create an instance of the object

    // allocate example before the engine to ensure that it outlives it
    QScopedPointer<SingletonTypeExample> example(new SingletonTypeExample);
    QQmlEngine engine;

    // Third, register the singleton type provider with QML by calling this
    // function in an initialization function.
    qmlRegisterSingletonInstance("Qt.example.qobjectSingleton", 1, 0, "MyApi", example.get());
    ```

    In order to use the registered singleton type in QML, you must import the URI with the corresponding version.

    See also

    QML\_SINGLETON, [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

---

qmlRegisterSingletonType([QUrl](../qtcore/qurl.html), str, int, int, str) → int
:   This function may be used to register a singleton type with the name *qmlName*, in the library imported from *uri* having the version number composed from *versionMajor* and *versionMinor*. The type is defined by the QML file located at *url*. The url must be an absolute URL, i.e. url.isRelative() == false.

    In addition the type’s QML file must have pragma Singleton statement among its import statements.

    A singleton type may be referenced via the type name with which it was registered, and this typename may be used as the target in a [Connections](https://doc.qt.io/qt-6/qml-qtqml-connections.html) type or otherwise used as any other type id would. One exception to this is that a singleton type property may not be aliased (because the singleton type name does not identify an object within the same component as any other item).

    Usage:

    ```
    // Second, register the QML singleton type by calling this function in an initialization function.
    qmlRegisterSingletonType(QUrl("file:///absolute/path/SingletonType.qml"), "Qt.example.qobjectSingleton", 1, 0, "RegisteredSingleton");
    ```

    In order to use the registered singleton type in QML, you must import the singleton type.

    It is also possible to have QML singleton types registered without using the qmlRegisterSingletonType function. That can be done by adding a pragma Singleton statement among the imports of the type’s QML file. In addition the type must be defined in a qmldir file with a singleton keyword and the qmldir must be imported by the QML files using the singleton.

    See also

    QML\_SINGLETON.

---

qmlRegisterSingletonType(type, str, int, int, Callable[[[QQmlEngine](qqmlengine.html), [QJSEngine](qjsengine.html)], Any], name: str = None) → int
:   TODO

---

qmlRegisterType([QUrl](../qtcore/qurl.html), str, int, int, str) → int
:   This function registers a type in the QML system with the name *qmlName*, in the library imported from *uri* having the version number composed from *versionMajor* and *versionMinor*. The type is defined by the QML file located at *url*. The url must be an absolute URL, i.e. url.isRelative() == false.

    Normally QML files can be loaded as types directly from other QML files, or using a qmldir file. This function allows registration of files to types from C++ code, such as when the type mapping needs to be procedurally determined at startup.

    Returns -1 if the registration was not successful.

---

qmlRegisterType(type, str, int, int, name: str = None, attachedProperties: type = None) → int
:   TODO

---

qmlRegisterTypeNotAvailable(str, int, int, str, str|None) → int
:   TODO

---

qmlRegisterUncreatableMetaObject([QMetaObject](../qtcore/qmetaobject.html), str, int, int, str, str|None) → int
:   TODO

---

qmlRegisterUncreatableType(type, str, int, int, str|None, qmlName: str = None) → int
:   TODO

---

qmlTypeId(str, int, int, str) → int
:   Returns the QML type id of a type that was registered with the name *qmlName* in a particular *uri* and a version specified in *versionMajor* and *versionMinor*.

    This function returns the same value as the QML type registration functions such as [qmlRegisterType()](#qmlRegisterType) and [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

    If *qmlName*, *uri* and *versionMajor* match a registered type, but the specified minor version in *versionMinor* is higher, then the id of the type with the closest minor version is returned.

    Returns -1 if no matching type was found or one of the given parameters was invalid.

    **Note:** : qmlTypeId tries to make modules available, even if they were not accessed by any engine yet. This can introduce overhead the first time a module is accessed. Trying to find types from a module which does not exist always introduces this overhead.

    See also

    QML\_ELEMENT, QML\_NAMED\_ELEMENT, QML\_SINGLETON, [qmlRegisterType()](#qmlRegisterType), [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

### [Table of Contents](../../index.html)

* QtQml
  + [Classes](#classes)
  + [Functions](#functions)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QtQml

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## qmlAttachedPropertiesObject() {#qmlattachedpropertiesobject}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QtQml

# QtQml[¶](#qtqml "Link to this heading")

The QtQml module contains classes to allow applications to
integrate support for QML and JavaScript. Python objects can be exported to
QML or be created from QML in the same way that Qt allows the same with C++
instances. See [Integrating Python and QML](../../qml.html#ref-integrating-qml) for a fuller description of how to
do this.

## Classes[¶](#classes "Link to this heading")

|  |  |  |  |
| --- | --- | --- | --- |
| [QJSEngine](qjsengine.html) | [QQmlAbstractUrlInterceptor](qqmlabstracturlinterceptor.html) | [QQmlExpression](qqmlexpression.html) | [QQmlNetworkAccessManagerFactory](qqmlnetworkaccessmanagerfactory.html) |
| [QJSManagedValue](qjsmanagedvalue.html) | [QQmlApplicationEngine](qqmlapplicationengine.html) | [QQmlExtensionPlugin](qqmlextensionplugin.html) | [QQmlParserStatus](qqmlparserstatus.html) |
| [QJSPrimitiveNull](qjsprimitivenull.html) | [QQmlComponent](qqmlcomponent.html) | [QQmlFileSelector](qqmlfileselector.html) | [QQmlProperty](qqmlproperty.html) |
| [QJSPrimitiveUndefined](qjsprimitiveundefined.html) | [QQmlContext](qqmlcontext.html) | [QQmlImageProviderBase](qqmlimageproviderbase.html) | [QQmlPropertyMap](qqmlpropertymap.html) |
| [QJSPrimitiveValue](qjsprimitivevalue.html) | [QQmlEngine](qqmlengine.html) | [QQmlIncubationController](qqmlincubationcontroller.html) | [QQmlPropertyValueSource](qqmlpropertyvaluesource.html) |
| [QJSValue](qjsvalue.html) | [QQmlEngineExtensionPlugin](qqmlengineextensionplugin.html) | [QQmlIncubator](qqmlincubator.html) | [QQmlScriptString](qqmlscriptstring.html) |
| [QJSValueIterator](qjsvalueiterator.html) | [QQmlError](qqmlerror.html) | [QQmlListReference](qqmllistreference.html) |

## Functions[¶](#functions "Link to this heading")

qjsEngine([QObject](../qtcore/qobject.html)) → [QJSEngine](qjsengine.html)
:   Returns the [QJSEngine](qjsengine.html) associated with *object*, if any.

    This function is useful if you have exposed a [QObject](../qtcore/qobject.html) to the JavaScript environment and later in your program would like to regain access. It does not require you to keep the wrapper around that was returned from [newQObject()](qjsengine.html#newQObject).

---

qmlAttachedPropertiesObject(type, [QObject](../qtcore/qobject.html), create: bool = True) → [QObject](../qtcore/qobject.html)
:   TODO

---

qmlClearTypeRegistrations()
:   Clears all stored type registrations, such as those produced with [qmlRegisterType()](#qmlRegisterType).

    Do not call this function while a [QQmlEngine](qqmlengine.html) exists or behavior will be undefined. Any existing QQmlEngines must be deleted before calling this function. This function only affects the application global cache. Delete the [QQmlEngine](qqmlengine.html) to clear all cached data relating to that engine.

---

qmlContext([QObject](../qtcore/qobject.html)) → [QQmlContext](qqmlcontext.html)
:   Returns the [QQmlContext](qqmlcontext.html) associated with *object*, if any. This is equivalent to [contextForObject()](qqmlengine.html#contextForObject)(object).

    **Note:** Add `#include <QtQml>` to use this function.

    See also

    [contextForObject()](qqmlengine.html#contextForObject), [qmlEngine()](#qmlEngine).

---

qmlEngine([QObject](../qtcore/qobject.html)) → [QQmlEngine](qqmlengine.html)
:   Returns the [QQmlEngine](qqmlengine.html) associated with *object*, if any. This is equivalent to [contextForObject()](qqmlengine.html#contextForObject)(object)->engine(), but more efficient.

    **Note:** Add `#include <QtQml>` to use this function.

    See also

    [contextForObject()](qqmlengine.html#contextForObject), [qmlContext()](#qmlContext).

---

qmlProtectModule(str, int) → bool
:   This function protects a module from further modification. This can be used to prevent other plugins from injecting types into your module. It can also be a performance improvement, as it allows the engine to skip checking for the possibility of new types or plugins when this import is reached.

    Once qmlProtectModule has been called, a QML engine will not search for a new `qmldir` file to load the module anymore. It will re-use any `qmldir` files it has loaded before, though. Therefore, types present at this point continue to work. Mind that different QML engines may load different modules. The module protection, however, is global and affects all engines. The overhead of locating `qmldir` files and loading plugins may be noticeable with slow file systems. Therefore, protecting a module once you are sure you won’t need to load it anymore can be a good optimization. Mind also that the module lock not only affects plugins but also any other qmldir directives, like `import` or `prefer`, as well as any composite types or scripts declared in a `qmldir` file.

    In addition, after this function is called, any attempt to register C++ types into this uri, major version combination will lead to a runtime error.

    Returns true if the module with *uri* as a [module identifier](https://doc.qt.io/qt-6/qtqml-modules-identifiedmodules.html) and *majVersion* as a major version number was found and locked, otherwise returns false. The module must contain exported types in order to be found.

---

qmlRegisterAnonymousType(type, str, int) → int
:   TODO

---

qmlRegisterModule(str, int, int)
:   This function registers a module in a particular *uri* with a version specified in *versionMajor* and *versionMinor*.

    This can be used to make a certain module version available, even if no types are registered for that version. This is particularly useful for keeping the versions of related modules in sync.

---

qmlRegisterRevision(type, str, int, int, attachedProperties: type = None) → int
:   TODO

---

qmlRegisterSingletonInstance(str, int, int, str, [QObject](../qtcore/qobject.html)) → int
:   This function is used to register a singleton object *cppObject*, with a particular *uri* and *typeName*. Its version is a combination of *versionMajor* and *versionMinor*.

    Installing a singleton type into a URI allows you to provide arbitrary functionality (methods and properties) to QML code without requiring individual instances of the type to be instantiated by the client.

    Use this function to register an object of the given type T as a singleton type.

    A [QObject](../qtcore/qobject.html) singleton type may be referenced via the type name with which it was registered; in turn this type name may be used as the target in a [Connections](https://doc.qt.io/qt-6/qml-qtqml-connections.html) type, or like any other type ID. However, there’s one exception: a [QObject](../qtcore/qobject.html) singleton type property can’t be aliased because the singleton type name does not identify an object within the same component as any other item.

    **Note:** *cppObject* must outlive the QML engine in which it is used. Moreover, cppObject must have the same thread affinity as the engine. If you want separate singleton instances for multiple engines, you need to use [qmlRegisterSingletonType()](#qmlRegisterSingletonType). See Threads and QObjects for more information about thread safety.

    **NOTE:** qmlRegisterSingleton can only be used when all types of that module are registered procedurally.

    Usage:

    ```
    // First, define your QObject which provides the functionality.
    class SingletonTypeExample : public QObject
    {
        Q_OBJECT
        Q_PROPERTY(int someProperty READ someProperty WRITE setSomeProperty NOTIFY somePropertyChanged)

    public:
        explicit SingletonTypeExample(QObject* parent = nullptr) : QObject(parent) {}

        Q_INVOKABLE int doSomething()
        {
            setSomeProperty(5);
            return m_someProperty;
        }

        int someProperty() const { return m_someProperty; }
        void setSomeProperty(int val) {
            if (m_someProperty != val) {
                m_someProperty = val;
                emit somePropertyChanged(val);
            }
        }

    signals:
        void somePropertyChanged(int newValue);

    private:
        int m_someProperty = 0;
    };
    ```

    ```
    // Second, create an instance of the object

    // allocate example before the engine to ensure that it outlives it
    QScopedPointer<SingletonTypeExample> example(new SingletonTypeExample);
    QQmlEngine engine;

    // Third, register the singleton type provider with QML by calling this
    // function in an initialization function.
    qmlRegisterSingletonInstance("Qt.example.qobjectSingleton", 1, 0, "MyApi", example.get());
    ```

    In order to use the registered singleton type in QML, you must import the URI with the corresponding version.

    See also

    QML\_SINGLETON, [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

---

qmlRegisterSingletonType([QUrl](../qtcore/qurl.html), str, int, int, str) → int
:   This function may be used to register a singleton type with the name *qmlName*, in the library imported from *uri* having the version number composed from *versionMajor* and *versionMinor*. The type is defined by the QML file located at *url*. The url must be an absolute URL, i.e. url.isRelative() == false.

    In addition the type’s QML file must have pragma Singleton statement among its import statements.

    A singleton type may be referenced via the type name with which it was registered, and this typename may be used as the target in a [Connections](https://doc.qt.io/qt-6/qml-qtqml-connections.html) type or otherwise used as any other type id would. One exception to this is that a singleton type property may not be aliased (because the singleton type name does not identify an object within the same component as any other item).

    Usage:

    ```
    // Second, register the QML singleton type by calling this function in an initialization function.
    qmlRegisterSingletonType(QUrl("file:///absolute/path/SingletonType.qml"), "Qt.example.qobjectSingleton", 1, 0, "RegisteredSingleton");
    ```

    In order to use the registered singleton type in QML, you must import the singleton type.

    It is also possible to have QML singleton types registered without using the qmlRegisterSingletonType function. That can be done by adding a pragma Singleton statement among the imports of the type’s QML file. In addition the type must be defined in a qmldir file with a singleton keyword and the qmldir must be imported by the QML files using the singleton.

    See also

    QML\_SINGLETON.

---

qmlRegisterSingletonType(type, str, int, int, Callable[[[QQmlEngine](qqmlengine.html), [QJSEngine](qjsengine.html)], Any], name: str = None) → int
:   TODO

---

qmlRegisterType([QUrl](../qtcore/qurl.html), str, int, int, str) → int
:   This function registers a type in the QML system with the name *qmlName*, in the library imported from *uri* having the version number composed from *versionMajor* and *versionMinor*. The type is defined by the QML file located at *url*. The url must be an absolute URL, i.e. url.isRelative() == false.

    Normally QML files can be loaded as types directly from other QML files, or using a qmldir file. This function allows registration of files to types from C++ code, such as when the type mapping needs to be procedurally determined at startup.

    Returns -1 if the registration was not successful.

---

qmlRegisterType(type, str, int, int, name: str = None, attachedProperties: type = None) → int
:   TODO

---

qmlRegisterTypeNotAvailable(str, int, int, str, str|None) → int
:   TODO

---

qmlRegisterUncreatableMetaObject([QMetaObject](../qtcore/qmetaobject.html), str, int, int, str, str|None) → int
:   TODO

---

qmlRegisterUncreatableType(type, str, int, int, str|None, qmlName: str = None) → int
:   TODO

---

qmlTypeId(str, int, int, str) → int
:   Returns the QML type id of a type that was registered with the name *qmlName* in a particular *uri* and a version specified in *versionMajor* and *versionMinor*.

    This function returns the same value as the QML type registration functions such as [qmlRegisterType()](#qmlRegisterType) and [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

    If *qmlName*, *uri* and *versionMajor* match a registered type, but the specified minor version in *versionMinor* is higher, then the id of the type with the closest minor version is returned.

    Returns -1 if no matching type was found or one of the given parameters was invalid.

    **Note:** : qmlTypeId tries to make modules available, even if they were not accessed by any engine yet. This can introduce overhead the first time a module is accessed. Trying to find types from a module which does not exist always introduces this overhead.

    See also

    QML\_ELEMENT, QML\_NAMED\_ELEMENT, QML\_SINGLETON, [qmlRegisterType()](#qmlRegisterType), [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

### [Table of Contents](../../index.html)

* QtQml
  + [Classes](#classes)
  + [Functions](#functions)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QtQml

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## qmlRegisterType() {#qmlregistertype}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QtQml

# QtQml[¶](#qtqml "Link to this heading")

The QtQml module contains classes to allow applications to
integrate support for QML and JavaScript. Python objects can be exported to
QML or be created from QML in the same way that Qt allows the same with C++
instances. See [Integrating Python and QML](../../qml.html#ref-integrating-qml) for a fuller description of how to
do this.

## Classes[¶](#classes "Link to this heading")

|  |  |  |  |
| --- | --- | --- | --- |
| [QJSEngine](qjsengine.html) | [QQmlAbstractUrlInterceptor](qqmlabstracturlinterceptor.html) | [QQmlExpression](qqmlexpression.html) | [QQmlNetworkAccessManagerFactory](qqmlnetworkaccessmanagerfactory.html) |
| [QJSManagedValue](qjsmanagedvalue.html) | [QQmlApplicationEngine](qqmlapplicationengine.html) | [QQmlExtensionPlugin](qqmlextensionplugin.html) | [QQmlParserStatus](qqmlparserstatus.html) |
| [QJSPrimitiveNull](qjsprimitivenull.html) | [QQmlComponent](qqmlcomponent.html) | [QQmlFileSelector](qqmlfileselector.html) | [QQmlProperty](qqmlproperty.html) |
| [QJSPrimitiveUndefined](qjsprimitiveundefined.html) | [QQmlContext](qqmlcontext.html) | [QQmlImageProviderBase](qqmlimageproviderbase.html) | [QQmlPropertyMap](qqmlpropertymap.html) |
| [QJSPrimitiveValue](qjsprimitivevalue.html) | [QQmlEngine](qqmlengine.html) | [QQmlIncubationController](qqmlincubationcontroller.html) | [QQmlPropertyValueSource](qqmlpropertyvaluesource.html) |
| [QJSValue](qjsvalue.html) | [QQmlEngineExtensionPlugin](qqmlengineextensionplugin.html) | [QQmlIncubator](qqmlincubator.html) | [QQmlScriptString](qqmlscriptstring.html) |
| [QJSValueIterator](qjsvalueiterator.html) | [QQmlError](qqmlerror.html) | [QQmlListReference](qqmllistreference.html) |

## Functions[¶](#functions "Link to this heading")

qjsEngine([QObject](../qtcore/qobject.html)) → [QJSEngine](qjsengine.html)
:   Returns the [QJSEngine](qjsengine.html) associated with *object*, if any.

    This function is useful if you have exposed a [QObject](../qtcore/qobject.html) to the JavaScript environment and later in your program would like to regain access. It does not require you to keep the wrapper around that was returned from [newQObject()](qjsengine.html#newQObject).

---

qmlAttachedPropertiesObject(type, [QObject](../qtcore/qobject.html), create: bool = True) → [QObject](../qtcore/qobject.html)
:   TODO

---

qmlClearTypeRegistrations()
:   Clears all stored type registrations, such as those produced with [qmlRegisterType()](#qmlRegisterType).

    Do not call this function while a [QQmlEngine](qqmlengine.html) exists or behavior will be undefined. Any existing QQmlEngines must be deleted before calling this function. This function only affects the application global cache. Delete the [QQmlEngine](qqmlengine.html) to clear all cached data relating to that engine.

---

qmlContext([QObject](../qtcore/qobject.html)) → [QQmlContext](qqmlcontext.html)
:   Returns the [QQmlContext](qqmlcontext.html) associated with *object*, if any. This is equivalent to [contextForObject()](qqmlengine.html#contextForObject)(object).

    **Note:** Add `#include <QtQml>` to use this function.

    See also

    [contextForObject()](qqmlengine.html#contextForObject), [qmlEngine()](#qmlEngine).

---

qmlEngine([QObject](../qtcore/qobject.html)) → [QQmlEngine](qqmlengine.html)
:   Returns the [QQmlEngine](qqmlengine.html) associated with *object*, if any. This is equivalent to [contextForObject()](qqmlengine.html#contextForObject)(object)->engine(), but more efficient.

    **Note:** Add `#include <QtQml>` to use this function.

    See also

    [contextForObject()](qqmlengine.html#contextForObject), [qmlContext()](#qmlContext).

---

qmlProtectModule(str, int) → bool
:   This function protects a module from further modification. This can be used to prevent other plugins from injecting types into your module. It can also be a performance improvement, as it allows the engine to skip checking for the possibility of new types or plugins when this import is reached.

    Once qmlProtectModule has been called, a QML engine will not search for a new `qmldir` file to load the module anymore. It will re-use any `qmldir` files it has loaded before, though. Therefore, types present at this point continue to work. Mind that different QML engines may load different modules. The module protection, however, is global and affects all engines. The overhead of locating `qmldir` files and loading plugins may be noticeable with slow file systems. Therefore, protecting a module once you are sure you won’t need to load it anymore can be a good optimization. Mind also that the module lock not only affects plugins but also any other qmldir directives, like `import` or `prefer`, as well as any composite types or scripts declared in a `qmldir` file.

    In addition, after this function is called, any attempt to register C++ types into this uri, major version combination will lead to a runtime error.

    Returns true if the module with *uri* as a [module identifier](https://doc.qt.io/qt-6/qtqml-modules-identifiedmodules.html) and *majVersion* as a major version number was found and locked, otherwise returns false. The module must contain exported types in order to be found.

---

qmlRegisterAnonymousType(type, str, int) → int
:   TODO

---

qmlRegisterModule(str, int, int)
:   This function registers a module in a particular *uri* with a version specified in *versionMajor* and *versionMinor*.

    This can be used to make a certain module version available, even if no types are registered for that version. This is particularly useful for keeping the versions of related modules in sync.

---

qmlRegisterRevision(type, str, int, int, attachedProperties: type = None) → int
:   TODO

---

qmlRegisterSingletonInstance(str, int, int, str, [QObject](../qtcore/qobject.html)) → int
:   This function is used to register a singleton object *cppObject*, with a particular *uri* and *typeName*. Its version is a combination of *versionMajor* and *versionMinor*.

    Installing a singleton type into a URI allows you to provide arbitrary functionality (methods and properties) to QML code without requiring individual instances of the type to be instantiated by the client.

    Use this function to register an object of the given type T as a singleton type.

    A [QObject](../qtcore/qobject.html) singleton type may be referenced via the type name with which it was registered; in turn this type name may be used as the target in a [Connections](https://doc.qt.io/qt-6/qml-qtqml-connections.html) type, or like any other type ID. However, there’s one exception: a [QObject](../qtcore/qobject.html) singleton type property can’t be aliased because the singleton type name does not identify an object within the same component as any other item.

    **Note:** *cppObject* must outlive the QML engine in which it is used. Moreover, cppObject must have the same thread affinity as the engine. If you want separate singleton instances for multiple engines, you need to use [qmlRegisterSingletonType()](#qmlRegisterSingletonType). See Threads and QObjects for more information about thread safety.

    **NOTE:** qmlRegisterSingleton can only be used when all types of that module are registered procedurally.

    Usage:

    ```
    // First, define your QObject which provides the functionality.
    class SingletonTypeExample : public QObject
    {
        Q_OBJECT
        Q_PROPERTY(int someProperty READ someProperty WRITE setSomeProperty NOTIFY somePropertyChanged)

    public:
        explicit SingletonTypeExample(QObject* parent = nullptr) : QObject(parent) {}

        Q_INVOKABLE int doSomething()
        {
            setSomeProperty(5);
            return m_someProperty;
        }

        int someProperty() const { return m_someProperty; }
        void setSomeProperty(int val) {
            if (m_someProperty != val) {
                m_someProperty = val;
                emit somePropertyChanged(val);
            }
        }

    signals:
        void somePropertyChanged(int newValue);

    private:
        int m_someProperty = 0;
    };
    ```

    ```
    // Second, create an instance of the object

    // allocate example before the engine to ensure that it outlives it
    QScopedPointer<SingletonTypeExample> example(new SingletonTypeExample);
    QQmlEngine engine;

    // Third, register the singleton type provider with QML by calling this
    // function in an initialization function.
    qmlRegisterSingletonInstance("Qt.example.qobjectSingleton", 1, 0, "MyApi", example.get());
    ```

    In order to use the registered singleton type in QML, you must import the URI with the corresponding version.

    See also

    QML\_SINGLETON, [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

---

qmlRegisterSingletonType([QUrl](../qtcore/qurl.html), str, int, int, str) → int
:   This function may be used to register a singleton type with the name *qmlName*, in the library imported from *uri* having the version number composed from *versionMajor* and *versionMinor*. The type is defined by the QML file located at *url*. The url must be an absolute URL, i.e. url.isRelative() == false.

    In addition the type’s QML file must have pragma Singleton statement among its import statements.

    A singleton type may be referenced via the type name with which it was registered, and this typename may be used as the target in a [Connections](https://doc.qt.io/qt-6/qml-qtqml-connections.html) type or otherwise used as any other type id would. One exception to this is that a singleton type property may not be aliased (because the singleton type name does not identify an object within the same component as any other item).

    Usage:

    ```
    // Second, register the QML singleton type by calling this function in an initialization function.
    qmlRegisterSingletonType(QUrl("file:///absolute/path/SingletonType.qml"), "Qt.example.qobjectSingleton", 1, 0, "RegisteredSingleton");
    ```

    In order to use the registered singleton type in QML, you must import the singleton type.

    It is also possible to have QML singleton types registered without using the qmlRegisterSingletonType function. That can be done by adding a pragma Singleton statement among the imports of the type’s QML file. In addition the type must be defined in a qmldir file with a singleton keyword and the qmldir must be imported by the QML files using the singleton.

    See also

    QML\_SINGLETON.

---

qmlRegisterSingletonType(type, str, int, int, Callable[[[QQmlEngine](qqmlengine.html), [QJSEngine](qjsengine.html)], Any], name: str = None) → int
:   TODO

---

qmlRegisterType([QUrl](../qtcore/qurl.html), str, int, int, str) → int
:   This function registers a type in the QML system with the name *qmlName*, in the library imported from *uri* having the version number composed from *versionMajor* and *versionMinor*. The type is defined by the QML file located at *url*. The url must be an absolute URL, i.e. url.isRelative() == false.

    Normally QML files can be loaded as types directly from other QML files, or using a qmldir file. This function allows registration of files to types from C++ code, such as when the type mapping needs to be procedurally determined at startup.

    Returns -1 if the registration was not successful.

---

qmlRegisterType(type, str, int, int, name: str = None, attachedProperties: type = None) → int
:   TODO

---

qmlRegisterTypeNotAvailable(str, int, int, str, str|None) → int
:   TODO

---

qmlRegisterUncreatableMetaObject([QMetaObject](../qtcore/qmetaobject.html), str, int, int, str, str|None) → int
:   TODO

---

qmlRegisterUncreatableType(type, str, int, int, str|None, qmlName: str = None) → int
:   TODO

---

qmlTypeId(str, int, int, str) → int
:   Returns the QML type id of a type that was registered with the name *qmlName* in a particular *uri* and a version specified in *versionMajor* and *versionMinor*.

    This function returns the same value as the QML type registration functions such as [qmlRegisterType()](#qmlRegisterType) and [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

    If *qmlName*, *uri* and *versionMajor* match a registered type, but the specified minor version in *versionMinor* is higher, then the id of the type with the closest minor version is returned.

    Returns -1 if no matching type was found or one of the given parameters was invalid.

    **Note:** : qmlTypeId tries to make modules available, even if they were not accessed by any engine yet. This can introduce overhead the first time a module is accessed. Trying to find types from a module which does not exist always introduces this overhead.

    See also

    QML\_ELEMENT, QML\_NAMED\_ELEMENT, QML\_SINGLETON, [qmlRegisterType()](#qmlRegisterType), [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

### [Table of Contents](../../index.html)

* QtQml
  + [Classes](#classes)
  + [Functions](#functions)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QtQml

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## qmlAttachedPropertiesObject() {#qmlattachedpropertiesobject}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QtQml

# QtQml[¶](#qtqml "Link to this heading")

The QtQml module contains classes to allow applications to
integrate support for QML and JavaScript. Python objects can be exported to
QML or be created from QML in the same way that Qt allows the same with C++
instances. See [Integrating Python and QML](../../qml.html#ref-integrating-qml) for a fuller description of how to
do this.

## Classes[¶](#classes "Link to this heading")

|  |  |  |  |
| --- | --- | --- | --- |
| [QJSEngine](qjsengine.html) | [QQmlAbstractUrlInterceptor](qqmlabstracturlinterceptor.html) | [QQmlExpression](qqmlexpression.html) | [QQmlNetworkAccessManagerFactory](qqmlnetworkaccessmanagerfactory.html) |
| [QJSManagedValue](qjsmanagedvalue.html) | [QQmlApplicationEngine](qqmlapplicationengine.html) | [QQmlExtensionPlugin](qqmlextensionplugin.html) | [QQmlParserStatus](qqmlparserstatus.html) |
| [QJSPrimitiveNull](qjsprimitivenull.html) | [QQmlComponent](qqmlcomponent.html) | [QQmlFileSelector](qqmlfileselector.html) | [QQmlProperty](qqmlproperty.html) |
| [QJSPrimitiveUndefined](qjsprimitiveundefined.html) | [QQmlContext](qqmlcontext.html) | [QQmlImageProviderBase](qqmlimageproviderbase.html) | [QQmlPropertyMap](qqmlpropertymap.html) |
| [QJSPrimitiveValue](qjsprimitivevalue.html) | [QQmlEngine](qqmlengine.html) | [QQmlIncubationController](qqmlincubationcontroller.html) | [QQmlPropertyValueSource](qqmlpropertyvaluesource.html) |
| [QJSValue](qjsvalue.html) | [QQmlEngineExtensionPlugin](qqmlengineextensionplugin.html) | [QQmlIncubator](qqmlincubator.html) | [QQmlScriptString](qqmlscriptstring.html) |
| [QJSValueIterator](qjsvalueiterator.html) | [QQmlError](qqmlerror.html) | [QQmlListReference](qqmllistreference.html) |

## Functions[¶](#functions "Link to this heading")

qjsEngine([QObject](../qtcore/qobject.html)) → [QJSEngine](qjsengine.html)
:   Returns the [QJSEngine](qjsengine.html) associated with *object*, if any.

    This function is useful if you have exposed a [QObject](../qtcore/qobject.html) to the JavaScript environment and later in your program would like to regain access. It does not require you to keep the wrapper around that was returned from [newQObject()](qjsengine.html#newQObject).

---

qmlAttachedPropertiesObject(type, [QObject](../qtcore/qobject.html), create: bool = True) → [QObject](../qtcore/qobject.html)
:   TODO

---

qmlClearTypeRegistrations()
:   Clears all stored type registrations, such as those produced with [qmlRegisterType()](#qmlRegisterType).

    Do not call this function while a [QQmlEngine](qqmlengine.html) exists or behavior will be undefined. Any existing QQmlEngines must be deleted before calling this function. This function only affects the application global cache. Delete the [QQmlEngine](qqmlengine.html) to clear all cached data relating to that engine.

---

qmlContext([QObject](../qtcore/qobject.html)) → [QQmlContext](qqmlcontext.html)
:   Returns the [QQmlContext](qqmlcontext.html) associated with *object*, if any. This is equivalent to [contextForObject()](qqmlengine.html#contextForObject)(object).

    **Note:** Add `#include <QtQml>` to use this function.

    See also

    [contextForObject()](qqmlengine.html#contextForObject), [qmlEngine()](#qmlEngine).

---

qmlEngine([QObject](../qtcore/qobject.html)) → [QQmlEngine](qqmlengine.html)
:   Returns the [QQmlEngine](qqmlengine.html) associated with *object*, if any. This is equivalent to [contextForObject()](qqmlengine.html#contextForObject)(object)->engine(), but more efficient.

    **Note:** Add `#include <QtQml>` to use this function.

    See also

    [contextForObject()](qqmlengine.html#contextForObject), [qmlContext()](#qmlContext).

---

qmlProtectModule(str, int) → bool
:   This function protects a module from further modification. This can be used to prevent other plugins from injecting types into your module. It can also be a performance improvement, as it allows the engine to skip checking for the possibility of new types or plugins when this import is reached.

    Once qmlProtectModule has been called, a QML engine will not search for a new `qmldir` file to load the module anymore. It will re-use any `qmldir` files it has loaded before, though. Therefore, types present at this point continue to work. Mind that different QML engines may load different modules. The module protection, however, is global and affects all engines. The overhead of locating `qmldir` files and loading plugins may be noticeable with slow file systems. Therefore, protecting a module once you are sure you won’t need to load it anymore can be a good optimization. Mind also that the module lock not only affects plugins but also any other qmldir directives, like `import` or `prefer`, as well as any composite types or scripts declared in a `qmldir` file.

    In addition, after this function is called, any attempt to register C++ types into this uri, major version combination will lead to a runtime error.

    Returns true if the module with *uri* as a [module identifier](https://doc.qt.io/qt-6/qtqml-modules-identifiedmodules.html) and *majVersion* as a major version number was found and locked, otherwise returns false. The module must contain exported types in order to be found.

---

qmlRegisterAnonymousType(type, str, int) → int
:   TODO

---

qmlRegisterModule(str, int, int)
:   This function registers a module in a particular *uri* with a version specified in *versionMajor* and *versionMinor*.

    This can be used to make a certain module version available, even if no types are registered for that version. This is particularly useful for keeping the versions of related modules in sync.

---

qmlRegisterRevision(type, str, int, int, attachedProperties: type = None) → int
:   TODO

---

qmlRegisterSingletonInstance(str, int, int, str, [QObject](../qtcore/qobject.html)) → int
:   This function is used to register a singleton object *cppObject*, with a particular *uri* and *typeName*. Its version is a combination of *versionMajor* and *versionMinor*.

    Installing a singleton type into a URI allows you to provide arbitrary functionality (methods and properties) to QML code without requiring individual instances of the type to be instantiated by the client.

    Use this function to register an object of the given type T as a singleton type.

    A [QObject](../qtcore/qobject.html) singleton type may be referenced via the type name with which it was registered; in turn this type name may be used as the target in a [Connections](https://doc.qt.io/qt-6/qml-qtqml-connections.html) type, or like any other type ID. However, there’s one exception: a [QObject](../qtcore/qobject.html) singleton type property can’t be aliased because the singleton type name does not identify an object within the same component as any other item.

    **Note:** *cppObject* must outlive the QML engine in which it is used. Moreover, cppObject must have the same thread affinity as the engine. If you want separate singleton instances for multiple engines, you need to use [qmlRegisterSingletonType()](#qmlRegisterSingletonType). See Threads and QObjects for more information about thread safety.

    **NOTE:** qmlRegisterSingleton can only be used when all types of that module are registered procedurally.

    Usage:

    ```
    // First, define your QObject which provides the functionality.
    class SingletonTypeExample : public QObject
    {
        Q_OBJECT
        Q_PROPERTY(int someProperty READ someProperty WRITE setSomeProperty NOTIFY somePropertyChanged)

    public:
        explicit SingletonTypeExample(QObject* parent = nullptr) : QObject(parent) {}

        Q_INVOKABLE int doSomething()
        {
            setSomeProperty(5);
            return m_someProperty;
        }

        int someProperty() const { return m_someProperty; }
        void setSomeProperty(int val) {
            if (m_someProperty != val) {
                m_someProperty = val;
                emit somePropertyChanged(val);
            }
        }

    signals:
        void somePropertyChanged(int newValue);

    private:
        int m_someProperty = 0;
    };
    ```

    ```
    // Second, create an instance of the object

    // allocate example before the engine to ensure that it outlives it
    QScopedPointer<SingletonTypeExample> example(new SingletonTypeExample);
    QQmlEngine engine;

    // Third, register the singleton type provider with QML by calling this
    // function in an initialization function.
    qmlRegisterSingletonInstance("Qt.example.qobjectSingleton", 1, 0, "MyApi", example.get());
    ```

    In order to use the registered singleton type in QML, you must import the URI with the corresponding version.

    See also

    QML\_SINGLETON, [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

---

qmlRegisterSingletonType([QUrl](../qtcore/qurl.html), str, int, int, str) → int
:   This function may be used to register a singleton type with the name *qmlName*, in the library imported from *uri* having the version number composed from *versionMajor* and *versionMinor*. The type is defined by the QML file located at *url*. The url must be an absolute URL, i.e. url.isRelative() == false.

    In addition the type’s QML file must have pragma Singleton statement among its import statements.

    A singleton type may be referenced via the type name with which it was registered, and this typename may be used as the target in a [Connections](https://doc.qt.io/qt-6/qml-qtqml-connections.html) type or otherwise used as any other type id would. One exception to this is that a singleton type property may not be aliased (because the singleton type name does not identify an object within the same component as any other item).

    Usage:

    ```
    // Second, register the QML singleton type by calling this function in an initialization function.
    qmlRegisterSingletonType(QUrl("file:///absolute/path/SingletonType.qml"), "Qt.example.qobjectSingleton", 1, 0, "RegisteredSingleton");
    ```

    In order to use the registered singleton type in QML, you must import the singleton type.

    It is also possible to have QML singleton types registered without using the qmlRegisterSingletonType function. That can be done by adding a pragma Singleton statement among the imports of the type’s QML file. In addition the type must be defined in a qmldir file with a singleton keyword and the qmldir must be imported by the QML files using the singleton.

    See also

    QML\_SINGLETON.

---

qmlRegisterSingletonType(type, str, int, int, Callable[[[QQmlEngine](qqmlengine.html), [QJSEngine](qjsengine.html)], Any], name: str = None) → int
:   TODO

---

qmlRegisterType([QUrl](../qtcore/qurl.html), str, int, int, str) → int
:   This function registers a type in the QML system with the name *qmlName*, in the library imported from *uri* having the version number composed from *versionMajor* and *versionMinor*. The type is defined by the QML file located at *url*. The url must be an absolute URL, i.e. url.isRelative() == false.

    Normally QML files can be loaded as types directly from other QML files, or using a qmldir file. This function allows registration of files to types from C++ code, such as when the type mapping needs to be procedurally determined at startup.

    Returns -1 if the registration was not successful.

---

qmlRegisterType(type, str, int, int, name: str = None, attachedProperties: type = None) → int
:   TODO

---

qmlRegisterTypeNotAvailable(str, int, int, str, str|None) → int
:   TODO

---

qmlRegisterUncreatableMetaObject([QMetaObject](../qtcore/qmetaobject.html), str, int, int, str, str|None) → int
:   TODO

---

qmlRegisterUncreatableType(type, str, int, int, str|None, qmlName: str = None) → int
:   TODO

---

qmlTypeId(str, int, int, str) → int
:   Returns the QML type id of a type that was registered with the name *qmlName* in a particular *uri* and a version specified in *versionMajor* and *versionMinor*.

    This function returns the same value as the QML type registration functions such as [qmlRegisterType()](#qmlRegisterType) and [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

    If *qmlName*, *uri* and *versionMajor* match a registered type, but the specified minor version in *versionMinor* is higher, then the id of the type with the closest minor version is returned.

    Returns -1 if no matching type was found or one of the given parameters was invalid.

    **Note:** : qmlTypeId tries to make modules available, even if they were not accessed by any engine yet. This can introduce overhead the first time a module is accessed. Trying to find types from a module which does not exist always introduces this overhead.

    See also

    QML\_ELEMENT, QML\_NAMED\_ELEMENT, QML\_SINGLETON, [qmlRegisterType()](#qmlRegisterType), [qmlRegisterSingletonType()](#qmlRegisterSingletonType).

### [Table of Contents](../../index.html)

* QtQml
  + [Classes](#classes)
  + [Functions](#functions)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QtQml

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Support for Cooperative Multi-inheritance {#support-for-cooperative-multi-inheritance}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Cooperative Multi-inheritance

# Support for Cooperative Multi-inheritance[¶](#support-for-cooperative-multi-inheritance "Link to this heading")

Note

This section is not about sub-classing from more that one Qt class.

Cooperative multi-inheritance is a technique for implementing classes that
inherit multiple super-classes - typically a main super-class and one or more
mixin classes that add additional behaviour. It makes it easy to add new
mixins at a later date to further extend the behavior, without needing to
change either the implementation of the class or any existing code that creates
an instance of the class.

The technique requires that all the super-class’s `__init__` methods follow
the same pattern in the way that they handle unrecognised keyword arguments and
use `super()` to invoke their own super-class’s `__init__` methods.

PyQt6’s classes follow this pattern.

See Raymond Hettinger’s [Python’s super() considered super!](http://rhettinger.wordpress.com/2011/05/26/super-considered-super/) blog
post for some more background on the subject.

As an example, let’s say we have a class that represents a person, and that a
person has a name. The following might be an initial implementation:

```
class Person(QObject):
    def __init__(self, name, parent=None)
        QObject.__init__(self, parent)

        self.name = name
```

An instance would normally be created in one of the following ways:

```
person = Person("Joe")
person = Person("Joe", some_parent)
```

This approach has some limitations:

* Only a sub-set of the [QObject](api/qtcore/qobject.html) API is exposed. For
  example you cannot set the value of a Qt property or connect a signal by
  passing appropriate keyword arguments to `Person.__init__`.
* Adding another class to `Person`’s list of super-classes means that its
  `__init__` implementation needs to be changed. If the new mixin takes
  non-optional arguments then every call to create a `Person` instance will
  need changing.

Consider this alternative implementation:

```
class Person(QObject):
    def __init__(self, name, **kwds):
        super().__init__(**kwds)

        self.name = name
```

The difference is that we only handle arguments that are used by the `Person`
class itself and we punt all the other arguments to the super-classes by
calling `super()`.

With this implementation an instance would normally be created in one of the
following ways:

```
person = Person("Joe")
person = Person("Joe", parent=some_parent)
```

Here the difference is that we are using keyword arguments to specify any
arguments that are not handled by the `Person` class itself. Note that we
could use keyword arguments for all arguments - whether or not you do so is
down to personal choice.

The limitations of the first implementation no longer apply. For example,
without any further changes we can also do this:

```
person = Person("Joe", destroyed=some_callable)
```

Let’s say we now want to extend the behaviour of the `Person` class by adding
a mixin that handles a person’s age. The implementation of the mixin would be
as follows:

```
class Age(object):
    def __init__(self, age=0, **kwds):
        super().__init__(**kwds)

        self.age = age
```

This follows a similar pattern to our `Person` implementation, but notice
that we have provided the `age` argument with a default value.

The following is our new `Person` implementation:

```
class Person(QObject, Age):
    def __init__(self, name, **kwds):
        super().__init__(**kwds)

        self.name = name
```

The only change we have had to make is to add `Age` to `Person`’s list of
super-classes. More importantly we do not need to change any call to create a
`Person` instance.

If we do want to create a `Person` instance with a non-default age then we
simply pass it as a keyword argument as follows:

```
person = Person("Joe", age=38)
```

This technique increases the use of keyword arguments - while this means a bit
more typing, it significantly increases the readability of application code.

#### Previous topic

[Integrating Python and QML](qml.html "previous chapter")

#### Next topic

[Things to be Aware Of](gotchas.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Cooperative Multi-inheritance

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Things to be Aware Of {#things-to-be-aware-of}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Things to be Aware Of

# Things to be Aware Of[¶](#things-to-be-aware-of "Link to this heading")

## TLS Support[¶](#tls-support "Link to this heading")

Support for Transport Layer Security (TLS) is increasingly important,
particularly on mobile platforms where an application is typically a front end
to a cloud-based server. As both Python and Qt implement different APIs that
support TLS, a PyQt application has a choice as to which to use. This is
particularly important when deploying an application as the support may have to
be included with, or built into, the application itself.

Ideally the TLS implementation provided by the target would be used (e.g.
CryptoAPI on Windows, Secure Transport on macOS and iOS). This would mean that
security updates, including certificate updates, would be handled by the vendor
of the target operating system and could be ignored by the application.
Unfortunately there is no common TLS API. The resolution to this problem is
the subject of [PEP 748](https://www.python.org/dev/peps/pep-0748) but that
has yet to be implemented.

Python uses OpenSSL v1.1.1 as its TLS implementation. On Windows and macOS the
standard Python binary installers include copies of the corresponding OpenSSL
libraries.

Qt has support for the native TLS implementation on macOS and iOS but on other
platforms (except for Linux) a deployed application must include it’s own
OpenSSL implementaion.

## Crashes On Exit[¶](#crashes-on-exit "Link to this heading")

When the Python interpreter leaves a *scope* (for example when it returns from
a function) it will potentially garbage collect all objects local to that
scope. The order in which it is done is, in effect, random. Theoretically
this can cause problems because it may mean that the C++ destructors of any
wrapped Qt instances are called in an order that Qt isn’t expecting and may
result in a crash. However, in practice, this is only likely to be a problem
when the application is terminating.

As a way of mitigating this possiblity PyQt6 ensures that the C++ destructors
of any [QObject](api/qtcore/qobject.html) instances owned by Python are invoked
before the destructor of any [QCoreApplication](api/qtcore/qcoreapplication.html) instance
is invoked. Note however that the order in which the
[QObject](api/qtcore/qobject.html) destructors are invoked is still random.

## Keyword Arguments[¶](#keyword-arguments "Link to this heading")

PyQt6 supports the use of keyword arguments for optional arguments. Although
the PyQt6 and Qt documentation may indicate that an argument has a particular
name, you may find that PyQt6 actually uses a different name. This is because
the name of an argument is not part of the Qt API and there is some
inconsistency in the way that similar arguments are named. Different versions
of Qt may use a different name for an argument which wouldn’t affect the C++
API but would break the Python API.

The docstrings that PyQt6 generates for all classes, functions and methods will
contain the correct argument names.

## Garbage Collection[¶](#garbage-collection "Link to this heading")

C++ does not garbage collect unreferenced class instances, whereas Python does.
In the following C++ fragment both colours exist even though the first can no
longer be referenced from within the program:

```
col = new QColor();
col = new QColor();
```

In the corresponding Python fragment, the first colour is destroyed when the
second is assigned to `col`:

```
col = QColor()
col = QColor()
```

In Python, each colour must be assigned to different names. Typically this is
done within class definitions, so the code fragment would be something like:

```
self.col1 = QColor()
self.col2 = QColor()
```

Sometimes a Qt class instance will maintain a pointer to another instance and
will eventually call the destructor of that second instance. The most common
example is that a [QObject](api/qtcore/qobject.html) (and any of its
sub-classes) keeps pointers to its children and will automatically call their
destructors. In these cases, the corresponding Python object will also keep a
reference to the corresponding child objects.

So, in the following Python fragment, the first
[QLabel](api/qtwidgets/qlabel.html) is not destroyed when the second is
assigned to `lab` because the parent [QWidget](api/qtwidgets/qwidget.html)
still has a reference to it:

```
parent = QWidget()
lab = QLabel("First label", parent)
lab = QLabel("Second label", parent)
```

## Multiple Inheritance[¶](#multiple-inheritance "Link to this heading")

It is not possible to define a new Python class that sub-classes from more than
one Qt class. The exception is classes specifically intended to act as mixin
classes such as those (like [QQmlParserStatus](api/qtqml/qqmlparserstatus.html)) that
implement Qt interfaces.

## Access to Protected Member Functions[¶](#access-to-protected-member-functions "Link to this heading")

When an instance of a C++ class is not created from Python it is not possible
to access the protected member functions of that instance. Attempts to do so
will raise a Python exception. Also, any Python methods corresponding to the
instance’s virtual member functions will never be called.

## `None` and `NULL`[¶](#none-and-null "Link to this heading")

Throughout PyQt6, the `None` value can be specified wherever `NULL` is
acceptable to the underlying C++ code.

Equally, `NULL` is converted to `None` whenever it is returned by the
underlying C++ code.

## Support for `void *`[¶](#support-for-void "Link to this heading")

PyQt6 (actually SIP) represents `void *` values as objects of type
[`voidptr`](api/sip/sip-module.html#PyQt6.sip.voidptr "PyQt6.sip.voidptr"). Such values are often used to pass the
addresses of external objects between different Python modules. To make this
easier, a Python integer (or anything that Python can convert to an integer)
can be used whenever a [`voidptr`](api/sip/sip-module.html#PyQt6.sip.voidptr "PyQt6.sip.voidptr") is expected.

A [`voidptr`](api/sip/sip-module.html#PyQt6.sip.voidptr "PyQt6.sip.voidptr") may be converted to a Python integer by using
the `int()` builtin function.

A [`voidptr`](api/sip/sip-module.html#PyQt6.sip.voidptr "PyQt6.sip.voidptr") may be converted to a Python string by using
its [`asstring()`](api/sip/sip-module.html#PyQt6.sip.voidptr.asstring "PyQt6.sip.voidptr.asstring") method. The
[`asstring()`](api/sip/sip-module.html#PyQt6.sip.voidptr.asstring "PyQt6.sip.voidptr.asstring") method takes an optional integer
argument which is the length of the data in bytes.

A [`voidptr`](api/sip/sip-module.html#PyQt6.sip.voidptr "PyQt6.sip.voidptr") may also be given a size (i.e. the size of the
block of memory that is pointed to) by calling its
[`setsize()`](api/sip/sip-module.html#PyQt6.sip.voidptr.setsize "PyQt6.sip.voidptr.setsize") method. If it has a size then it is also
able to support Python’s buffer protocol and behaves like a Python
[`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "(in Python v3.14)") object so that the block of memory can be treated as a
mutable list of bytes. It also means that the Python [`struct`](https://docs.python.org/3/library/struct.html#module-struct "(in Python v3.14)") module
can be used to unpack and pack binary data structures in memory, memory mapped
files or shared memory.

### [Table of Contents](index.html)

* Things to be Aware Of
  + [TLS Support](#tls-support)
  + [Crashes On Exit](#crashes-on-exit)
  + [Keyword Arguments](#keyword-arguments)
  + [Garbage Collection](#garbage-collection)
  + [Multiple Inheritance](#multiple-inheritance)
  + [Access to Protected Member Functions](#access-to-protected-member-functions)
  + [`None` and `NULL`](#none-and-null)
  + [Support for `void *`](#support-for-void)

#### Previous topic

[Support for Cooperative Multi-inheritance](multiinheritance.html "previous chapter")

#### Next topic

[Using Qt Designer](designer.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Things to be Aware Of

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Using Qt Designer {#using-qt-designer}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Using Qt Designer

# Using Qt Designer[¶](#using-qt-designer "Link to this heading")

Qt Designer is the Qt tool for designing and building graphical user
interfaces. It allows you to design widgets, dialogs or complete main windows
using on-screen forms and a simple drag-and-drop interface. It has the ability
to preview your designs to ensure they work as you intended, and to allow you
to prototype them with your users, before you have to write any code.

Qt Designer uses XML `.ui` files to store designs and does not generate any
code itself. Qt includes the `uic` utility that generates the C++ code that
creates the user interface. Qt also includes the `QUiLoader` class that
allows an application to load a `.ui` file and to create the corresponding
user interface dynamically.

PyQt6 does not wrap the `QUiLoader` class but instead includes the
[uic](api/uic/uic-module.html) Python module. Like `QUiLoader` this module can load
`.ui` files to create a user interface dynamically. Like the **uic**
utility it can also generate the Python code that will create the user
interface. PyQt6’s **pyuic6** utility is a command line interface to
the [uic](api/uic/uic-module.html) module. Both are described in detail in the
following sections.

## Using the Generated Code[¶](#using-the-generated-code "Link to this heading")

The code that is generated has an identical structure to that generated by Qt’s
`uic` and can be used in the same way.

The code is structured as a single class that is derived from the Python
`object` type. The name of the class is the name of the toplevel object set
in Designer with `Ui_` prepended. (In the C++ version the class is defined
in the `Ui` namespace.) We refer to this class as the *form class*.

The class contains a method called `setupUi()`. This takes a single argument
which is the widget in which the user interface is created. The type of this
argument (typically [QDialog](api/qtwidgets/qdialog.html),
[QWidget](api/qtwidgets/qwidget.html) or
[QMainWindow](api/qtwidgets/qmainwindow.html)) is set in Designer. We refer to
this type as the *Qt base class*.

In the following examples we assume that a `.ui` file has been created
containing a dialog and the name of the [QDialog](api/qtwidgets/qdialog.html)
object is `ImageDialog`. We also assume that the name of the file containing
the generated Python code is `ui_imagedialog.py`. The generated code can
then be used in a number of ways.

The first example shows the direct approach where we simply create a simple
application to create the dialog:

```
import sys
from PyQt6.QtWidgets import QApplication, QDialog
from ui_imagedialog import Ui_ImageDialog

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_ImageDialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec())
```

The second example shows the single inheritance approach where we sub-class
[QDialog](api/qtwidgets/qdialog.html) and set up the user interface in the
`__init__()` method:

```
from PyQt6.QtWidgets import QDialog
from ui_imagedialog import Ui_ImageDialog

class ImageDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_ImageDialog()
        self.ui.setupUi(self)

        # Make some local modifications.
        self.ui.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons.
        self.ui.okButton.clicked.connect(self.accept)
        self.ui.cancelButton.clicked.connect(self.reject)
```

The final example shows the multiple inheritance approach:

```
from PyQt6.QtGui import QDialog
from ui_imagedialog import Ui_ImageDialog

class ImageDialog(QDialog, Ui_ImageDialog):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Make some local modifications.
        self.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons.
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
```

For a full description see the Qt Designer Manual in the Qt Documentation.

## **pyuic6**[¶](#pyuic6 "Link to this heading")

The **pyuic6** utility is a command line interface to the
[uic](api/uic/uic-module.html) module. The command has the following syntax:

```
pyuic6 [options] .ui-file
```

If `.ui_file` is a file then that file is converted. If it is a
directory then every file with a `.ui` extension in the directory is
converted.

The full set of command line options is:

-h, --help[¶](#cmdoption-pyuic6-h "Link to this definition")
:   A help message is written to `stdout`.

-V, --version[¶](#cmdoption-pyuic6-V "Link to this definition")
:   The version number is written to `stdout`.

-d, --debug[¶](#cmdoption-pyuic6-d "Link to this definition")
:   Show debug output.

-i <N>, --indent <N>[¶](#cmdoption-pyuic6-i "Link to this definition")
:   The Python code is generated using an indentation of `<N>` spaces. If
    `<N>` is 0 then a tab is used. The default is 4.

-o <FILE>, --output <FILE>[¶](#cmdoption-pyuic6-o "Link to this definition")
:   If a single file is being converted then the Python code generated is
    written to the file `<FILE>`. If `<FILE>` is `-` then it is written
    to `stdout`. If a directory is converted then the generatee code is
    written to this directory.

-p, --preview[¶](#cmdoption-pyuic6-p "Link to this definition")
:   The GUI is created dynamically and displayed. No Python code is generated.

-w <N>, --max-workers <N>[¶](#cmdoption-pyuic6-w "Link to this definition")
:   A maximum of N worker processes are used when converting a directory. The
    default is 0.

-x, --execute[¶](#cmdoption-pyuic6-x "Link to this definition")
:   The generated Python code includes a small amount of additional code that
    creates and displays the GUI when it is executes as a standalone
    application.

Note that code generated by **pyuic6** is not guaranteed to be
compatible with earlier versions of PyQt6. However, it is guaranteed to be
compatible with later versions. If you have no control over the version of
PyQt6 the users of your application are using then you should run
**pyuic6**, or call [`compileUi()`](api/uic/uic-module.html#PyQt6.uic.compileUi "PyQt6.uic.compileUi"), as part of your
installation process. Another alternative would be to distribute the `.ui`
files (perhaps as part of a resource file) and have your application load them
dynamically.

## Writing Qt Designer Plugins[¶](#writing-qt-designer-plugins "Link to this heading")

Qt Designer can be extended by writing plugins. Normally this is done using
C++ but PyQt6 also allows you to write plugins in Python. Most of the time a
plugin is used to expose a custom widget to Designer so that it appears in
Designer’s widget box just like any other widget. It is possibe to change the
widget’s properties and to connect its signals and slots.

It is also possible to add new functionality to Designer. See the Qt
documentation for the full details. Here we will concentrate on describing
how to write custom widgets in Python.

The process of integrating Python custom widgets with Designer is very similar
to that used with widget written using C++. However, there are particular
issues that have to be addressed.

* Designer needs to have a C++ plugin that conforms to the interface defined by
  the `QDesignerCustomWidgetInterface` class. (If the plugin exposes more
  than one custom widget then it must conform to the interface defined by the
  `QDesignerCustomWidgetCollectionInterface` class.) In addition the plugin
  class must sub-class [QObject](api/qtcore/qobject.html) as well as the
  interface class. PyQt6 does not allow Python classes to be sub-classed from
  more than one Qt class.
* Designer can only connect Qt signals and slots. It has no understanding of
  Python signals or callables.
* Designer can only edit Qt properties that represent C++ types. It has no
  understanding of Python attributes or Python types.

PyQt6 provides the following components and features to resolve these issues as
simply as possible.

* PyQt6’s QtDesigner module includes additional classes (all of which have a
  `QPy` prefix) that are already sub-classed from the necessary Qt classes.
  This avoids the need to sub-class from more than one Qt class in Python. For
  example, where a C++ custom widget plugin would sub-class from
  [QObject](api/qtcore/qobject.html) and `QDesignerCustomWidgetInterface`, a
  Python custom widget plugin would instead sub-class from
  [QPyDesignerCustomWidgetPlugin](api/qtdesigner/qpydesignercustomwidgetplugin.html).
* PyQt6 installs a C++ plugin in Designer’s plugin directory. It conforms to
  the interface defined by the `QDesignerCustomWidgetCollectionInterface`
  class. It searches a configurable set of directories looking for Python
  plugins that implement a class sub-classed from
  [QPyDesignerCustomWidgetPlugin](api/qtdesigner/qpydesignercustomwidgetplugin.html). Each class
  that is found is instantiated and the instance created is added to the custom
  widget collection.

  The `PYQTDESIGNERPATH` environment variable specifies the set of
  directories to search for plugins. Directory names are separated by a path
  separator (a semi-colon on Windows and a colon on other platforms). If a
  directory name is empty (ie. there are consecutive path separators or a
  leading or trailing path separator) then a set of default directories is
  automatically inserted at that point. The default directories are the
  `python` subdirectory of each directory that Designer searches for its
  own plugins. If the environment variable is not set then only the default
  directories are searched. If a file’s basename does not end with `plugin`
  then it is ignored.
* A Python custom widget may define new Qt signals using
  pyqtSignal.
* A Python method may be defined as a new Qt slot by using the
  [pyqtSlot()](api/qtcore/qtcore-module.html#pyqtSlot) decorator.
* A new Qt property may be defined using the
  pyqtProperty
  function.

Note that the ability to define new Qt signals, slots and properties from
Python is potentially useful to plugins conforming to any plugin interface and
not just that used by Designer.

For a simple but complete and fully documented example of a custom widget that
defines new Qt signals, slots and properties, and its plugin, look in the
`examples/designer/plugins` directory of the PyQt6 source package. The
`widgets` subdirectory contains the `pydemo.py` custom widget and
the `python` subdirectory contains its `pydemoplugin.py` plugin.

### [Table of Contents](index.html)

* Using Qt Designer
  + [Using the Generated Code](#using-the-generated-code)
  + [**pyuic6**](#pyuic6)
  + [Writing Qt Designer Plugins](#writing-qt-designer-plugins)

#### Previous topic

[Things to be Aware Of](gotchas.html "previous chapter")

#### Next topic

[Support for Pickling](pickle.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Using Qt Designer

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QObject {#qobject}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QObject

# QObject[¶](#qobject "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QObject
:   Inherited by [Q3DGraphsWidgetItem](../qtgraphswidgets/q3dgraphswidgetitem.html), [Q3DObject](../qtdatavisualization/q3dobject.html), [Q3DScene](../qtdatavisualization/q3dscene.html), [Q3DScene](../qtgraphs/q3dscene.html), [Q3DTheme](../qtdatavisualization/q3dtheme.html), [QAbstract3DAxis](../qtdatavisualization/qabstract3daxis.html), [QAbstract3DAxis](../qtgraphs/qabstract3daxis.html), [QAbstract3DInputHandler](../qtdatavisualization/qabstract3dinputhandler.html), [QAbstract3DSeries](../qtdatavisualization/qabstract3dseries.html), [QAbstract3DSeries](../qtgraphs/qabstract3dseries.html), [QAbstractAnimation](../qt3danimation/qabstractanimation.html), [QAbstractAnimation](qabstractanimation.html), [QAbstractAspect](../qt3dcore/qabstractaspect.html), [QAbstractAxis](../qtcharts/qabstractaxis.html), [QAbstractAxis](../qtgraphs/qabstractaxis.html), [QAbstractDataProxy](../qtdatavisualization/qabstractdataproxy.html), [QAbstractDataProxy](../qtgraphs/qabstractdataproxy.html), [QAbstractEventDispatcher](qabstracteventdispatcher.html), [QAbstractItemDelegate](../qtwidgets/qabstractitemdelegate.html), [QAbstractItemModel](qabstractitemmodel.html), [QAbstractItemModelTester](../qttest/qabstractitemmodeltester.html), [QAbstractNetworkCache](../qtnetwork/qabstractnetworkcache.html), [QAbstractOAuth](../qtnetworkauth/qabstractoauth.html), [QAbstractOAuthReplyHandler](../qtnetworkauth/qabstractoauthreplyhandler.html), [QAbstractSeries](../qtcharts/qabstractseries.html), [QAbstractSeries](../qtgraphs/qabstractseries.html), [QAbstractState](../qtstatemachine/qabstractstate.html), [QAbstractTextDocumentLayout](../qtgui/qabstracttextdocumentlayout.html), [QAbstractTransition](../qtstatemachine/qabstracttransition.html), [QAccessibilityHints](../qtgui/qaccessibilityhints.html), [QAction](../qtgui/qaction.html), [QActionGroup](../qtgui/qactiongroup.html), [QAmbientSound](../qtspatialaudio/qambientsound.html), [QAnimationController](../qt3danimation/qanimationcontroller.html), [QAnimationGroup](../qt3danimation/qanimationgroup.html), [QAspectEngine](../qt3dcore/qaspectengine.html), [QAudioBufferInput](../qtmultimedia/qaudiobufferinput.html), [QAudioBufferOutput](../qtmultimedia/qaudiobufferoutput.html), [QAudioDecoder](../qtmultimedia/qaudiodecoder.html), [QAudioEngine](../qtspatialaudio/qaudioengine.html), [QAudioInput](../qtmultimedia/qaudioinput.html), [QAudioListener](../qtspatialaudio/qaudiolistener.html), [QAudioOutput](../qtmultimedia/qaudiooutput.html), [QAudioRoom](../qtspatialaudio/qaudioroom.html), [QAudioSink](../qtmultimedia/qaudiosink.html), [QAudioSource](../qtmultimedia/qaudiosource.html), [QAxBaseObject](../qaxcontainer/qaxbaseobject.html), [QBarModelMapper](../qtgraphs/qbarmodelmapper.html), [QBarSet](../qtcharts/qbarset.html), [QBarSet](../qtgraphs/qbarset.html), [QBluetoothDeviceDiscoveryAgent](../qtbluetooth/qbluetoothdevicediscoveryagent.html), [QBluetoothLocalDevice](../qtbluetooth/qbluetoothlocaldevice.html), [QBluetoothServer](../qtbluetooth/qbluetoothserver.html), [QBluetoothServiceDiscoveryAgent](../qtbluetooth/qbluetoothservicediscoveryagent.html), [QBoxSet](../qtcharts/qboxset.html), [QButtonGroup](../qtwidgets/qbuttongroup.html), [QCamera](../qtmultimedia/qcamera.html), [QCandlestickModelMapper](../qtcharts/qcandlestickmodelmapper.html), [QCandlestickSet](../qtcharts/qcandlestickset.html), [QClipboard](../qtgui/qclipboard.html), [QCompleter](../qtwidgets/qcompleter.html), [QCoreApplication](qcoreapplication.html), [QCustom3DItem](../qtdatavisualization/qcustom3ditem.html), [QCustom3DItem](../qtgraphs/qcustom3ditem.html), [QDataWidgetMapper](../qtwidgets/qdatawidgetmapper.html), [QDBusAbstractAdaptor](../qtdbus/qdbusabstractadaptor.html), [QDBusAbstractInterface](../qtdbus/qdbusabstractinterface.html), [QDBusPendingCallWatcher](../qtdbus/qdbuspendingcallwatcher.html), [QDBusServiceWatcher](../qtdbus/qdbusservicewatcher.html), [QDesignerFormEditorInterface](../qtdesigner/qdesignerformeditorinterface.html), [QDesignerFormWindowManagerInterface](../qtdesigner/qdesignerformwindowmanagerinterface.html), [QDnsLookup](../qtnetwork/qdnslookup.html), [QDrag](../qtgui/qdrag.html), [QEventLoop](qeventloop.html), [QExtensionFactory](../qtdesigner/qextensionfactory.html), [QExtensionManager](../qtdesigner/qextensionmanager.html), [QFileSelector](qfileselector.html), [QFileSystemWatcher](qfilesystemwatcher.html), [QGeoAreaMonitorSource](../qtpositioning/qgeoareamonitorsource.html), [QGeoPositionInfoSource](../qtpositioning/qgeopositioninfosource.html), [QGeoSatelliteInfoSource](../qtpositioning/qgeosatelliteinfosource.html), [QGesture](../qtwidgets/qgesture.html), [QGraphicsAnchor](../qtwidgets/qgraphicsanchor.html), [QGraphicsApiFilter](../qt3drender/qgraphicsapifilter.html), [QGraphicsEffect](../qtwidgets/qgraphicseffect.html), [QGraphicsObject](../qtwidgets/qgraphicsobject.html), [QGraphicsScene](../qtwidgets/qgraphicsscene.html), [QGraphicsTransform](../qtwidgets/qgraphicstransform.html), [QGraphsTheme](../qtgraphs/qgraphstheme.html), [QHBarModelMapper](../qtcharts/qhbarmodelmapper.html), [QHBoxPlotModelMapper](../qtcharts/qhboxplotmodelmapper.html), [QHelpEngineCore](../qthelp/qhelpenginecore.html), [QHelpFilterEngine](../qthelp/qhelpfilterengine.html), [QHelpSearchEngine](../qthelp/qhelpsearchengine.html), [QHelpSearchEngineCore](../qthelp/qhelpsearchenginecore.html), [QHPieModelMapper](../qtcharts/qhpiemodelmapper.html), [QHttpMultiPart](../qtnetwork/qhttpmultipart.html), [QHXYModelMapper](../qtcharts/qhxymodelmapper.html), [QImageCapture](../qtmultimedia/qimagecapture.html), [QInputDevice](../qtgui/qinputdevice.html), [QInputMethod](../qtgui/qinputmethod.html), [QIODevice](qiodevice.html), [QItemSelectionModel](qitemselectionmodel.html), [QJSEngine](../qtqml/qjsengine.html), [QKeyEvent](../qt3dinput/qkeyevent.html), [QLayout](../qtwidgets/qlayout.html), [QLegendMarker](../qtcharts/qlegendmarker.html), [QLibrary](qlibrary.html), [QLocalServer](../qtnetwork/qlocalserver.html), [QLowEnergyController](../qtbluetooth/qlowenergycontroller.html), [QLowEnergyService](../qtbluetooth/qlowenergyservice.html), [QMaskGenerator](../qtwebsockets/qmaskgenerator.html), [QMediaCaptureSession](../qtmultimedia/qmediacapturesession.html), [QMediaDevices](../qtmultimedia/qmediadevices.html), [QMediaPlayer](../qtmultimedia/qmediaplayer.html), [QMediaRecorder](../qtmultimedia/qmediarecorder.html), [QMimeData](qmimedata.html), [QMorphTarget](../qt3danimation/qmorphtarget.html), [QMouseEvent](../qt3dinput/qmouseevent.html), [QMovie](../qtgui/qmovie.html), [QNearFieldManager](../qtnfc/qnearfieldmanager.html), [QNearFieldTarget](../qtnfc/qnearfieldtarget.html), [QNetworkAccessManager](../qtnetwork/qnetworkaccessmanager.html), [QNetworkCookieJar](../qtnetwork/qnetworkcookiejar.html), [QNetworkInformation](../qtnetwork/qnetworkinformation.html), [QNode](../qt3dcore/qnode.html), [QObjectCleanupHandler](qobjectcleanuphandler.html), [QOffscreenSurface](../qtgui/qoffscreensurface.html), [QOpenGLContext](../qtgui/qopenglcontext.html), [QOpenGLContextGroup](../qtgui/qopenglcontextgroup.html), [QOpenGLDebugLogger](../qtopengl/qopengldebuglogger.html), [QOpenGLShader](../qtopengl/qopenglshader.html), [QOpenGLShaderProgram](../qtopengl/qopenglshaderprogram.html), [QOpenGLTimeMonitor](../qtopengl/qopengltimemonitor.html), [QOpenGLTimerQuery](../qtopengl/qopengltimerquery.html), [QOpenGLVertexArrayObject](../qtopengl/qopenglvertexarrayobject.html), [QPdfDocument](../qtpdf/qpdfdocument.html), [QPdfPageNavigator](../qtpdf/qpdfpagenavigator.html), [QPdfPageRenderer](../qtpdf/qpdfpagerenderer.html), [QPdfWriter](../qtgui/qpdfwriter.html), [QPickEvent](../qt3drender/qpickevent.html), [QPieModelMapper](../qtgraphs/qpiemodelmapper.html), [QPieSlice](../qtcharts/qpieslice.html), [QPieSlice](../qtgraphs/qpieslice.html), [QPluginLoader](qpluginloader.html), [QPyAbstractRange](qpyabstractrange.html), [QPyDesignerContainerExtension](../qtdesigner/qpydesignercontainerextension.html), [QPyDesignerCustomWidgetCollectionPlugin](../qtdesigner/qpydesignercustomwidgetcollectionplugin.html), [QPyDesignerCustomWidgetPlugin](../qtdesigner/qpydesignercustomwidgetplugin.html), [QPyDesignerMemberSheetExtension](../qtdesigner/qpydesignermembersheetextension.html), [QPyDesignerPropertySheetExtension](../qtdesigner/qpydesignerpropertysheetextension.html), [QPyDesignerTaskMenuExtension](../qtdesigner/qpydesignertaskmenuextension.html), [QQmlComponent](../qtqml/qqmlcomponent.html), [QQmlContext](../qtqml/qqmlcontext.html), [QQmlEngineExtensionPlugin](../qtqml/qqmlengineextensionplugin.html), [QQmlExpression](../qtqml/qqmlexpression.html), [QQmlExtensionPlugin](../qtqml/qqmlextensionplugin.html), [QQmlFileSelector](../qtqml/qqmlfileselector.html), [QQmlImageProviderBase](../qtqml/qqmlimageproviderbase.html), [QQmlPropertyMap](../qtqml/qqmlpropertymap.html), [QQuick3DObject](../qtquick3d/qquick3dobject.html), [QQuickImageResponse](../qtquick/qquickimageresponse.html), [QQuickItem](../qtquick/qquickitem.html), [QQuickItemGrabResult](../qtquick/qquickitemgrabresult.html), [QQuickRenderControl](../qtquick/qquickrendercontrol.html), [QQuickTextDocument](../qtquick/qquicktextdocument.html), [QQuickTextureFactory](../qtquick/qquicktexturefactory.html), [QQuickWebEngineProfile](../qtwebenginequick/qquickwebengineprofile.html), [QRemoteObjectAbstractPersistedStore](../qtremoteobjects/qremoteobjectabstractpersistedstore.html), [QRemoteObjectNode](../qtremoteobjects/qremoteobjectnode.html), [QRemoteObjectReplica](../qtremoteobjects/qremoteobjectreplica.html), [QRenderCapabilities](../qt3drender/qrendercapabilities.html), [QRenderCaptureReply](../qt3drender/qrendercapturereply.html), [QRestAccessManager](../qtnetwork/qrestaccessmanager.html), [QScreen](../qtgui/qscreen.html), [QScreenCapture](../qtmultimedia/qscreencapture.html), [QScroller](../qtwidgets/qscroller.html), [QSensor](../qtsensors/qsensor.html), [QSensorReading](../qtsensors/qsensorreading.html), [QSessionManager](../qtgui/qsessionmanager.html), [QSettings](qsettings.html), [QSGTexture](../qtquick/qsgtexture.html), [QSGTextureProvider](../qtquick/qsgtextureprovider.html), [QSharedMemory](qsharedmemory.html), [QShortcut](../qtgui/qshortcut.html), [QSignalMapper](qsignalmapper.html), [QSocketNotifier](qsocketnotifier.html), [QSoundEffect](../qtmultimedia/qsoundeffect.html), [QSpatialSound](../qtspatialaudio/qspatialsound.html), [QSqlDriver](../qtsql/qsqldriver.html), [QStencilOperationArguments](../qt3drender/qstenciloperationarguments.html), [QStencilTestArguments](../qt3drender/qstenciltestarguments.html), [QStyle](../qtwidgets/qstyle.html), [QStyleHints](../qtgui/qstylehints.html), [QSvgRenderer](../qtsvg/qsvgrenderer.html), [QSyntaxHighlighter](../qtgui/qsyntaxhighlighter.html), [QSystemTrayIcon](../qtwidgets/qsystemtrayicon.html), [QTcpServer](../qtnetwork/qtcpserver.html), [QTextDocument](../qtgui/qtextdocument.html), [QTextObject](../qtgui/qtextobject.html), [QTextToSpeech](../qttexttospeech/qtexttospeech.html), [QTextureWrapMode](../qt3drender/qtexturewrapmode.html), [QThread](qthread.html), [QThreadPool](qthreadpool.html), [QTimeLine](qtimeline.html), [QTimer](qtimer.html), [QTranslator](qtranslator.html), [QUndoGroup](../qtgui/qundogroup.html), [QUndoStack](../qtgui/qundostack.html), [QValidator](../qtgui/qvalidator.html), [QValue3DAxisFormatter](../qtdatavisualization/qvalue3daxisformatter.html), [QValue3DAxisFormatter](../qtgraphs/qvalue3daxisformatter.html), [QVBarModelMapper](../qtcharts/qvbarmodelmapper.html), [QVBoxPlotModelMapper](../qtcharts/qvboxplotmodelmapper.html), [QVideoFrameInput](../qtmultimedia/qvideoframeinput.html), [QVideoSink](../qtmultimedia/qvideosink.html), [QVPieModelMapper](../qtcharts/qvpiemodelmapper.html), [QVXYModelMapper](../qtcharts/qvxymodelmapper.html), [QWebChannel](../qtwebchannel/qwebchannel.html), [QWebChannelAbstractTransport](../qtwebchannel/qwebchannelabstracttransport.html), [QWebEngineClientHints](../qtwebenginecore/qwebengineclienthints.html), [QWebEngineContextMenuRequest](../qtwebenginecore/qwebenginecontextmenurequest.html), [QWebEngineCookieStore](../qtwebenginecore/qwebenginecookiestore.html), [QWebEngineDownloadRequest](../qtwebenginecore/qwebenginedownloadrequest.html), [QWebEngineExtensionManager](../qtwebenginecore/qwebengineextensionmanager.html), [QWebEngineHistory](../qtwebenginecore/qwebenginehistory.html), [QWebEngineNavigationRequest](../qtwebenginecore/qwebenginenavigationrequest.html), [QWebEngineNewWindowRequest](../qtwebenginecore/qwebenginenewwindowrequest.html), [QWebEngineNotification](../qtwebenginecore/qwebenginenotification.html), [QWebEnginePage](../qtwebenginecore/qwebenginepage.html), [QWebEngineProfile](../qtwebenginecore/qwebengineprofile.html), [QWebEngineUrlRequestInterceptor](../qtwebenginecore/qwebengineurlrequestinterceptor.html), [QWebEngineUrlRequestJob](../qtwebenginecore/qwebengineurlrequestjob.html), [QWebEngineUrlSchemeHandler](../qtwebenginecore/qwebengineurlschemehandler.html), [QWebEngineWebAuthUxRequest](../qtwebenginecore/qwebenginewebauthuxrequest.html), [QWebSocket](../qtwebsockets/qwebsocket.html), [QWebSocketServer](../qtwebsockets/qwebsocketserver.html), [QWheelEvent](../qt3dinput/qwheelevent.html), [QWidget](../qtwidgets/qwidget.html), [QWindow](../qtgui/qwindow.html), [QWindowCapture](../qtmultimedia/qwindowcapture.html), [QWinEventNotifier](qwineventnotifier.html), [QXYModelMapper](../qtgraphs/qxymodelmapper.html).

## Description[¶](#description "Link to this heading")

The QObject class is the base class of all Qt objects.

QObject is the heart of the Qt [Object Model](https://doc.qt.io/qt-6/object.html). The central feature in this model is a very powerful mechanism for seamless object communication called [signals and slots](https://doc.qt.io/qt-6/signalsandslots.html). You can connect a signal to a slot with connect() and destroy the connection with [disconnect()](#disconnect). To avoid never ending notification loops you can temporarily block signals with [blockSignals()](#blockSignals). The protected functions [connectNotify()](#connectNotify) and [disconnectNotify()](#disconnectNotify) make it possible to track connections.

QObjects organize themselves in [object trees](https://doc.qt.io/qt-6/objecttrees.html). When you create a QObject with another object as parent, the object will automatically add itself to the parent’s [children()](#children) list. The parent takes ownership of the object; i.e., it will automatically delete its children in its destructor. You can look for an object by name and optionally type using [findChild()](#findChild) or [findChildren()](#findChildren).

Every object has an [objectName()](#objectName) and its class name can be found via the corresponding [metaObject()](#metaObject) (see [className()](qmetaobject.html#className)). You can determine whether the object’s class inherits another class in the QObject inheritance hierarchy by using the [inherits()](#inherits) function.

When an object is deleted, it emits a [destroyed](#destroyed) signal. You can catch this signal to avoid dangling references to QObjects.

QObjects can receive events through [event()](#event) and filter the events of other objects. See [installEventFilter()](#installEventFilter) and [eventFilter()](#eventFilter) for details. A convenience handler, [childEvent()](#childEvent), can be reimplemented to catch child events.

Last but not least, QObject provides the basic timer support in Qt; see QChronoTimer for high-level support for timers.

Notice that the Q\_OBJECT macro is mandatory for any object that implements signals, slots or properties. You also need to run the Meta Object Compiler on the source file. We strongly recommend the use of this macro in all subclasses of QObject regardless of whether or not they actually use signals, slots and properties, since failure to do so may lead certain functions to exhibit strange behavior.

All Qt widgets inherit QObject. The convenience function [isWidgetType()](#isWidgetType) returns whether an object is actually a widget. It is much faster than qobject\_cast<[QWidget](../qtwidgets/qwidget.html) \*>(*obj*) or *obj*->[inherits()](#inherits)(”[QWidget](../qtwidgets/qwidget.html)”).

Some QObject functions, e.g. [children()](#children), return a QObjectList. QObjectList is a typedef for QList<QObject \*>.

### Thread Affinity[¶](#thread-affinity "Link to this heading")

A QObject instance is said to have a *thread affinity*, or that it *lives* in a certain thread. When a QObject receives a [QueuedConnection](qt.html#ConnectionType-QueuedConnection) or a [posted event](https://doc.qt.io/qt-6/eventsandfilters.html#sending-events), the slot or event handler will run in the thread that the object lives in.

**Note:** If a QObject has no thread affinity (that is, if [thread()](#thread) returns zero), or if it lives in a thread that has no running event loop, then it cannot receive queued signals or posted events.

By default, a QObject lives in the thread in which it is created. An object’s thread affinity can be queried using [thread()](#thread) and changed using [moveToThread()](#moveToThread).

All QObjects must live in the same thread as their parent. Consequently:

* [setParent()](#setParent) will fail if the two QObjects involved live in different threads.
* When a QObject is moved to another thread, all its children will be automatically moved too.
* [moveToThread()](#moveToThread) will fail if the QObject has a parent.
* If QObjects are created within [run()](qthread.html#run), they cannot become children of the [QThread](qthread.html) object because the [QThread](qthread.html) does not live in the thread that calls [run()](qthread.html#run).

**Note:** A QObject’s member variables *do not* automatically become its children. The parent-child relationship must be set by either passing a pointer to the child’s QObject, or by calling [setParent()](#setParent). Without this step, the object’s member variables will remain in the old thread when [moveToThread()](#moveToThread) is called.

### No Copy Constructor or Assignment Operator[¶](#no-copy-constructor-or-assignment-operator "Link to this heading")

QObject has neither a copy constructor nor an assignment operator. This is by design. Actually, they are declared, but in a `private` section with the macro Q\_DISABLE\_COPY(). In fact, all Qt classes derived from QObject (direct or indirect) use this macro to declare their copy constructor and assignment operator to be private. The reasoning is found in the discussion on [Identity vs Value](https://doc.qt.io/qt-6/object.html#qt-objects-identity-vs-value) on the Qt [Object Model](https://doc.qt.io/qt-6/object.html) page.

The main consequence is that you should use pointers to QObject (or to your QObject subclass) where you might otherwise be tempted to use your QObject subclass as a value. For example, without a copy constructor, you can’t use a subclass of QObject as the value to be stored in one of the container classes. You must store pointers.

### Auto-Connection[¶](#auto-connection "Link to this heading")

Qt’s meta-object system provides a mechanism to automatically connect signals and slots between QObject subclasses and their children. As long as objects are defined with suitable object names, and slots follow a simple naming convention, this connection can be performed at run-time by the [connectSlotsByName()](qmetaobject.html#connectSlotsByName) function.

uic generates code that invokes this function to enable auto-connection to be performed between widgets on forms created with *Qt Widgets Designer*. More information about using auto-connection with *Qt Widgets Designer* is given in the [Using a Designer UI File in Your Application](https://doc.qt.io/qt-6/designer-using-a-ui-file.html) section of the [Qt Widgets Designer](https://doc.qt.io/qt-6/qtdesigner-manual.html) manual.

### Dynamic Properties[¶](#dynamic-properties "Link to this heading")

Dynamic properties can be added to and removed from QObject instances at run-time. Dynamic properties do not need to be declared at compile-time, yet they provide the same advantages as static properties and are manipulated using the same API - using [property()](#property) to read them and [setProperty()](#setProperty) to write them.

Dynamic properties are supported by [Qt Widgets Designer](https://doc.qt.io/qt-6/designer-widget-mode.html#the-property-editor), and both standard Qt widgets and user-created forms can be given dynamic properties.

### Internationalization (I18n)[¶](#internationalization-i18n "Link to this heading")

All QObject subclasses support Qt’s translation features, making it possible to translate an application’s user interface into different languages.

To make user-visible text translatable, it must be wrapped in calls to the [tr()](#tr) function. This is explained in detail in the Writing Source Code for Translation document.

See also

[QMetaObject](qmetaobject.html), QPointer, [QObjectCleanupHandler](qobjectcleanuphandler.html), Q\_DISABLE\_COPY(), [Object Trees & Ownership](https://doc.qt.io/qt-6/objecttrees.html).

## Attributes[¶](#attributes "Link to this heading")

staticMetaObject: [QMetaObject](qmetaobject.html)
:   This is a read-only class attribute.

    This variable stores the meta-object for the class.

    A meta-object contains information about a class that inherits QObject, e.g. class name, superclass name, properties, signals and slots. Every class that contains the Q\_OBJECT macro will also have a meta-object.

    The meta-object information is required by the signal/slot connection mechanism and the property system. The [inherits()](#inherits) function also makes use of the meta-object.

    If you have a pointer to an object, you can use [metaObject()](#metaObject) to retrieve the meta-object associated with that object.

    Example:

    ```
    # QPushButton::staticMetaObject.className();  // returns "QPushButton"

    # QObject *obj = new QPushButton;
    # obj->metaObject()->className();             // returns "QPushButton"
    ```

    See also

    [metaObject()](#metaObject).

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_(parent: QObject = None)
:   Constructs an object with parent object *parent*.

    The parent of an object may be viewed as the object’s owner. For instance, a [QDialog](../qtwidgets/qdialog.html) is the parent of the OK and Cancel buttons it contains.

    The destructor of a parent object destroys all child objects.

    Setting *parent* to `nullptr` constructs an object with no parent. If the object is a widget, it will become a top-level window.

    See also

    [parent()](#parent), [findChild()](#findChild), [findChildren()](#findChildren).

---

blockSignals(bool) → bool
:   If *block* is true, signals emitted by this object are blocked (i.e., emitting a signal will not invoke anything connected to it). If *block* is false, no such blocking will occur.

    The return value is the previous value of [signalsBlocked()](#signalsBlocked).

    Note that the [destroyed](#destroyed) signal will be emitted even if the signals for this object have been blocked.

    Signals emitted while being blocked are not buffered.

    See also

    [signalsBlocked()](#signalsBlocked), [QSignalBlocker](qsignalblocker.html).

---

childEvent([QChildEvent](qchildevent.html))
:   This event handler can be reimplemented in a subclass to receive child events. The event is passed in the *event* parameter.

    [ChildAdded](qevent.html#Type-ChildAdded) and [ChildRemoved](qevent.html#Type-ChildRemoved) events are sent to objects when children are added or removed. In both cases you can only rely on the child being a QObject, or if [isWidgetType()](#isWidgetType) returns `true`, a [QWidget](https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget). (This is because, in the [ChildAdded](qevent.html#Type-ChildAdded) case, the child is not yet fully constructed, and in the [ChildRemoved](qevent.html#Type-ChildRemoved) case it might have been destructed already).

    [ChildPolished](qevent.html#Type-ChildPolished) events are sent to widgets when children are polished, or when polished children are added. If you receive a child polished event, the child’s construction is usually completed. However, this is not guaranteed, and multiple polish events may be delivered during the execution of a widget’s constructor.

    For every child widget, you receive one [ChildAdded](qevent.html#Type-ChildAdded) event, zero or more [ChildPolished](qevent.html#Type-ChildPolished) events, and one [ChildRemoved](qevent.html#Type-ChildRemoved) event.

    The [ChildPolished](qevent.html#Type-ChildPolished) event is omitted if a child is removed immediately after it is added. If a child is polished several times during construction and destruction, you may receive several child polished events for the same child, each time with a different virtual table.

    See also

    [event()](#event).

---

children() → list[QObject]
:   Returns a list of child objects. The QObjectList class is defined in the `<QObject>` header file as the following:

    The first child added is the first object in the list and the last child added is the last object in the list, i.e. new children are appended at the end.

    Note that the list order changes when [QWidget](../qtwidgets/qwidget.html) children are [raise\_()](../qtwidgets/qwidget.html#raise_) or [lower()](../qtwidgets/qwidget.html#lower). A widget that is raised becomes the last object in the list, and a widget that is lowered becomes the first object in the list.

    See also

    [findChild()](#findChild), [findChildren()](#findChildren), [parent()](#parent), [setParent()](#setParent).

---

connectNotify([QMetaMethod](qmetamethod.html))
:   This virtual function is called when something has been connected to *signal* in this object.

    If you want to compare *signal* with a specific signal, you can use QMetaMethod::fromSignal() as follows:

    ```
    # if (signal == QMetaMethod::fromSignal(&MyObject::valueChanged)) {
    #     // signal is valueChanged
    # }
    ```

    **Warning:** This function violates the object-oriented principle of modularity. However, it might be useful when you need to perform expensive initialization only if something is connected to a signal.

    **Warning:** This function is called from the thread which performs the connection, which may be a different thread from the thread in which this object lives. This function may also be called with a QObject internal mutex locked. It is therefore not allowed to re-enter any QObject functions, including [isSignalConnected()](#isSignalConnected), from your reimplementation. If you lock a mutex in your reimplementation, make sure that you don’t call QObject functions with that mutex held in other places or it will result in a deadlock.

    See also

    connect(), [disconnectNotify()](#disconnectNotify).

---

customEvent([QEvent](qevent.html))
:   This event handler can be reimplemented in a subclass to receive custom events. Custom events are user-defined events with a type value at least as large as the [User](qevent.html#Type-User) item of the [Type](qevent.html#Type) enum, and is typically a [QEvent](qevent.html) subclass. The event is passed in the *event* parameter.

    See also

    [event()](#event), [QEvent](qevent.html).

---

deleteLater()
:   Schedules this object for deletion.

    The object will be deleted when control returns to the event loop. If the event loop is not running when this function is called (e.g. deleteLater() is called on an object before [exec()](qcoreapplication.html#exec)), the object will be deleted once the event loop is started. If deleteLater() is called after the main event loop has stopped, the object will not be deleted. If deleteLater() is called on an object that lives in a thread with no running event loop, the object will be destroyed when the thread finishes.

    A common pattern when using a worker `QObject` in a `QThread` is to connect the thread’s `finished()` signal to the worker’s `deleteLater()` slot to ensure it is safely deleted:

    ```
    connect(thread, &QThread::finished, worker, &QObject::deleteLater);
    ```

    Note that entering and leaving a new event loop (e.g., by opening a modal dialog) will *not* perform the deferred deletion; for the object to be deleted, the control must return to the event loop from which deleteLater() was called. This does not apply to objects deleted while a previous, nested event loop was still running: the Qt event loop will delete those objects as soon as the new nested event loop starts.

    In situations where Qt is not driving the event dispatcher via e.g. [exec()](qcoreapplication.html#exec) or [exec()](qeventloop.html#exec), deferred deletes will not be processed automatically. To ensure deferred deletion in this scenario, the following workaround can be used:

    ```
    const auto *eventDispatcher = QThread::currentThread()->eventDispatcher();
    QObject::connect(eventDispatcher, &QAbstractEventDispatcher::aboutToBlock,
        QThread::currentThread(), []{
            if (QThread::currentThread()->loopLevel() == 0)
                QCoreApplication::sendPostedEvents(nullptr, QEvent::DeferredDelete);
        }
    );
    ```

    See also

    [destroyed](#destroyed), QPointer.

---

disconnect()
:   TODO

---

@staticmethod disconnect([Connection](qmetaobject-connection.html)) → bool
:   Disconnect a connection.

    If the *connection* is invalid or has already been disconnected, do nothing and return false.

    See also

    connect().

---

disconnectNotify([QMetaMethod](qmetamethod.html))
:   This virtual function is called when something has been disconnected from *signal* in this object.

    See [connectNotify()](#connectNotify) for an example of how to compare *signal* with a specific signal.

    If all signals were disconnected from this object (e.g., the signal argument to [disconnect()](#disconnect) was `nullptr`), disconnectNotify() is only called once, and the *signal* will be an invalid [QMetaMethod](qmetamethod.html) ([isValid()](qmetamethod.html#isValid) returns `false`).

    **Warning:** This function violates the object-oriented principle of modularity. However, it might be useful for optimizing access to expensive resources.

    **Warning:** This function is called from the thread which performs the disconnection, which may be a different thread from the thread in which this object lives. This function may also be called with a QObject internal mutex locked. It is therefore not allowed to re-enter any QObject functions, including [isSignalConnected()](#isSignalConnected), from your reimplementation. If you lock a mutex in your reimplementation, make sure that you don’t call QObject functions with that mutex held in other places or it will result in a deadlock.

    See also

    [disconnect()](#disconnect), [connectNotify()](#connectNotify).

---

dumpObjectInfo()
:   Dumps information about signal connections, etc. for this object to the debug output.

    **Note:** before Qt 5.9, this function was not const.

    See also

    [dumpObjectTree()](#dumpObjectTree).

---

dumpObjectTree()
:   Dumps a tree of children to the debug output.

    **Note:** before Qt 5.9, this function was not const.

    See also

    [dumpObjectInfo()](#dumpObjectInfo).

---

dynamicPropertyNames() → list[[QByteArray](qbytearray.html)]
:   Returns the names of all properties that were dynamically added to the object using [setProperty()](#setProperty).

---

event([QEvent](qevent.html)) → bool
:   This virtual function receives events to an object and should return true if the event *e* was recognized and processed.

    The event() function can be reimplemented to customize the behavior of an object.

    Make sure you call the parent event class implementation for all the events you did not handle.

    Example:

    ```
    # class MyClass : public QWidget
    # {
    #     Q_OBJECT

    # public:
    #     MyClass(QWidget *parent = nullptr);
    #     ~MyClass();

    #     bool event(QEvent* ev) override
    #     {
    #         if (ev->type() == QEvent::PolishRequest) {
    #             // overwrite handling of PolishRequest if any
    #             doThings();
    #             return true;
    #         } else  if (ev->type() == QEvent::Show) {
    #             // complement handling of Show if any
    #             doThings2();
    #             QWidget::event(ev);
    #             return true;
    #         }
    #         // Make sure the rest of events are handled
    #         return QWidget::event(ev);
    #     }
    # };
    ```

    See also

    [installEventFilter()](#installEventFilter), [timerEvent()](#timerEvent), [sendEvent()](qcoreapplication.html#sendEvent), [postEvent()](qcoreapplication.html#postEvent).

---

eventFilter(QObject, [QEvent](qevent.html)) → bool
:   Filters events if this object has been installed as an event filter for the *watched* object.

    In your reimplementation of this function, if you want to filter the *event* out, i.e. stop it being handled further, return true; otherwise return false.

    Example:

    ```
    # class MainWindow : public QMainWindow
    # {
    # public:
    #     MainWindow();

    # protected:
    #     bool eventFilter(QObject *obj, QEvent *ev) override;

    # private:
    #     QTextEdit *textEdit;
    # };

    # MainWindow::MainWindow()
    # {
    #     textEdit = new QTextEdit;
    #     setCentralWidget(textEdit);

    #     textEdit->installEventFilter(this);
    # }

    # bool MainWindow::eventFilter(QObject *obj, QEvent *event)
    # {
    #     if (obj == textEdit) {
    #         if (event->type() == QEvent::KeyPress) {
    #             QKeyEvent *keyEvent = static_cast<QKeyEvent*>(event);
    #             qDebug() << "Ate key press" << keyEvent->key();
    #             return true;
    #         } else {
    #             return false;
    #         }
    #     } else {
    #         // pass the event on to the parent class
    #         return QMainWindow::eventFilter(obj, event);
    #     }
    # }
    ```

    Notice in the example above that unhandled events are passed to the base class’s eventFilter() function, since the base class might have reimplemented eventFilter() for its own internal purposes.

    Some events, such as [ShortcutOverride](qevent.html#Type-ShortcutOverride) must be explicitly accepted (by calling [accept()](qevent.html#accept) on them) in order to prevent propagation.

    **Warning:** If you delete the receiver object in this function, be sure to return true. Otherwise, Qt will forward the event to the deleted object and the program might crash.

    See also

    [installEventFilter()](#installEventFilter).

---

findChild(type[QObjectT], name: str|None = '', options: [FindChildOption](qt.html#FindChildOption) = [FindChildrenRecursively](qt.html#FindChildOption-FindChildrenRecursively)) → QObjectT
:   TODO

---

findChild(tuple[type[QObjectT], ...], name: str|None = '', options: [FindChildOption](qt.html#FindChildOption) = [FindChildrenRecursively](qt.html#FindChildOption-FindChildrenRecursively)) → QObjectT
:   TODO

---

findChildren(type[QObjectT], name: str|None = '', options: [FindChildOption](qt.html#FindChildOption) = [FindChildrenRecursively](qt.html#FindChildOption-FindChildrenRecursively)) → list[QObjectT]
:   TODO

---

findChildren(tuple[type[QObjectT], ...], name: str|None = '', options: [FindChildOption](qt.html#FindChildOption) = [FindChildrenRecursively](qt.html#FindChildOption-FindChildrenRecursively)) → list[QObjectT]
:   TODO

---

findChildren(type[QObjectT], [QRegularExpression](qregularexpression.html), options: [FindChildOption](qt.html#FindChildOption) = [FindChildrenRecursively](qt.html#FindChildOption-FindChildrenRecursively)) → list[QObjectT]
:   TODO

---

findChildren(tuple[type[QObjectT], ...], [QRegularExpression](qregularexpression.html), options: [FindChildOption](qt.html#FindChildOption) = [FindChildrenRecursively](qt.html#FindChildOption-FindChildrenRecursively)) → list[QObjectT]
:   TODO

---

\_\_getattr\_\_(str) → Any
:   TODO

---

inherits(str) → bool
:   Returns `true` if this object is an instance of a class that inherits *className* or a QObject subclass that inherits *className*; otherwise returns `false`.

    A class is considered to inherit itself.

    Example:

    ```
    # QTimer *timer = new QTimer;         // QTimer inherits QObject
    # timer->inherits("QTimer");          // returns true
    # timer->inherits("QObject");         // returns true
    # timer->inherits("QAbstractButton"); // returns false

    # // QVBoxLayout inherits QObject and QLayoutItem
    # QVBoxLayout *layout = new QVBoxLayout;
    # layout->inherits("QObject");        // returns true
    # layout->inherits("QLayoutItem");    // returns true (even though QLayoutItem is not a QObject)
    ```

    If you need to determine whether an object is an instance of a particular class for the purpose of casting it, consider using qobject\_cast<Type \*>(object) instead.

    See also

    [metaObject()](#metaObject), qobject\_cast().

---

installEventFilter(QObject)
:   Installs an event filter *filterObj* on this object. For example:

    ```
    # monitoredObj->installEventFilter(filterObj);
    ```

    An event filter is an object that receives all events that are sent to this object. The filter can either stop the event or forward it to this object. The event filter *filterObj* receives events via its [eventFilter()](#eventFilter) function. The [eventFilter()](#eventFilter) function must return true if the event should be filtered, (i.e. stopped); otherwise it must return false.

    If multiple event filters are installed on a single object, the filter that was installed last is activated first.

    If *filterObj* has already been installed for this object, this function moves it so it acts as if it was installed last.

    Here’s a `KeyPressEater` class that eats the key presses of its monitored objects:

    ```
    # class KeyPressEater : public QObject
    # {
    #     Q_OBJECT
    #     ...

    # protected:
    #     bool eventFilter(QObject *obj, QEvent *event) override;
    # };

    # bool KeyPressEater::eventFilter(QObject *obj, QEvent *event)
    # {
    #     if (event->type() == QEvent::KeyPress) {
    #         QKeyEvent *keyEvent = static_cast<QKeyEvent *>(event);
    #         qDebug("Ate key press %d", keyEvent->key());
    #         return true;
    #     } else {
    #         // standard event processing
    #         return QObject::eventFilter(obj, event);
    #     }
    # }
    ```

    And here’s how to install it on two widgets:

    ```
    # KeyPressEater *keyPressEater = new KeyPressEater(this);
    # QPushButton *pushButton = new QPushButton(this);
    # QListView *listView = new QListView(this);

    # pushButton->installEventFilter(keyPressEater);
    # listView->installEventFilter(keyPressEater);
    ```

    The [QShortcut](../qtgui/qshortcut.html) class, for example, uses this technique to intercept shortcut key presses.

    **Warning:** If you delete the receiver object in your [eventFilter()](#eventFilter) function, be sure to return true. If you return false, Qt sends the event to the deleted object and the program will crash.

    Note that the filtering object must be in the same thread as this object. If *filterObj* is in a different thread, this function does nothing. If either *filterObj* or this object are moved to a different thread after calling this function, the event filter will not be called until both objects have the same thread affinity again (it is *not* removed).

    See also

    [removeEventFilter()](#removeEventFilter), [eventFilter()](#eventFilter), [event()](#event).

---

isQmlExposed() → bool
:   Returns whether the object has been created by the QML engine or ownership has been explicitly set via [setObjectOwnership()](../qtqml/qjsengine.html#setObjectOwnership).

---

isQuickItemType() → bool
:   Returns `true` if the object is a [QQuickItem](../qtquick/qquickitem.html); otherwise returns `false`.

    Calling this function is equivalent to calling `inherits("QQuickItem")`, except that it is much faster.

---

isSignalConnected([QMetaMethod](qmetamethod.html)) → bool
:   Returns `true` if the *signal* is connected to at least one receiver, otherwise returns `false`.

    *signal* must be a signal member of this object, otherwise the behaviour is undefined.

    ```
    # static const QMetaMethod valueChangedSignal = QMetaMethod::fromSignal(&MyObject::valueChanged);
    # if (isSignalConnected(valueChangedSignal)) {
    #     QByteArray data;
    #     data = get_the_value();       // expensive operation
    #     emit valueChanged(data);
    # }
    ```

    As the code snippet above illustrates, you can use this function to avoid expensive operations or emitting a signal that nobody listens to.

    **Warning:** In a multithreaded application, consecutive calls to this function are not guaranteed to yield the same results.

    **Warning:** This function violates the object-oriented principle of modularity. In particular, this function must not be called from an override of [connectNotify()](#connectNotify) or [disconnectNotify()](#disconnectNotify), as those might get called from any thread.

    See also

    [receivers()](#receivers).

---

isWidgetType() → bool
:   Returns `true` if the object is a widget; otherwise returns `false`.

    Calling this function is equivalent to calling `inherits("QWidget")`, except that it is much faster.

---

isWindowType() → bool
:   Returns `true` if the object is a window; otherwise returns `false`.

    Calling this function is equivalent to calling `inherits("QWindow")`, except that it is much faster.

---

killTimer(int)
:   Kills the timer with timer identifier, *id*.

    The timer identifier is returned by [startTimer()](#startTimer) when a timer event is started.

    See also

    [timerEvent()](#timerEvent), [startTimer()](#startTimer).

---

metaObject() → [QMetaObject](qmetaobject.html)
:   Returns a pointer to the meta-object of this object.

    A meta-object contains information about a class that inherits QObject, e.g. class name, superclass name, properties, signals and slots. Every QObject subclass that contains the Q\_OBJECT macro will have a meta-object.

    The meta-object information is required by the signal/slot connection mechanism and the property system. The [inherits()](#inherits) function also makes use of the meta-object.

    If you have no pointer to an actual object instance but still want to access the meta-object of a class, you can use staticMetaObject.

    Example:

    ```
    # QObject *obj = new QPushButton;
    # obj->metaObject()->className();             // returns "QPushButton"

    # QPushButton::staticMetaObject.className();  // returns "QPushButton"
    ```

    See also

    staticMetaObject.

---

moveToThread([QThread](qthread.html))
:   Changes the thread affinity for this object and its children and returns `true` on success. The object cannot be moved if it has a parent. Event processing will continue in the *targetThread*.

    To move an object to the main thread, use QApplication::instance() to retrieve a pointer to the current application, and then use QApplication::thread() to retrieve the thread in which the application lives. For example:

    ```
    # myObject->moveToThread(QApplication::instance()->thread());
    ```

    If *targetThread* is `nullptr`, all event processing for this object and its children stops, as they are no longer associated with any thread.

    Note that all active timers for the object will be reset. The timers are first stopped in the current thread and restarted (with the same interval) in the *targetThread*. As a result, constantly moving an object between threads can postpone timer events indefinitely.

    A [ThreadChange](qevent.html#Type-ThreadChange) event is sent to this object just before the thread affinity is changed. You can handle this event to perform any special processing. Note that any new events that are posted to this object will be handled in the *targetThread*, provided it is not `nullptr`: when it is `nullptr`, no event processing for this object or its children can happen, as they are no longer associated with any thread.

    **Warning:** This function is *not* thread-safe; the current thread must be same as the current thread affinity. In other words, this function can only “push” an object from the current thread to another thread, it cannot “pull” an object from any arbitrary thread to the current thread. There is one exception to this rule however: objects with no thread affinity can be “pulled” to the current thread.

    In Qt versions prior to 6.7, this function had no return value (`void`).

    See also

    [thread()](#thread).

---

objectName() → str
:   See also

    [setObjectName()](#setObjectName).

---

parent() → QObject
:   Returns a pointer to the parent object.

    See also

    [setParent()](#setParent), [children()](#children).

---

property(str) → Any
:   Returns the value of the object’s *name* property.

    If no such property exists, the returned variant is invalid.

    Information about all available properties is provided through the [metaObject()](#metaObject) and [dynamicPropertyNames()](#dynamicPropertyNames).

    See also

    [setProperty()](#setProperty), [isValid()](qvariant.html#isValid), [metaObject()](#metaObject), [dynamicPropertyNames()](#dynamicPropertyNames).

---

pyqtConfigure(Any)
:   TODO

---

receivers(PYQT\_SIGNAL) → int
:   Returns the number of receivers connected to the *signal*.

    Since both slots and signals can be used as receivers for signals, and the same connections can be made many times, the number of receivers is the same as the number of connections made from this signal.

    When calling this function, you can use the `SIGNAL()` macro to pass a specific signal:

    ```
    # if (receivers(SIGNAL(valueChanged(QByteArray))) > 0) {
    #     QByteArray data;
    #     get_the_value(&data);       // expensive operation
    #     emit valueChanged(data);
    # }
    ```

    As the code snippet above illustrates, you can use this function to avoid expensive operations or emitting a signal that nobody listens to.

    **Warning:** In a multithreaded application, consecutive calls to this function are not guaranteed to yield the same results.

    **Warning:** This function violates the object-oriented principle of modularity. In particular, this function must not be called from an override of [connectNotify()](#connectNotify) or [disconnectNotify()](#disconnectNotify), as those might get called from any thread.

    See also

    [isSignalConnected()](#isSignalConnected).

---

removeEventFilter(QObject)
:   Removes an event filter object *obj* from this object. The request is ignored if such an event filter has not been installed.

    All event filters for this object are automatically removed when this object is destroyed.

    It is always safe to remove an event filter, even during event filter activation (i.e. from the [eventFilter()](#eventFilter) function).

    See also

    [installEventFilter()](#installEventFilter), [eventFilter()](#eventFilter), [event()](#event).

---

sender() → QObject
:   Returns a pointer to the object that sent the signal, if called in a slot activated by a signal; otherwise it returns `nullptr`. The pointer is valid only during the execution of the slot that calls this function from this object’s thread context.

    The pointer returned by this function becomes invalid if the sender is destroyed, or if the slot is disconnected from the sender’s signal.

    **Warning:** This function violates the object-oriented principle of modularity. However, getting access to the sender might be useful when many signals are connected to a single slot.

    **Warning:** As mentioned above, the return value of this function is not valid when the slot is called via a [DirectConnection](qt.html#ConnectionType-DirectConnection) from a thread different from this object’s thread. Do not use this function in this type of scenario.

    See also

    [senderSignalIndex()](#senderSignalIndex).

---

senderSignalIndex() → int
:   Returns the meta-method index of the signal that called the currently executing slot, which is a member of the class returned by [sender()](#sender). If called outside of a slot activated by a signal, -1 is returned.

    For signals with default parameters, this function will always return the index with all parameters, regardless of which was used with connect(). For example, the signal `destroyed(QObject \*obj = \nullptr)` will have two different indexes (with and without the parameter), but this function will always return the index with a parameter. This does not apply when overloading signals with different parameters.

    **Warning:** This function violates the object-oriented principle of modularity. However, getting access to the signal index might be useful when many signals are connected to a single slot.

    **Warning:** The return value of this function is not valid when the slot is called via a [DirectConnection](qt.html#ConnectionType-DirectConnection) from a thread different from this object’s thread. Do not use this function in this type of scenario.

    See also

    [sender()](#sender), [indexOfSignal()](qmetaobject.html#indexOfSignal), [method()](qmetaobject.html#method).

---

setObjectName([QByteArray](qbytearray.html)|bytes|bytearray|memoryview|str|None)
:   TODO

---

setParent(QObject)
:   Makes the object a child of *parent*.

    See also

    [parent()](#parent), [children()](#children).

---

setProperty(str, Any) → bool
:   Sets the value of the object’s *name* property to *value*.

    If the property is defined in the class using Q\_PROPERTY then true is returned on success and false otherwise. If the property is not defined using Q\_PROPERTY, and therefore not listed in the meta-object, it is added as a dynamic property and false is returned.

    Information about all available properties is provided through the [metaObject()](#metaObject) and [dynamicPropertyNames()](#dynamicPropertyNames).

    Dynamic properties can be queried again using [property()](#property) and can be removed by setting the property value to an invalid [QVariant](https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant). Changing the value of a dynamic property causes a [QDynamicPropertyChangeEvent](qdynamicpropertychangeevent.html) to be sent to the object.

    **Note:** Dynamic properties starting with “\_q\_” are reserved for internal purposes.

    See also

    [property()](#property), [metaObject()](#metaObject), [dynamicPropertyNames()](#dynamicPropertyNames), [write()](qmetaproperty.html#write).

---

signalsBlocked() → bool
:   Returns `true` if signals are blocked; otherwise returns `false`.

    Signals are not blocked by default.

    See also

    [blockSignals()](#blockSignals), [QSignalBlocker](qsignalblocker.html).

---

startTimer(int, timerType: [TimerType](qt.html#TimerType) = [CoarseTimer](qt.html#TimerType-CoarseTimer)) → int
:   This is an overloaded function that will start a timer of type *timerType* and a timeout of *interval* milliseconds. This is equivalent to calling:

    ```
    startTimer(std::chrono::milliseconds{interval}, timerType);
    ```

    Starting from Qt 6.10, setting a negative interval will result in a run-time warning and the value being reset to 1ms. Before Qt 6.10 a Qt Timer would let you set a negative interval but behave in surprising ways (for example stop the timer if it was running or not start it at all).

    See also

    [timerEvent()](#timerEvent), [killTimer()](#killTimer), QChronoTimer, [QBasicTimer](qbasictimer.html).

---

thread() → [QThread](qthread.html)
:   Returns the thread in which the object lives.

    See also

    [moveToThread()](#moveToThread).

---

timerEvent([QTimerEvent](qtimerevent.html))
:   This event handler can be reimplemented in a subclass to receive timer events for the object.

    QChronoTimer provides higher-level interfaces to the timer functionality, and also more general information about timers. The timer event is passed in the *event* parameter.

    See also

    [startTimer()](#startTimer), [killTimer()](#killTimer), [event()](#event).

---

@staticmethod tr(str, disambiguation: str = None, n: int = -1) → str
:   Returns a translated version of *sourceText*, optionally based on a *disambiguation* string and value of *n* for strings containing plurals; otherwise returns QString::fromUtf8(*sourceText*) if no appropriate translated string is available.

    Example:

    ```
    # void SpreadSheet::setupMenuBar()
    # {
    #     QMenu *fileMenu = menuBar()->addMenu(tr("&File"));
    ```

    If the same *sourceText* is used in different roles within the same context, an additional identifying string may be passed in *disambiguation* (`nullptr` by default). In Qt 4.4 and earlier, this was the preferred way to pass comments to translators.

    Example:

    ```
    # MyWindow::MyWindow()
    # {
    #     QLabel *senderLabel = new QLabel(tr("Name:"));
    #     QLabel *recipientLabel = new QLabel(tr("Name:", "recipient"));
    ```

    See Writing Source Code for Translation for a detailed description of Qt’s translation mechanisms in general, and the Disambiguate Identical Text section for information on disambiguation.

    **Warning:** This method is reentrant only if all translators are installed *before* calling this method. Installing or removing translators while performing translations is not supported. Doing so will probably result in crashes or other undesirable behavior.

    See also

    [translate()](qcoreapplication.html#translate).

## Signals[¶](#signals "Link to this heading")

destroyed(object: QObject = None)
:   This signal is emitted immediately before the object *obj* is destroyed, after any instances of QPointer have been notified, and cannot be blocked.

    All the objects’s children are destroyed immediately after this signal is emitted.

    See also

    [deleteLater()](#deleteLater), QPointer.

---

objectNameChanged(str|None)
:   This signal is emitted after the object’s name has been changed. The new object name is passed as *objectName*.

    See also

    [objectName()](#objectName).

### [Table of Contents](../../index.html)

* QObject
  + [Description](#description)
    - [Thread Affinity](#thread-affinity)
    - [No Copy Constructor or Assignment Operator](#no-copy-constructor-or-assignment-operator)
    - [Auto-Connection](#auto-connection)
    - [Dynamic Properties](#dynamic-properties)
    - [Internationalization (I18n)](#internationalization-i18n)
  + [Attributes](#attributes)
  + [Methods](#methods)
  + [Signals](#signals)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QObject

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QPyDesignerCustomWidgetPlugin {#qpydesignercustomwidgetplugin}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QPyDesignerCustomWidgetPlugin

# QPyDesignerCustomWidgetPlugin[¶](#qpydesignercustomwidgetplugin "Link to this heading")

[PyQt6.QtDesigner](qtdesigner-module.html).QPyDesignerCustomWidgetPlugin
:   Inherits from [QObject](../qtcore/qobject.html), [QDesignerCustomWidgetInterface](qdesignercustomwidgetinterface.html).

## Description[¶](#description "Link to this heading")

TODO

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_(parent: [QObject](../qtcore/qobject.html) = None)
:   TODO

### [Table of Contents](../../index.html)

* QPyDesignerCustomWidgetPlugin
  + [Description](#description)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QPyDesignerCustomWidgetPlugin

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QPyDesignerCustomWidgetPlugin {#qpydesignercustomwidgetplugin}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QPyDesignerCustomWidgetPlugin

# QPyDesignerCustomWidgetPlugin[¶](#qpydesignercustomwidgetplugin "Link to this heading")

[PyQt6.QtDesigner](qtdesigner-module.html).QPyDesignerCustomWidgetPlugin
:   Inherits from [QObject](../qtcore/qobject.html), [QDesignerCustomWidgetInterface](qdesignercustomwidgetinterface.html).

## Description[¶](#description "Link to this heading")

TODO

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_(parent: [QObject](../qtcore/qobject.html) = None)
:   TODO

### [Table of Contents](../../index.html)

* QPyDesignerCustomWidgetPlugin
  + [Description](#description)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QPyDesignerCustomWidgetPlugin

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## pyqtSlot() {#pyqtslot}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QtCore

# QtCore[¶](#qtcore "Link to this heading")

The QtCore module contains the core classes, including the
event loop and Qt’s signal and slot mechanism. It also includes platform
independent abstractions for animations, state machines, threads, mapped files,
shared memory, regular expressions, and user and application settings.

## Classes[¶](#classes "Link to this heading")

|  |  |  |  |
| --- | --- | --- | --- |
| [QAbstractAnimation](qabstractanimation.html) | [QFileDevice](qfiledevice.html) | [QMutexLocker](qmutexlocker.html) | [QSortFilterProxyModel](qsortfilterproxymodel.html) |
| [QAbstractEventDispatcher](qabstracteventdispatcher.html) | [QFileInfo](qfileinfo.html) | [QNativeInterface](qnativeinterface.html) | [QStandardPaths](qstandardpaths.html) |
| [QAbstractItemModel](qabstractitemmodel.html) | [QFileSelector](qfileselector.html) | [QNativeIpcKey](qnativeipckey.html) | [QStorageInfo](qstorageinfo.html) |
| [QAbstractListModel](qabstractlistmodel.html) | [QFileSystemWatcher](qfilesystemwatcher.html) | [QObject](qobject.html) | [QStringConverter](qstringconverter.html) |
| [QAbstractNativeEventFilter](qabstractnativeeventfilter.html) | [QGenericArgument](qgenericargument.html) | [QObjectCleanupHandler](qobjectcleanuphandler.html) | [QStringConverterBase](qstringconverterbase.html) |
| [QAbstractProxyModel](qabstractproxymodel.html) | [QGenericReturnArgument](qgenericreturnargument.html) | [QOperatingSystemVersion](qoperatingsystemversion.html) | [QStringDecoder](qstringdecoder.html) |
| [QAbstractTableModel](qabstracttablemodel.html) | [QIdentityProxyModel](qidentityproxymodel.html) | [QOperatingSystemVersionBase](qoperatingsystemversionbase.html) | [QStringEncoder](qstringencoder.html) |
| [QAnimationGroup](qanimationgroup.html) | [QIODevice](qiodevice.html) | [QParallelAnimationGroup](qparallelanimationgroup.html) | [QStringListModel](qstringlistmodel.html) |
| [QBasicTimer](qbasictimer.html) | [QIODeviceBase](qiodevicebase.html) | [QPauseAnimation](qpauseanimation.html) | [QSysInfo](qsysinfo.html) |
| [QBitArray](qbitarray.html) | [QItemSelection](qitemselection.html) | [QPermission](qpermission.html) | [QSystemSemaphore](qsystemsemaphore.html) |
| [QBluetoothPermission](qbluetoothpermission.html) | [QItemSelectionModel](qitemselectionmodel.html) | [QPersistentModelIndex](qpersistentmodelindex.html) | [Qt](qt.html) |
| [QBuffer](qbuffer.html) | [QItemSelectionRange](qitemselectionrange.html) | [QPluginLoader](qpluginloader.html) | [QTemporaryDir](qtemporarydir.html) |
| [QByteArray](qbytearray.html) | [QJsonDocument](qjsondocument.html) | [QPoint](qpoint.html) | [QTemporaryFile](qtemporaryfile.html) |
| [QByteArrayMatcher](qbytearraymatcher.html) | [QJsonParseError](qjsonparseerror.html) | [QPointF](qpointf.html) | [QTextBoundaryFinder](qtextboundaryfinder.html) |
| [QCalendar](qcalendar.html) | [QJsonValue](qjsonvalue.html) | [QProcess](qprocess.html) | [QTextStream](qtextstream.html) |
| [QCalendarPermission](qcalendarpermission.html) | [QKeyCombination](qkeycombination.html) | [QProcessEnvironment](qprocessenvironment.html) | [QThread](qthread.html) |
| [QCameraPermission](qcamerapermission.html) | [QLibrary](qlibrary.html) | [QPropertyAnimation](qpropertyanimation.html) | [QThreadPool](qthreadpool.html) |
| [QCborError](qcborerror.html) | [QLibraryInfo](qlibraryinfo.html) | [QPyAbstractRange](qpyabstractrange.html) | [QTime](qtime.html) |
| [QCborStreamReader](qcborstreamreader.html) | [QLine](qline.html) | [QPySequenceRange](qpysequencerange.html) | [QTimeLine](qtimeline.html) |
| [QCborStreamWriter](qcborstreamwriter.html) | [QLineF](qlinef.html) | [QPyTableRange](qpytablerange.html) | [QTimer](qtimer.html) |
| [QChar](qchar.html) | [QLocale](qlocale.html) | [QRandomGenerator](qrandomgenerator.html) | [QTimerEvent](qtimerevent.html) |
| [QChildEvent](qchildevent.html) | [QLocationPermission](qlocationpermission.html) | [QRangeModel](qrangemodel.html) | [QTimeZone](qtimezone.html) |
| [QCollator](qcollator.html) | [QLockFile](qlockfile.html) | [QReadLocker](qreadlocker.html) | [QTranslator](qtranslator.html) |
| [QCollatorSortKey](qcollatorsortkey.html) | [QLoggingCategory](qloggingcategory.html) | [QReadWriteLock](qreadwritelock.html) | [QTransposeProxyModel](qtransposeproxymodel.html) |
| [QCommandLineOption](qcommandlineoption.html) | [QMargins](qmargins.html) | [QRect](qrect.html) | [QTypeRevision](qtyperevision.html) |
| [QCommandLineParser](qcommandlineparser.html) | [QMarginsF](qmarginsf.html) | [QRectF](qrectf.html) | [QUrl](qurl.html) |
| [QConcatenateTablesProxyModel](qconcatenatetablesproxymodel.html) | [QMessageAuthenticationCode](qmessageauthenticationcode.html) | [QRecursiveMutex](qrecursivemutex.html) | [QUrlQuery](qurlquery.html) |
| [QContactsPermission](qcontactspermission.html) | [QMessageLogContext](qmessagelogcontext.html) | [QRegularExpression](qregularexpression.html) | [QUuid](quuid.html) |
| [QCoreApplication](qcoreapplication.html) | [QMessageLogger](qmessagelogger.html) | [QRegularExpressionMatch](qregularexpressionmatch.html) | [QVariant](qvariant.html) |
| [QCryptographicHash](qcryptographichash.html) | [QMetaClassInfo](qmetaclassinfo.html) | [QRegularExpressionMatchIterator](qregularexpressionmatchiterator.html) | [QVariantAnimation](qvariantanimation.html) |
| [QDataStream](qdatastream.html) | [QMetaEnum](qmetaenum.html) | [QResource](qresource.html) | [QVersionNumber](qversionnumber.html) |
| [QDate](qdate.html) | [QMetaMethod](qmetamethod.html) | [QRunnable](qrunnable.html) | [QWaitCondition](qwaitcondition.html) |
| [QDateTime](qdatetime.html) | [QMetaObject](qmetaobject.html) | [QSaveFile](qsavefile.html) | [QWinEventNotifier](qwineventnotifier.html) |
| [QDeadlineTimer](qdeadlinetimer.html) | [QMetaProperty](qmetaproperty.html) | [QSemaphore](qsemaphore.html) | [QWriteLocker](qwritelocker.html) |
| [QDir](qdir.html) | [QMetaType](qmetatype.html) | [QSemaphoreReleaser](qsemaphorereleaser.html) | [QXmlStreamAttribute](qxmlstreamattribute.html) |
| [QDirIterator](qdiriterator.html) | [QMicrophonePermission](qmicrophonepermission.html) | [QSequentialAnimationGroup](qsequentialanimationgroup.html) | [QXmlStreamAttributes](qxmlstreamattributes.html) |
| [QDynamicPropertyChangeEvent](qdynamicpropertychangeevent.html) | [QMimeData](qmimedata.html) | [QSettings](qsettings.html) | [QXmlStreamEntityDeclaration](qxmlstreamentitydeclaration.html) |
| [QEasingCurve](qeasingcurve.html) | [QMimeDatabase](qmimedatabase.html) | [QSharedMemory](qsharedmemory.html) | [QXmlStreamEntityResolver](qxmlstreamentityresolver.html) |
| [QElapsedTimer](qelapsedtimer.html) | [QMimeType](qmimetype.html) | [QSignalBlocker](qsignalblocker.html) | [QXmlStreamNamespaceDeclaration](qxmlstreamnamespacedeclaration.html) |
| [QEvent](qevent.html) | [QModelIndex](qmodelindex.html) | [QSignalMapper](qsignalmapper.html) | [QXmlStreamNotationDeclaration](qxmlstreamnotationdeclaration.html) |
| [QEventLoop](qeventloop.html) | [QModelRoleData](qmodelroledata.html) | [QSize](qsize.html) | [QXmlStreamReader](qxmlstreamreader.html) |
| [QEventLoopLocker](qeventlooplocker.html) | [QModelRoleDataSpan](qmodelroledataspan.html) | [QSizeF](qsizef.html) | [QXmlStreamWriter](qxmlstreamwriter.html) |
| [QFile](qfile.html) | [QMutex](qmutex.html) | [QSocketNotifier](qsocketnotifier.html) |

## Enums[¶](#enums "Link to this heading")

QCborKnownTags
:   This enum contains a list of CBOR tags, known at the time of the Qt implementation. This list is not meant to be complete and contains only tags that are either backed by an RFC or specifically used by the Qt implementation.

    The authoritative list is maintained by IANA in the [CBOR tag registry](https://www.iana.org/assignments/cbor-tags/cbor-tags.xhtml).

    The following tags are interpreted by QCborValue during decoding and will produce objects with extended Qt types, and it will use those tags when encoding the same extended types.

    Additionally, if a QCborValue containing a [QByteArray](qbytearray.html) is tagged using one of `ExpectedBase64url`, `ExpectedBase64` or `ExpectedBase16`, QCborValue will use the expected encoding when converting to JSON (see QCborValue::toJsonValue).

    See also

    QCborTag, QCborStreamWriter::append(QCborTag), [isTag()](qcborstreamreader.html#isTag), QCborStreamReader::toTag(), QCborValue::isTag(), QCborValue::tag().

    | Member | Value | Description |
    | --- | --- | --- |
    | Base64 | 34 | Indicates that the string contains data encoded using Base64. |
    | Base64url | 33 | Indicates that the string contains data encoded using Base64url. |
    | Bigfloat | 5 | Similar to Decimal, but the exponent is a power of 2 instead. |
    | COSE\_Encrypt | 96 | An `Encrypt` map as specified by RFC 8152 (CBOR Object Signing and Encryption). |
    | COSE\_Encrypt0 | 16 | An `Encrypt0` map as specified by RFC 8152 (CBOR Object Signing and Encryption). |
    | COSE\_Mac | 97 | A `Mac` map as specified by RFC 8152 (CBOR Object Signing and Encryption). |
    | COSE\_Mac0 | 17 | A `Mac0` map as specified by RFC 8152 (CBOR Object Signing and Encryption). |
    | COSE\_Sign | 98 | A `Sign` map as specified by RFC 8152 (CBOR Object Signing and Encryption). |
    | COSE\_Sign1 | 18 | A `Sign1` map as specified by RFC 8152 (CBOR Object Signing and Encryption). |
    | DateTimeString | 0 | [QDateTime](qdatetime.html) |
    | Decimal | 4 | A decimal fraction, encoded as an array of two integers: the first is the exponent of the power of 10, the second the integral mantissa. The value 273.15 would be encoded as array `[-2, 27315]`. |
    | EncodedCbor | 24 | Indicates that the byte array contains a CBOR stream. |
    | ExpectedBase16 | 23 | Indicates that the byte array should be encoded using Base16 (hex) if the stream is converted to JSON. |
    | ExpectedBase64 | 22 | Indicates that the byte array should be encoded using Base64 if the stream is converted to JSON. |
    | ExpectedBase64url | 21 | Indicates that the byte array should be encoded using Base64url if the stream is converted to JSON. |
    | MimeMessage | 36 | Indicates that the string contains a MIME message (according to RFC 2045). |
    | NegativeBignum | 3 | A negative number of arbitrary length, encoded as the absolute value of that number, minus one. For example, a byte array containing byte value 0x02 followed by 8 zero bytes represents the number -265 - 1. |
    | PositiveBignum | 2 | A positive number of arbitrary length, encoded as a byte array in network byte order. For example, the number 264 is represented by a byte array containing the byte value 0x01 followed by 8 zero bytes. |
    | RegularExpression | 35 | Indicates that the string contains a Perl-Compatible Regular Expression pattern. |
    | Signature | 55799 | No change in interpretation; this tag can be used as the outermost tag in a CBOR stream as the file header. |
    | UnixTime\_t | 1 | [QDateTime](qdatetime.html) (only in decoding) |
    | Url | 32 | [QUrl](qurl.html) |
    | Uuid | 37 | [QUuid](quuid.html) |

---

QCborSimpleType
:   This enum contains the possible “Simple Types” for CBOR. Simple Types range from 0 to 255 and are types that carry no further value.

    The following values are currently known:

    Qt CBOR API supports encoding and decoding any Simple Type, whether one of those above or any other value.

    Applications should only use further values if a corresponding specification has been published, otherwise interpretation and validation by the remote may fail. Values 24 to 31 are reserved and must not be used.

    The current authoritative list is maintained by IANA in the [Simple Values registry](https://www.iana.org/assignments/cbor-simple-values/cbor-simple-values.xml).

    See also

    QCborStreamWriter::append(QCborSimpleType), [isSimpleType()](qcborstreamreader.html#isSimpleType), [toSimpleType()](qcborstreamreader.html#toSimpleType), QCborValue::isSimpleType(), QCborValue::toSimpleType().

    | Member | Value | Description |
    | --- | --- | --- |
    | False\_ | 20 | A “false” boolean. |
    | Null | 22 | Absence of value (null). |
    | True\_ | 21 | A “true” boolean. |
    | Undefined | 23 | Missing or deleted value, usually an error. |

---

QtMsgType
:   This enum describes the messages that can be sent to a message handler (QtMessageHandler). You can use the enum to identify and associate the various message types with the appropriate actions.

    `QtInfoMsg` was added in Qt 5.5.

    See also

    QtMessageHandler, [qInstallMessageHandler()](#qInstallMessageHandler).

    | Member | Value | Description |
    | --- | --- | --- |
    | QtCriticalMsg | 2 | A message generated by the [qCritical()](#qCritical) function. |
    | QtDebugMsg | 0 | A message generated by the [qDebug()](#qDebug) function. |
    | QtFatalMsg | 3 | A message generated by the [qFatal()](#qFatal) function. |
    | QtInfoMsg | 4 | A message generated by the [qInfo()](#qInfo) function. |
    | QtSystemMsg | TODO | TODO |
    | QtWarningMsg | 1 | A message generated by the [qWarning()](#qWarning) function. |

## Attributes[¶](#attributes "Link to this heading")

PYQT\_VERSION: int
:   This is a read-only attribute.

    TODO

---

PYQT\_VERSION\_STR: str
:   This is a read-only attribute.

    TODO

---

QT\_VERSION: int
:   This is a read-only attribute.

    This macro expands to a numeric value of the same form as QT\_VERSION\_CHECK() constructs, that specifies the version of Qt with which code using it is compiled. For example, if you compile your application with Qt 6.1.2, the QT\_VERSION macro will expand to `0x060102`, the same as `QT_VERSION_CHECK(6, 1, 2)`. Note that this need not agree with the version the application will find itself using at *runtime*.

    You can use QT\_VERSION to select the latest Qt features where available while falling back to older implementations otherwise. Using QT\_VERSION\_CHECK() for the value to compare with is recommended.

    Example:

    ```
    # #if QT_VERSION >= 0x040100
    #     QIcon icon = style()->standardIcon(QStyle::SP_TrashIcon);
    # #else
    #     QPixmap pixmap = style()->standardPixmap(QStyle::SP_TrashIcon);
    #     QIcon icon(pixmap);
    # #endif
    ```

    See also

    [QT\_VERSION\_STR](#QT_VERSION_STR), QT\_VERSION\_CHECK(), [qVersion()](#qVersion).

---

QT\_VERSION\_STR: str
:   This is a read-only attribute.

    This macro expands to a string that specifies Qt’s version number (for example, “6.1.2”). This is the version with which the application is compiled. This may be a different version than the version the application will find itself using at *runtime*.

    See also

    [qVersion()](#qVersion), [QT\_VERSION](#QT_VERSION).

## Functions[¶](#functions "Link to this heading")

pyqtClassInfo(str, str)
:   TODO

---

pyqtEnum(enum.Enum)
:   TODO

---

pyqtPickleProtocol() → int|None
:   TODO

---

pyqtRemoveInputHook()
:   TODO

---

pyqtRestoreInputHook()
:   TODO

---

pyqtSetPickleProtocol(int|None)
:   TODO

---

pyqtSlot(Any, name: str = None, result: str = None) → Any
:   TODO

---

Q\_ARG(Any, Any) → [QGenericArgument](qgenericargument.html)
:   This macro takes a *Type* and a *value* of that type and returns a QMetaMethodArgument, which can be passed to the template [invokeMethod()](qmetaobject.html#invokeMethod) with the `Args &&...` arguments.

    See also

    [Q\_RETURN\_ARG()](#Q_RETURN_ARG).

---

Q\_RETURN\_ARG(Any) → [QGenericReturnArgument](qgenericreturnargument.html)
:   This macro takes a *Type* and a non-const reference to a *value* of that type and returns a QMetaMethodReturnArgument, which can be passed to the template [invokeMethod()](qmetaobject.html#invokeMethod) with the `Args &&...` arguments.

    See also

    [Q\_ARG()](#Q_ARG).

---

qAbs(float) → float
:   TODO

---

qAddPostRoutine(Callable[..., None])
:   TODO

---

qAddPreRoutine(Callable[[], None])
:   TODO

---

qChecksum([QByteArray](qbytearray.html)|bytes|bytearray|memoryview, standard: [ChecksumType](qt.html#ChecksumType) = [ChecksumIso3309](qt.html#ChecksumType-ChecksumIso3309)) → int
:   Returns the CRC-16 checksum of *data*.

    The checksum is independent of the byte order (endianness) and will be calculated accorded to the algorithm published in *standard*. By default the algorithm published in ISO 3309 ([ChecksumIso3309](qt.html#ChecksumType-ChecksumIso3309)) is used.

    **Note:** This function is a 16-bit cache conserving (16 entry table) implementation of the CRC-16-CCITT algorithm.

---

qCompress(bytes, compressionLevel: int = -1) → [QByteArray](qbytearray.html)
:   TODO

---

qCompress([QByteArray](qbytearray.html)|bytes|bytearray|memoryview, compressionLevel: int = -1) → [QByteArray](qbytearray.html)
:   Compresses the *data* byte array and returns the compressed data in a new byte array.

    The *compressionLevel* parameter specifies how much compression should be used. Valid values are between 0 and 9, with 9 corresponding to the greatest compression (i.e. smaller compressed data) at the cost of using a slower algorithm. Smaller values (8, 7, …, 1) provide successively less compression at slightly faster speeds. The value 0 corresponds to no compression at all. The default value is -1, which specifies zlib’s default compression.

    See also

    qUncompress(const QByteArray &data).

---

qCritical(str)
:   Calls the message handler with the critical message *message*. If no message handler has been installed, the message is printed to stderr. Under Windows, the message is sent to the debugger. On QNX the message is sent to slogger2.

    It exits if the environment variable QT\_FATAL\_CRITICALS is not empty.

    This function takes a format string and a list of arguments, similar to the C printf() function. The format should be a Latin-1 string.

    Example:

    ```
    # void load(const QString &fileName)
    # {
    #     QFile file(fileName);
    #     if (!file.exists())
    #         qCritical("File '%s' does not exist!", qUtf8Printable(fileName));
    # }
    ```

    If you include <QtDebug>, a more convenient syntax is also available:

    ```
    # qCritical() << "Brush:" << myQBrush << "Other
    # value:" << i;
    ```

    A space is inserted between the items, and a newline is appended at the end.

    To suppress the output at runtime, install your own message handler with [qInstallMessageHandler()](#qInstallMessageHandler).

    See also

    [qDebug()](#qDebug), [qInfo()](#qInfo), [qWarning()](#qWarning), [qFatal()](#qFatal), [qInstallMessageHandler()](#qInstallMessageHandler).

---

qDebug(str)
:   Returns a QDebug object that logs a debug message to the central message handler.

    Example:

    ```
    # qDebug() << "Brush:" << myQBrush << "Other value:" << i;
    ```

    Using qDebug() is an alternative to qDebug(const char [\*](#id1), …), which follows the printf paradigm.

    Note that QDebug and the type specific stream operators do add various formatting to make the debug message easier to read. See the qdebug-formatting-options documentation for more details.

    This function does nothing if `QT_NO_DEBUG_OUTPUT` was defined during compilation.

    See also

    qDebug(const char [\*](#id3), …), qCDebug().

---

qEnvironmentVariable(str) → str
:   TODO

---

qEnvironmentVariable(str, str|None) → str
:   TODO

---

qEnvironmentVariableIntegerValue(str) → int|None
:   TODO

---

qEnvironmentVariableIntValue(str) → (int, bool)
:   Returns the numerical value of the environment variable *varName*. If *ok* is not null, sets `\*ok` to `true` or `false` depending on the success of the conversion.

    Equivalent to

    ```
    #     qgetenv(varName).toInt(ok, 0)
    ```

    except that it’s much faster, and can’t throw exceptions.

    **Note:** there’s a limit on the length of the value, which is sufficient for all valid values of int, not counting leading zeroes or spaces. Values that are too long will either be truncated or this function will set *ok* to `false`.

    See also

    qgetenv(), [qEnvironmentVariable()](#qEnvironmentVariable), [qEnvironmentVariableIsSet()](#qEnvironmentVariableIsSet).

---

qEnvironmentVariableIsEmpty(str) → bool
:   Returns whether the environment variable *varName* is empty.

    Equivalent to

    ```
    #     qgetenv(varName).isEmpty()
    ```

    except that it’s potentially much faster, and can’t throw exceptions.

    See also

    qgetenv(), [qEnvironmentVariable()](#qEnvironmentVariable), [qEnvironmentVariableIsSet()](#qEnvironmentVariableIsSet).

---

qEnvironmentVariableIsSet(str) → bool
:   Returns whether the environment variable *varName* is set.

    Equivalent to

    ```
    #     !qgetenv(varName).isNull()
    ```

    except that it’s potentially much faster, and can’t throw exceptions.

    See also

    qgetenv(), [qEnvironmentVariable()](#qEnvironmentVariable), [qEnvironmentVariableIsEmpty()](#qEnvironmentVariableIsEmpty).

---

qFatal(str)
:   Calls the message handler with the fatal message *message*. If no message handler has been installed, the message is printed to stderr. Under Windows, the message is sent to the debugger. On QNX the message is sent to slogger2.

    If you are using the **default message handler** this function will abort to create a core dump. On Windows, for debug builds, this function will report a \_CRT\_ERROR enabling you to connect a debugger to the application.

    This function takes a format string and a list of arguments, similar to the C printf() function.

    Example:

    ```
    # int divide(int a, int b)
    # {
    #     if (b == 0)                                // program error
    #         qFatal("divide: cannot divide by zero");
    #     return a / b;
    # }
    ```

    To suppress the output at runtime, install your own message handler with [qInstallMessageHandler()](#qInstallMessageHandler).

    See also

    [qDebug()](#qDebug), [qInfo()](#qInfo), [qWarning()](#qWarning), [qCritical()](#qCritical), [qInstallMessageHandler()](#qInstallMessageHandler).

---

qFloatDistance(float, float) → int
:   Returns the number of representable floating-point numbers between *a* and *b*.

    This function serves the same purpose as `qFloatDistance(float, float)`, but returns the distance between two `double` numbers. Since the range is larger than for two `float` numbers (`[-DBL_MAX,DBL_MAX]`), the return type is quint64.

    See also

    [qFuzzyCompare()](#qFuzzyCompare).

---

qFormatLogMessage([QtMsgType](#QtMsgType), [QMessageLogContext](qmessagelogcontext.html), str|None) → str
:   TODO

---

qFuzzyCompare([QLineF](qlinef.html), [QLineF](qlinef.html)) → bool
:   TODO

---

qFuzzyCompare([QMarginsF](qmarginsf.html), [QMarginsF](qmarginsf.html)) → bool
:   TODO

---

qFuzzyCompare(float, float) → bool
:   Compares the floating point value *p1* and *p2* and returns `true` if they are considered equal, otherwise `false`.

    Note that comparing values where either *p1* or *p2* is 0.0 will not work, nor does comparing values where one of the values is NaN or infinity. If one of the values is always 0.0, use qFuzzyIsNull instead. If one of the values is likely to be 0.0, one solution is to add 1.0 to both values.

    ```
    # // Instead of comparing with 0.0
    # qFuzzyCompare(0.0, 1.0e-200); // This will return false
    # // Compare adding 1 to both values will fix the problem
    # qFuzzyCompare(1 + 0.0, 1 + 1.0e-200); // This will return true
    ```

    The two numbers are compared in a relative way, where the exactness is stronger the smaller the numbers are.

---

qFuzzyCompare([QPointF](qpointf.html), [QPointF](qpointf.html)) → bool
:   TODO

---

qFuzzyCompare([QRectF](qrectf.html), [QRectF](qrectf.html)) → bool
:   TODO

---

qFuzzyCompare([QSizeF](qsizef.html), [QSizeF](qsizef.html)) → bool
:   TODO

---

qFuzzyIsNull([QLineF](qlinef.html)) → bool
:   TODO

---

qFuzzyIsNull([QMarginsF](qmarginsf.html)) → bool
:   TODO

---

qFuzzyIsNull(float) → bool
:   Returns true if the absolute value of *d* is within 0.000000000001 of 0.0.

---

qFuzzyIsNull([QPointF](qpointf.html)) → bool
:   TODO

---

qFuzzyIsNull([QRectF](qrectf.html)) → bool
:   TODO

---

qFuzzyIsNull([QSizeF](qsizef.html)) → bool
:   TODO

---

qInf() → float
:   Returns the bit pattern for an infinite number as a double.

    See also

    [qIsInf()](#qIsInf).

---

qInfo(str)
:   Calls the message handler with the informational message *message*. If no message handler has been installed, the message is printed to stderr. Under Windows, the message is sent to the console, if it is a console application; otherwise, it is sent to the debugger. On QNX the message is sent to slogger2. This function does nothing if `QT_NO_INFO_OUTPUT` was defined during compilation.

    If you pass the function a format string and a list of arguments, it works in similar way to the C printf() function. The format should be a Latin-1 string.

    Example:

    ```
    # qInfo("Items in list: %d", myList.size());
    ```

    If you include `<QtDebug>`, a more convenient syntax is also available:

    ```
    # qInfo() << "Brush:" << myQBrush << "Other value:" << i;
    ```

    With this syntax, the function returns a QDebug object that is configured to use the [QtInfoMsg](#QtMsgType-QtInfoMsg) message type. It automatically puts a single space between each item, and outputs a newline at the end. It supports many C++ and Qt types.

    To suppress the output at runtime, install your own message handler using [qInstallMessageHandler()](#qInstallMessageHandler).

    See also

    [qDebug()](#qDebug), [qWarning()](#qWarning), [qCritical()](#qCritical), [qFatal()](#qFatal), [qInstallMessageHandler()](#qInstallMessageHandler).

---

qInstallMessageHandler(Callable[[[QtMsgType](#QtMsgType), [QMessageLogContext](qmessagelogcontext.html), str|None], None]|None) → Callable[[[QtMsgType](#QtMsgType), [QMessageLogContext](qmessagelogcontext.html), str|None], None]|None
:   TODO

---

qIsFinite(float) → bool
:   Returns `true` if the double *d* is a finite number.

---

qIsInf(float) → bool
:   Returns `true` if the double *d* is equivalent to infinity.

    See also

    [qInf()](#qInf).

---

qIsNaN(float) → bool
:   Returns `true` if the double *d* is not a number (NaN).

---

qQNaN() → float
:   Returns the bit pattern of a quiet NaN as a double.

    See also

    [qIsNaN()](#qIsNaN).

---

qRegisterResourceData(int, bytes, bytes, bytes) → bool
:   TODO

---

qRemovePostRoutine(Callable[..., None])
:   TODO

---

qRound(float) → int
:   TODO

---

qRound64(float) → int
:   TODO

---

qSetFieldWidth(int) → QTextStreamManipulator
:   Equivalent to [setFieldWidth()](qtextstream.html#setFieldWidth)(*width*).

---

qSetMessagePattern(str|None)
:   TODO

---

qSetPadChar(str) → QTextStreamManipulator
:   Equivalent to [setPadChar()](qtextstream.html#setPadChar)(*ch*).

---

qSetRealNumberPrecision(int) → QTextStreamManipulator
:   Equivalent to [setRealNumberPrecision()](qtextstream.html#setRealNumberPrecision)(*precision*).

---

qSNaN() → float
:   Returns the bit pattern of a signalling NaN as a double.

---

QT\_TR\_NOOP(str) → str
:   Marks the UTF-8 encoded string literal *sourceText* for delayed translation in the current context (class).

    The macro tells lupdate to collect the string, and expands to *sourceText* itself.

    Example:

    ```
    # QString FriendlyConversation::greeting(int type)
    # {
    #     static const char *greeting_strings[] = {
    #         QT_TR_NOOP("Hello"),
    #         QT_TR_NOOP("Goodbye")
    #     };
    #     return tr(greeting_strings[type]);
    # }
    ```

    The macro QT\_TR\_NOOP\_UTF8() is identical and obsolete; this applies to all other \_UTF8 macros as well.

    See also

    [QT\_TRANSLATE\_NOOP()](#QT_TRANSLATE_NOOP).

---

QT\_TRANSLATE\_NOOP(str, str) → str
:   Marks the UTF-8 encoded string literal *sourceText* for delayed translation in the given *context*. The *context* is typically a class name and also needs to be specified as a string literal.

    The macro tells lupdate to collect the string, and expands to *sourceText* itself.

    Example:

    ```
    # static const char *greeting_strings[] = {
    #     QT_TRANSLATE_NOOP("FriendlyConversation", "Hello"),
    #     QT_TRANSLATE_NOOP("FriendlyConversation", "Goodbye")
    # };

    # QString FriendlyConversation::greeting(int type)
    # {
    #     return tr(greeting_strings[type]);
    # }

    # QString global_greeting(int type)
    # {
    #     return qApp->translate("FriendlyConversation",
    #                            greeting_strings[type]);
    # }
    ```

    See also

    [QT\_TR\_NOOP()](#QT_TR_NOOP), QT\_TRANSLATE\_NOOP3().

---

qUncompress(bytes) → [QByteArray](qbytearray.html)
:   TODO

---

qUncompress([QByteArray](qbytearray.html)|bytes|bytearray|memoryview) → [QByteArray](qbytearray.html)
:   Uncompresses the *data* byte array and returns a new byte array with the uncompressed data.

    Returns an empty [QByteArray](qbytearray.html) if the input data was corrupt.

    This function will uncompress data compressed with [qCompress()](#qCompress) from this and any earlier Qt version, back to Qt 3.1 when this feature was added.

    **Note:** If you want to use this function to uncompress external data that was compressed using zlib, you first need to prepend a four byte header to the byte array containing the data. The header must contain the expected length (in bytes) of the uncompressed data, expressed as an unsigned, big-endian, 32-bit integer. This number is just a hint for the initial size of the output buffer size, though. If the indicated size is too small to hold the result, the output buffer size will still be increased until either the output fits or the system runs out of memory. So, despite the 32-bit header, this function, on 64-bit platforms, can produce more than 4GiB of output.

    **Note:** In Qt versions prior to Qt 6.5, more than 2GiB of data worked unreliably; in Qt versions prior to Qt 6.0, not at all.

    See also

    [qCompress()](#qCompress).

---

qUnregisterResourceData(int, bytes, bytes, bytes) → bool
:   TODO

---

qVersion() → str
:   Returns the version number of Qt at runtime as a string (for example, “6.1.2”). This may be a different version than the version the application was *compiled* with.

    See also

    [QT\_VERSION\_STR](#QT_VERSION_STR), [version()](qlibraryinfo.html#version).

---

qWarning(str)
:   Calls the message handler with the warning message *message*. If no message handler has been installed, the message is printed to stderr. Under Windows, the message is sent to the debugger. On QNX the message is sent to slogger2. This function does nothing if `QT_NO_WARNING_OUTPUT` was defined during compilation; it exits if at the nth warning corresponding to the counter in environment variable `QT_FATAL_WARNINGS`. That is, if the environment variable contains the value 1, it will exit on the 1st message; if it contains the value 10, it will exit on the 10th message. Any non-numeric value is equivalent to 1.

    This function takes a format string and a list of arguments, similar to the C printf() function. The format should be a Latin-1 string.

    Example:

    ```
    # void f(int c)
    # {
    #     if (c > 200)
    #         qWarning("f: bad argument, c == %d", c);
    # }
    ```

    If you include <QtDebug>, a more convenient syntax is also available:

    ```
    # qWarning() << "Brush:" << myQBrush << "Other value:"
    # << i;
    ```

    This syntax inserts a space between each item, and appends a newline at the end.

    To suppress the output at runtime, install your own message handler with [qInstallMessageHandler()](#qInstallMessageHandler).

    See also

    [qDebug()](#qDebug), [qInfo()](#qInfo), [qCritical()](#qCritical), [qFatal()](#qFatal), [qInstallMessageHandler()](#qInstallMessageHandler).

---

qYieldCpu()
:   Pauses the execution of the current thread for an unspecified time, using hardware instructions, without de-scheduling this thread. This function is meant to be used in high-throughput loops where the code expects another thread to modify an atomic variable. This is completely different from [yieldCurrentThread()](qthread.html#yieldCurrentThread), which is an OS-level operation that may take the whole thread off the CPU and allow other threads (possibly belonging to other processes) to run.

    So, instead of

    ```
    while (!condition)
        ;
    ```

    one should write

    ```
    while (!condition)
        qYieldCpu();
    ```

    This is useful both with and without hardware multithreading on the same core. In the case of hardware threads, it serves to prevent further speculative execution filling up the pipeline, which could starve the sibling thread of resources. Across cores and higher levels of separation, it allows the cache coherency protocol to allocate the cache line being modified and inspected to the logical processor whose result this code is expecting.

    It is also recommended to loop around code that does not modify the global variable, to avoid contention in exclusively obtaining the memory location. Therefore, an atomic modification loop such as a spinlock acquisition should be:

    ```
    while (true) {
        while (!readOnlyCondition(atomic))
            qYieldCpu();
        if (modify(atomic))
            break;
    }
    ```

    On x86 processors and on RISC-V processors with the `Zihintpause` extension, this will emit the `PAUSE` instruction, which is ignored on processors that don’t support it; on ARMv7 or later ARM processors, it will emit the `YIELD` instruction.

### [Table of Contents](../../index.html)

* QtCore
  + [Classes](#classes)
  + [Enums](#enums)
  + [Attributes](#attributes)
  + [Functions](#functions)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QtCore

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Support for Pickling {#support-for-pickling}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Pickling

# Support for Pickling[¶](#support-for-pickling "Link to this heading")

The following PyQt6 classes may be pickled.

* [QByteArray](api/qtcore/qbytearray.html)
* [QColor](api/qtgui/qcolor.html)
* [QDate](api/qtcore/qdate.html)
* [QDateTime](api/qtcore/qdatetime.html)
* [QKeySequence](api/qtgui/qkeysequence.html)
* [QLine](api/qtcore/qline.html)
* [QLineF](api/qtcore/qlinef.html)
* [QPoint](api/qtcore/qpoint.html)
* [QPointF](api/qtcore/qpointf.html)
* [QPolygon](api/qtgui/qpolygon.html)
* [QRect](api/qtcore/qrect.html)
* [QRectF](api/qtcore/qrectf.html)
* [QSize](api/qtcore/qsize.html)
* [QSizeF](api/qtcore/qsizef.html)
* [QTime](api/qtcore/qtime.html)

Also all named enums ([PyQt6.QtCore.Qt.Key](api/qtcore/qt.html#Key) for example) may be
pickled.

#### Previous topic

[Using Qt Designer](designer.html "previous chapter")

#### Next topic

[Using PyQt6 from the Python Shell](python_shell.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Support for Pickling

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QByteArray {#qbytearray}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QByteArray

# QByteArray[¶](#qbytearray "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QByteArray

## Description[¶](#description "Link to this heading")

The QByteArray class provides an array of bytes.

QByteArray can be used to store both raw bytes (including ‘`\0`’s) and traditional 8-bit ‘`\0`’-terminated strings. Using QByteArray is much more convenient than using `const char \*`. Behind the scenes, it always ensures that the data is followed by a ‘`\0`’ terminator, and uses [implicit sharing](https://doc.qt.io/qt-6/implicit-sharing.html) (copy-on-write) to reduce memory usage and avoid needless copying of data.

In addition to QByteArray, Qt also provides the QString class to store string data. For most purposes, QString is the class you want to use. It understands its content as Unicode text (encoded using UTF-16) where QByteArray aims to avoid assumptions about the encoding or semantics of the bytes it stores (aside from a few legacy cases where it uses ASCII). Furthermore, QString is used throughout in the Qt API. The two main cases where QByteArray is appropriate are when you need to store raw binary data, and when memory conservation is critical (e.g., with Qt for Embedded Linux).

One way to initialize a QByteArray is simply to pass a `const char \*` to its constructor. For example, the following code creates a byte array of size 5 containing the data “Hello”:

```
# QByteArray ba("Hello");
```

Although the [size()](#size) is 5, the byte array also maintains an extra ‘`\0`’ byte at the end so that if a function is used that asks for a pointer to the underlying data (e.g. a call to [data()](#data)), the data pointed to is guaranteed to be ‘`\0`’-terminated.

QByteArray makes a deep copy of the `const char \*` data, so you can modify it later without experiencing side effects. (If, for example for performance reasons, you don’t want to take a deep copy of the data, use QByteArray::fromRawData() instead.)

Another approach is to set the size of the array using [resize()](#resize) and to initialize the data byte by byte. QByteArray uses 0-based indexes, just like C++ arrays. To access the byte at a particular index position, you can use operator[](). On non-const byte arrays, operator[]() returns a reference to a byte that can be used on the left side of an assignment. For example:

```
# QByteArray ba;
# ba.resize(5);
# ba[0] = 0x3c;
# ba[1] = 0xb8;
# ba[2] = 0x64;
# ba[3] = 0x18;
# ba[4] = 0xca;
```

For read-only access, an alternative syntax is to use [at()](#at):

```
# for (qsizetype i = 0; i < ba.size(); ++i) {
#     if (ba.at(i) >= 'a' && ba.at(i) <= 'f')
#         cout << "Found character in range [a-f]" << Qt::endl;
# }
```

[at()](#at) can be faster than operator[](), because it never causes a [deep copy](https://doc.qt.io/qt-6/implicit-sharing.html#deep-copy) to occur.

To extract many bytes at a time, use [first()](#first), [last()](#last), or [sliced()](#sliced).

A QByteArray can embed ‘`\0`’ bytes. The [size()](#size) function always returns the size of the whole array, including embedded ‘`\0`’ bytes, but excluding the terminating ‘`\0`’ added by QByteArray. For example:

```
# QByteArray ba1("ca\0r\0t");
# ba1.size();                     // Returns 2.
# ba1.constData();                // Returns "ca" with terminating \0.

# QByteArray ba2("ca\0r\0t", 3);
# ba2.size();                     // Returns 3.
# ba2.constData();                // Returns "ca\0" with terminating \0.

# QByteArray ba3("ca\0r\0t", 4);
# ba3.size();                     // Returns 4.
# ba3.constData();                // Returns "ca\0r" with terminating \0.

# const char cart[] = {'c', 'a', '\0', 'r', '\0', 't'};
# QByteArray ba4(QByteArray::fromRawData(cart, 6));
# ba4.size();                     // Returns 6.
# ba4.constData();                // Returns "ca\0r\0t" without terminating \0.
```

If you want to obtain the length of the data up to and excluding the first ‘`\0`’ byte, call qstrlen() on the byte array.

After a call to [resize()](#resize), newly allocated bytes have undefined values. To set all the bytes to a particular value, call [fill()](#fill).

To obtain a pointer to the actual bytes, call [data()](#data) or constData(). These functions return a pointer to the beginning of the data. The pointer is guaranteed to remain valid until a non-const function is called on the QByteArray. It is also guaranteed that the data ends with a ‘`\0`’ byte unless the QByteArray was created from raw data. This ‘`\0`’ byte is automatically provided by QByteArray and is not counted in [size()](#size).

QByteArray provides the following basic functions for modifying the byte data: [append()](#append), [prepend()](#prepend), [insert()](#insert), [replace()](#replace), and [remove()](#remove). For example:

```
# QByteArray x("and");
# x.prepend("rock ");         // x == "rock and"
# x.append(" roll");          // x == "rock and roll"
# x.replace(5, 3, "&");       // x == "rock & roll"
```

In the above example the [replace()](#replace) function’s first two arguments are the position from which to start replacing and the number of bytes that should be replaced.

When data-modifying functions increase the size of the array, they may lead to reallocation of memory for the QByteArray object. When this happens, QByteArray expands by more than it immediately needs so as to have space for further expansion without reallocation until the size of the array has greatly increased.

The [insert()](#insert), [remove()](#remove) and, when replacing a sub-array with one of different size, [replace()](#replace) functions can be slow ([linear time](https://doc.qt.io/qt-6/containers.html#linear-time)) for large arrays, because they require moving many bytes in the array by at least one position in memory.

If you are building a QByteArray gradually and know in advance approximately how many bytes the QByteArray will contain, you can call [reserve()](#reserve), asking QByteArray to preallocate a certain amount of memory. You can also call [capacity()](#capacity) to find out how much memory the QByteArray actually has allocated.

Note that using non-const operators and functions can cause QByteArray to do a deep copy of the data, due to [implicit sharing](https://doc.qt.io/qt-6/implicit-sharing.html).

QByteArray provides [STL-style iterators](https://doc.qt.io/qt-6/containers.html#stl-style-iterators) (QByteArray::const\_iterator and QByteArray::iterator). In practice, iterators are handy when working with generic algorithms provided by the C++ standard library.

**Note:** Iterators and references to individual QByteArray elements are subject to stability issues. They are often invalidated when a QByteArray-modifying operation (e.g. [insert()](#insert) or [remove()](#remove)) is called. When stability and iterator-like functionality is required, you should use indexes instead of iterators as they are not tied to QByteArray’s internal state and thus do not get invalidated.

**Note:** Iterators over a QByteArray, and references to individual bytes within one, cannot be relied on to remain valid when any non-const method of the QByteArray is called. Accessing such an iterator or reference after the call to a non-const method leads to undefined behavior. When stability for iterator-like functionality is required, you should use indexes instead of iterators as they are not tied to QByteArray’s internal state and thus do not get invalidated.

If you want to find all occurrences of a particular byte or sequence of bytes in a QByteArray, use [indexOf()](#indexOf) or [lastIndexOf()](#lastIndexOf). The former searches forward starting from a given index position, the latter searches backward. Both return the index position of the byte sequence if they find it; otherwise, they return -1. For example, here’s a typical loop that finds all occurrences of a particular string:

```
# QByteArray ba("We must be <b>bold</b>, very <b>bold</b>");
# qsizetype j = 0;
# while ((j = ba.indexOf("<b>", j)) != -1) {
#     cout << "Found <b> tag at index position " << j << Qt::endl;
#     ++j;
# }
```

If you simply want to check whether a QByteArray contains a particular byte sequence, use [contains()](#contains). If you want to find out how many times a particular byte sequence occurs in the byte array, use [count()](#count). If you want to replace all occurrences of a particular value with another, use one of the two-parameter [replace()](#replace) overloads.

QByteArrays can be compared using overloaded operators such as operator<(), operator<=(), operator==(), operator>=(), and so on. The comparison is based exclusively on the numeric values of the bytes and is very fast, but is not what a human would expect. QString::localeAwareCompare() is a better choice for sorting user-interface strings.

For historical reasons, QByteArray distinguishes between a null byte array and an empty byte array. A *null* byte array is a byte array that is initialized using QByteArray’s default constructor or by passing (const char \*)0 to the constructor. An *empty* byte array is any byte array with size 0. A null byte array is always empty, but an empty byte array isn’t necessarily null:

```
# QByteArray().isNull();          // returns true
# QByteArray().isEmpty();         // returns true

# QByteArray("").isNull();        // returns false
# QByteArray("").isEmpty();       // returns true

# QByteArray("abc").isNull();     // returns false
# QByteArray("abc").isEmpty();    // returns false
```

All functions except [isNull()](#isNull) treat null byte arrays the same as empty byte arrays. For example, [data()](#data) returns a valid pointer (*not* nullptr) to a ‘`\0`’ byte for a null byte array and QByteArray compares equal to QByteArray(“”). We recommend that you always use [isEmpty()](#isEmpty) and avoid [isNull()](#isNull).

### Maximum size and out-of-memory conditions[¶](#maximum-size-and-out-of-memory-conditions "Link to this heading")

The maximum size of QByteArray depends on the architecture. Most 64-bit systems can allocate more than 2 GB of memory, with a typical limit of 2^63 bytes. The actual value also depends on the overhead required for managing the data block. As a result, you can expect the maximum size of 2 GB minus overhead on 32-bit platforms, and 2^63 bytes minus overhead on 64-bit platforms. The number of elements that can be stored in a QByteArray is this maximum size.

When memory allocation fails, QByteArray throws a `std::bad_alloc` exception if the application is being compiled with exception support. Out of memory conditions in Qt containers are the only case where Qt will throw exceptions. If exceptions are disabled, then running out of memory is undefined behavior.

Note that the operating system may impose further limits on applications holding a lot of allocated memory, especially large, contiguous blocks. Such considerations, the configuration of such behavior or any mitigation are outside the scope of the QByteArray API.

### C locale and ASCII functions[¶](#c-locale-and-ascii-functions "Link to this heading")

QByteArray generally handles data as bytes, without presuming any semantics; where it does presume semantics, it uses the C locale and ASCII encoding. Standard Unicode encodings are supported by QString, other encodings may be supported using [QStringEncoder](qstringencoder.html) and [QStringDecoder](qstringdecoder.html) to convert to Unicode. For locale-specific interpretation of text, use [QLocale](qlocale.html) or QString.

#### C Strings[¶](#c-strings "Link to this heading")

Traditional C strings, also known as ‘`\0`’-terminated strings, are sequences of bytes, specified by a start-point and implicitly including each byte up to, but not including, the first ‘`\0`’ byte thereafter. Methods that accept such a pointer, without a length, will interpret it as this sequence of bytes. Such a sequence, by construction, cannot contain a ‘`\0`’ byte.

Other overloads accept a start-pointer and a byte-count; these use the given number of bytes, following the start address, regardless of whether any of them happen to be ‘`\0`’ bytes. In some cases, where there is no overload taking only a pointer, passing a length of -1 will cause the method to use the offset of the first ‘`\0`’ byte after the pointer as the length; a length of -1 should only be passed if the method explicitly says it does this (in which case it is typically a default argument).

#### Spacing Characters[¶](#spacing-characters "Link to this heading")

A frequent requirement is to remove spacing characters from a byte array (`'\n'`, `'\t'`, `' '`, etc.). If you want to remove spacing from both ends of a QByteArray, use [trimmed()](#trimmed). If you want to also replace each run of spacing characters with a single space character within the byte array, use [simplified()](#simplified). Only ASCII spacing characters are recognized for these purposes.

#### Number-String Conversions[¶](#number-string-conversions "Link to this heading")

Functions that perform conversions between numeric data types and string representations are performed in the C locale, regardless of the user’s locale settings. Use [QLocale](qlocale.html) to perform locale-aware conversions between numbers and strings.

#### Character Case[¶](#character-case "Link to this heading")

In QByteArray, the notion of uppercase and lowercase and of case-independent comparison is limited to ASCII. Non-ASCII characters are treated as caseless, since their case depends on encoding. This affects functions that support a case insensitive option or that change the case of their arguments. Functions that this affects include [compare()](#compare), [isLower()](#isLower), [isUpper()](#isUpper), [toLower()](#toLower) and [toUpper()](#toUpper).

This issue does not apply to QStrings since they represent characters using Unicode.

See also

QByteArrayView, QString, [QBitArray](qbitarray.html).

## Classes[¶](#classes "Link to this heading")

|  |
| --- |
| [FromBase64Result](qbytearray-frombase64result.html) |

## Enums[¶](#enums "Link to this heading")

Base64DecodingStatus
:   TODO

    | Member | Value | Description |
    | --- | --- | --- |
    | IllegalCharacter | TODO | TODO |
    | IllegalInputLength | TODO | TODO |
    | IllegalPadding | TODO | TODO |
    | Ok | TODO | TODO |

---

Base64Option
:   This enum contains the options available for encoding and decoding Base64. Base64 is defined by RFC 4648, with the following options:

    [fromBase64Encoding()](#fromBase64Encoding) and [fromBase64()](#fromBase64) ignore the and options. If the option is specified, they will not flag errors in case trailing equal signs are missing or if there are too many of them. If instead the is specified, then the input must either have no padding or have the correct amount of equal signs.

    | Member | Value | Description |
    | --- | --- | --- |
    | AbortOnBase64DecodingErrors | 4 | When decoding Base64-encoded data, stops at the first decoding error. This enum value has been added in Qt 5.15. |
    | Base64Encoding | 0 | (default) The regular Base64 alphabet, called simply “base64” |
    | Base64UrlEncoding | 1 | An alternate alphabet, called “base64url”, which replaces two characters in the alphabet to be more friendly to URLs. |
    | IgnoreBase64DecodingErrors | 0 | When decoding Base64-encoded data, ignores errors in the input; invalid characters are simply skipped. This enum value has been added in Qt 5.15. |
    | KeepTrailingEquals | 0 | (default) Keeps the trailing padding equal signs at the end of the encoded data, so the data is always a size multiple of four. |
    | OmitTrailingEquals | 2 | Omits adding the padding equal signs at the end of the encoded data. |

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs an empty byte array.

    See also

    [isEmpty()](#isEmpty).

---

\_\_init\_\_(QByteArray|bytes|bytearray|memoryview)
:   Constructs a copy of *other*.

    This operation takes [constant time](https://doc.qt.io/qt-6/containers.html#constant-time), because QByteArray is [implicitly shared](https://doc.qt.io/qt-6/implicit-sharing.html). This makes returning a QByteArray from a function very fast. If a shared instance is modified, it will be copied (copy-on-write), taking [linear time](https://doc.qt.io/qt-6/containers.html#linear-time).

    See also

    operator=().

---

\_\_init\_\_(int, bytes)
:   Constructs a byte array of size *size* with every byte set to *ch*.

    See also

    [fill()](#fill).

---

\_\_add\_\_(QByteArray|bytes|bytearray|memoryview) → QByteArray
:   TODO

---

append(QByteArray|bytes|bytearray|memoryview) → QByteArray
:   Appends *data* to this byte array.

---

append(int, bytes) → QByteArray
:   Appends *count* copies of byte *ch* to this byte array and returns a reference to this byte array.

    If *count* is negative or zero nothing is appended to the byte array.

---

assign(QByteArray|bytes|bytearray|memoryview) → QByteArray
:   Replaces the contents of this byte array with a copy of *v* and returns a reference to this byte array.

    The size of this byte array will be equal to the size of *v*.

    This function only allocates memory if the size of *v* exceeds the capacity of this byte array or this byte array is shared.

---

at(int) → bytes
:   Returns the byte at index position *i* in the byte array.

    *i* must be a valid index position in the byte array (i.e., 0 <= *i* < [size()](#size)).

    See also

    operator[]().

---

capacity() → int
:   Returns the maximum number of bytes that can be stored in the byte array without forcing a reallocation.

    The sole purpose of this function is to provide a means of fine tuning QByteArray’s memory usage. In general, you will rarely ever need to call this function. If you want to know how many bytes are in the byte array, call [size()](#size).

    **Note:** a statically allocated byte array will report a capacity of 0, even if it’s not empty.

    **Note:** The free space position in the allocated memory block is undefined. In other words, one should not assume that the free memory is always located after the initialized elements.

    See also

    [reserve()](#reserve), [squeeze()](#squeeze).

---

chop(int)
:   Removes *n* bytes from the end of the byte array.

    If *n* is greater than [size()](#size), the result is an empty byte array.

    Example:

    ```
    # QByteArray ba("STARTTLS\r\n");
    # ba.chop(2);                 // ba == "STARTTLS"
    ```

    See also

    [truncate()](#truncate), [resize()](#resize), [first()](#first).

---

chopped(int) → QByteArray
:   Returns a byte array that contains the leftmost [size()](#size) - *len* bytes of this byte array.

    **Note:** The behavior is undefined if *len* is negative or greater than [size()](#size).

    See also

    [endsWith()](#endsWith), [first()](#first), [last()](#last), [sliced()](#sliced), [chop()](#chop), [truncate()](#truncate).

---

clear()
:   Clears the contents of the byte array and makes it null.

    See also

    [resize()](#resize), [isNull()](#isNull).

---

compare(QByteArray|bytes|bytearray|memoryview, cs: [CaseSensitivity](qt.html#CaseSensitivity) = [CaseSensitive](qt.html#CaseSensitivity-CaseSensitive)) → int
:   Returns an integer less than, equal to, or greater than zero depending on whether this QByteArray sorts before, at the same position as, or after the QByteArrayView *bv*. The comparison is performed according to case sensitivity *cs*.

    See also

    operator==, [Character Case](#qbytearray-character-case).

---

contains(QByteArray|bytes|bytearray|memoryview) → bool
:   Returns `true` if this byte array contains an occurrence of the sequence of bytes viewed by *bv*; otherwise returns `false`.

    See also

    [indexOf()](#indexOf), [count()](#count).

---

\_\_contains\_\_(QByteArray|bytes|bytearray|memoryview) → int
:   TODO

---

count() → int
:   Use [size()](#size) or [length()](#length) instead.

    Same as [size()](#size).

---

count(QByteArray|bytes|bytearray|memoryview) → int
:   Returns the number of (potentially overlapping) occurrences of the sequence of bytes viewed by *bv* in this byte array.

    See also

    [contains()](#contains), [indexOf()](#indexOf).

---

data() → bytes
:   Returns a pointer to the data stored in the byte array. The pointer can be used to access and modify the bytes that compose the array. The data is ‘`\0`’-terminated, i.e. the number of bytes you can access following the returned pointer is [size()](#size) + 1, including the ‘`\0`’ terminator.

    Example:

    ```
    # QByteArray ba("Hello world");
    # char *data = ba.data();
    # while (*data) {
    #     cout << "[" << *data << "]" << Qt::endl;
    #     ++data;
    # }
    ```

    The pointer remains valid as long as no detach happens and the QByteArray is not modified.

    For read-only access, constData() is faster because it never causes a [deep copy](https://doc.qt.io/qt-6/implicit-sharing.html#deep-copy) to occur.

    This function is mostly useful to pass a byte array to a function that accepts a `const char \*`.

    The following example makes a copy of the char\* returned by data(), but it will corrupt the heap and cause a crash because it does not allocate a byte for the ‘`\0`’ at the end:

    ```
    # QString tmp = "test";
    # QByteArray text = tmp.toLocal8Bit();
    # char *data = new char[text.size()];
    # strcpy(data, text.data());
    # delete [] data;
    ```

    This one allocates the correct amount of space:

    ```
    # QString tmp = "test";
    # QByteArray text = tmp.toLocal8Bit();
    # char *data = new char[text.size() + 1];
    # strcpy(data, text.data());
    # delete [] data;
    ```

    Note: A QByteArray can store any byte values including ‘`\0`’s, but most functions that take `char \*` arguments assume that the data ends at the first ‘`\0`’ they encounter.

    See also

    constData(), operator[]().

---

endsWith(QByteArray|bytes|bytearray|memoryview) → bool
:   Returns `true` if this byte array ends with the sequence of bytes viewed by *bv*; otherwise returns `false`.

    Example:

    ```
    # QByteArray url("http://qt-project.org/doc/qt-5.0/qtdoc/index.html");
    # if (url.endsWith(".html"))
    #     ...
    ```

    See also

    [startsWith()](#startsWith), [last()](#last).

---

\_\_eq\_\_(str|None) → bool
:   TODO

---

\_\_eq\_\_(QByteArray|bytes|bytearray|memoryview) → bool
:   TODO

---

fill(bytes, size: int = -1) → QByteArray
:   Sets every byte in the byte array to *ch*. If *size* is different from -1 (the default), the byte array is resized to size *size* beforehand.

    Example:

    ```
    # QByteArray ba("Istambul");
    # ba.fill('o');
    # // ba == "oooooooo"

    # ba.fill('X', 2);
    # // ba == "XX"
    ```

    See also

    [resize()](#resize).

---

first(int) → QByteArray
:   Returns the first *n* bytes of the byte array.

    **Note:** The behavior is undefined when *n* < 0 or *n* > [size()](#size).

    Example:

    ```
    # QByteArray x("Pineapple");
    # QByteArray y = x.first(4);
    # // y == "Pine"
    ```

    See also

    [last()](#last), [sliced()](#sliced), [startsWith()](#startsWith), [chopped()](#chopped), [chop()](#chop), [truncate()](#truncate).

---

@staticmethod fromBase64(QByteArray|bytes|bytearray|memoryview, options: [Base64Option](#Base64Option) = [Base64Encoding](#Base64Option-Base64Encoding)) → QByteArray
:   Returns a decoded copy of the Base64 array *base64*, using the options defined by *options*. If *options* contains `IgnoreBase64DecodingErrors` (the default), the input is not checked for validity; invalid characters in the input are skipped, enabling the decoding process to continue with subsequent characters. If *options* contains `AbortOnBase64DecodingErrors`, then decoding will stop at the first invalid character.

    For example:

    ```
    # QByteArray text = QByteArray::fromBase64("UXQgaXMgZ3JlYXQh");
    # text.data();            // returns "Qt is great!"

    # QByteArray::fromBase64("PHA+SGVsbG8/PC9wPg==", QByteArray::Base64Encoding); // returns "<p>Hello?</p>"
    # QByteArray::fromBase64("PHA-SGVsbG8_PC9wPg==", QByteArray::Base64UrlEncoding); // returns "<p>Hello?</p>"
    ```

    The algorithm used to decode Base64-encoded data is defined in RFC 4648.

    Returns the decoded data, or, if the `AbortOnBase64DecodingErrors` option was passed and the input data was invalid, an empty byte array.

    **Note:** The [fromBase64Encoding()](#fromBase64Encoding) function is recommended in new code.

    See also

    [toBase64()](#toBase64), [fromBase64Encoding()](#fromBase64Encoding).

---

@staticmethod fromBase64Encoding(QByteArray|bytes|bytearray|memoryview, options: [Base64Option](#Base64Option) = [Base64Encoding](#Base64Option-Base64Encoding)) → [FromBase64Result](qbytearray-frombase64result.html)
:   TODO

---

@staticmethod fromHex(QByteArray|bytes|bytearray|memoryview) → QByteArray
:   Returns a decoded copy of the hex encoded array *hexEncoded*. Input is not checked for validity; invalid characters in the input are skipped, enabling the decoding process to continue with subsequent characters.

    For example:

    ```
    # QByteArray text = QByteArray::fromHex("517420697320677265617421");
    # text.data();            // returns "Qt is great!"
    ```

    See also

    [toHex()](#toHex).

---

@staticmethod fromPercentEncoding(QByteArray|bytes|bytearray|memoryview, percent: str = '%') → QByteArray
:   Decodes *input* from URI/URL-style percent-encoding.

    Returns a byte array containing the decoded text. The *percent* parameter allows use of a different character than ‘%’ (for instance, ‘\_’ or ‘=’) as the escape character. Equivalent to input.[percentDecoded()](#percentDecoded)(percent).

    For example:

    ```
    # QByteArray text = QByteArray::fromPercentEncoding("Qt%20is%20great%33");
    # text.data();            // returns "Qt is great!"
    ```

    See also

    [percentDecoded()](#percentDecoded).

---

\_\_ge\_\_(str|None) → bool
:   TODO

---

\_\_ge\_\_(QByteArray|bytes|bytearray|memoryview) → bool
:   TODO

---

\_\_getitem\_\_(int) → bytes
:   TODO

---

\_\_getitem\_\_(slice) → QByteArray
:   TODO

---

\_\_gt\_\_(str|None) → bool
:   TODO

---

\_\_gt\_\_(QByteArray|bytes|bytearray|memoryview) → bool
:   TODO

---

\_\_hash\_\_() → int
:   TODO

---

\_\_iadd\_\_(QByteArray|bytes|bytearray|memoryview) → QByteArray
:   TODO

---

\_\_imul\_\_(int) → QByteArray
:   TODO

---

indexOf(QByteArray|bytes|bytearray|memoryview, from: int = 0) → int
:   Returns the index position of the start of the first occurrence of the sequence of bytes viewed by *bv* in this byte array, searching forward from index position *from*. Returns -1 if no match is found.

    Example:

    ```
    # QByteArray x("sticky question");
    # QByteArrayView y("sti");
    # x.indexOf(y);               // returns 0
    # x.indexOf(y, 1);            // returns 10
    # x.indexOf(y, 10);           // returns 10
    # x.indexOf(y, 11);           // returns -1
    ```

    See also

    [lastIndexOf()](#lastIndexOf), [contains()](#contains), [count()](#count).

---

insert(int, QByteArray|bytes|bytearray|memoryview) → QByteArray
:   Inserts *data* at index position *i* and returns a reference to this byte array.

    Example:

    ```
    # QByteArray ba("Meal");
    # ba.insert(1, QByteArrayView("ontr"));
    # // ba == "Montreal"
    ```

    For large byte arrays, this operation can be slow ([linear time](https://doc.qt.io/qt-6/containers.html#linear-time)), because it requires moving all the bytes at indexes *i* and above by at least one position further in memory.

    This array grows to accommodate the insertion. If *i* is beyond the end of the array, the array is first extended with space characters to reach this *i*.

    See also

    [append()](#append), [prepend()](#prepend), [replace()](#replace), [remove()](#remove).

---

insert(int, int, bytes) → QByteArray
:   Inserts *count* copies of byte *ch* at index position *i* in the byte array.

    This array grows to accommodate the insertion. If *i* is beyond the end of the array, the array is first extended with space characters to reach this *i*.

---

isEmpty() → bool
:   Returns `true` if the byte array has size 0; otherwise returns `false`.

    Example:

    ```
    # QByteArray().isEmpty();         // returns true
    # QByteArray("").isEmpty();       // returns true
    # QByteArray("abc").isEmpty();    // returns false
    ```

    See also

    [size()](#size).

---

isLower() → bool
:   Returns `true` if this byte array is lowercase, that is, if it’s identical to its [toLower()](#toLower) folding.

    Note that this does *not* mean that the byte array only contains lowercase letters; only that it contains no ASCII uppercase letters.

    See also

    [isUpper()](#isUpper), [toLower()](#toLower).

---

isNull() → bool
:   Returns `true` if this byte array is null; otherwise returns `false`.

    Example:

    ```
    # QByteArray().isNull();          // returns true
    # QByteArray("").isNull();        // returns false
    # QByteArray("abc").isNull();     // returns false
    ```

    Qt makes a distinction between null byte arrays and empty byte arrays for historical reasons. For most applications, what matters is whether or not a byte array contains any data, and this can be determined using [isEmpty()](#isEmpty).

    See also

    [isEmpty()](#isEmpty).

---

isUpper() → bool
:   Returns `true` if this byte array is uppercase, that is, if it’s identical to its [toUpper()](#toUpper) folding.

    Note that this does *not* mean that the byte array only contains uppercase letters; only that it contains no ASCII lowercase letters.

    See also

    [isLower()](#isLower), [toUpper()](#toUpper).

---

isValidUtf8() → bool
:   Returns `true` if this byte array contains valid UTF-8 encoded data, or `false` otherwise.

---

last(int) → QByteArray
:   Returns the last *n* bytes of the byte array.

    **Note:** The behavior is undefined when *n* < 0 or *n* > [size()](#size).

    Example:

    ```
    # QByteArray x("Pineapple");
    # QByteArray y = x.last(5);
    # // y == "apple"
    ```

    See also

    [first()](#first), [sliced()](#sliced), [endsWith()](#endsWith), [chopped()](#chopped), [chop()](#chop), [truncate()](#truncate).

---

lastIndexOf(QByteArray|bytes|bytearray|memoryview, from: int = -1) → int
:   Returns the index position of the start of the last occurrence of the sequence of bytes viewed by *bv* in this byte array, searching backward from index position *from*.

    If *from* is -1, the search starts at the last character; if it is -2, at the next to last character and so on.

    Returns -1 if no match is found.

    Example:

    ```
    # QByteArray x("crazy azimuths");
    # QByteArrayView y("az");
    # x.lastIndexOf(y);           // returns 6
    # x.lastIndexOf(y, 6);        // returns 6
    # x.lastIndexOf(y, 5);        // returns 2
    # x.lastIndexOf(y, 1);        // returns -1
    ```

    **Note:** When searching for a 0-length *bv*, the match at the end of the data is excluded from the search by a negative *from*, even though `-1` is normally thought of as searching from the end of the byte array: the match at the end is *after* the last character, so it is excluded. To include such a final empty match, either give a positive value for *from* or omit the *from* parameter entirely.

    See also

    [indexOf()](#indexOf), [contains()](#contains), [count()](#count).

---

\_\_le\_\_(str|None) → bool
:   TODO

---

\_\_le\_\_(QByteArray|bytes|bytearray|memoryview) → bool
:   TODO

---

left(int) → QByteArray
:   Returns a byte array that contains the first *len* bytes of this byte array.

    If you know that *len* cannot be out of bounds, use [first()](#first) instead in new code, because it is faster.

    The entire byte array is returned if *len* is greater than [size()](#size).

    Returns an empty QByteArray if *len* is smaller than 0.

    See also

    [first()](#first), [last()](#last), [startsWith()](#startsWith), [chopped()](#chopped), [chop()](#chop), [truncate()](#truncate).

---

leftJustified(int, fill: bytes = ' ', truncate: bool = False) → QByteArray
:   Returns a byte array of size *width* that contains this byte array padded with the *fill* byte.

    If *truncate* is false and the [size()](#size) of the byte array is more than *width*, then the returned byte array is a copy of this byte array.

    If *truncate* is true and the [size()](#size) of the byte array is more than *width*, then any bytes in a copy of the byte array after position *width* are removed, and the copy is returned.

    Example:

    ```
    # QByteArray x("apple");
    # QByteArray y = x.leftJustified(8, '.');   // y == "apple..."
    ```

    See also

    [rightJustified()](#rightJustified).

---

\_\_len\_\_() → int
:   TODO

---

length() → int
:   Same as [size()](#size).

---

\_\_lt\_\_(str|None) → bool
:   TODO

---

\_\_lt\_\_(QByteArray|bytes|bytearray|memoryview) → bool
:   TODO

---

max\_size() → int
:   TODO

---

@staticmethod maxSize() → int
:   TODO

---

mid(int, length: int = -1) → QByteArray
:   Returns a byte array containing *len* bytes from this byte array, starting at position *pos*.

    If you know that *pos* and *len* cannot be out of bounds, use [sliced()](#sliced) instead in new code, because it is faster.

    If *len* is -1 (the default), or *pos* + *len* >= [size()](#size), returns a byte array containing all bytes starting at position *pos* until the end of the byte array.

    See also

    [first()](#first), [last()](#last), [sliced()](#sliced), [chopped()](#chopped), [chop()](#chop), [truncate()](#truncate).

---

\_\_mul\_\_(int) → QByteArray
:   TODO

---

\_\_ne\_\_(str|None) → bool
:   TODO

---

\_\_ne\_\_(QByteArray|bytes|bytearray|memoryview) → bool
:   TODO

---

nullTerminate() → QByteArray
:   If this byte array’s data isn’t null-terminated, this method will make a deep-copy of the data and make it null-terminated.

    A QByteArray is null-terminated by default, however in some cases (e.g. when using fromRawData()), the data doesn’t necessarily end with a `\0` character, which could be a problem when calling methods that expect a null-terminated string (for example, C API).

    See also

    [nullTerminated()](#nullTerminated), fromRawData(), setRawData().

---

nullTerminated() → QByteArray
:   TODO

---

@staticmethod number(int, base: int = 10) → QByteArray
:   TODO

---

@staticmethod number(float, format: str = 'g', precision: int = 6) → QByteArray
:   Returns a byte-array representing the floating-point number *n* as text.

    Returns a byte array containing a string representing *n*, with a given *format* and *precision*, with the same meanings as for QLocale::toString(double, char, int). For example:

    ```
    # QByteArray ba = QByteArray::number(12.3456, 'E', 3);
    # // ba == 1.235E+01
    ```

    See also

    [toDouble()](#toDouble), [FloatingPointPrecisionOption](qlocale.html#FloatingPointPrecisionOption).

---

percentDecoded(percent: str = '%') → QByteArray
:   Decodes URI/URL-style percent-encoding.

    Returns a byte array containing the decoded text. The *percent* parameter allows use of a different character than ‘%’ (for instance, ‘\_’ or ‘=’) as the escape character.

    For example:

    ```
    # This code needs porting to Python.

    # /****************************************************************************
    # **
    # ** Copyright (C) 2016 The Qt Company Ltd.
    # ** Contact: https://www.qt.io/licensing/
    # **
    # ** This file is part of the documentation of the Qt Toolkit.
    # **
    # ** $QT_BEGIN_LICENSE:BSD$
    # ** Commercial License Usage
    # ** Licensees holding valid commercial Qt licenses may use this file in
    # ** accordance with the commercial license agreement provided with the
    # ** Software or, alternatively, in accordance with the terms contained in
    # ** a written agreement between you and The Qt Company. For licensing terms
    # ** and conditions see https://www.qt.io/terms-conditions. For further
    # ** information use the contact form at https://www.qt.io/contact-us.
    # **
    # ** BSD License Usage
    # ** Alternatively, you may use this file under the terms of the BSD license
    # ** as follows:
    # **
    # ** "Redistribution and use in source and binary forms, with or without
    # ** modification, are permitted provided that the following conditions are
    # ** met:
    # **   * Redistributions of source code must retain the above copyright
    # **     notice, this list of conditions and the following disclaimer.
    # **   * Redistributions in binary form must reproduce the above copyright
    # **     notice, this list of conditions and the following disclaimer in
    # **     the documentation and/or other materials provided with the
    # **     distribution.
    # **   * Neither the name of The Qt Company Ltd nor the names of its
    # **     contributors may be used to endorse or promote products derived
    # **     from this software without specific prior written permission.
    # **
    # **
    # ** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    # ** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    # ** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    # ** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    # ** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    # ** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    # ** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    # ** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    # ** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # ** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    # ** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
    # **
    # ** $QT_END_LICENSE$
    # **
    # ****************************************************************************/

    # void wrapInFunction()
    # {

    # #! [0]
    # QByteArray ba("Hello");
    # #! [0]

    # #! [1]
    # QByteArray ba;
    # ba.resize(5);
    # ba[0] = 0x3c;
    # ba[1] = 0xb8;
    # ba[2] = 0x64;
    # ba[3] = 0x18;
    # ba[4] = 0xca;
    # #! [1]

    # #! [2]
    # for (qsizetype i = 0; i < ba.size(); ++i) {
    #     if (ba.at(i) >= 'a' && ba.at(i) <= 'f')
    #         cout << "Found character in range [a-f]" << Qt::endl;
    # }
    # #! [2]

    # #! [3]
    # QByteArray x("and");
    # x.prepend("rock ");         // x == "rock and"
    # x.append(" roll");          // x == "rock and roll"
    # x.replace(5, 3, "&");       // x == "rock & roll"
    # #! [3]

    # #! [4]
    # QByteArray ba("We must be <b>bold</b>, very <b>bold</b>");
    # qsizetype j = 0;
    # while ((j = ba.indexOf("<b>", j)) != -1) {
    #     cout << "Found <b> tag at index position " << j << Qt::endl;
    #     ++j;
    # }
    # #! [4]

    # #! [5]
    # QByteArray().isNull();          // returns true
    # QByteArray().isEmpty();         // returns true

    # QByteArray("").isNull();        // returns false
    # QByteArray("").isEmpty();       // returns true

    # QByteArray("abc").isNull();     // returns false
    # QByteArray("abc").isEmpty();    // returns false
    # #! [5]

    # #! [6]
    # QByteArray ba("Hello");
    # qsizetype n = ba.size();    // n == 5
    # ba.data()[0];               // returns 'H'
    # ba.data()[4];               // returns 'o'
    # ba.data()[5];               // returns '\0'
    # #! [6]

    # #! [7]
    # QByteArray().isEmpty();         // returns true
    # QByteArray("").isEmpty();       // returns true
    # QByteArray("abc").isEmpty();    // returns false
    # #! [7]

    # #! [8]
    # QByteArray ba("Hello world");
    # char *data = ba.data();
    # while (*data) {
    #     cout << "[" << *data << "]" << Qt::endl;
    #     ++data;
    # }
    # #! [8]

    # #! [9]
    # QByteArray ba("Hello, world");
    # cout << ba[0]; // prints H
    # ba[7] = 'W';
    # // ba == "Hello, World"
    # #! [9]

    # #! [10]
    # QByteArray ba("Stockholm");
    # ba.truncate(5);             // ba == "Stock"
    # #! [10]

    # #! [11]
    # QByteArray ba("STARTTLS\r\n");
    # ba.chop(2);                 // ba == "STARTTLS"
    # #! [11]

    # #! [12]
    # QByteArray x("free");
    # QByteArray y("dom");
    # x += y;
    # // x == "freedom"
    # #! [12]

    # #! [13]
    # QByteArray().isNull();          // returns true
    # QByteArray("").isNull();        // returns false
    # QByteArray("abc").isNull();     // returns false
    # #! [13]

    # #! [14]
    # QByteArray ba("Istambul");
    # ba.fill('o');
    # // ba == "oooooooo"

    # ba.fill('X', 2);
    # // ba == "XX"
    # #! [14]

    # #! [15]
    # QByteArray x("ship");
    # QByteArray y("air");
    # x.prepend(y);
    # // x == "airship"
    # #! [15]

    # #! [16]
    # QByteArray x("free");
    # QByteArray y("dom");
    # x.append(y);
    # // x == "freedom"
    # #! [16]

    # #! [17]
    # QByteArray ba("Meal");
    # ba.insert(1, QByteArrayView("ontr"));
    # // ba == "Montreal"
    # #! [17]

    # #! [18]
    # QByteArray ba("Montreal");
    # ba.remove(1, 4);
    # // ba == "Meal"
    # #! [18]

    # #! [19]
    # QByteArray x("Say yes!");
    # QByteArray y("no");
    # x.replace(4, 3, y);
    # // x == "Say no!"
    # #! [19]

    # #! [20]
    # QByteArray ba("colour behaviour flavour neighbour");
    # ba.replace(QByteArray("ou"), QByteArray("o"));
    # // ba == "color behavior flavor neighbor"
    # #! [20]

    # #! [21]
    # QByteArray x("sticky question");
    # QByteArrayView y("sti");
    # x.indexOf(y);               // returns 0
    # x.indexOf(y, 1);            // returns 10
    # x.indexOf(y, 10);           // returns 10
    # x.indexOf(y, 11);           // returns -1
    # #! [21]

    # #! [22]
    # QByteArray ba("ABCBA");
    # ba.indexOf("B");            // returns 1
    # ba.indexOf("B", 1);         // returns 1
    # ba.indexOf("B", 2);         // returns 3
    # ba.indexOf("X");            // returns -1
    # #! [22]

    # #! [23]
    # QByteArray x("crazy azimuths");
    # QByteArrayView y("az");
    # x.lastIndexOf(y);           // returns 6
    # x.lastIndexOf(y, 6);        // returns 6
    # x.lastIndexOf(y, 5);        // returns 2
    # x.lastIndexOf(y, 1);        // returns -1
    # #! [23]

    # #! [24]
    # QByteArray ba("ABCBA");
    # ba.lastIndexOf("B");        // returns 3
    # ba.lastIndexOf("B", 3);     // returns 3
    # ba.lastIndexOf("B", 2);     // returns 1
    # ba.lastIndexOf("X");        // returns -1
    # #! [24]

    # #! [25]
    # QByteArray url("ftp://ftp.qt-project.org/");
    # if (url.startsWith("ftp:"))
    #     ...
    # #! [25]

    # #! [26]
    # QByteArray url("http://qt-project.org/doc/qt-5.0/qtdoc/index.html");
    # if (url.endsWith(".html"))
    #     ...
    # #! [26]

    # #! [27]
    # QByteArray x("Pineapple");
    # QByteArray y = x.first(4);
    # // y == "Pine"
    # #! [27]

    # #! [28]
    # QByteArray x("Pineapple");
    # QByteArray y = x.last(5);
    # // y == "apple"
    # #! [28]

    # #! [29]
    # QByteArray x("Five pineapples");
    # QByteArray y = x.sliced(5, 4);     // y == "pine"
    # QByteArray z = x.sliced(5);        // z == "pineapples"
    # #! [29]

    # #! [30]
    # QByteArray x("Qt by THE QT COMPANY");
    # QByteArray y = x.toLower();
    # // y == "qt by the qt company"
    # #! [30]

    # #! [31]
    # QByteArray x("Qt by THE QT COMPANY");
    # QByteArray y = x.toUpper();
    # // y == "QT BY THE QT COMPANY"
    # #! [31]

    # #! [32]
    # QByteArray ba("  lots\t of\nwhitespace\r\n ");
    # ba = ba.simplified();
    # // ba == "lots of whitespace";
    # #! [32]

    # #! [33]
    # QByteArray ba("  lots\t of\nwhitespace\r\n ");
    # ba = ba.trimmed();
    # // ba == "lots\t of\nwhitespace";
    # #! [33]

    # #! [34]
    # QByteArray x("apple");
    # QByteArray y = x.leftJustified(8, '.');   // y == "apple..."
    # #! [34]

    # #! [35]
    # QByteArray x("apple");
    # QByteArray y = x.rightJustified(8, '.');    // y == "...apple"
    # #! [35]

    # #! [36]
    # QByteArray str("FF");
    # bool ok;
    # int hex = str.toInt(&ok, 16);     // hex == 255, ok == true
    # int dec = str.toInt(&ok, 10);     // dec == 0, ok == false
    # #! [36]

    # #! [37]
    # QByteArray str("FF");
    # bool ok;
    # long hex = str.toLong(&ok, 16);   // hex == 255, ok == true
    # long dec = str.toLong(&ok, 10);   // dec == 0, ok == false
    # #! [37]

    # #! [38]
    # QByteArray string("1234.56");
    # bool ok;
    # double a = string.toDouble(&ok);   // a == 1234.56, ok == true

    # string = "1234.56 Volt";
    # a = str.toDouble(&ok);             // a == 0, ok == false
    # #! [38]

    # #! [38float]
    # QByteArray string("1234.56");
    # bool ok;
    # float a = string.toFloat(&ok);    // a == 1234.56, ok == true

    # string = "1234.56 Volt";
    # a = str.toFloat(&ok);              // a == 0, ok == false
    # #! [38float]

    # #! [39]
    # QByteArray text("Qt is great!");
    # text.toBase64();        // returns "UXQgaXMgZ3JlYXQh"

    # QByteArray text("<p>Hello?</p>");
    # text.toBase64(QByteArray::Base64Encoding | QByteArray::OmitTrailingEquals);      // returns "PHA+SGVsbG8/PC9wPg"
    # text.toBase64(QByteArray::Base64Encoding);                                       // returns "PHA+SGVsbG8/PC9wPg=="
    # text.toBase64(QByteArray::Base64UrlEncoding);                                    // returns "PHA-SGVsbG8_PC9wPg=="
    # text.toBase64(QByteArray::Base64UrlEncoding | QByteArray::OmitTrailingEquals);   // returns "PHA-SGVsbG8_PC9wPg"
    # #! [39]

    # #! [40]
    # QByteArray ba;
    # int n = 63;
    # ba.setNum(n);           // ba == "63"
    # ba.setNum(n, 16);       // ba == "3f"
    # #! [40]

    # #! [41]
    # int n = 63;
    # QByteArray::number(n);              // returns "63"
    # QByteArray::number(n, 16);          // returns "3f"
    # QByteArray::number(n, 16).toUpper();  // returns "3F"
    # #! [41]

    # #! [42]
    # QByteArray ba = QByteArray::number(12.3456, 'E', 3);
    # // ba == 1.235E+01
    # #! [42]

    # #! [43]
    #  static const char mydata[] = {
    #     '\x00', '\x00', '\x03', '\x84', '\x78', '\x9c', '\x3b', '\x76',
    #     '\xec', '\x18', '\xc3', '\x31', '\x0a', '\xf1', '\xcc', '\x99',
    #     ...
    #     '\x6d', '\x5b'
    # };

    # QByteArray data = QByteArray::fromRawData(mydata, sizeof(mydata));
    # QDataStream in(&data, QIODevice::ReadOnly);
    # ...
    # #! [43]

    # #! [44]
    # QByteArray text = QByteArray::fromBase64("UXQgaXMgZ3JlYXQh");
    # text.data();            // returns "Qt is great!"

    # QByteArray::fromBase64("PHA+SGVsbG8/PC9wPg==", QByteArray::Base64Encoding); // returns "<p>Hello?</p>"
    # QByteArray::fromBase64("PHA-SGVsbG8_PC9wPg==", QByteArray::Base64UrlEncoding); // returns "<p>Hello?</p>"
    # #! [44]

    # #! [44ter]
    # void process(const QByteArray &);

    # if (auto result = QByteArray::fromBase64Encoding(encodedData))
    #     process(*result);
    # #! [44ter]

    # #! [44quater]
    # auto result = QByteArray::fromBase64Encoding(encodedData);
    # if (result.decodingStatus == QByteArray::Base64DecodingStatus::Ok)
    #     process(result.decoded);
    # #! [44quater]

    # #! [45]
    # QByteArray text = QByteArray::fromHex("517420697320677265617421");
    # text.data();            // returns "Qt is great!"
    # #! [45]

    # #! [46]
    # QString tmp = "test";
    # QByteArray text = tmp.toLocal8Bit();
    # char *data = new char[text.size()];
    # strcpy(data, text.data());
    # delete [] data;
    # #! [46]

    # #! [47]
    # QString tmp = "test";
    # QByteArray text = tmp.toLocal8Bit();
    # char *data = new char[text.size() + 1];
    # strcpy(data, text.data());
    # delete [] data;
    # #! [47]

    # #! [48]
    # QByteArray ba1("ca\0r\0t");
    # ba1.size();                     // Returns 2.
    # ba1.constData();                // Returns "ca" with terminating \0.

    # QByteArray ba2("ca\0r\0t", 3);
    # ba2.size();                     // Returns 3.
    # ba2.constData();                // Returns "ca\0" with terminating \0.

    # QByteArray ba3("ca\0r\0t", 4);
    # ba3.size();                     // Returns 4.
    # ba3.constData();                // Returns "ca\0r" with terminating \0.

    # const char cart[] = {'c', 'a', '\0', 'r', '\0', 't'};
    # QByteArray ba4(QByteArray::fromRawData(cart, 6));
    # ba4.size();                     // Returns 6.
    # ba4.constData();                // Returns "ca\0r\0t" without terminating \0.
    # #! [48]

    # #! [49]
    # QByteArray ba("ab");
    # ba.repeated(4);             // returns "abababab"
    # #! [49]

    # #! [50]
    # QByteArray macAddress = QByteArray::fromHex("123456abcdef");
    # macAddress.toHex(':'); // returns "12:34:56:ab:cd:ef"
    # macAddress.toHex(0);   // returns "123456abcdef"
    # #! [50]

    # #! [51]
    # QByteArray text = QByteArray::fromPercentEncoding("Qt%20is%20great%33");
    # text.data();            // returns "Qt is great!"
    # #! [51]

    # #! [52]
    # QByteArray text = "{a fishy string?}";
    # QByteArray ba = text.toPercentEncoding("{}", "s");
    # qDebug(ba.constData());
    # // prints "{a fi%73hy %73tring%3F}"
    # #! [52]

    # #! [53]
    # QByteArray ba = QByteArrayLiteral("byte array contents");
    # #! [53]
    # }
    ```

    **Note:** Given invalid input (such as a string containing the sequence “%G5”, which is not a valid hexadecimal number) the output will be invalid as well. As an example: the sequence “%G5” could be decoded to ‘W’.

    See also

    [toPercentEncoding()](#toPercentEncoding), [fromPercentEncoding()](qurl.html#fromPercentEncoding).

---

prepend(QByteArray|bytes|bytearray|memoryview) → QByteArray
:   Prepends the byte array view *ba* to this byte array and returns a reference to this byte array.

    This operation is typically very fast ([constant time](https://doc.qt.io/qt-6/containers.html#constant-time)), because QByteArray preallocates extra space at the beginning of the data, so it can grow without reallocating the entire array each time.

    Example:

    ```
    # QByteArray x("ship");
    # QByteArray y("air");
    # x.prepend(y);
    # // x == "airship"
    ```

    This is the same as insert(0, *ba*).

    See also

    [append()](#append), [insert()](#insert).

---

prepend(int, bytes) → QByteArray
:   Prepends *count* copies of byte *ch* to this byte array.

---

push\_back(QByteArray|bytes|bytearray|memoryview)
:   Same as append(*str*).

---

push\_front(QByteArray|bytes|bytearray|memoryview)
:   Same as prepend(*str*).

---

remove(int, int) → QByteArray
:   Removes *len* bytes from the array, starting at index position *pos*, and returns a reference to the array.

    If *pos* is out of range, nothing happens. If *pos* is valid, but *pos* + *len* is larger than the size of the array, the array is truncated at position *pos*.

    Example:

    ```
    # QByteArray ba("Montreal");
    # ba.remove(1, 4);
    # // ba == "Meal"
    ```

    Element removal will preserve the array’s capacity and not reduce the amount of allocated memory. To shed extra capacity and free as much memory as possible, call [squeeze()](#squeeze) after the last change to the array’s size.

    See also

    [insert()](#insert), [replace()](#replace), [squeeze()](#squeeze).

---

removeAt(int) → QByteArray
:   Removes the character at index *pos*. If *pos* is out of bounds (i.e. *pos* >= [size()](#size)) this function does nothing.

    See also

    [remove()](#remove).

---

removeFirst() → QByteArray
:   Removes the first character in this byte array. If the byte array is empty, this function does nothing.

    See also

    [remove()](#remove).

---

removeLast() → QByteArray
:   Removes the last character in this byte array. If the byte array is empty, this function does nothing.

    See also

    [remove()](#remove).

---

repeated(int) → QByteArray
:   Returns a copy of this byte array repeated the specified number of *times*.

    If *times* is less than 1, an empty byte array is returned.

    Example:

    ```
    # QByteArray ba("ab");
    # ba.repeated(4);             // returns "abababab"
    ```

---

replace(QByteArray|bytes|bytearray|memoryview, QByteArray|bytes|bytearray|memoryview) → QByteArray
:   Replaces every occurrence of the byte array *before* with the byte array *after*.

    Example:

    ```
    # QByteArray ba("colour behaviour flavour neighbour");
    # ba.replace(QByteArray("ou"), QByteArray("o"));
    # // ba == "color behavior flavor neighbor"
    ```

---

replace(int, int, QByteArray|bytes|bytearray|memoryview) → QByteArray
:   Replaces *len* bytes from index position *pos* with the byte array *after*, and returns a reference to this byte array.

    Example:

    ```
    # QByteArray x("Say yes!");
    # QByteArray y("no");
    # x.replace(4, 3, y);
    # // x == "Say no!"
    ```

    See also

    [insert()](#insert), [remove()](#remove).

---

\_\_repr\_\_() → str
:   TODO

---

reserve(int)
:   Attempts to allocate memory for at least *size* bytes.

    If you know in advance how large the byte array will be, you can call this function, and if you call [resize()](#resize) often you are likely to get better performance.

    If in doubt about how much space shall be needed, it is usually better to use an upper bound as *size*, or a high estimate of the most likely size, if a strict upper bound would be much bigger than this. If *size* is an underestimate, the array will grow as needed once the reserved size is exceeded, which may lead to a larger allocation than your best overestimate would have and will slow the operation that triggers it.

    **Warning:** reserves memory but does not change the size of the byte array. Accessing data beyond the end of the byte array is undefined behavior. If you need to access memory beyond the current end of the array, use [resize()](#resize).

    The sole purpose of this function is to provide a means of fine tuning QByteArray’s memory usage. In general, you will rarely ever need to call this function.

    See also

    [squeeze()](#squeeze), [capacity()](#capacity).

---

resize(int)
:   Sets the size of the byte array to *size* bytes.

    If *size* is greater than the current size, the byte array is extended to make it *size* bytes with the extra bytes added to the end. The new bytes are uninitialized.

    If *size* is less than the current size, bytes beyond position *size* are excluded from the byte array.

    **Note:** While will grow the capacity if needed, it never shrinks capacity. To shed excess capacity, use [squeeze()](#squeeze).

    See also

    [size()](#size), [truncate()](#truncate), [squeeze()](#squeeze).

---

resize(int, str)
:   Sets the size of the byte array to *newSize* bytes.

    If *newSize* is greater than the current size, the byte array is extended to make it *newSize* bytes with the extra bytes added to the end. The new bytes are initialized to *c*.

    If *newSize* is less than the current size, bytes beyond position *newSize* are excluded from the byte array.

    **Note:** While [resize()](#resize) will grow the capacity if needed, it never shrinks capacity. To shed excess capacity, use [squeeze()](#squeeze).

    See also

    [size()](#size), [truncate()](#truncate), [squeeze()](#squeeze).

---

right(int) → QByteArray
:   Returns a byte array that contains the last *len* bytes of this byte array.

    If you know that *len* cannot be out of bounds, use [last()](#last) instead in new code, because it is faster.

    The entire byte array is returned if *len* is greater than [size()](#size).

    Returns an empty QByteArray if *len* is smaller than 0.

    See also

    [endsWith()](#endsWith), [last()](#last), [first()](#first), [sliced()](#sliced), [chopped()](#chopped), [chop()](#chop), [truncate()](#truncate).

---

rightJustified(int, fill: bytes = ' ', truncate: bool = False) → QByteArray
:   Returns a byte array of size *width* that contains the *fill* byte followed by this byte array.

    If *truncate* is false and the size of the byte array is more than *width*, then the returned byte array is a copy of this byte array.

    If *truncate* is true and the size of the byte array is more than *width*, then the resulting byte array is truncated at position *width*.

    Example:

    ```
    # QByteArray x("apple");
    # QByteArray y = x.rightJustified(8, '.');    // y == "...apple"
    ```

    See also

    [leftJustified()](#leftJustified).

---

setNum(int, base: int = 10) → QByteArray
:   TODO

---

setNum(float, format: str = 'g', precision: int = 6) → QByteArray
:   Represent the floating-point number *n* as text.

    Sets this byte array to a string representing *n*, with a given *format* and *precision* (with the same meanings as for QString::number(double, char, int)), and returns a reference to this byte array.

    See also

    [toDouble()](#toDouble), [FloatingPointPrecisionOption](qlocale.html#FloatingPointPrecisionOption).

---

simplified() → QByteArray
:   Returns a copy of this byte array that has spacing characters removed from the start and end, and in which each sequence of internal spacing characters is replaced with a single space.

    The spacing characters are those for which the standard C++ `isspace()` function returns `true` in the C locale; these are the ASCII characters tabulation ‘`\t`’, line feed ‘`\n`’, carriage return ‘`\r`’, vertical tabulation ‘`\v`’, form feed ‘`\f`’, and space ‘ ‘.

    Example:

    ```
    # QByteArray ba("  lots\t of\nwhitespace\r\n ");
    # ba = ba.simplified();
    # // ba == "lots of whitespace";
    ```

    See also

    [trimmed()](#trimmed), QChar::SpecialCharacter, [Spacing Characters](#qbytearray-spacing-characters).

---

size() → int
:   Returns the number of bytes in this byte array.

    The last byte in the byte array is at position size() - 1. In addition, QByteArray ensures that the byte at position size() is always ‘`\0`’, so that you can use the return value of [data()](#data) and constData() as arguments to functions that expect ‘`\0`’-terminated strings. If the QByteArray object was created from a raw data that didn’t include the trailing ‘`\0`’-termination byte, then QByteArray doesn’t add it automatically unless a [deep copy](https://doc.qt.io/qt-6/implicit-sharing.html#deep-copy) is created.

    Example:

    ```
    # QByteArray ba("Hello");
    # qsizetype n = ba.size();    // n == 5
    # ba.data()[0];               // returns 'H'
    # ba.data()[4];               // returns 'o'
    # ba.data()[5];               // returns '\0'
    ```

    See also

    [isEmpty()](#isEmpty), [resize()](#resize).

---

slice(int) → QByteArray
:   Modifies this byte array to start at position *pos*, extending to its end, and returns a reference to this byte array.

    **Note:** The behavior is undefined if *pos* < 0 or *pos* > [size()](#size).

    See also

    [sliced()](#sliced), [first()](#first), [last()](#last), [chopped()](#chopped), [chop()](#chop), [truncate()](#truncate).

---

slice(int, int) → QByteArray
:   Modifies this byte array to start at position *pos*, extending for *n* bytes, and returns a reference to this byte array.

    **Note:** The behavior is undefined if *pos* < 0, *n* < 0, or *pos* + *n* > [size()](#size).

    Example:

    ```
    # This code needs porting to Python.

    # /****************************************************************************
    # **
    # ** Copyright (C) 2016 The Qt Company Ltd.
    # ** Contact: https://www.qt.io/licensing/
    # **
    # ** This file is part of the documentation of the Qt Toolkit.
    # **
    # ** $QT_BEGIN_LICENSE:BSD$
    # ** Commercial License Usage
    # ** Licensees holding valid commercial Qt licenses may use this file in
    # ** accordance with the commercial license agreement provided with the
    # ** Software or, alternatively, in accordance with the terms contained in
    # ** a written agreement between you and The Qt Company. For licensing terms
    # ** and conditions see https://www.qt.io/terms-conditions. For further
    # ** information use the contact form at https://www.qt.io/contact-us.
    # **
    # ** BSD License Usage
    # ** Alternatively, you may use this file under the terms of the BSD license
    # ** as follows:
    # **
    # ** "Redistribution and use in source and binary forms, with or without
    # ** modification, are permitted provided that the following conditions are
    # ** met:
    # **   * Redistributions of source code must retain the above copyright
    # **     notice, this list of conditions and the following disclaimer.
    # **   * Redistributions in binary form must reproduce the above copyright
    # **     notice, this list of conditions and the following disclaimer in
    # **     the documentation and/or other materials provided with the
    # **     distribution.
    # **   * Neither the name of The Qt Company Ltd nor the names of its
    # **     contributors may be used to endorse or promote products derived
    # **     from this software without specific prior written permission.
    # **
    # **
    # ** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    # ** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    # ** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    # ** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    # ** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    # ** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    # ** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    # ** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    # ** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # ** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    # ** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
    # **
    # ** $QT_END_LICENSE$
    # **
    # ****************************************************************************/

    # void wrapInFunction()
    # {

    # #! [0]
    # QByteArray ba("Hello");
    # #! [0]

    # #! [1]
    # QByteArray ba;
    # ba.resize(5);
    # ba[0] = 0x3c;
    # ba[1] = 0xb8;
    # ba[2] = 0x64;
    # ba[3] = 0x18;
    # ba[4] = 0xca;
    # #! [1]

    # #! [2]
    # for (qsizetype i = 0; i < ba.size(); ++i) {
    #     if (ba.at(i) >= 'a' && ba.at(i) <= 'f')
    #         cout << "Found character in range [a-f]" << Qt::endl;
    # }
    # #! [2]

    # #! [3]
    # QByteArray x("and");
    # x.prepend("rock ");         // x == "rock and"
    # x.append(" roll");          // x == "rock and roll"
    # x.replace(5, 3, "&");       // x == "rock & roll"
    # #! [3]

    # #! [4]
    # QByteArray ba("We must be <b>bold</b>, very <b>bold</b>");
    # qsizetype j = 0;
    # while ((j = ba.indexOf("<b>", j)) != -1) {
    #     cout << "Found <b> tag at index position " << j << Qt::endl;
    #     ++j;
    # }
    # #! [4]

    # #! [5]
    # QByteArray().isNull();          // returns true
    # QByteArray().isEmpty();         // returns true

    # QByteArray("").isNull();        // returns false
    # QByteArray("").isEmpty();       // returns true

    # QByteArray("abc").isNull();     // returns false
    # QByteArray("abc").isEmpty();    // returns false
    # #! [5]

    # #! [6]
    # QByteArray ba("Hello");
    # qsizetype n = ba.size();    // n == 5
    # ba.data()[0];               // returns 'H'
    # ba.data()[4];               // returns 'o'
    # ba.data()[5];               // returns '\0'
    # #! [6]

    # #! [7]
    # QByteArray().isEmpty();         // returns true
    # QByteArray("").isEmpty();       // returns true
    # QByteArray("abc").isEmpty();    // returns false
    # #! [7]

    # #! [8]
    # QByteArray ba("Hello world");
    # char *data = ba.data();
    # while (*data) {
    #     cout << "[" << *data << "]" << Qt::endl;
    #     ++data;
    # }
    # #! [8]

    # #! [9]
    # QByteArray ba("Hello, world");
    # cout << ba[0]; // prints H
    # ba[7] = 'W';
    # // ba == "Hello, World"
    # #! [9]

    # #! [10]
    # QByteArray ba("Stockholm");
    # ba.truncate(5);             // ba == "Stock"
    # #! [10]

    # #! [11]
    # QByteArray ba("STARTTLS\r\n");
    # ba.chop(2);                 // ba == "STARTTLS"
    # #! [11]

    # #! [12]
    # QByteArray x("free");
    # QByteArray y("dom");
    # x += y;
    # // x == "freedom"
    # #! [12]

    # #! [13]
    # QByteArray().isNull();          // returns true
    # QByteArray("").isNull();        // returns false
    # QByteArray("abc").isNull();     // returns false
    # #! [13]

    # #! [14]
    # QByteArray ba("Istambul");
    # ba.fill('o');
    # // ba == "oooooooo"

    # ba.fill('X', 2);
    # // ba == "XX"
    # #! [14]

    # #! [15]
    # QByteArray x("ship");
    # QByteArray y("air");
    # x.prepend(y);
    # // x == "airship"
    # #! [15]

    # #! [16]
    # QByteArray x("free");
    # QByteArray y("dom");
    # x.append(y);
    # // x == "freedom"
    # #! [16]

    # #! [17]
    # QByteArray ba("Meal");
    # ba.insert(1, QByteArrayView("ontr"));
    # // ba == "Montreal"
    # #! [17]

    # #! [18]
    # QByteArray ba("Montreal");
    # ba.remove(1, 4);
    # // ba == "Meal"
    # #! [18]

    # #! [19]
    # QByteArray x("Say yes!");
    # QByteArray y("no");
    # x.replace(4, 3, y);
    # // x == "Say no!"
    # #! [19]

    # #! [20]
    # QByteArray ba("colour behaviour flavour neighbour");
    # ba.replace(QByteArray("ou"), QByteArray("o"));
    # // ba == "color behavior flavor neighbor"
    # #! [20]

    # #! [21]
    # QByteArray x("sticky question");
    # QByteArrayView y("sti");
    # x.indexOf(y);               // returns 0
    # x.indexOf(y, 1);            // returns 10
    # x.indexOf(y, 10);           // returns 10
    # x.indexOf(y, 11);           // returns -1
    # #! [21]

    # #! [22]
    # QByteArray ba("ABCBA");
    # ba.indexOf("B");            // returns 1
    # ba.indexOf("B", 1);         // returns 1
    # ba.indexOf("B", 2);         // returns 3
    # ba.indexOf("X");            // returns -1
    # #! [22]

    # #! [23]
    # QByteArray x("crazy azimuths");
    # QByteArrayView y("az");
    # x.lastIndexOf(y);           // returns 6
    # x.lastIndexOf(y, 6);        // returns 6
    # x.lastIndexOf(y, 5);        // returns 2
    # x.lastIndexOf(y, 1);        // returns -1
    # #! [23]

    # #! [24]
    # QByteArray ba("ABCBA");
    # ba.lastIndexOf("B");        // returns 3
    # ba.lastIndexOf("B", 3);     // returns 3
    # ba.lastIndexOf("B", 2);     // returns 1
    # ba.lastIndexOf("X");        // returns -1
    # #! [24]

    # #! [25]
    # QByteArray url("ftp://ftp.qt-project.org/");
    # if (url.startsWith("ftp:"))
    #     ...
    # #! [25]

    # #! [26]
    # QByteArray url("http://qt-project.org/doc/qt-5.0/qtdoc/index.html");
    # if (url.endsWith(".html"))
    #     ...
    # #! [26]

    # #! [27]
    # QByteArray x("Pineapple");
    # QByteArray y = x.first(4);
    # // y == "Pine"
    # #! [27]

    # #! [28]
    # QByteArray x("Pineapple");
    # QByteArray y = x.last(5);
    # // y == "apple"
    # #! [28]

    # #! [29]
    # QByteArray x("Five pineapples");
    # QByteArray y = x.sliced(5, 4);     // y == "pine"
    # QByteArray z = x.sliced(5);        // z == "pineapples"
    # #! [29]

    # #! [30]
    # QByteArray x("Qt by THE QT COMPANY");
    # QByteArray y = x.toLower();
    # // y == "qt by the qt company"
    # #! [30]

    # #! [31]
    # QByteArray x("Qt by THE QT COMPANY");
    # QByteArray y = x.toUpper();
    # // y == "QT BY THE QT COMPANY"
    # #! [31]

    # #! [32]
    # QByteArray ba("  lots\t of\nwhitespace\r\n ");
    # ba = ba.simplified();
    # // ba == "lots of whitespace";
    # #! [32]

    # #! [33]
    # QByteArray ba("  lots\t of\nwhitespace\r\n ");
    # ba = ba.trimmed();
    # // ba == "lots\t of\nwhitespace";
    # #! [33]

    # #! [34]
    # QByteArray x("apple");
    # QByteArray y = x.leftJustified(8, '.');   // y == "apple..."
    # #! [34]

    # #! [35]
    # QByteArray x("apple");
    # QByteArray y = x.rightJustified(8, '.');    // y == "...apple"
    # #! [35]

    # #! [36]
    # QByteArray str("FF");
    # bool ok;
    # int hex = str.toInt(&ok, 16);     // hex == 255, ok == true
    # int dec = str.toInt(&ok, 10);     // dec == 0, ok == false
    # #! [36]

    # #! [37]
    # QByteArray str("FF");
    # bool ok;
    # long hex = str.toLong(&ok, 16);   // hex == 255, ok == true
    # long dec = str.toLong(&ok, 10);   // dec == 0, ok == false
    # #! [37]

    # #! [38]
    # QByteArray string("1234.56");
    # bool ok;
    # double a = string.toDouble(&ok);   // a == 1234.56, ok == true

    # string = "1234.56 Volt";
    # a = str.toDouble(&ok);             // a == 0, ok == false
    # #! [38]

    # #! [38float]
    # QByteArray string("1234.56");
    # bool ok;
    # float a = string.toFloat(&ok);    // a == 1234.56, ok == true

    # string = "1234.56 Volt";
    # a = str.toFloat(&ok);              // a == 0, ok == false
    # #! [38float]

    # #! [39]
    # QByteArray text("Qt is great!");
    # text.toBase64();        // returns "UXQgaXMgZ3JlYXQh"

    # QByteArray text("<p>Hello?</p>");
    # text.toBase64(QByteArray::Base64Encoding | QByteArray::OmitTrailingEquals);      // returns "PHA+SGVsbG8/PC9wPg"
    # text.toBase64(QByteArray::Base64Encoding);                                       // returns "PHA+SGVsbG8/PC9wPg=="
    # text.toBase64(QByteArray::Base64UrlEncoding);                                    // returns "PHA-SGVsbG8_PC9wPg=="
    # text.toBase64(QByteArray::Base64UrlEncoding | QByteArray::OmitTrailingEquals);   // returns "PHA-SGVsbG8_PC9wPg"
    # #! [39]

    # #! [40]
    # QByteArray ba;
    # int n = 63;
    # ba.setNum(n);           // ba == "63"
    # ba.setNum(n, 16);       // ba == "3f"
    # #! [40]

    # #! [41]
    # int n = 63;
    # QByteArray::number(n);              // returns "63"
    # QByteArray::number(n, 16);          // returns "3f"
    # QByteArray::number(n, 16).toUpper();  // returns "3F"
    # #! [41]

    # #! [42]
    # QByteArray ba = QByteArray::number(12.3456, 'E', 3);
    # // ba == 1.235E+01
    # #! [42]

    # #! [43]
    #  static const char mydata[] = {
    #     '\x00', '\x00', '\x03', '\x84', '\x78', '\x9c', '\x3b', '\x76',
    #     '\xec', '\x18', '\xc3', '\x31', '\x0a', '\xf1', '\xcc', '\x99',
    #     ...
    #     '\x6d', '\x5b'
    # };

    # QByteArray data = QByteArray::fromRawData(mydata, sizeof(mydata));
    # QDataStream in(&data, QIODevice::ReadOnly);
    # ...
    # #! [43]

    # #! [44]
    # QByteArray text = QByteArray::fromBase64("UXQgaXMgZ3JlYXQh");
    # text.data();            // returns "Qt is great!"

    # QByteArray::fromBase64("PHA+SGVsbG8/PC9wPg==", QByteArray::Base64Encoding); // returns "<p>Hello?</p>"
    # QByteArray::fromBase64("PHA-SGVsbG8_PC9wPg==", QByteArray::Base64UrlEncoding); // returns "<p>Hello?</p>"
    # #! [44]

    # #! [44ter]
    # void process(const QByteArray &);

    # if (auto result = QByteArray::fromBase64Encoding(encodedData))
    #     process(*result);
    # #! [44ter]

    # #! [44quater]
    # auto result = QByteArray::fromBase64Encoding(encodedData);
    # if (result.decodingStatus == QByteArray::Base64DecodingStatus::Ok)
    #     process(result.decoded);
    # #! [44quater]

    # #! [45]
    # QByteArray text = QByteArray::fromHex("517420697320677265617421");
    # text.data();            // returns "Qt is great!"
    # #! [45]

    # #! [46]
    # QString tmp = "test";
    # QByteArray text = tmp.toLocal8Bit();
    # char *data = new char[text.size()];
    # strcpy(data, text.data());
    # delete [] data;
    # #! [46]

    # #! [47]
    # QString tmp = "test";
    # QByteArray text = tmp.toLocal8Bit();
    # char *data = new char[text.size() + 1];
    # strcpy(data, text.data());
    # delete [] data;
    # #! [47]

    # #! [48]
    # QByteArray ba1("ca\0r\0t");
    # ba1.size();                     // Returns 2.
    # ba1.constData();                // Returns "ca" with terminating \0.

    # QByteArray ba2("ca\0r\0t", 3);
    # ba2.size();                     // Returns 3.
    # ba2.constData();                // Returns "ca\0" with terminating \0.

    # QByteArray ba3("ca\0r\0t", 4);
    # ba3.size();                     // Returns 4.
    # ba3.constData();                // Returns "ca\0r" with terminating \0.

    # const char cart[] = {'c', 'a', '\0', 'r', '\0', 't'};
    # QByteArray ba4(QByteArray::fromRawData(cart, 6));
    # ba4.size();                     // Returns 6.
    # ba4.constData();                // Returns "ca\0r\0t" without terminating \0.
    # #! [48]

    # #! [49]
    # QByteArray ba("ab");
    # ba.repeated(4);             // returns "abababab"
    # #! [49]

    # #! [50]
    # QByteArray macAddress = QByteArray::fromHex("123456abcdef");
    # macAddress.toHex(':'); // returns "12:34:56:ab:cd:ef"
    # macAddress.toHex(0);   // returns "123456abcdef"
    # #! [50]

    # #! [51]
    # QByteArray text = QByteArray::fromPercentEncoding("Qt%20is%20great%33");
    # text.data();            // returns "Qt is great!"
    # #! [51]

    # #! [52]
    # QByteArray text = "{a fishy string?}";
    # QByteArray ba = text.toPercentEncoding("{}", "s");
    # qDebug(ba.constData());
    # // prints "{a fi%73hy %73tring%3F}"
    # #! [52]

    # #! [53]
    # QByteArray ba = QByteArrayLiteral("byte array contents");
    # #! [53]
    # }
    ```

    See also

    [sliced()](#sliced), [first()](#first), [last()](#last), [chopped()](#chopped), [chop()](#chop), [truncate()](#truncate).

---

sliced(int) → QByteArray
:   This is an overloaded function.

    Returns a byte array containing the bytes starting at position *pos* in this object, and extending to the end of this object.

    **Note:** The behavior is undefined when *pos* < 0 or *pos* > [size()](#size).

    See also

    [first()](#first), [last()](#last), [sliced()](#sliced), [chopped()](#chopped), [chop()](#chop), [truncate()](#truncate).

---

sliced(int, int) → QByteArray
:   Returns a byte array containing the *n* bytes of this object starting at position *pos*.

    **Note:** The behavior is undefined when *pos* < 0, *n* < 0, or *pos* + *n* > [size()](#size).

    Example:

    ```
    # QByteArray x("Five pineapples");
    # QByteArray y = x.sliced(5, 4);     // y == "pine"
    # QByteArray z = x.sliced(5);        // z == "pineapples"
    ```

    See also

    [first()](#first), [last()](#last), [chopped()](#chopped), [chop()](#chop), [truncate()](#truncate).

---

split(bytes) → list[QByteArray]
:   Splits the byte array into subarrays wherever *sep* occurs, and returns the list of those arrays. If *sep* does not match anywhere in the byte array, split() returns a single-element list containing this byte array.

---

squeeze()
:   Releases any memory not required to store the array’s data.

    The sole purpose of this function is to provide a means of fine tuning QByteArray’s memory usage. In general, you will rarely ever need to call this function.

    See also

    [reserve()](#reserve), [capacity()](#capacity).

---

startsWith(QByteArray|bytes|bytearray|memoryview) → bool
:   Returns `true` if this byte array starts with the sequence of bytes viewed by *bv*; otherwise returns `false`.

    Example:

    ```
    # QByteArray url("ftp://ftp.qt-project.org/");
    # if (url.startsWith("ftp:"))
    #     ...
    ```

    See also

    [endsWith()](#endsWith), [first()](#first).

---

\_\_str\_\_() → str
:   TODO

---

swap(QByteArray)
:   Swaps this byte array with *other*. This operation is very fast and never fails.

---

toBase64(options: [Base64Option](#Base64Option) = [Base64Encoding](#Base64Option-Base64Encoding)) → QByteArray
:   Returns a copy of the byte array, encoded using the options *options*.

    ```
    # QByteArray text("Qt is great!");
    # text.toBase64();        // returns "UXQgaXMgZ3JlYXQh"

    # QByteArray text("<p>Hello?</p>");
    # text.toBase64(QByteArray::Base64Encoding | QByteArray::OmitTrailingEquals);      // returns "PHA+SGVsbG8/PC9wPg"
    # text.toBase64(QByteArray::Base64Encoding);                                       // returns "PHA+SGVsbG8/PC9wPg=="
    # text.toBase64(QByteArray::Base64UrlEncoding);                                    // returns "PHA-SGVsbG8_PC9wPg=="
    # text.toBase64(QByteArray::Base64UrlEncoding | QByteArray::OmitTrailingEquals);   // returns "PHA-SGVsbG8_PC9wPg"
    ```

    The algorithm used to encode Base64-encoded data is defined in RFC 4648.

    See also

    [fromBase64()](#fromBase64).

---

toDouble() → (float, bool)
:   Returns the byte array converted to a `double` value.

    Returns an infinity if the conversion overflows or 0.0 if the conversion fails for other reasons (e.g. underflow).

    If *ok* is not `nullptr`, failure is reported by setting \**ok* to `false`, and success by setting \**ok* to `true`.

    ```
    # QByteArray string("1234.56");
    # bool ok;
    # double a = string.toDouble(&ok);   // a == 1234.56, ok == true

    # string = "1234.56 Volt";
    # a = str.toDouble(&ok);             // a == 0, ok == false
    ```

    **Warning:** The QByteArray content may only contain valid numerical characters which includes the plus/minus sign, the character e used in scientific notation, and the decimal point. Including the unit or additional characters leads to a conversion error.

    **Note:** The conversion of the number is performed in the default C locale, regardless of the user’s locale. Use [QLocale](qlocale.html) to perform locale-aware conversions between numbers and strings.

    This function ignores leading and trailing whitespace.

    See also

    [number()](#number).

---

toFloat() → (float, bool)
:   Returns the byte array converted to a `float` value.

    Returns an infinity if the conversion overflows or 0.0 if the conversion fails for other reasons (e.g. underflow).

    If *ok* is not `nullptr`, failure is reported by setting \**ok* to `false`, and success by setting \**ok* to `true`.

    ```
    # QByteArray string("1234.56");
    # bool ok;
    # float a = string.toFloat(&ok);    // a == 1234.56, ok == true

    # string = "1234.56 Volt";
    # a = str.toFloat(&ok);              // a == 0, ok == false
    ```

    **Warning:** The QByteArray content may only contain valid numerical characters which includes the plus/minus sign, the character e used in scientific notation, and the decimal point. Including the unit or additional characters leads to a conversion error.

    **Note:** The conversion of the number is performed in the default C locale, regardless of the user’s locale. Use [QLocale](qlocale.html) to perform locale-aware conversions between numbers and strings.

    This function ignores leading and trailing whitespace.

    See also

    [number()](#number).

---

toHex(separator: bytes = '\000') → QByteArray
:   Returns a hex encoded copy of the byte array.

    The hex encoding uses the numbers 0-9 and the letters a-f.

    If *separator* is not ‘`\0`’, the separator character is inserted between the hex bytes.

    Example:

    ```
    # QByteArray macAddress = QByteArray::fromHex("123456abcdef");
    # macAddress.toHex(':'); // returns "12:34:56:ab:cd:ef"
    # macAddress.toHex(0);   // returns "123456abcdef"
    ```

    See also

    [fromHex()](#fromHex).

---

toInt(base: int = 10) → (int, bool)
:   Returns the byte array converted to an `int` using base *base*, which is ten by default. Bases 0 and 2 through 36 are supported, using letters for digits beyond 9; A is ten, B is eleven and so on.

    If *base* is 0, the base is determined automatically using the following rules: If the byte array begins with “0x”, it is assumed to be hexadecimal (base 16); otherwise, if it begins with “0b”, it is assumed to be binary (base 2); otherwise, if it begins with “0”, it is assumed to be octal (base 8); otherwise it is assumed to be decimal.

    Returns 0 if the conversion fails.

    If *ok* is not `nullptr`, failure is reported by setting \**ok* to `false`, and success by setting \**ok* to `true`.

    ```
    # QByteArray str("FF");
    # bool ok;
    # int hex = str.toInt(&ok, 16);     // hex == 255, ok == true
    # int dec = str.toInt(&ok, 10);     // dec == 0, ok == false
    ```

    **Note:** The conversion of the number is performed in the default C locale, regardless of the user’s locale. Use [QLocale](qlocale.html) to perform locale-aware conversions between numbers and strings.

    **Note:** Support for the “0b” prefix was added in Qt 6.4.

    See also

    [number()](#number).

---

toLong(base: int = 10) → (int, bool)
:   Returns the byte array converted to a `long` int using base *base*, which is ten by default. Bases 0 and 2 through 36 are supported, using letters for digits beyond 9; A is ten, B is eleven and so on.

    If *base* is 0, the base is determined automatically using the following rules: If the byte array begins with “0x”, it is assumed to be hexadecimal (base 16); otherwise, if it begins with “0b”, it is assumed to be binary (base 2); otherwise, if it begins with “0”, it is assumed to be octal (base 8); otherwise it is assumed to be decimal.

    Returns 0 if the conversion fails.

    If *ok* is not `nullptr`, failure is reported by setting \**ok* to `false`, and success by setting \**ok* to `true`.

    ```
    # QByteArray str("FF");
    # bool ok;
    # long hex = str.toLong(&ok, 16);   // hex == 255, ok == true
    # long dec = str.toLong(&ok, 10);   // dec == 0, ok == false
    ```

    **Note:** The conversion of the number is performed in the default C locale, regardless of the user’s locale. Use [QLocale](qlocale.html) to perform locale-aware conversions between numbers and strings.

    **Note:** Support for the “0b” prefix was added in Qt 6.4.

    See also

    [number()](#number).

---

toLongLong(base: int = 10) → (int, bool)
:   Returns the byte array converted to a `long long` using base *base*, which is ten by default. Bases 0 and 2 through 36 are supported, using letters for digits beyond 9; A is ten, B is eleven and so on.

    If *base* is 0, the base is determined automatically using the following rules: If the byte array begins with “0x”, it is assumed to be hexadecimal (base 16); otherwise, if it begins with “0b”, it is assumed to be binary (base 2); otherwise, if it begins with “0”, it is assumed to be octal (base 8); otherwise it is assumed to be decimal.

    Returns 0 if the conversion fails.

    If *ok* is not `nullptr`, failure is reported by setting \**ok* to `false`, and success by setting \**ok* to `true`.

    **Note:** The conversion of the number is performed in the default C locale, regardless of the user’s locale. Use [QLocale](qlocale.html) to perform locale-aware conversions between numbers and strings.

    **Note:** Support for the “0b” prefix was added in Qt 6.4.

    See also

    [number()](#number).

---

toLower() → QByteArray
:   Returns a copy of the byte array in which each ASCII uppercase letter converted to lowercase.

    Example:

    ```
    # QByteArray x("Qt by THE QT COMPANY");
    # QByteArray y = x.toLower();
    # // y == "qt by the qt company"
    ```

    See also

    [isLower()](#isLower), [toUpper()](#toUpper), [Character Case](#qbytearray-character-case).

---

toPercentEncoding(exclude: QByteArray|bytes|bytearray|memoryview = QByteArray(), include: QByteArray|bytes|bytearray|memoryview = QByteArray(), percent: str = '%') → QByteArray
:   Returns a URI/URL-style percent-encoded copy of this byte array. The *percent* parameter allows you to override the default ‘%’ character for another.

    By default, this function will encode all bytes that are not one of the following:

    ALPHA (“a” to “z” and “A” to “Z”) / DIGIT (0 to 9) / “-” / “.” / “\_” / “~”

    To prevent bytes from being encoded pass them to *exclude*. To force bytes to be encoded pass them to *include*. The *percent* character is always encoded.

    Example:

    ```
    # QByteArray text = "{a fishy string?}";
    # QByteArray ba = text.toPercentEncoding("{}", "s");
    # qDebug(ba.constData());
    # // prints "{a fi%73hy %73tring%3F}"
    ```

    The hex encoding uses the numbers 0-9 and the uppercase letters A-F.

    See also

    [fromPercentEncoding()](#fromPercentEncoding), [toPercentEncoding()](qurl.html#toPercentEncoding).

---

toShort(base: int = 10) → (int, bool)
:   Returns the byte array converted to a `short` using base *base*, which is ten by default. Bases 0 and 2 through 36 are supported, using letters for digits beyond 9; A is ten, B is eleven and so on.

    If *base* is 0, the base is determined automatically using the following rules: If the byte array begins with “0x”, it is assumed to be hexadecimal (base 16); otherwise, if it begins with “0b”, it is assumed to be binary (base 2); otherwise, if it begins with “0”, it is assumed to be octal (base 8); otherwise it is assumed to be decimal.

    Returns 0 if the conversion fails.

    If *ok* is not `nullptr`, failure is reported by setting \**ok* to `false`, and success by setting \**ok* to `true`.

    **Note:** The conversion of the number is performed in the default C locale, regardless of the user’s locale. Use [QLocale](qlocale.html) to perform locale-aware conversions between numbers and strings.

    **Note:** Support for the “0b” prefix was added in Qt 6.4.

    See also

    [number()](#number).

---

toUInt(base: int = 10) → (int, bool)
:   Returns the byte array converted to an `unsigned int` using base *base*, which is ten by default. Bases 0 and 2 through 36 are supported, using letters for digits beyond 9; A is ten, B is eleven and so on.

    If *base* is 0, the base is determined automatically using the following rules: If the byte array begins with “0x”, it is assumed to be hexadecimal (base 16); otherwise, if it begins with “0b”, it is assumed to be binary (base 2); otherwise, if it begins with “0”, it is assumed to be octal (base 8); otherwise it is assumed to be decimal.

    Returns 0 if the conversion fails.

    If *ok* is not `nullptr`, failure is reported by setting \**ok* to `false`, and success by setting \**ok* to `true`.

    **Note:** The conversion of the number is performed in the default C locale, regardless of the user’s locale. Use [QLocale](qlocale.html) to perform locale-aware conversions between numbers and strings.

    **Note:** Support for the “0b” prefix was added in Qt 6.4.

    See also

    [number()](#number).

---

toULong(base: int = 10) → (int, bool)
:   Returns the byte array converted to an `unsigned long int` using base *base*, which is ten by default. Bases 0 and 2 through 36 are supported, using letters for digits beyond 9; A is ten, B is eleven and so on.

    If *base* is 0, the base is determined automatically using the following rules: If the byte array begins with “0x”, it is assumed to be hexadecimal (base 16); otherwise, if it begins with “0b”, it is assumed to be binary (base 2); otherwise, if it begins with “0”, it is assumed to be octal (base 8); otherwise it is assumed to be decimal.

    Returns 0 if the conversion fails.

    If *ok* is not `nullptr`, failure is reported by setting \**ok* to `false`, and success by setting \**ok* to `true`.

    **Note:** The conversion of the number is performed in the default C locale, regardless of the user’s locale. Use [QLocale](qlocale.html) to perform locale-aware conversions between numbers and strings.

    **Note:** Support for the “0b” prefix was added in Qt 6.4.

    See also

    [number()](#number).

---

toULongLong(base: int = 10) → (int, bool)
:   Returns the byte array converted to an `unsigned long long` using base *base*, which is ten by default. Bases 0 and 2 through 36 are supported, using letters for digits beyond 9; A is ten, B is eleven and so on.

    If *base* is 0, the base is determined automatically using the following rules: If the byte array begins with “0x”, it is assumed to be hexadecimal (base 16); otherwise, if it begins with “0b”, it is assumed to be binary (base 2); otherwise, if it begins with “0”, it is assumed to be octal (base 8); otherwise it is assumed to be decimal.

    Returns 0 if the conversion fails.

    If *ok* is not `nullptr`, failure is reported by setting \**ok* to `false`, and success by setting \**ok* to `true`.

    **Note:** The conversion of the number is performed in the default C locale, regardless of the user’s locale. Use [QLocale](qlocale.html) to perform locale-aware conversions between numbers and strings.

    **Note:** Support for the “0b” prefix was added in Qt 6.4.

    See also

    [number()](#number).

---

toUpper() → QByteArray
:   Returns a copy of the byte array in which each ASCII lowercase letter converted to uppercase.

    Example:

    ```
    # QByteArray x("Qt by THE QT COMPANY");
    # QByteArray y = x.toUpper();
    # // y == "QT BY THE QT COMPANY"
    ```

    See also

    [isUpper()](#isUpper), [toLower()](#toLower), [Character Case](#qbytearray-character-case).

---

toUShort(base: int = 10) → (int, bool)
:   Returns the byte array converted to an `unsigned short` using base *base*, which is ten by default. Bases 0 and 2 through 36 are supported, using letters for digits beyond 9; A is ten, B is eleven and so on.

    If *base* is 0, the base is determined automatically using the following rules: If the byte array begins with “0x”, it is assumed to be hexadecimal (base 16); otherwise, if it begins with “0b”, it is assumed to be binary (base 2); otherwise, if it begins with “0”, it is assumed to be octal (base 8); otherwise it is assumed to be decimal.

    Returns 0 if the conversion fails.

    If *ok* is not `nullptr`, failure is reported by setting \**ok* to `false`, and success by setting \**ok* to `true`.

    **Note:** The conversion of the number is performed in the default C locale, regardless of the user’s locale. Use [QLocale](qlocale.html) to perform locale-aware conversions between numbers and strings.

    **Note:** Support for the “0b” prefix was added in Qt 6.4.

    See also

    [number()](#number).

---

trimmed() → QByteArray
:   Returns a copy of this byte array with spacing characters removed from the start and end.

    The spacing characters are those for which the standard C++ `isspace()` function returns `true` in the C locale; these are the ASCII characters tabulation ‘`\t`’, line feed ‘`\n`’, carriage return ‘`\r`’, vertical tabulation ‘`\v`’, form feed ‘`\f`’, and space ‘ ‘.

    Example:

    ```
    # QByteArray ba("  lots\t of\nwhitespace\r\n ");
    # ba = ba.trimmed();
    # // ba == "lots\t of\nwhitespace";
    ```

    Unlike [simplified()](#simplified), trimmed() leaves internal spacing unchanged.

    See also

    [simplified()](#simplified), QChar::SpecialCharacter, [Spacing Characters](#qbytearray-spacing-characters).

---

truncate(int)
:   Truncates the byte array at index position *pos*.

    If *pos* is beyond the end of the array, nothing happens.

    Example:

    ```
    # QByteArray ba("Stockholm");
    # ba.truncate(5);             // ba == "Stock"
    ```

    See also

    [chop()](#chop), [resize()](#resize), [first()](#first).

### [Table of Contents](../../index.html)

* QByteArray
  + [Description](#description)
    - [Maximum size and out-of-memory conditions](#maximum-size-and-out-of-memory-conditions)
    - [C locale and ASCII functions](#c-locale-and-ascii-functions)
      * [C Strings](#c-strings)
      * [Spacing Characters](#spacing-characters)
      * [Number-String Conversions](#number-string-conversions)
      * [Character Case](#character-case)
  + [Classes](#classes)
  + [Enums](#enums)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QByteArray

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QColor {#qcolor}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QColor

# QColor[¶](#qcolor "Link to this heading")

[PyQt6.QtGui](qtgui-module.html).QColor

## Description[¶](#description "Link to this heading")

The QColor class provides colors based on RGB, HSV or CMYK values.

A color is normally specified in terms of RGB (red, green, and blue) components, but it is also possible to specify it in terms of HSV (hue, saturation, and value) and CMYK (cyan, magenta, yellow and black) components. In addition a color can be specified using a color name. The color name can be any of the SVG 1.0 color names.

| RGB | HSV | CMYK |
| --- | --- | --- |
| ![image-qcolor-rgb-png](../../_images/qcolor-rgb.png) | ![image-qcolor-hsv-png](../../_images/qcolor-hsv.png) | ![image-qcolor-cmyk-png](../../_images/qcolor-cmyk.png) |

The QColor constructor creates the color based on RGB values. To create a QColor based on either HSV or CMYK values, use the [toHsv()](#toHsv) and [toCmyk()](#toCmyk) functions respectively. These functions return a copy of the color using the desired format. In addition the static [fromRgb()](#fromRgb), [fromHsv()](#fromHsv) and [fromCmyk()](#fromCmyk) functions create colors from the specified values. Alternatively, a color can be converted to any of the three formats using the [convertTo()](#convertTo) function (returning a copy of the color in the desired format), or any of the [setRgb()](#setRgb), [setHsv()](#setHsv) and [setCmyk()](#setCmyk) functions altering *this* color’s format. The [spec()](#spec) function tells how the color was specified.

A color can be set by passing an RGB string (such as “#112233”), or an ARGB string (such as “#ff112233”) or a color name (such as “blue”), to the [fromString()](#fromString) function. The color names are taken from the SVG 1.0 color names. The [name()](#name) function returns the name of the color in the format “#RRGGBB”. Colors can also be set using [setRgb()](#setRgb), [setHsv()](#setHsv) and [setCmyk()](#setCmyk). To get a lighter or darker color use the [lighter()](#lighter) and [darker()](#darker) functions respectively.

The [isValid()](#isValid) function indicates whether a QColor is legal at all. For example, a RGB color with RGB values out of range is illegal. For performance reasons, QColor mostly disregards illegal colors, and for that reason, the result of using an invalid color is undefined.

The color components can be retrieved individually, e.g with [red()](#red), [hue()](#hue) and [cyan()](#cyan). The values of the color components can also be retrieved in one go using the [getRgb()](#getRgb), [getHsv()](#getHsv) and [getCmyk()](#getCmyk) functions. Using the RGB color model, the color components can in addition be accessed with [rgb()](#rgb).

There are several related non-members: QRgb is a typdef for an unsigned int representing the RGB value triplet (r, g, b). Note that it also can hold a value for the alpha-channel (for more information, see the Alpha-Blended Drawing section). The [qRed()](qtgui-module.html#qRed), [qBlue()](qtgui-module.html#qBlue) and [qGreen()](qtgui-module.html#qGreen) functions return the respective component of the given QRgb value, while the [qRgb()](qtgui-module.html#qRgb) and [qRgba()](qtgui-module.html#qRgba) functions create and return the QRgb triplet based on the given component values. Finally, the [qAlpha()](qtgui-module.html#qAlpha) function returns the alpha component of the provided QRgb, and the [qGray()](qtgui-module.html#qGray) function calculates and return a gray value based on the given value.

QColor is platform and device independent.

For more information about painting in general, see the [Paint System](https://doc.qt.io/qt-6/paintsystem.html) documentation.

### Integer vs. Floating Point Precision[¶](#integer-vs-floating-point-precision "Link to this heading")

QColor supports floating point precision and provides floating point versions of all the color components functions, e.g. [getRgbF()](#getRgbF), [hueF()](#hueF) and [fromCmykF()](#fromCmykF). Note that since the components are stored using 16-bit integers, there might be minor deviations between the values set using, for example, [setRgbF()](#setRgbF) and the values returned by the [getRgbF()](#getRgbF) function due to rounding.

While the integer based functions take values in the range 0-255 (except [hue()](#hue) which must have values within the range 0-359), the floating point functions accept values in the range 0.0 - 1.0.

### Alpha-Blended Drawing[¶](#alpha-blended-drawing "Link to this heading")

QColor also support alpha-blended outlining and filling. The alpha channel of a color specifies the transparency effect, 0 represents a fully transparent color, while 255 represents a fully opaque color. For example:

```
# // Specify semi-transparent red
# painter.setBrush(QColor(255, 0, 0, 127));
# painter.drawRect(0, 0, width() / 2, height());

# // Specify semi-transparent blue
# painter.setBrush(QColor(0, 0, 255, 127));
# painter.drawRect(0, 0, width(), height() / 2);
```

The code above produces the following output:

![../../_images/alphafill.png](../../_images/alphafill.png)

The alpha channel of a color can be retrieved and set using the [alpha()](#alpha) and [setAlpha()](#setAlpha) functions if its value is an integer, and [alphaF()](#alphaF) and [setAlphaF()](#setAlphaF) if its value is float. By default, the alpha-channel is set to 255 (opaque). To retrieve and set *all* the RGB color components (including the alpha-channel) in one go, use the [rgba()](#rgba) and [setRgba()](#setRgba) functions.

### Predefined Colors[¶](#predefined-colors "Link to this heading")

There are 20 predefined QColor objects in the `QColorConstants` namespace, including black, white, primary and secondary colors, darker versions of these colors, and three shades of gray. Furthermore, the `QColorConstants::Svg` namespace defines QColor objects for the standard [SVG color keyword names](https://www.w3.org/TR/SVG11/types.html#ColorKeywords).

![../../_images/qt-colors.png](../../_images/qt-colors.png)

The `QColorConstants::Color0`, `QColorConstants::Color1` and `QColorConstants::Transparent` colors are used for special purposes.

`QColorConstants::Color0` (zero pixel value) and `QColorConstants::Color1` (non-zero pixel value) are special colors for drawing in QBitmaps. Painting with `QColorConstants::Color0` sets the bitmap bits to 0 (transparent; i.e., background), and painting with c{QColorConstants::Color1} sets the bits to 1 (opaque; i.e., foreground).

`QColorConstants::Transparent` is used to indicate a transparent pixel. When painting with this value, a pixel value will be used that is appropriate for the underlying pixel format in use.

For historical reasons, the 20 predefined colors are also available in the [GlobalColor](../qtcore/qt.html#GlobalColor) enumeration.

Finally, QColor recognizes a variety of color names (as strings); the static [colorNames()](#colorNames) function returns a QStringList color names that QColor knows about.

### The Extended RGB Color Model[¶](#the-extended-rgb-color-model "Link to this heading")

The extended RGB color model, also known as the scRGB color space, is the same the RGB color model except it allows values under 0.0, and over 1.0. This makes it possible to represent colors that would otherwise be outside the range of the RGB colorspace but still use the same values for colors inside the RGB colorspace.

### The HSV Color Model[¶](#the-hsv-color-model "Link to this heading")

The RGB model is hardware-oriented. Its representation is close to what most monitors show. In contrast, HSV represents color in a way more suited to the human perception of color. For example, the relationships “stronger than”, “darker than”, and “the opposite of” are easily expressed in HSV but are much harder to express in RGB.

HSV, like RGB, has three components:

* H, for hue, is in the range 0 to 359 if the color is chromatic (not gray), or meaningless if it is gray. It represents degrees on the color wheel familiar to most people. Red is 0 (degrees), green is 120, and blue is 240.

  ![image-qcolor-hue-png](../../_images/qcolor-hue.png)
* S, for saturation, is in the range 0 to 255, and the bigger it is, the stronger the color is. Grayish colors have saturation near 0; very strong colors have saturation near 255.

  ![image-qcolor-saturation-png](../../_images/qcolor-saturation.png)
* V, for value, is in the range 0 to 255 and represents lightness or brightness of the color. 0 is black; 255 is as far from black as possible.

  ![image-qcolor-value-png](../../_images/qcolor-value.png)

Here are some examples: pure red is H=0, S=255, V=255; a dark red, moving slightly towards the magenta, could be H=350 (equivalent to -10), S=255, V=180; a grayish light red could have H about 0 (say 350-359 or 0-10), S about 50-100, and S=255.

Qt returns a hue value of -1 for achromatic colors. If you pass a hue value that is too large, Qt forces it into range. Hue 360 or 720 is treated as 0; hue 540 is treated as 180.

In addition to the standard HSV model, Qt provides an alpha-channel to feature alpha-blended drawing.

### The HSL Color Model[¶](#the-hsl-color-model "Link to this heading")

HSL is similar to HSV, however instead of the Value parameter, HSL specifies a Lightness parameter which maps somewhat differently to the brightness of the color.

Similarly, the HSL saturation value is not in general the same as the HSV saturation value for the same color. [hslSaturation()](#hslSaturation) provides the color’s HSL saturation value, while [saturation()](#saturation) and [hsvSaturation()](#hsvSaturation) provides the HSV saturation value.

The hue value is defined to be the same in HSL and HSV.

### The CMYK Color Model[¶](#the-cmyk-color-model "Link to this heading")

While the RGB and HSV color models are used for display on computer monitors, the CMYK model is used in the four-color printing process of printing presses and some hard-copy devices.

CMYK has four components, all in the range 0-255: cyan (C), magenta (M), yellow (Y) and black (K). Cyan, magenta and yellow are called subtractive colors; the CMYK color model creates color by starting with a white surface and then subtracting color by applying the appropriate components. While combining cyan, magenta and yellow gives the color black, subtracting one or more will yield any other color. When combined in various percentages, these three colors can create the entire spectrum of colors.

Mixing 100 percent of cyan, magenta and yellow *does* produce black, but the result is unsatisfactory since it wastes ink, increases drying time, and gives a muddy colour when printing. For that reason, black is added in professional printing to provide a solid black tone; hence the term ‘four color process’.

In addition to the standard CMYK model, Qt provides an alpha-channel to feature alpha-blended drawing.

See also

[QPalette](qpalette.html), [QBrush](qbrush.html), [QColorConstants](qcolorconstants.html).

## Enums[¶](#enums "Link to this heading")

NameFormat
:   How to format the output of the [name()](#name) function

    See also

    [name()](#name).

    | Member | Value | Description |
    | --- | --- | --- |
    | HexArgb | 1 | #AARRGGBB A “#” character followed by four two-digit hexadecimal numbers (i.e. `#AARRGGBB`). |
    | HexRgb | 0 | #RRGGBB A “#” character followed by three two-digit hexadecimal numbers (i.e. `#RRGGBB`). |

---

Spec
:   The type of color specified, either RGB, extended RGB, HSV, CMYK or HSL.

    See also

    [spec()](#spec), [convertTo()](#convertTo).

    | Member | Value | Description |
    | --- | --- | --- |
    | Cmyk | TODO | TODO |
    | ExtendedRgb | TODO | TODO |
    | Hsl | TODO | TODO |
    | Hsv | TODO | TODO |
    | Invalid | TODO | TODO |
    | Rgb | TODO | TODO |

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs an invalid color with the RGB value (0, 0, 0). An invalid color is a color that is not properly set up for the underlying window system.

    The alpha value of an invalid color is unspecified.

    See also

    [isValid()](#isValid).

---

\_\_init\_\_([GlobalColor](../qtcore/qt.html#GlobalColor))
:   Constructs a new color with a color value of *color*.

    See also

    [isValid()](#isValid), Predefined Colors.

---

\_\_init\_\_(int)
:   Constructs a color with the value *color*. The alpha component is ignored and set to solid.

    See also

    [fromRgb()](#fromRgb), [isValid()](#isValid).

---

\_\_init\_\_([QRgba64](qrgba64.html))
:   Constructs a color with the value *rgba64*.

    See also

    [fromRgba64()](#fromRgba64).

---

\_\_init\_\_(Any)
:   TODO

---

\_\_init\_\_(str)
:   TODO

---

\_\_init\_\_(QColor)
:   TODO

---

\_\_init\_\_(int, int, int, alpha: int = 255)
:   Constructs a color with the RGB value *r*, *g*, *b*, and the alpha-channel (transparency) value of *a*.

    The color is left invalid if any of the arguments are invalid.

    See also

    [setRgba()](#setRgba), [isValid()](#isValid).

---

alpha() → int
:   Returns the alpha color component of this color.

    See also

    [setAlpha()](#setAlpha), [alphaF()](#alphaF), Alpha-Blended Drawing.

---

alphaF() → float
:   Returns the alpha color component of this color.

    See also

    [setAlphaF()](#setAlphaF), [alpha()](#alpha), Alpha-Blended Drawing.

---

black() → int
:   Returns the black color component of this color.

    See also

    [blackF()](#blackF), [getCmyk()](#getCmyk), The CMYK Color Model.

---

blackF() → float
:   Returns the black color component of this color.

    See also

    [black()](#black), [getCmykF()](#getCmykF), The CMYK Color Model.

---

blue() → int
:   Returns the blue color component of this color.

    See also

    [setBlue()](#setBlue), [blueF()](#blueF), [getRgb()](#getRgb).

---

blueF() → float
:   Returns the blue color component of this color.

    See also

    [setBlueF()](#setBlueF), [blue()](#blue), [getRgbF()](#getRgbF).

---

@staticmethod colorNames() → list[str]
:   Returns a QStringList containing the color names Qt knows about.

    See also

    Predefined Colors.

---

convertTo([Spec](#Spec)) → QColor
:   Creates a copy of *this* color in the format specified by *colorSpec*.

    See also

    [spec()](#spec), [toCmyk()](#toCmyk), [toHsv()](#toHsv), [toRgb()](#toRgb), [isValid()](#isValid).

---

cyan() → int
:   Returns the cyan color component of this color.

    See also

    [cyanF()](#cyanF), [getCmyk()](#getCmyk), The CMYK Color Model.

---

cyanF() → float
:   Returns the cyan color component of this color.

    See also

    [cyan()](#cyan), [getCmykF()](#getCmykF), The CMYK Color Model.

---

darker(factor: int = 200) → QColor
:   Returns a darker (or lighter) color, but does not change this object.

    If the *factor* is greater than 100, this functions returns a darker color. Setting *factor* to 300 returns a color that has one-third the brightness. If the *factor* is less than 100, the return color is lighter, but we recommend using the [lighter()](#lighter) function for this purpose. If the *factor* is 0 or negative, the return value is unspecified.

    The function converts the current color to HSV, divides the value (V) component by *factor* and converts the color back to it’s original color spec.

    See also

    [lighter()](#lighter), [isValid()](#isValid).

---

\_\_eq\_\_(QColor|[GlobalColor](../qtcore/qt.html#GlobalColor)|int) → bool
:   TODO

---

\_\_eq\_\_([QBrush](qbrush.html)|QColor|[GlobalColor](../qtcore/qt.html#GlobalColor)|int|[QGradient](qgradient.html)) → bool
:   TODO

---

\_\_eq\_\_([QPen](qpen.html)|QColor|[GlobalColor](../qtcore/qt.html#GlobalColor)|int) → bool
:   TODO

---

@staticmethod fromCmyk(int, int, int, int, alpha: int = 255) → QColor
:   Static convenience function that returns a QColor constructed from the given CMYK color values: *c* (cyan), *m* (magenta), *y* (yellow), *k* (black), and *a* (alpha-channel, i.e. transparency).

    All the values must be in the range 0-255.

    See also

    [toCmyk()](#toCmyk), [fromCmykF()](#fromCmykF), [isValid()](#isValid), The CMYK Color Model.

---

@staticmethod fromCmykF(float, float, float, float, alpha: float = 1) → QColor
:   Static convenience function that returns a QColor constructed from the given CMYK color values: *c* (cyan), *m* (magenta), *y* (yellow), *k* (black), and *a* (alpha-channel, i.e. transparency).

    All the values must be in the range 0.0-1.0.

    See also

    [toCmyk()](#toCmyk), [fromCmyk()](#fromCmyk), [isValid()](#isValid), The CMYK Color Model.

---

@staticmethod fromHsl(int, int, int, alpha: int = 255) → QColor
:   Static convenience function that returns a QColor constructed from the HSV color values, *h* (hue), *s* (saturation), *l* (lightness), and *a* (alpha-channel, i.e. transparency).

    The value of *s*, *l*, and *a* must all be in the range 0-255; the value of *h* must be in the range 0-359.

    See also

    [toHsl()](#toHsl), [fromHslF()](#fromHslF), [isValid()](#isValid), The HSL Color Model.

---

@staticmethod fromHslF(float, float, float, alpha: float = 1) → QColor
:   Static convenience function that returns a QColor constructed from the HSV color values, *h* (hue), *s* (saturation), *l* (lightness), and *a* (alpha-channel, i.e. transparency).

    All the values must be in the range 0.0-1.0.

    See also

    [toHsl()](#toHsl), [fromHsl()](#fromHsl), [isValid()](#isValid), The HSL Color Model.

---

@staticmethod fromHsv(int, int, int, alpha: int = 255) → QColor
:   Static convenience function that returns a QColor constructed from the HSV color values, *h* (hue), *s* (saturation), *v* (value), and *a* (alpha-channel, i.e. transparency).

    The value of *s*, *v*, and *a* must all be in the range 0-255; the value of *h* must be in the range 0-359.

    See also

    [toHsv()](#toHsv), [fromHsvF()](#fromHsvF), [isValid()](#isValid), The HSV Color Model.

---

@staticmethod fromHsvF(float, float, float, alpha: float = 1) → QColor
:   Static convenience function that returns a QColor constructed from the HSV color values, *h* (hue), *s* (saturation), *v* (value), and *a* (alpha-channel, i.e. transparency).

    All the values must be in the range 0.0-1.0.

    See also

    [toHsv()](#toHsv), [fromHsv()](#fromHsv), [isValid()](#isValid), The HSV Color Model.

---

@staticmethod fromRgb(int) → QColor
:   Static convenience function that returns a QColor constructed from the given QRgb value *rgb*.

    The alpha component of *rgb* is ignored (i.e. it is automatically set to 255), use the [fromRgba()](#fromRgba) function to include the alpha-channel specified by the given QRgb value.

    See also

    [fromRgba()](#fromRgba), [fromRgbF()](#fromRgbF), [toRgb()](#toRgb), [isValid()](#isValid).

---

@staticmethod fromRgb(int, int, int, alpha: int = 255) → QColor
:   Static convenience function that returns a QColor constructed from the RGB color values, *r* (red), *g* (green), *b* (blue), and *a* (alpha-channel, i.e. transparency).

    All the values must be in the range 0-255.

    See also

    [toRgb()](#toRgb), [fromRgba64()](#fromRgba64), [fromRgbF()](#fromRgbF), [isValid()](#isValid).

---

@staticmethod fromRgba(int) → QColor
:   Static convenience function that returns a QColor constructed from the given QRgb value *rgba*.

    Unlike the [fromRgb()](#fromRgb) function, the alpha-channel specified by the given QRgb value is included.

    See also

    [fromRgb()](#fromRgb), [fromRgba64()](#fromRgba64), [isValid()](#isValid).

---

@staticmethod fromRgba64([QRgba64](qrgba64.html)) → QColor
:   Static convenience function that returns a QColor constructed from the given [QRgba64](qrgba64.html) value *rgba64*.

    See also

    [fromRgb()](#fromRgb), [fromRgbF()](#fromRgbF), [toRgb()](#toRgb), [isValid()](#isValid).

---

@staticmethod fromRgba64(int, int, int, alpha: int = USHRT\_MAX) → QColor
:   Static convenience function that returns a QColor constructed from the RGBA64 color values, *r* (red), *g* (green), *b* (blue), and *a* (alpha-channel, i.e. transparency).

    See also

    [fromRgb()](#fromRgb), [fromRgbF()](#fromRgbF), [toRgb()](#toRgb), [isValid()](#isValid).

---

@staticmethod fromRgbF(float, float, float, alpha: float = 1) → QColor
:   Static convenience function that returns a QColor constructed from the RGB color values, *r* (red), *g* (green), *b* (blue), and *a* (alpha-channel, i.e. transparency).

    The alpha value must be in the range 0.0-1.0. If any of the other values are outside the range of 0.0-1.0 the color model will be set as `ExtendedRgb`.

    See also

    [fromRgb()](#fromRgb), [fromRgba64()](#fromRgba64), [toRgb()](#toRgb), [isValid()](#isValid).

---

@staticmethod fromString([QByteArray](../qtcore/qbytearray.html)|bytes|bytearray|memoryview|str|None) → QColor
:   Returns an RGB QColor parsed from *name*, which may be in one of these formats:

    * #RGB (each of R, G, and B is a single hex digit)
    * #RRGGBB
    * #AARRGGBB (Since 5.2)
    * #RRRGGGBBB
    * #RRRRGGGGBBBB
    * A name from the list of colors defined in the list of [SVG color keyword names](https://www.w3.org/TR/SVG11/types.html#ColorKeywords) provided by the World Wide Web Consortium; for example, “steelblue” or “gainsboro”. These color names work on all platforms. Note that these color names are *not* the same as defined by the [GlobalColor](../qtcore/qt.html#GlobalColor) enums, e.g. “green” and [green](../qtcore/qt.html#GlobalColor-green) does not refer to the same color.
    * `transparent` - representing the absence of a color.

    Returns an invalid color if *name* cannot be parsed.

    See also

    [isValidColorName()](#isValidColorName).

---

getCmyk() → (int, int, int, int, int)
:   Sets the contents pointed to by *c*, *m*, *y*, *k*, and *a*, to the cyan, magenta, yellow, black, and alpha-channel (transparency) components of the color’s CMYK value.

    These components can be retrieved individually using the [cyan()](#cyan), [magenta()](#magenta), [yellow()](#yellow), [black()](#black) and [alpha()](#alpha) functions.

    See also

    [setCmyk()](#setCmyk), The CMYK Color Model.

---

getCmykF() → (float, float, float, float, float)
:   Sets the contents pointed to by *c*, *m*, *y*, *k*, and *a*, to the cyan, magenta, yellow, black, and alpha-channel (transparency) components of the color’s CMYK value.

    These components can be retrieved individually using the [cyanF()](#cyanF), [magentaF()](#magentaF), [yellowF()](#yellowF), [blackF()](#blackF) and [alphaF()](#alphaF) functions.

    See also

    [setCmykF()](#setCmykF), The CMYK Color Model.

---

getHsl() → (int, int, int, int)
:   Sets the contents pointed to by *h*, *s*, *l*, and *a*, to the hue, saturation, lightness, and alpha-channel (transparency) components of the color’s HSL value.

    These components can be retrieved individually using the [hslHue()](#hslHue), [hslSaturation()](#hslSaturation), [lightness()](#lightness) and [alpha()](#alpha) functions.

    See also

    [getHslF()](#getHslF), [setHsl()](#setHsl), The HSL Color Model.

---

getHslF() → (float, float, float, float)
:   Sets the contents pointed to by *h*, *s*, *l*, and *a*, to the hue, saturation, lightness, and alpha-channel (transparency) components of the color’s HSL value.

    These components can be retrieved individually using the [hslHueF()](#hslHueF), [hslSaturationF()](#hslSaturationF), [lightnessF()](#lightnessF) and [alphaF()](#alphaF) functions.

    See also

    [getHsl()](#getHsl), [setHslF()](#setHslF), The HSL Color Model.

---

getHsv() → (int, int, int, int)
:   Sets the contents pointed to by *h*, *s*, *v*, and *a*, to the hue, saturation, value, and alpha-channel (transparency) components of the color’s HSV value.

    These components can be retrieved individually using the [hue()](#hue), [saturation()](#saturation), [value()](#value) and [alpha()](#alpha) functions.

    See also

    [setHsv()](#setHsv), The HSV Color Model.

---

getHsvF() → (float, float, float, float)
:   Sets the contents pointed to by *h*, *s*, *v*, and *a*, to the hue, saturation, value, and alpha-channel (transparency) components of the color’s HSV value.

    These components can be retrieved individually using the [hueF()](#hueF), [saturationF()](#saturationF), [valueF()](#valueF) and [alphaF()](#alphaF) functions.

    See also

    [setHsv()](#setHsv), The HSV Color Model.

---

getRgb() → (int, int, int, int)
:   Sets the contents pointed to by *r*, *g*, *b*, and *a*, to the red, green, blue, and alpha-channel (transparency) components of the color’s RGB value.

    These components can be retrieved individually using the [red()](#red), [green()](#green), [blue()](#blue) and [alpha()](#alpha) functions.

    See also

    [rgb()](#rgb), [setRgb()](#setRgb).

---

getRgbF() → (float, float, float, float)
:   Sets the contents pointed to by *r*, *g*, *b*, and *a*, to the red, green, blue, and alpha-channel (transparency) components of the color’s RGB value.

    These components can be retrieved individually using the [redF()](#redF), [greenF()](#greenF), [blueF()](#blueF) and [alphaF()](#alphaF) functions.

    See also

    [rgb()](#rgb), [setRgb()](#setRgb).

---

green() → int
:   Returns the green color component of this color.

    See also

    [setGreen()](#setGreen), [greenF()](#greenF), [getRgb()](#getRgb).

---

greenF() → float
:   Returns the green color component of this color.

    See also

    [setGreenF()](#setGreenF), [green()](#green), [getRgbF()](#getRgbF).

---

hslHue() → int
:   Returns the HSL hue color component of this color.

    See also

    [hslHueF()](#hslHueF), [hsvHue()](#hsvHue), [getHsl()](#getHsl), The HSL Color Model.

---

hslHueF() → float
:   Returns the HSL hue color component of this color.

    See also

    [hslHue()](#hslHue), [hsvHueF()](#hsvHueF), [getHslF()](#getHslF).

---

hslSaturation() → int
:   Returns the HSL saturation color component of this color.

    See also

    [hslSaturationF()](#hslSaturationF), [hsvSaturation()](#hsvSaturation), [getHsl()](#getHsl), The HSL Color Model.

---

hslSaturationF() → float
:   Returns the HSL saturation color component of this color.

    See also

    [hslSaturation()](#hslSaturation), [hsvSaturationF()](#hsvSaturationF), [getHslF()](#getHslF), The HSL Color Model.

---

hsvHue() → int
:   Returns the HSV hue color component of this color.

    See also

    [hueF()](#hueF), [hslHue()](#hslHue), [getHsv()](#getHsv), The HSV Color Model.

---

hsvHueF() → float
:   Returns the hue color component of this color.

    See also

    [hue()](#hue), [hslHueF()](#hslHueF), [getHsvF()](#getHsvF), The HSV Color Model.

---

hsvSaturation() → int
:   Returns the HSV saturation color component of this color.

    See also

    [saturationF()](#saturationF), [hslSaturation()](#hslSaturation), [getHsv()](#getHsv), The HSV Color Model.

---

hsvSaturationF() → float
:   Returns the HSV saturation color component of this color.

    See also

    [saturation()](#saturation), [hslSaturationF()](#hslSaturationF), [getHsvF()](#getHsvF), The HSV Color Model.

---

hue() → int
:   Returns the HSV hue color component of this color.

    The color is implicitly converted to HSV.

    See also

    [hsvHue()](#hsvHue), [hslHue()](#hslHue), [hueF()](#hueF), [getHsv()](#getHsv), The HSV Color Model.

---

hueF() → float
:   Returns the HSV hue color component of this color.

    The color is implicitly converted to HSV.

    See also

    [hsvHueF()](#hsvHueF), [hslHueF()](#hslHueF), [hue()](#hue), [getHsvF()](#getHsvF), The HSV Color Model.

---

isValid() → bool
:   Returns `true` if the color is valid; otherwise returns `false`.

---

@staticmethod isValidColor(str|None) → bool
:   Use [isValidColorName()](#isValidColorName) instead.

    Returns `true` if the *name* is a valid color name and can be used to construct a valid QColor object, otherwise returns false.

    It uses the same algorithm used in [fromString()](#fromString).

    See also

    [fromString()](#fromString).

---

@staticmethod isValidColorName([QByteArray](../qtcore/qbytearray.html)|bytes|bytearray|memoryview|str|None) → bool
:   Returns `true` if the *name* is a valid color name and can be used to construct a valid QColor object, otherwise returns false.

    It uses the same algorithm used in [fromString()](#fromString).

    See also

    [fromString()](#fromString).

---

lighter(factor: int = 150) → QColor
:   Returns a lighter (or darker) color, but does not change this object.

    If the *factor* is greater than 100, this functions returns a lighter color. Setting *factor* to 150 returns a color that is 50% brighter. If the *factor* is less than 100, the return color is darker, but we recommend using the [darker()](#darker) function for this purpose. If the *factor* is 0 or negative, the return value is unspecified.

    The function converts the current color to HSV, multiplies the value (V) component by *factor* and converts the color back to it’s original color spec.

    See also

    [darker()](#darker), [isValid()](#isValid).

---

lightness() → int
:   Returns the lightness color component of this color.

    See also

    [lightnessF()](#lightnessF), [getHsl()](#getHsl).

---

lightnessF() → float
:   Returns the lightness color component of this color.

    See also

    [value()](#value), [getHslF()](#getHslF).

---

magenta() → int
:   Returns the magenta color component of this color.

    See also

    [magentaF()](#magentaF), [getCmyk()](#getCmyk), The CMYK Color Model.

---

magentaF() → float
:   Returns the magenta color component of this color.

    See also

    [magenta()](#magenta), [getCmykF()](#getCmykF), The CMYK Color Model.

---

name(format: [NameFormat](#NameFormat) = [HexRgb](#NameFormat-HexRgb)) → str
:   Returns the name of the color in the specified *format*.

    See also

    [fromString()](#fromString), NameFormat.

---

\_\_ne\_\_(QColor|[GlobalColor](../qtcore/qt.html#GlobalColor)|int) → bool
:   TODO

---

\_\_ne\_\_([QBrush](qbrush.html)|QColor|[GlobalColor](../qtcore/qt.html#GlobalColor)|int|[QGradient](qgradient.html)) → bool
:   TODO

---

\_\_ne\_\_([QPen](qpen.html)|QColor|[GlobalColor](../qtcore/qt.html#GlobalColor)|int) → bool
:   TODO

---

red() → int
:   Returns the red color component of this color.

    See also

    [setRed()](#setRed), [redF()](#redF), [getRgb()](#getRgb).

---

redF() → float
:   Returns the red color component of this color.

    See also

    [setRedF()](#setRedF), [red()](#red), [getRgbF()](#getRgbF).

---

rgb() → int
:   Returns the RGB value of the color. The alpha value is opaque.

    See also

    [setRgb()](#setRgb), [getRgb()](#getRgb), [rgba()](#rgba).

---

rgba() → int
:   Returns the RGB value of the color, including its alpha.

    For an invalid color, the alpha value of the returned color is unspecified.

    See also

    [setRgba()](#setRgba), [rgb()](#rgb), [rgba64()](#rgba64).

---

rgba64() → [QRgba64](qrgba64.html)
:   Returns the RGB64 value of the color, including its alpha.

    For an invalid color, the alpha value of the returned color is unspecified.

    See also

    [setRgba64()](#setRgba64), [rgba()](#rgba), [rgb()](#rgb).

---

saturation() → int
:   Returns the HSV saturation color component of this color.

    The color is implicitly converted to HSV.

    See also

    [hsvSaturation()](#hsvSaturation), [hslSaturation()](#hslSaturation), [saturationF()](#saturationF), [getHsv()](#getHsv), The HSV Color Model.

---

saturationF() → float
:   Returns the HSV saturation color component of this color.

    The color is implicitly converted to HSV.

    See also

    [hsvSaturationF()](#hsvSaturationF), [hslSaturationF()](#hslSaturationF), [saturation()](#saturation), [getHsvF()](#getHsvF), The HSV Color Model.

---

setAlpha(int)
:   Sets the alpha of this color to *alpha*. Integer alpha is specified in the range 0-255.

    See also

    [alpha()](#alpha), [alphaF()](#alphaF), Alpha-Blended Drawing.

---

setAlphaF(float)
:   Sets the alpha of this color to *alpha*. float alpha is specified in the range 0.0-1.0.

    See also

    [alphaF()](#alphaF), [alpha()](#alpha), Alpha-Blended Drawing.

---

setBlue(int)
:   Sets the blue color component of this color to *blue*. Integer components are specified in the range 0-255.

    See also

    [blue()](#blue), [blueF()](#blueF), [setRgb()](#setRgb).

---

setBlueF(float)
:   Sets the blue color component of this color to *blue*. If *blue* lies outside the 0.0-1.0 range, the color model will be changed to `ExtendedRgb`.

    See also

    [blueF()](#blueF), [blue()](#blue), [setRgbF()](#setRgbF).

---

setCmyk(int, int, int, int, alpha: int = 255)
:   Sets the color to CMYK values, *c* (cyan), *m* (magenta), *y* (yellow), *k* (black), and *a* (alpha-channel, i.e. transparency).

    All the values must be in the range 0-255.

    See also

    [getCmyk()](#getCmyk), [setCmykF()](#setCmykF), The CMYK Color Model.

---

setCmykF(float, float, float, float, alpha: float = 1)
:   Sets the color to CMYK values, *c* (cyan), *m* (magenta), *y* (yellow), *k* (black), and *a* (alpha-channel, i.e. transparency).

    All the values must be in the range 0.0-1.0.

    See also

    [getCmykF()](#getCmykF), [setCmyk()](#setCmyk), The CMYK Color Model.

---

setGreen(int)
:   Sets the green color component of this color to *green*. Integer components are specified in the range 0-255.

    See also

    [green()](#green), [greenF()](#greenF), [setRgb()](#setRgb).

---

setGreenF(float)
:   Sets the green color component of this color to *green*. If *green* lies outside the 0.0-1.0 range, the color model will be changed to `ExtendedRgb`.

    See also

    [greenF()](#greenF), [green()](#green), [setRgbF()](#setRgbF).

---

setHsl(int, int, int, alpha: int = 255)
:   Sets a HSL color value; *h* is the hue, *s* is the saturation, *l* is the lightness and *a* is the alpha component of the HSL color.

    The saturation, value and alpha-channel values must be in the range 0-255, and the hue value must be greater than -1.

    See also

    [getHsl()](#getHsl), [setHslF()](#setHslF).

---

setHslF(float, float, float, alpha: float = 1)
:   Sets a HSL color lightness; *h* is the hue, *s* is the saturation, *l* is the lightness and *a* is the alpha component of the HSL color.

    All the values must be in the range 0.0-1.0.

    See also

    [getHslF()](#getHslF), [setHsl()](#setHsl).

---

setHsv(int, int, int, alpha: int = 255)
:   Sets a HSV color value; *h* is the hue, *s* is the saturation, *v* is the value and *a* is the alpha component of the HSV color.

    The saturation, value and alpha-channel values must be in the range 0-255, and the hue value must be greater than -1.

    See also

    [getHsv()](#getHsv), [setHsvF()](#setHsvF), The HSV Color Model.

---

setHsvF(float, float, float, alpha: float = 1)
:   Sets a HSV color value; *h* is the hue, *s* is the saturation, *v* is the value and *a* is the alpha component of the HSV color.

    All the values must be in the range 0.0-1.0.

    See also

    [getHsvF()](#getHsvF), [setHsv()](#setHsv), The HSV Color Model.

---

setNamedColor(str)
:   Use [fromString()](#fromString) instead.

---

setRed(int)
:   Sets the red color component of this color to *red*. Integer components are specified in the range 0-255.

    See also

    [red()](#red), [redF()](#redF), [setRgb()](#setRgb).

---

setRedF(float)
:   Sets the red color component of this color to *red*. If *red* lies outside the 0.0-1.0 range, the color model will be changed to `ExtendedRgb`.

    See also

    [redF()](#redF), [red()](#red), [setRgbF()](#setRgbF).

---

setRgb(int)
:   Sets the RGB value to *rgb*. The alpha value is set to opaque.

---

setRgb(int, int, int, alpha: int = 255)
:   Sets the RGB value to *r*, *g*, *b* and the alpha value to *a*.

    All the values must be in the range 0-255.

    See also

    [rgb()](#rgb), [getRgb()](#getRgb), [setRgbF()](#setRgbF).

---

setRgba(int)
:   Sets the RGB value to *rgba*, including its alpha.

    See also

    [rgba()](#rgba), [rgb()](#rgb), [setRgba64()](#setRgba64).

---

setRgba64([QRgba64](qrgba64.html))
:   Sets the RGB64 value to *rgba*, including its alpha.

    See also

    [setRgba()](#setRgba), [rgba64()](#rgba64).

---

setRgbF(float, float, float, alpha: float = 1)
:   Sets the color channels of this color to *r* (red), *g* (green), *b* (blue) and *a* (alpha, transparency).

    The alpha value must be in the range 0.0-1.0. If any of the other values are outside the range of 0.0-1.0 the color model will be set as `ExtendedRgb`.

    See also

    [rgb()](#rgb), [getRgbF()](#getRgbF), [setRgb()](#setRgb).

---

spec() → [Spec](#Spec)
:   Returns how the color was specified.

    See also

    Spec, [convertTo()](#convertTo).

---

toCmyk() → QColor
:   Creates and returns a CMYK QColor based on this color.

    See also

    [fromCmyk()](#fromCmyk), [convertTo()](#convertTo), [isValid()](#isValid), The CMYK Color Model.

---

toExtendedRgb() → QColor
:   Create and returns an extended RGB QColor based on this color.

    See also

    [toRgb()](#toRgb), [convertTo()](#convertTo).

---

toHsl() → QColor
:   Creates and returns an HSL QColor based on this color.

    See also

    [fromHsl()](#fromHsl), [convertTo()](#convertTo), [isValid()](#isValid), The HSL Color Model.

---

toHsv() → QColor
:   Creates and returns an HSV QColor based on this color.

    See also

    [fromHsv()](#fromHsv), [convertTo()](#convertTo), [isValid()](#isValid), The HSV Color Model.

---

toRgb() → QColor
:   Create and returns an RGB QColor based on this color.

    See also

    [fromRgb()](#fromRgb), [convertTo()](#convertTo), [isValid()](#isValid).

---

value() → int
:   Returns the value color component of this color.

    See also

    [valueF()](#valueF), [getHsv()](#getHsv), The HSV Color Model.

---

valueF() → float
:   Returns the value color component of this color.

    See also

    [value()](#value), [getHsvF()](#getHsvF), The HSV Color Model.

---

yellow() → int
:   Returns the yellow color component of this color.

    See also

    [yellowF()](#yellowF), [getCmyk()](#getCmyk), The CMYK Color Model.

---

yellowF() → float
:   Returns the yellow color component of this color.

    See also

    [yellow()](#yellow), [getCmykF()](#getCmykF), The CMYK Color Model.

### [Table of Contents](../../index.html)

* QColor
  + [Description](#description)
    - [Integer vs. Floating Point Precision](#integer-vs-floating-point-precision)
    - [Alpha-Blended Drawing](#alpha-blended-drawing)
    - [Predefined Colors](#predefined-colors)
    - [The Extended RGB Color Model](#the-extended-rgb-color-model)
    - [The HSV Color Model](#the-hsv-color-model)
    - [The HSL Color Model](#the-hsl-color-model)
    - [The CMYK Color Model](#the-cmyk-color-model)
  + [Enums](#enums)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QColor

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QDate {#qdate}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QDate

# QDate[¶](#qdate "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QDate

## Description[¶](#description "Link to this heading")

The QDate class provides date functions.

A QDate object represents a particular day, regardless of calendar, locale or other settings used when creating it or supplied by the system. It can report the year, month and day of the month that represent the day with respect to the proleptic Gregorian calendar or any calendar supplied as a [QCalendar](qcalendar.html) object. QDate objects should be passed by value rather than by reference to const; they simply package `qint64`.

A QDate object is typically created by giving the year, month, and day numbers explicitly. Note that QDate interprets year numbers less than 100 as presented, i.e., as years 1 through 99, without adding any offset. The static function [currentDate()](#currentDate) creates a QDate object containing the date read from the system clock. An explicit date can also be set using [setDate()](#setDate). The [fromString()](#fromString) function returns a QDate given a string and a date format which is used to interpret the date within the string.

The [year()](#year), [month()](#month), and [day()](#day) functions provide access to the year, month, and day numbers. When more than one of these values is needed, it is more efficient to call [partsFromDate()](qcalendar.html#partsFromDate), to save repeating (potentially expensive) calendrical calculations.

Also, [dayOfWeek()](#dayOfWeek) and [dayOfYear()](#dayOfYear) functions are provided. The same information is provided in textual format by [toString()](#toString). [QLocale](qlocale.html) can map the day numbers to names, [QCalendar](qcalendar.html) can map month numbers to names.

QDate provides a full set of operators to compare two QDate objects where smaller means earlier, and larger means later.

You can increment (or decrement) a date by a given number of days using [addDays()](#addDays). Similarly you can use [addMonths()](#addMonths) and [addYears()](#addYears). The [daysTo()](#daysTo) function returns the number of days between two dates.

The [daysInMonth()](#daysInMonth) and [daysInYear()](#daysInYear) functions return how many days there are in this date’s month and year, respectively. The [isLeapYear()](#isLeapYear) function indicates whether a date is in a leap year. [QCalendar](qcalendar.html) can also supply this information, in some cases more conveniently.

### Remarks[¶](#remarks "Link to this heading")

**Note:** All conversion to and from string formats is done using the C locale. For localized conversions, see [QLocale](qlocale.html).

In the Gregorian calendar, there is no year 0. Dates in that year are considered invalid. The year -1 is the year “1 before Christ” or “1 before common era.” The day before 1 January 1 CE, QDate(1, 1, 1), is 31 December 1 BCE, QDate(-1, 12, 31). Various other calendars behave similarly; see [hasYearZero()](qcalendar.html#hasYearZero).

#### Range of Valid Dates[¶](#range-of-valid-dates "Link to this heading")

Dates are stored internally as a modified Julian Day number, an integer count of every day in a contiguous range, with 24 November 4714 BCE in the Gregorian calendar being Julian Day 0 (1 January 4713 BCE in the Julian calendar). As well as being an efficient and accurate way of storing an absolute date, it is suitable for converting a date into other calendar systems such as Hebrew, Islamic or Chinese. For the purposes of QDate, Julian Days are delimited at midnight and, for those of [QDateTime](qdatetime.html), in the zone used by the datetime. (This departs from the formal definition, which delimits Julian Days at UTC noon.) The Julian Day number can be obtained using [toJulianDay()](#toJulianDay) and can be set using [fromJulianDay()](#fromJulianDay).

The range of Julian Day numbers that QDate can represent is, for technical reasons, limited to between -784350574879 and 784354017364, which means from before 2 billion BCE to after 2 billion CE. This is more than seven times as wide as the range of dates a [QDateTime](qdatetime.html) can represent.

See also

[QTime](qtime.html), [QDateTime](qdatetime.html), [QCalendar](qcalendar.html), [YearRange](qdatetime.html#YearRange), [QDateEdit](../qtwidgets/qdateedit.html), [QDateTimeEdit](../qtwidgets/qdatetimeedit.html), [QCalendarWidget](../qtwidgets/qcalendarwidget.html).

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs a null date. Null dates are invalid.

    See also

    [isNull()](#isNull), [isValid()](#isValid).

---

\_\_init\_\_(QDate)
:   TODO

---

\_\_init\_\_(int, int, int)
:   Constructs a date with year *y*, month *m* and day *d*.

    The date is understood in terms of the Gregorian calendar. If the specified date is invalid, the date is not set and [isValid()](#isValid) returns `false`.

    **Warning:** Years 1 to 99 are interpreted as is. Year 0 is invalid.

    See also

    [isValid()](#isValid), [dateFromParts()](qcalendar.html#dateFromParts).

---

\_\_init\_\_(int, int, int, [QCalendar](qcalendar.html))
:   TODO

---

addDays(int) → QDate
:   Returns a QDate object containing a date *ndays* later than the date of this object (or earlier if *ndays* is negative).

    Returns a null date if the current date is invalid or the new date is out of range.

    See also

    [addMonths()](#addMonths), [addYears()](#addYears), [daysTo()](#daysTo).

---

addMonths(int) → QDate
:   This is an overloaded function.

---

addMonths(int, [QCalendar](qcalendar.html)) → QDate
:   Returns a QDate object containing a date *nmonths* later than the date of this object (or earlier if *nmonths* is negative).

    Uses *cal* as calendar, if supplied, else the Gregorian calendar.

    **Note:** If the ending day/month combination does not exist in the resulting month/year, this function will return a date that is the latest valid date in the selected month.

    See also

    [addDays()](#addDays), [addYears()](#addYears).

---

addYears(int) → QDate
:   This is an overloaded function.

---

addYears(int, [QCalendar](qcalendar.html)) → QDate
:   Returns a QDate object containing a date *nyears* later than the date of this object (or earlier if *nyears* is negative).

    Uses *cal* as calendar, if supplied, else the Gregorian calendar.

    **Note:** If the ending day/month combination does not exist in the resulting year (e.g., for the Gregorian calendar, if the date was Feb 29 and the final year is not a leap year), this function will return a date that is the latest valid date in the given month (in the example, Feb 28).

    See also

    [addDays()](#addDays), [addMonths()](#addMonths).

---

\_\_bool\_\_() → int
:   TODO

---

@staticmethod currentDate() → QDate
:   Returns the system clock’s current date.

    See also

    [currentTime()](qtime.html#currentTime), [currentDateTime()](qdatetime.html#currentDateTime).

---

day() → int
:   This is an overloaded function.

---

day([QCalendar](qcalendar.html)) → int
:   Returns the day of the month for this date.

    Uses *cal* as calendar if supplied, else the Gregorian calendar (for which the return ranges from 1 to 31). Returns 0 if the date is invalid.

    See also

    [year()](#year), [month()](#month), [dayOfWeek()](#dayOfWeek), [partsFromDate()](qcalendar.html#partsFromDate).

---

dayOfWeek() → int
:   This is an overloaded function.

---

dayOfWeek([QCalendar](qcalendar.html)) → int
:   Returns the weekday (1 = Monday to 7 = Sunday) for this date.

    Uses *cal* as calendar if supplied, else the Gregorian calendar. Returns 0 if the date is invalid. Some calendars may give special meaning (e.g. intercallary days) to values greater than 7.

    See also

    [day()](#day), [dayOfYear()](#dayOfYear), [dayOfWeek()](qcalendar.html#dayOfWeek), [DayOfWeek](qt.html#DayOfWeek).

---

dayOfYear() → int
:   This is an overloaded function.

---

dayOfYear([QCalendar](qcalendar.html)) → int
:   Returns the day of the year (1 for the first day) for this date.

    Uses *cal* as calendar if supplied, else the Gregorian calendar. Returns 0 if either the date or the first day of its year is invalid.

    See also

    [day()](#day), [dayOfWeek()](#dayOfWeek), [daysInYear()](qcalendar.html#daysInYear).

---

daysInMonth() → int
:   This is an overloaded function.

---

daysInMonth([QCalendar](qcalendar.html)) → int
:   Returns the number of days in the month for this date.

    Uses *cal* as calendar if supplied, else the Gregorian calendar (for which the result ranges from 28 to 31). Returns 0 if the date is invalid.

    See also

    [day()](#day), [daysInYear()](#daysInYear), [daysInMonth()](qcalendar.html#daysInMonth), [maximumDaysInMonth()](qcalendar.html#maximumDaysInMonth), [minimumDaysInMonth()](qcalendar.html#minimumDaysInMonth).

---

daysInYear() → int
:   This is an overloaded function.

---

daysInYear([QCalendar](qcalendar.html)) → int
:   Returns the number of days in the year for this date.

    Uses *cal* as calendar if supplied, else the Gregorian calendar (for which the result is 365 or 366). Returns 0 if the date is invalid.

    See also

    [day()](#day), [daysInMonth()](#daysInMonth), [daysInYear()](qcalendar.html#daysInYear), [maximumMonthsInYear()](qcalendar.html#maximumMonthsInYear).

---

daysTo(QDate|datetime.date) → int
:   Returns the number of days from this date to *d* (which is negative if *d* is earlier than this date).

    Returns 0 if either date is invalid.

    Example:

    ```
    # QDate d1(1995, 5, 17);  // May 17, 1995
    # QDate d2(1995, 5, 20);  // May 20, 1995
    # d1.daysTo(d2);          // returns 3
    # d2.daysTo(d1);          // returns -3
    ```

    See also

    [addDays()](#addDays).

---

endOfDay([QTimeZone](qtimezone.html)) → [QDateTime](qdatetime.html)
:   Returns the end-moment of the day.

    When a day ends depends on a how time is described: each day starts and ends earlier for those in time-zones further west and later for those in time-zones further east. The time representation to use can be specified by an optional time *zone*. The default time representation is the system’s local time.

    Usually, the end of the day is one millisecond before the midnight, 24:00: however, if a time-zone transition causes the given date to skip over that moment (e.g. a DST spring-forward skipping over 23:00 and the following hour), the actual latest time in the day is returned. This can only arise when the time representation is a time-zone or local time.

    When *zone* has a timeSpec() of [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) or [UTC](qt.html#TimeSpec-UTC), the time representation has no transitions so the end of the day is [QTime](qtime.html)(23, 59, 59, 999).

    In the rare case of a date that was entirely skipped (this happens when a zone east of the international date-line switches to being west of it), the return shall be invalid. Passing an invalid time-zone as *zone* will also produce an invalid result, as shall dates that end outside the range representable by [QDateTime](qdatetime.html).

    See also

    [startOfDay()](#startOfDay).

---

endOfDay(spec: [TimeSpec](qt.html#TimeSpec) = [LocalTime](qt.html#TimeSpec-LocalTime), offsetSeconds: int = 0) → [QDateTime](qdatetime.html)
:   Use `endOfDay(const QTimeZone &) instead. Returns the end-moment of the day. When a day ends depends on a how time is described: each day starts and ends earlier for those with higher offsets from UTC and later for those with lower offsets from UTC. The time representation to use can be specified either by a \a spec and \a offsetSeconds (ignored unless \a spec is Qt::OffsetSeconds) or by a time zone. Usually, the end of the day is one millisecond before the midnight, 24:00: however, if a local time transition causes the given date to skip over that moment (e.g. a DST spring-forward skipping over 23:00 and the following hour), the actual latest time in the day is returned. When \a spec is Qt::OffsetFromUTC, \a offsetSeconds gives the implied zone's offset from UTC. As UTC and such zones have no transitions, the end of the day is QTime(23, 59, 59, 999) in these cases. In the rare case of a date that was entirely skipped (this happens when a zone east of the international date-line switches to being west of it), the return shall be invalid. Passing Qt::TimeZone as \a spec (instead of passing a QTimeZone) will also produce an invalid result, as shall dates that end outside the range representable by QDateTime.`

---

\_\_eq\_\_(QDate|datetime.date) → bool
:   TODO

---

@staticmethod fromJulianDay(int) → QDate
:   Converts the Julian day *jd* to a QDate.

    See also

    [toJulianDay()](#toJulianDay).

---

@staticmethod fromString(str|None, format: [DateFormat](qt.html#DateFormat) = [TextDate](qt.html#DateFormat-TextDate)) → QDate
:   Returns the QDate represented by the *string*, using the *format* given, or an invalid date if the string cannot be parsed.

    Note for [TextDate](qt.html#DateFormat-TextDate): only English month names (e.g. “Jan” in short form or “January” in long form) are recognized.

    See also

    [toString()](#toString), [toDate()](qlocale.html#toDate).

---

@staticmethod fromString(str|None, str|None, cal: [QCalendar](qcalendar.html) = QCalendar()) → QDate
:   TODO

---

@staticmethod fromString(str|None, str|None, int, cal: [QCalendar](qcalendar.html) = QCalendar()) → QDate
:   Returns the QDate represented by the *string*, using the *format* given, or an invalid date if the string cannot be parsed.

    Uses *cal* as calendar if supplied, else the Gregorian calendar. Ranges of values in the format descriptions below are for the latter; they may be different for other calendars.

    These expressions may be used for the format:

    | Expression | Output |
    | --- | --- |
    | d | The day as a number without a leading zero (1 to 31) |
    | dd | The day as a number with a leading zero (01 to 31) |
    | ddd | The abbreviated day name (‘Mon’ to ‘Sun’). |
    | dddd | The long day name (‘Monday’ to ‘Sunday’). |
    | M | The month as a number without a leading zero (1 to 12) |
    | MM | The month as a number with a leading zero (01 to 12) |
    | MMM | The abbreviated month name (‘Jan’ to ‘Dec’). |
    | MMMM | The long month name (‘January’ to ‘December’). |
    | yy | The year as a two digit number (00 to 99) |
    | yyyy | The year as a four digit number, possibly plus a leading minus sign for negative years. |

    **Note:** Day and month names must be given in English (C locale). If localized month and day names are to be recognized, use [system()](qlocale.html#system).toDate().

    All other input characters will be treated as text. Any non-empty sequence of characters enclosed in single quotes will also be treated (stripped of the quotes) as text and not be interpreted as expressions. For example:

    ```
    # QDate date = QDate::fromString("1MM12car2003", "d'MM'MMcaryyyy");
    # // date is 1 December 2003
    ```

    If the format is not satisfied, an invalid QDate is returned. The expressions that don’t expect leading zeroes (d, M) will be greedy. This means that they will use two digits even if this will put them outside the accepted range of values and leaves too few digits for other sections. For example, the following format string could have meant January 30 but the M will grab two digits, resulting in an invalid date:

    ```
    # QDate date = QDate::fromString("130", "Md"); // invalid
    ```

    For any field that is not represented in the format the following defaults are used:

    | Field | Default value |
    | --- | --- |
    | Year | *baseYear* (or 1900) |
    | Month | 1 (January) |
    | Day | 1 |

    When *format* only specifies the last two digits of a year, the 100 years starting at *baseYear* are the candidates first considered. Prior to 6.7 there was no *baseYear* parameter and 1900 was always used. This is the default for *baseYear*, selecting a year from then to 1999. Passing 1976 as *baseYear* will select a year from 1976 through 2075, for example. When the format also includes month, day (of month) and day-of-week, these suffice to imply the century. In such a case, a matching date is selected in the nearest century to the one indicated by *baseYear*, prefering later over earlier. See [matchCenturyToWeekday()](qcalendar.html#matchCenturyToWeekday) and Date ambiguities for further details,

    The following examples demonstrate the default values:

    ```
    # QDate::fromString("1.30", "M.d");           // January 30 1900
    # QDate::fromString("20000110", "yyyyMMdd");  // January 10, 2000
    # QDate::fromString("20000110", "yyyyMd");    // January 10, 2000
    ```

    **Note:** If a format character is repeated more times than the longest expression in the table above using it, this part of the format will be read as several expressions with no separator between them; the longest above, possibly repeated as many times as there are copies of it, ending with a residue that may be a shorter expression. Thus `'MMMMMMMMMM'` would match `"MayMay05"` and set the month to May. Likewise, `'MMMMMM'` would match `"May08"` and find it inconsistent, leading to an invalid date.

    ### Date ambiguities[¶](#date-ambiguities "Link to this heading")

    Different cultures use different formats for dates and, as a result, users may mix up the order in which date fields should be given. For example, `"Wed 28-Nov-01"` might mean either 2028 November 1st or the 28th of November, 2001 (each of which happens to be a Wednesday). Using format `"ddd yy-MMM-dd"` it shall be interpreted the first way, using `"ddd dd-MMM-yy"` the second. However, which the user meant may depend on the way the user normally writes dates, rather than the format the code was expecting.

    The example considered above mixed up day of the month and a two-digit year. Similar confusion can arise over interchanging the month and day of the month, when both are given as numbers. In these cases, including a day of the week field in the date format can provide some redundancy, that may help to catch errors of this kind. However, as in the example above, this is not always effective: the interchange of two fields (or their meanings) may produce dates with the same day of the week.

    Including a day of the week in the format can also resolve the century of a date specified using only the last two digits of its year. Unfortunately, when combined with a date in which the user (or other source of data) has mixed up two of the fields, this resolution can lead to finding a date which does match the format’s reading but isn’t the one intended by its author. Likewise, if the user simply gets the day of the week wrong, in an otherwise correct date, this can lead a date in a different century. In each case, finding a date in a different century can turn a wrongly-input date into a wildly different one.

    The best way to avoid date ambiguities is to use four-digit years and months specified by name (whether full or abbreviated), ideally collected via user interface idioms that make abundantly clear to the user which part of the date they are selecting. Including a day of the week can also help by providing the means to check consistency of the data. Where data comes from the user, using a format supplied by a locale selected by the user, it is best to use a long format as short formats are more likely to use two-digit years. Of course, it is not always possible to control the format - data may come from a source you do not control, for example.

    As a result of these possible sources of confusion, particularly when you cannot be sure an unambiguous format is in use, it is important to check that the result of reading a string as a date is not just valid but reasonable for the purpose for which it was supplied. If the result is outside some range of reasonable values, it may be worth getting the user to confirm their date selection, showing the date read from the string in a long format that does include month name and four-digit year, to make it easier for them to recognize any errors.

    See also

    [toString()](#toString), [fromString()](qdatetime.html#fromString), [fromString()](qtime.html#fromString), [toDate()](qlocale.html#toDate).

---

\_\_ge\_\_(QDate|datetime.date) → bool
:   TODO

---

getDate() → (int, int, int)
:   Extracts the date’s year, month, and day, and assigns them to \**year*, \**month*, and \**day*. The pointers may be null.

    Returns 0 if the date is invalid.

    **Note:** In Qt versions prior to 5.7, this function is marked as non-`const`.

    See also

    [year()](#year), [month()](#month), [day()](#day), [isValid()](#isValid), [partsFromDate()](qcalendar.html#partsFromDate).

---

\_\_gt\_\_(QDate|datetime.date) → bool
:   TODO

---

\_\_hash\_\_() → int
:   TODO

---

@staticmethod isLeapYear(int) → bool
:   Returns `true` if the specified *year* is a leap year in the Gregorian calendar; otherwise returns `false`.

    See also

    [isLeapYear()](qcalendar.html#isLeapYear).

---

isNull() → bool
:   Returns `true` if the date is null; otherwise returns `false`. A null date is invalid.

    **Note:** The behavior of this function is equivalent to [isValid()](#isValid).

    See also

    [isValid()](#isValid).

---

isValid() → bool
:   Returns `true` if this date is valid; otherwise returns `false`.

    See also

    [isNull()](#isNull), [isDateValid()](qcalendar.html#isDateValid).

---

@staticmethod isValid(int, int, int) → bool
:   Returns `true` if the specified date (*year*, *month*, and *day*) is valid in the Gregorian calendar; otherwise returns `false`.

    Example:

    ```
    # QDate::isValid(2002, 5, 17);  // true
    # QDate::isValid(2002, 2, 30);  // false (Feb 30 does not exist)
    # QDate::isValid(2004, 2, 29);  // true (2004 is a leap year)
    # QDate::isValid(2000, 2, 29);  // true (2000 is a leap year)
    # QDate::isValid(2006, 2, 29);  // false (2006 is not a leap year)
    # QDate::isValid(2100, 2, 29);  // false (2100 is not a leap year)
    # QDate::isValid(1202, 6, 6);   // true (even though 1202 is pre-Gregorian)
    ```

    See also

    [isNull()](#isNull), [setDate()](#setDate), [isDateValid()](qcalendar.html#isDateValid).

---

\_\_le\_\_(QDate|datetime.date) → bool
:   TODO

---

\_\_lt\_\_(QDate|datetime.date) → bool
:   TODO

---

month() → int
:   This is an overloaded function.

---

month([QCalendar](qcalendar.html)) → int
:   Returns the month-number for the date.

    Numbers the months of the year starting with 1 for the first. Uses *cal* as calendar if supplied, else the Gregorian calendar, for which the month numbering is as follows:

    * 1 = “January”
    * 2 = “February”
    * 3 = “March”
    * 4 = “April”
    * 5 = “May”
    * 6 = “June”
    * 7 = “July”
    * 8 = “August”
    * 9 = “September”
    * 10 = “October”
    * 11 = “November”
    * 12 = “December”

    Returns 0 if the date is invalid. Note that some calendars may have more than 12 months in some years.

    See also

    [year()](#year), [day()](#day), [partsFromDate()](qcalendar.html#partsFromDate).

---

\_\_ne\_\_(QDate|datetime.date) → bool
:   TODO

---

\_\_repr\_\_() → str
:   TODO

---

setDate(int, int, int) → bool
:   Sets this to represent the date, in the Gregorian calendar, with the given *year*, *month* and *day* numbers. Returns true if the resulting date is valid, otherwise it sets this to represent an invalid date and returns false.

    See also

    [isValid()](#isValid), [dateFromParts()](qcalendar.html#dateFromParts).

---

setDate(int, int, int, [QCalendar](qcalendar.html)) → bool
:   Sets this to represent the date, in the given calendar *cal*, with the given *year*, *month* and *day* numbers. Returns true if the resulting date is valid, otherwise it sets this to represent an invalid date and returns false.

    See also

    [isValid()](#isValid), [dateFromParts()](qcalendar.html#dateFromParts).

---

startOfDay([QTimeZone](qtimezone.html)) → [QDateTime](qdatetime.html)
:   Returns the start-moment of the day.

    When a day starts depends on a how time is described: each day starts and ends earlier for those in time-zones further west and later for those in time-zones further east. The time representation to use can be specified by an optional time *zone*. The default time representation is the system’s local time.

    Usually, the start of the day is midnight, 00:00: however, if a time-zone transition causes the given date to skip over that midnight (e.g. a DST spring-forward skipping over the first hour of the day day), the actual earliest time in the day is returned. This can only arise when the time representation is a time-zone or local time.

    When *zone* has a timeSpec() of is [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) or [UTC](qt.html#TimeSpec-UTC), the time representation has no transitions so the start of the day is [QTime](qtime.html)(0, 0).

    In the rare case of a date that was entirely skipped (this happens when a zone east of the international date-line switches to being west of it), the return shall be invalid. Passing an invalid time-zone as *zone* will also produce an invalid result, as shall dates that start outside the range representable by [QDateTime](qdatetime.html).

    See also

    [endOfDay()](#endOfDay).

---

startOfDay(spec: [TimeSpec](qt.html#TimeSpec) = [LocalTime](qt.html#TimeSpec-LocalTime), offsetSeconds: int = 0) → [QDateTime](qdatetime.html)
:   Use `startOfDay(const QTimeZone &)` instead.

    Returns the start-moment of the day.

    When a day starts depends on a how time is described: each day starts and ends earlier for those with higher offsets from UTC and later for those with lower offsets from UTC. The time representation to use can be specified either by a *spec* and *offsetSeconds* (ignored unless *spec* is Qt::OffsetSeconds) or by a time zone.

    Usually, the start of the day is midnight, 00:00: however, if a local time transition causes the given date to skip over that midnight (e.g. a DST spring-forward skipping over the first hour of the day day), the actual earliest time in the day is returned.

    When *spec* is [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC), *offsetSeconds* gives an implied zone’s offset from UTC. As UTC and such zones have no transitions, the start of the day is [QTime](qtime.html)(0, 0) in these cases.

    In the rare case of a date that was entirely skipped (this happens when a zone east of the international date-line switches to being west of it), the return shall be invalid. Passing [TimeZone](qt.html#TimeSpec-TimeZone) as *spec* (instead of passing a [QTimeZone](qtimezone.html)) will also produce an invalid result, as shall dates that start outside the range representable by [QDateTime](qdatetime.html).

---

toJulianDay() → int
:   Converts the date to a Julian day.

    See also

    [fromJulianDay()](#fromJulianDay).

---

toPyDate() → datetime.date
:   TODO

---

toString(format: [DateFormat](qt.html#DateFormat) = [TextDate](qt.html#DateFormat-TextDate)) → str
:   Returns the date as a string. The *format* parameter determines the format of the string.

    If the *format* is [TextDate](qt.html#DateFormat-TextDate), the string is formatted in the default way. The day and month names will be in English. An example of this formatting is “Sat May 20 1995”. For localized formatting, see [toString()](qlocale.html#toString).

    If the *format* is [ISODate](qt.html#DateFormat-ISODate), the string format corresponds to the ISO 8601 extended specification for representations of dates and times, taking the form yyyy-MM-dd, where yyyy is the year, MM is the month of the year (between 01 and 12), and dd is the day of the month between 01 and 31.

    If the *format* is [RFC2822Date](qt.html#DateFormat-RFC2822Date), the string is formatted in an RFC 2822 compatible way. An example of this formatting is “20 May 1995”.

    If the date is invalid, an empty string will be returned.

    **Warning:** The [ISODate](qt.html#DateFormat-ISODate) format is only valid for years in the range 0 to 9999.

    See also

    [fromString()](#fromString), [toString()](qlocale.html#toString).

---

toString(str|None, cal: [QCalendar](qcalendar.html) = QCalendar()) → str
:   TODO

---

weekNumber() → (int, int)
:   Returns the ISO 8601 week number (1 to 53).

    Returns 0 if the date is invalid. Otherwise, returns the week number for the date. If *yearNumber* is not `nullptr` (its default), stores the year as \**yearNumber*.

    In accordance with ISO 8601, each week falls in the year to which most of its days belong, in the Gregorian calendar. As ISO 8601’s week starts on Monday, this is the year in which the week’s Thursday falls. Most years have 52 weeks, but some have 53.

    **Note:** \**yearNumber* is not always the same as [year()](#year). For example, 1 January 2000 has week number 52 in the year 1999, and 31 December 2002 has week number 1 in the year 2003.

    See also

    [isValid()](#isValid).

---

year() → int
:   This is an overloaded function.

---

year([QCalendar](qcalendar.html)) → int
:   Returns the year of this date.

    Uses *cal* as calendar, if supplied, else the Gregorian calendar.

    Returns 0 if the date is invalid. For some calendars, dates before their first year may all be invalid.

    If using a calendar which has a year 0, check using [isValid()](#isValid) if the return is 0. Such calendars use negative year numbers in the obvious way, with year 1 preceded by year 0, in turn preceded by year -1 and so on.

    Some calendars, despite having no year 0, have a conventional numbering of the years before their first year, counting backwards from 1. For example, in the proleptic Gregorian calendar, successive years before 1 CE (the first year) are identified as 1 BCE, 2 BCE, 3 BCE and so on. For such calendars, negative year numbers are used to indicate these years before year 1, with -1 indicating the year before 1.

    See also

    [month()](#month), [day()](#day), [hasYearZero()](qcalendar.html#hasYearZero), [isProleptic()](qcalendar.html#isProleptic), [partsFromDate()](qcalendar.html#partsFromDate).

### [Table of Contents](../../index.html)

* QDate
  + [Description](#description)
    - [Remarks](#remarks)
      * [Range of Valid Dates](#range-of-valid-dates)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QDate

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QDateTime {#qdatetime}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QDateTime

# QDateTime[¶](#qdatetime "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QDateTime

## Description[¶](#description "Link to this heading")

The QDateTime class provides date and time functions.

A QDateTime object encodes a calendar date and a clock time (a “datetime”) in accordance with a time representation. It combines features of the [QDate](qdate.html) and [QTime](qtime.html) classes. It can read the current datetime from the system clock. It provides functions for comparing datetimes and for manipulating a datetime by adding a number of seconds, days, months, or years.

QDateTime can describe datetimes with respect to [LocalTime](qt.html#TimeSpec-LocalTime), to [UTC](qt.html#TimeSpec-UTC), to a specified [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) or to a specified [TimeZone](qt.html#TimeSpec-TimeZone). Each of these time representations can be encapsulated in a suitable instance of the [QTimeZone](qtimezone.html) class. For example, a time zone of “Europe/Berlin” will apply the daylight-saving rules as used in Germany. In contrast, a fixed offset from UTC of +3600 seconds is one hour ahead of UTC (usually written in ISO standard notation as “UTC+01:00”), with no daylight-saving complications. When using either local time or a specified time zone, time-zone transitions (see [Timezone transitions](#qdatetime-timezone-transitions)) are taken into account. A QDateTime’s [timeSpec()](#timeSpec) will tell you which of the four types of time representation is in use; its [timeRepresentation()](#timeRepresentation) provides a full description of that time representation, as a [QTimeZone](qtimezone.html).

A QDateTime object is typically created either by giving a date and time explicitly in the constructor, or by using a static function such as [currentDateTime()](#currentDateTime) or [fromMSecsSinceEpoch()](#fromMSecsSinceEpoch). The date and time can be changed with [setDate()](#setDate) and [setTime()](#setTime). A datetime can also be set using the [setMSecsSinceEpoch()](#setMSecsSinceEpoch) function that takes the time, in milliseconds, since the start, in UTC, of the year 1970. The [fromString()](#fromString) function returns a QDateTime, given a string and a date format used to interpret the date within the string.

[currentDateTime()](#currentDateTime) returns a QDateTime that expresses the current date and time with respect to a specific time representation, such as local time (its default). [currentDateTimeUtc()](#currentDateTimeUtc) returns a QDateTime that expresses the current date and time with respect to UTC; it is equivalent to `QDateTime::currentDateTime(QTimeZone::UTC)`.

The [date()](#date) and [time()](#time) functions provide access to the date and time parts of the datetime. The same information is provided in textual format by the [toString()](#toString) function.

QDateTime provides a full set of operators to compare two QDateTime objects, where smaller means earlier and larger means later.

You can increment (or decrement) a datetime by a given number of milliseconds using [addMSecs()](#addMSecs), seconds using [addSecs()](#addSecs), or days using [addDays()](#addDays). Similarly, you can use [addMonths()](#addMonths) and [addYears()](#addYears). The [daysTo()](#daysTo) function returns the number of days between two datetimes, [secsTo()](#secsTo) returns the number of seconds between two datetimes, and [msecsTo()](#msecsTo) returns the number of milliseconds between two datetimes. These operations are aware of daylight-saving time (DST) and other time-zone transitions, where applicable.

Use [toTimeZone()](#toTimeZone) to re-express a datetime in terms of a different time representation. By passing a lightweight [QTimeZone](qtimezone.html) that represents local time, UTC or a fixed offset from UTC, you can convert the datetime to use the corresponding time representation; or you can pass a full time zone (whose [timeSpec()](qtimezone.html#timeSpec) is `Qt::TimeZone`) to use that instead.

### Remarks[¶](#remarks "Link to this heading")

QDateTime does not account for leap seconds.

All conversions to and from string formats are done using the C locale. For localized conversions, see [QLocale](qlocale.html).

There is no year 0 in the Gregorian calendar. Dates in that year are considered invalid. The year -1 is the year “1 before Christ” or “1 before common era.” The day before 1 January 1 CE is 31 December 1 BCE.

Using local time (the default) or a specified time zone implies a need to resolve any issues around [Timezone transitions](#qdatetime-timezone-transitions). As a result, operations on such QDateTime instances (notably including constructing them) may be more expensive than the equivalent when using UTC or a fixed offset from it.

#### Range of Valid Dates[¶](#range-of-valid-dates "Link to this heading")

The range of values that QDateTime can represent is dependent on the internal storage implementation. QDateTime is currently stored in a qint64 as a serial msecs value encoding the date and time. This restricts the date range to about ±292 million years, compared to the [QDate](qdate.html) range of ±2 billion years. Care must be taken when creating a QDateTime with extreme values that you do not overflow the storage. The exact range of supported values varies depending on the time representation used.

#### Use of Timezones[¶](#use-of-timezones "Link to this heading")

QDateTime uses the system’s time zone information to determine the current local time zone and its offset from UTC. If the system is not configured correctly or not up-to-date, QDateTime will give wrong results.

QDateTime likewise uses system-provided information to determine the offsets of other timezones from UTC. If this information is incomplete or out of date, QDateTime will give wrong results. See the [QTimeZone](qtimezone.html) documentation for more details.

On modern Unix systems, this means QDateTime usually has accurate information about historical transitions (including DST, see below) whenever possible. On Windows, where the system doesn’t support historical timezone data, historical accuracy is not maintained with respect to timezone transitions, notably including DST. However, building Qt with the ICU library will equip [QTimeZone](qtimezone.html) with the same timezone database as is used on Unix.

#### Timezone transitions[¶](#timezone-transitions "Link to this heading")

QDateTime takes into account timezone transitions, both the transitions between Standard Time and Daylight-Saving Time (DST) and the transitions that arise when a zone changes its standard offset. For example, if the transition is at 2am and the clock goes forward to 3am, then there is a “missing” hour from 02:00:00 to 02:59:59.999. Such a transition is known as a “spring forward” and the times skipped over have no meaning. When a transition goes the other way, known as a “fall back”, a time interval is repeated, first in the old zone (usually DST), then in the new zone (usually Standard Time), so times in this interval are ambiguous.

Some zones use “reversed” DST, using standard time in summer and daylight-saving time (with a lowered offset) in winter. For such zones, the spring forward still happens in spring and skips an hour, but is a transition *out of* daylight-saving time, while the fall back still repeats an autumn hour but is a transition *to* daylight-saving time.

When converting from a UTC time (or a time at fixed offset from UTC), there is always an unambiguous valid result in any timezone. However, when combining a date and time to make a datetime, expressed with respect to local time or a specific time-zone, the nominal result may fall in a transition, making it either invalid or ambiguous. Methods where this situation may arise take a `resolve` parameter: this is always ignored if the requested datetime is valid and unambiguous. See TransitionResolution for the options it lets you control. Prior to Qt 6.7, the equivalent of its [LegacyBehavior](#TransitionResolution-LegacyBehavior) was selected.

For a spring forward’s skipped interval, interpreting the requested time with either offset yields an actual time at which the other offset was in use; so passing `TransitionResolution::RelativeToBefore` for `resolve` will actually result in a time after the transition, that would have had the requested representation had the transition not happened. Likewise, `TransitionResolution::RelativeToAfter` for `resolve` results in a time before the transition, that would have had the requested representation, had the transition happened earlier.

When QDateTime performs arithmetic, as with addDay() or [addSecs()](#addSecs), it takes care to produce a valid result. For example, on a day when there is a spring forward from 02:00 to 03:00, adding one second to 01:59:59 will get 03:00:00. Adding one day to 02:30 on the preceding day will get 03:30 on the day of the transition, while subtracting one day, by calling `addDay(-1)`, to 02:30 on the following day will get 01:30 on the day of the transition. While [addSecs()](#addSecs) will deliver a time offset by the given number of seconds, [addDays()](#addDays) adjusts the date and only adjusts time if it would otherwise get an invalid result. Applying `addDays(1)` to 03:00 on the day before the spring-forward will simply get 03:00 on the day of the transition, even though the latter is only 23 hours after the former; but `addSecs(24 \* 60 \* 60)` will get 04:00 on the day of the transition, since that’s 24 hours later. Typical transitions make some days 23 or 25 hours long.

For datetimes that the system `time_t` can represent (from 1901-12-14 to 2038-01-18 on systems with 32-bit `time_t`; for the full range QDateTime can represent if the type is 64-bit), the standard system APIs are used to determine local time’s offset from UTC. For datetimes not handled by these system APIs (potentially including some within the `time_t` range), [systemTimeZone()](qtimezone.html#systemTimeZone) is used, if available, or a best effort is made to estimate. In any case, the offset information used depends on the system and may be incomplete or, for past times, historically inaccurate. Furthermore, for future dates, the local time zone’s offsets and DST rules may change before that date comes around.

##### Whole day transitions[¶](#whole-day-transitions "Link to this heading")

A small number of zones have skipped or repeated entire days as part of moving The International Date Line across themselves. For these, [daysTo()](#daysTo) will be unaware of the duplication or gap, simply using the difference in calendar date; in contrast, [msecsTo()](#msecsTo) and [secsTo()](#secsTo) know the true time interval. Likewise, [addMSecs()](#addMSecs) and [addSecs()](#addSecs) correspond directly to elapsed time, where [addDays()](#addDays), [addMonths()](#addMonths) and [addYears()](#addYears) follow the nominal calendar, aside from where landing in a gap or duplication requires resolving an ambiguity or invalidity due to a duplication or omission.

**Note:** Days “lost” during a change of calendar, such as from Julian to Gregorian, do not affect QDateTime. Although the two calendars describe dates differently, the successive days across the change are described by consecutive [QDate](qdate.html) instances, each one day later than the previous, as described by either calendar or by their toJulianDay() values. In contrast, a zone skipping or duplicating a day is changing its description of *time*, not date, for all that it does so by a whole 24 hours.

#### Offsets From UTC[¶](#offsets-from-utc "Link to this heading")

Offsets from UTC are measured in seconds east of Greenwich. The moment described by a particular date and time, such as noon on a particular day, depends on the time representation used. Those with a higher offset from UTC describe an earlier moment, and those with a lower offset a later moment, by any given combination of date and time.

There is no explicit size restriction on an offset from UTC, but there is an implicit limit imposed when using the [toString()](#toString) and [fromString()](#fromString) methods which use a ±hh:mm format, effectively limiting the range to ± 99 hours and 59 minutes and whole minutes only. Note that currently no time zone has an offset outside the range of ±14 hours and all known offsets are multiples of five minutes. Historical time zones have a wider range and may have offsets including seconds; these last cannot be faithfully represented in strings.

See also

[QDate](qdate.html), [QTime](qtime.html), [QDateTimeEdit](../qtwidgets/qdatetimeedit.html), [QTimeZone](qtimezone.html).

## Enums[¶](#enums "Link to this heading")

TransitionResolution
:   This enumeration is used to resolve datetime combinations which fall in [Timezone transitions](#qdatetime-timezone-transitions).

    When constructing a datetime, specified in terms of local time or a time-zone that has daylight-saving time, or revising one with [setDate()](#setDate), [setTime()](#setTime) or [setTimeZone()](#setTimeZone), the given parameters may imply a time representation that either has no meaning or has two meanings in the zone. Such time representations are described as being in the transition. In either case, we can simply return an invalid datetime, to indicate that the operation is ill-defined. In the ambiguous case, we can alternatively select one of the two times that could be meant. When there is no meaning, we can select a time either side of it that might plausibly have been meant. For example, when advancing from an earlier time, we can select the time after the transition that is actually the specified amount of time after the earlier time in question. The options specified here configure how such selection is performed.

    An additional constant, `LegacyBehavior`, is used as a default value for TransitionResolution parameters in some constructors and setter functions. This is an alias for `RelativeToBefore`, which implements behavior that most closely matches the behavior of QDateTime prior to Qt 6.7.

    For [addDays()](#addDays), [addMonths()](#addMonths) or [addYears()](#addYears), the behavior is and (mostly) was to use `RelativeToBefore` if adding a positive adjustment and `RelativeToAfter` if adding a negative adjustment.

    **Note:** In time zones where daylight-saving increases the offset from UTC in summer (known as “positive DST”), PreferStandard is an alias for RelativeToAfter and PreferDaylightSaving for RelativeToBefore. In time zones where the daylight-saving mechanism is a decrease in offset from UTC in winter (known as “negative DST”), the reverse applies, provided the operating system reports - as it does on most platforms - whether a datetime is in DST or standard time. For some platforms, where transition details are unavailable even for [TimeZone](qt.html#TimeSpec-TimeZone) datetimes, [QTimeZone](qtimezone.html) is obliged to presume that the side with lower offset from UTC is standard time, effectively assuming positive DST.

    The following tables illustrate how a QDateTime constructor resolves a request for 02:30 on a day when local time has a transition between 02:00 and 03:00, with a nominal standard time LST and daylight-saving time LDT on the two sides, in the various possible cases. The transition type may be to skip an hour or repeat it. The type of transition and value of a parameter `resolve` determine which actual time on the given date is selected. First, the common case of positive daylight-saving, where:

    | Before | 02:00–03:00 | After | `resolve` | selected |
    | --- | --- | --- | --- | --- |
    | LST | skip | LDT | RelativeToBefore | 03:30 LDT |
    | LST | skip | LDT | RelativeToAfter | 01:30 LST |
    | LST | skip | LDT | PreferBefore | 01:30 LST |
    | LST | skip | LDT | PreferAfter | 03:30 LDT |
    | LST | skip | LDT | PreferStandard | 01:30 LST |
    | LST | skip | LDT | PreferDaylightSaving | 03:30 LDT |
    | LDT | repeat | LST | RelativeToBefore | 02:30 LDT |
    | LDT | repeat | LST | RelativeToAfter | 02:30 LST |
    | LDT | repeat | LST | PreferBefore | 02:30 LDT |
    | LDT | repeat | LST | PreferAfter | 02:30 LST |
    | LDT | repeat | LST | PreferStandard | 02:30 LST |
    | LDT | repeat | LST | PreferDaylightSaving | 02:30 LDT |

    Second, the case for negative daylight-saving, using LDT in winter and skipping an hour to transition to LST in summer, then repeating an hour at the transition back to winter:

    |  |  |  |  |  |
    | --- | --- | --- | --- | --- |
    | LDT | skip | LST | RelativeToBefore | 03:30 LST |
    | LDT | skip | LST | RelativeToAfter | 01:30 LDT |
    | LDT | skip | LST | PreferBefore | 01:30 LDT |
    | LDT | skip | LST | PreferAfter | 03:30 LST |
    | LDT | skip | LST | PreferStandard | 03:30 LST |
    | LDT | skip | LST | PreferDaylightSaving | 01:30 LDT |
    | LST | repeat | LDT | RelativeToBefore | 02:30 LST |
    | LST | repeat | LDT | RelativeToAfter | 02:30 LDT |
    | LST | repeat | LDT | PreferBefore | 02:30 LST |
    | LST | repeat | LDT | PreferAfter | 02:30 LDT |
    | LST | repeat | LDT | PreferStandard | 02:30 LST |
    | LST | repeat | LDT | PreferDaylightSaving | 02:30 LDT |

    Reject can be used to prompt relevant QDateTime APIs to return an invalid datetime object so that your code can deal with transitions for itself, for example by alerting a user to the fact that the datetime they have selected is in a transition interval, to offer them the opportunity to resolve a conflict or ambiguity. Code using this may well find the other options above useful to determine relevant information to use in its own (or the user’s) resolution. If the start or end of the transition, or the moment of the transition itself, is the right resolution, [QTimeZone](qtimezone.html)’s transition APIs can be used to obtain that information. You can determine whether the transition is a repeated or skipped interval by using [secsTo()](#secsTo) to measure the actual time between noon on the previous and following days. The result will be less than 48 hours for a skipped interval (such as a spring-forward) and more than 48 hours for a repeated interval (such as a fall-back).

    **Note:** When a resolution other than Reject is specified, a valid QDateTime object is returned, if possible. If the requested date-time falls in a gap, the returned date-time will not have the [time()](#time) requested - or, in some cases, the [date()](#date), if a whole day was skipped. You can thus detect when a gap is hit by comparing [date()](#date) and [time()](#time) to what was requested.

    ### Relation to other datetime software[¶](#relation-to-other-datetime-software "Link to this heading")

    The Python programming language’s datetime APIs have a `fold` parameter that corresponds to `RelativeToBefore` (`fold = True`) and `RelativeToAfter` (`fold = False`).

    The `Temporal` proposal to replace JavaScript’s `Date` offers four options for how to resolve a transition, as value for a `disambiguation` parameter. Its `'reject'` raises an exception, which roughly corresponds to `Reject` producing an invalid result. Its `'earlier'` and `'later'` options correspond to `PreferBefore` and `PreferAfter`. Its `'compatible'` option corresponds to `RelativeToBefore` (and Python’s `fold = True`).

    See also

    [Timezone transitions](#qdatetime-timezone-transitions).

    | Member | Value | Description |
    | --- | --- | --- |
    | LegacyBehavior | RelativeToBefore | An alias for RelativeToBefore, which is used as default for TransitionResolution parameters, as this most closely matches the behavior prior to Qt 6.7. |
    | PreferAfter | 4 | Selects a time after the transition. |
    | PreferBefore | 3 | Selects a time before the transition, |
    | PreferDaylightSaving | 6 | Selects a time on the daylight-saving-time side of the transition. |
    | PreferStandard | 5 | Selects a time on the standard time side of the transition. |
    | Reject | 0 | Treat any time in a transition as invalid. Either it really is, or it is ambiguous. |
    | RelativeToAfter | 2 | Select a time as if stepping backward from a time after the transition. This interprets the requested time using the offset in effect after the transition and, if necessary, converts the result to the offset in effect at the resulting time. |
    | RelativeToBefore | 1 | Selects a time as if stepping forward from a time before the transition. This interprets the requested time using the offset in effect before the transition and, if necessary, converts the result to the offset in effect at the resulting time. |

---

YearRange
:   This enumerated type describes the range of years (in the Gregorian calendar) representable by QDateTime:

    All dates strictly between these two years are also representable. Note, however, that the Gregorian Calendar has no year zero.

    **Note:** [QDate](qdate.html) can describe dates in a wider range of years. For most purposes, this makes little difference, as the range of years that QDateTime can support reaches 292 million years either side of 1970.

    See also

    [isValid()](#isValid), [QDate](qdate.html).

    | Member | Value | Description |
    | --- | --- | --- |
    | First | -292275056 | The later parts of this year are representable |
    | Last | +292278994 | The earlier parts of this year are representable |

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs a null datetime, nominally using local time.

    A null datetime is invalid, since its date and time are invalid.

    See also

    [isValid()](#isValid), [setMSecsSinceEpoch()](#setMSecsSinceEpoch), [setDate()](#setDate), [setTime()](#setTime), [setTimeZone()](#setTimeZone).

---

\_\_init\_\_(QDateTime|datetime.datetime)
:   Constructs a copy of the *other* datetime.

---

\_\_init\_\_([QDate](qdate.html)|datetime.date, [QTime](qtime.html)|datetime.time, [TransitionResolution](#TransitionResolution))
:   Constructs a datetime with the given *date* and *time*, using local time.

    If *date* is valid and *time* is not, midnight will be used as the time. If *date* and *time* describe a moment close to a transition for local time, *resolve* controls how that situation is resolved.

    **Note:** Prior to Qt 6.7, the version of this function lacked the *resolve* parameter so had no way to resolve the ambiguities related to transitions.

---

\_\_init\_\_([QDate](qdate.html)|datetime.date, [QTime](qtime.html)|datetime.time, spec: [TimeSpec](qt.html#TimeSpec) = [LocalTime](qt.html#TimeSpec-LocalTime), offsetSeconds: int = 0)
:   Use `QDateTime(date, time)` or `QDateTime(date, time, QTimeZone::fromSecondsAheadOfUtc(offsetSeconds))`.

    Constructs a datetime with the given *date* and *time*, using the time representation implied by *spec* and *offsetSeconds* seconds.

    If *date* is valid and *time* is not, the time will be set to midnight.

    If *spec* is not [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) then *offsetSeconds* will be ignored. If *spec* is [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) and *offsetSeconds* is 0 then the [timeSpec()](#timeSpec) will be set to [UTC](qt.html#TimeSpec-UTC), i.e. an offset of 0 seconds.

    If *spec* is [TimeZone](qt.html#TimeSpec-TimeZone) then the spec will be set to [LocalTime](qt.html#TimeSpec-LocalTime), i.e. the current system time zone. To create a [TimeZone](qt.html#TimeSpec-TimeZone) datetime use the correct constructor.

    If *date* lies outside the range of dates representable by QDateTime, the result is invalid. If *spec* is [LocalTime](qt.html#TimeSpec-LocalTime) and the system’s time-zone skipped over the given date and time, the result is invalid.

---

\_\_init\_\_([QDate](qdate.html)|datetime.date, [QTime](qtime.html)|datetime.time, [QTimeZone](qtimezone.html), resolve: [TransitionResolution](#TransitionResolution) = [LegacyBehavior](#TransitionResolution-LegacyBehavior))
:   Constructs a datetime with the given *date* and *time*, using the time representation described by *timeZone*.

    If *date* is valid and *time* is not, the time will be set to midnight. If *timeZone* is invalid then the datetime will be invalid. If *date* and *time* describe a moment close to a transition for *timeZone*, *resolve* controls how that situation is resolved.

    **Note:** Prior to Qt 6.7, the version of this function lacked the *resolve* parameter so had no way to resolve the ambiguities related to transitions.

---

\_\_init\_\_(int, int, int, int, int, second: int = 0, msec: int = 0, timeSpec: int = 0)
:   TODO

---

addDays(int) → QDateTime
:   Returns a QDateTime object containing a datetime *ndays* days later than the datetime of this object (or earlier if *ndays* is negative).

    If the [timeSpec()](#timeSpec) is [LocalTime](qt.html#TimeSpec-LocalTime) or [TimeZone](qt.html#TimeSpec-TimeZone) and the resulting date and time fall in the Standard Time to Daylight-Saving Time transition hour then the result will be just beyond this gap, in the direction of change. If the transition is at 2am and the clock goes forward to 3am, the result of aiming between 2am and 3am will be adjusted to fall before 2am (if `ndays < 0`) or after 3am (otherwise).

    See also

    [daysTo()](#daysTo), [addMonths()](#addMonths), [addYears()](#addYears), [addSecs()](#addSecs), [Timezone transitions](#qdatetime-timezone-transitions).

---

addMonths(int) → QDateTime
:   Returns a QDateTime object containing a datetime *nmonths* months later than the datetime of this object (or earlier if *nmonths* is negative).

    If the [timeSpec()](#timeSpec) is [LocalTime](qt.html#TimeSpec-LocalTime) or [TimeZone](qt.html#TimeSpec-TimeZone) and the resulting date and time fall in the Standard Time to Daylight-Saving Time transition hour then the result will be just beyond this gap, in the direction of change. If the transition is at 2am and the clock goes forward to 3am, the result of aiming between 2am and 3am will be adjusted to fall before 2am (if `nmonths < 0`) or after 3am (otherwise).

    See also

    [daysTo()](#daysTo), [addDays()](#addDays), [addYears()](#addYears), [addSecs()](#addSecs), [Timezone transitions](#qdatetime-timezone-transitions).

---

addMSecs(int) → QDateTime
:   Returns a QDateTime object containing a datetime *msecs* miliseconds later than the datetime of this object (or earlier if *msecs* is negative).

    If this datetime is invalid, an invalid datetime will be returned.

    See also

    [addSecs()](#addSecs), [msecsTo()](#msecsTo), [addDays()](#addDays), [addMonths()](#addMonths), [addYears()](#addYears).

---

addSecs(int) → QDateTime
:   Returns a QDateTime object containing a datetime *s* seconds later than the datetime of this object (or earlier if *s* is negative).

    If this datetime is invalid, an invalid datetime will be returned.

    See also

    [addMSecs()](#addMSecs), [secsTo()](#secsTo), [addDays()](#addDays), [addMonths()](#addMonths), [addYears()](#addYears).

---

addYears(int) → QDateTime
:   Returns a QDateTime object containing a datetime *nyears* years later than the datetime of this object (or earlier if *nyears* is negative).

    If the [timeSpec()](#timeSpec) is [LocalTime](qt.html#TimeSpec-LocalTime) or [TimeZone](qt.html#TimeSpec-TimeZone) and the resulting date and time fall in the Standard Time to Daylight-Saving Time transition hour then the result will be just beyond this gap, in the direction of change. If the transition is at 2am and the clock goes forward to 3am, the result of aiming between 2am and 3am will be adjusted to fall before 2am (if `nyears < 0`) or after 3am (otherwise).

    See also

    [daysTo()](#daysTo), [addDays()](#addDays), [addMonths()](#addMonths), [addSecs()](#addSecs), [Timezone transitions](#qdatetime-timezone-transitions).

---

\_\_bool\_\_() → int
:   TODO

---

@staticmethod currentDateTime() → QDateTime
:   This is an overloaded function.

---

@staticmethod currentDateTime([QTimeZone](qtimezone.html)) → QDateTime
:   Returns the system clock’s current datetime, using the time representation described by *zone*. If *zone* is omitted, local time is used.

    See also

    [currentDateTimeUtc()](#currentDateTimeUtc), [currentDate()](qdate.html#currentDate), [currentTime()](qtime.html#currentTime), [toTimeZone()](#toTimeZone).

---

@staticmethod currentDateTimeUtc() → QDateTime
:   Returns the system clock’s current datetime, expressed in terms of UTC.

    Equivalent to `currentDateTime(QTimeZone::UTC)`.

    See also

    [currentDateTime()](#currentDateTime), [currentDate()](qdate.html#currentDate), [currentTime()](qtime.html#currentTime), [toTimeZone()](#toTimeZone).

---

@staticmethod currentMSecsSinceEpoch() → int
:   Returns the current number of milliseconds since the start, in UTC, of the year 1970.

    This number is like the POSIX time\_t variable, but expressed in milliseconds instead of seconds.

    See also

    [currentDateTime()](#currentDateTime), [currentDateTimeUtc()](#currentDateTimeUtc), [toTimeZone()](#toTimeZone).

---

@staticmethod currentSecsSinceEpoch() → int
:   Returns the number of seconds since the start, in UTC, of the year 1970.

    This number is like the POSIX time\_t variable.

    See also

    [currentMSecsSinceEpoch()](#currentMSecsSinceEpoch).

---

date() → [QDate](qdate.html)
:   Returns the date part of the datetime.

    See also

    [setDate()](#setDate), [time()](#time), [timeRepresentation()](#timeRepresentation).

---

daysTo(QDateTime|datetime.datetime) → int
:   Returns the number of days from this datetime to the *other* datetime. The number of days is counted as the number of times midnight is reached between this datetime to the *other* datetime. This means that a 10 minute difference from 23:55 to 0:05 the next day counts as one day.

    If the *other* datetime is earlier than this datetime, the value returned is negative.

    Example:

    ```
    # QDateTime startDate(QDate(2012, 7, 6), QTime(8, 30, 0));
    # QDateTime endDate(QDate(2012, 7, 7), QTime(16, 30, 0));
    # qDebug() << "Days from startDate to endDate: " << startDate.daysTo(endDate);

    # startDate = QDateTime(QDate(2012, 7, 6), QTime(23, 55, 0));
    # endDate = QDateTime(QDate(2012, 7, 7), QTime(0, 5, 0));
    # qDebug() << "Days from startDate to endDate: " << startDate.daysTo(endDate);

    # qSwap(startDate, endDate); // Make endDate before startDate.
    # qDebug() << "Days from startDate to endDate: " << startDate.daysTo(endDate);
    ```

    See also

    [addDays()](#addDays), [secsTo()](#secsTo), [msecsTo()](#msecsTo).

---

\_\_eq\_\_(QDateTime|datetime.datetime) → bool
:   TODO

---

@staticmethod fromMSecsSinceEpoch(int, [QTimeZone](qtimezone.html)) → QDateTime
:   Returns a datetime representing a moment the given number *msecs* of milliseconds after the start, in UTC, of the year 1970, described as specified by *timeZone*. The default time representation is local time.

    Note that there are possible values for *msecs* that lie outside the valid range of QDateTime, both negative and positive. The behavior of this function is undefined for those values.

    See also

    [fromSecsSinceEpoch()](#fromSecsSinceEpoch), [toMSecsSinceEpoch()](#toMSecsSinceEpoch), [setMSecsSinceEpoch()](#setMSecsSinceEpoch).

---

@staticmethod fromMSecsSinceEpoch(int, spec: [TimeSpec](qt.html#TimeSpec) = [LocalTime](qt.html#TimeSpec-LocalTime), offsetSeconds: int = 0) → QDateTime
:   Pass a [QTimeZone](qtimezone.html) instead, or omit *spec* and *offsetSeconds*.

    Returns a datetime representing a moment the given number *msecs* of milliseconds after the start, in UTC, of the year 1970, described as specified by *spec* and *offsetSeconds*.

    Note that there are possible values for *msecs* that lie outside the valid range of QDateTime, both negative and positive. The behavior of this function is undefined for those values.

    If the *spec* is not [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) then the *offsetSeconds* will be ignored. If the *spec* is [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) and the *offsetSeconds* is 0 then [UTC](qt.html#TimeSpec-UTC) will be used as the *spec*, since UTC has zero offset.

    If *spec* is [TimeZone](qt.html#TimeSpec-TimeZone) then [LocalTime](qt.html#TimeSpec-LocalTime) will be used in its place, equivalent to using the current system time zone (but differently represented).

    See also

    [fromSecsSinceEpoch()](#fromSecsSinceEpoch), [toMSecsSinceEpoch()](#toMSecsSinceEpoch), [setMSecsSinceEpoch()](#setMSecsSinceEpoch).

---

@staticmethod fromSecsSinceEpoch(int, [QTimeZone](qtimezone.html)) → QDateTime
:   Returns a datetime representing a moment the given number *secs* of seconds after the start, in UTC, of the year 1970, described as specified by *timeZone*. The default time representation is local time.

    Note that there are possible values for *secs* that lie outside the valid range of QDateTime, both negative and positive. The behavior of this function is undefined for those values.

    See also

    [fromMSecsSinceEpoch()](#fromMSecsSinceEpoch), [toSecsSinceEpoch()](#toSecsSinceEpoch), [setSecsSinceEpoch()](#setSecsSinceEpoch).

---

@staticmethod fromSecsSinceEpoch(int, spec: [TimeSpec](qt.html#TimeSpec) = [LocalTime](qt.html#TimeSpec-LocalTime), offsetSeconds: int = 0) → QDateTime
:   Pass a [QTimeZone](qtimezone.html) instead, or omit *spec* and *offsetSeconds*.

    Returns a datetime representing a moment the given number *secs* of seconds after the start, in UTC, of the year 1970, described as specified by *spec* and *offsetSeconds*.

    Note that there are possible values for *secs* that lie outside the valid range of QDateTime, both negative and positive. The behavior of this function is undefined for those values.

    If the *spec* is not [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) then the *offsetSeconds* will be ignored. If the *spec* is [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) and the *offsetSeconds* is 0 then [UTC](qt.html#TimeSpec-UTC) will be used as the *spec*, since UTC has zero offset.

    If *spec* is [TimeZone](qt.html#TimeSpec-TimeZone) then [LocalTime](qt.html#TimeSpec-LocalTime) will be used in its place, equivalent to using the current system time zone (but differently represented).

    See also

    [fromMSecsSinceEpoch()](#fromMSecsSinceEpoch), [toSecsSinceEpoch()](#toSecsSinceEpoch), [setSecsSinceEpoch()](#setSecsSinceEpoch).

---

@staticmethod fromString(str|None, format: [DateFormat](qt.html#DateFormat) = [TextDate](qt.html#DateFormat-TextDate)) → QDateTime
:   Returns the QDateTime represented by the *string*, using the *format* given, or an invalid datetime if this is not possible.

    Note for [TextDate](qt.html#DateFormat-TextDate): only English short month names (e.g. “Jan” in short form or “January” in long form) are recognized.

    See also

    [toString()](#toString), [toDateTime()](qlocale.html#toDateTime).

---

@staticmethod fromString(str|None, str|None, cal: [QCalendar](qcalendar.html) = QCalendar()) → QDateTime
:   TODO

---

@staticmethod fromString(str|None, str|None, int, cal: [QCalendar](qcalendar.html) = QCalendar()) → QDateTime
:   Returns the QDateTime represented by the *string*, using the *format* given, or an invalid datetime if the string cannot be parsed.

    Uses the calendar *cal* if supplied, else Gregorian.

    When *format* only specifies the last two digits of a year, the 100 years starting at *baseYear* are the candidates first considered. Prior to 6.7 there was no *baseYear* parameter and 1900 was always used. This is the default for *baseYear*, selecting a year from then to 1999. In some cases, other fields may lead to the next or previous century being selected, to get a result consistent with all fields given. See [fromString()](qdate.html#fromString) for details.

    In addition to the expressions, recognized in the format string to represent parts of the date and time, by [fromString()](qdate.html#fromString) and [fromString()](qtime.html#fromString), this method supports:

    | Expression | Output |
    | --- | --- |
    | t | the timezone (offset, name, “Z” or offset with “UTC” prefix) |
    | tt | the timezone in offset format with no colon between hours and minutes (for example “+0200”) |
    | ttt | the timezone in offset format with a colon between hours and minutes (for example “+02:00”) |
    | tttt | the timezone name, either what [displayName()](qtimezone.html#displayName) reports for [LongName](qtimezone.html#NameType-LongName) or the IANA ID of the zone (for example “Europe/Berlin”). The names recognized are those known to [QTimeZone](qtimezone.html), which may depend on the operating system in use. |

    If no ‘t’ format specifier is present, the system’s local time-zone is used. For the defaults of all other fields, see [fromString()](qdate.html#fromString) and [fromString()](qtime.html#fromString).

    For example:

    ```
    # QDateTime dateTime = QDateTime::fromString("1.30.1", "M.d.s");
    # // dateTime is January 30 in 1900 at 00:00:01.
    # dateTime = QDateTime::fromString("12", "yy");
    # // dateTime is January 1 in 1912 at 00:00:00.
    ```

    All other input characters will be treated as text. Any non-empty sequence of characters enclosed in single quotes will also be treated (stripped of the quotes) as text and not be interpreted as expressions.

    ```
    # QTime time1 = QTime::fromString("131", "HHh");
    # // time1 is 13:00:00
    # QTime time1 = QTime::fromString("1apA", "1amAM");
    # // time1 is 01:00:00

    # QDateTime dateTime2 = QDateTime::fromString("M1d1y9800:01:02",
    #                                             "'M'M'd'd'y'yyhh:mm:ss");
    # // dateTime is 1 January 1998 00:01:02
    ```

    If the format is not satisfied, an invalid QDateTime is returned. If the format is satisfied but *string* represents an invalid datetime (e.g. in a gap skipped by a time-zone transition), an valid QDateTime is returned, that represents a near-by datetime that is valid.

    The expressions that don’t have leading zeroes (d, M, h, m, s, z) will be greedy. This means that they will use two digits (or three, for z) even if this will put them outside the range and/or leave too few digits for other sections.

    ```
    # QDateTime dateTime = QDateTime::fromString("130", "Mm"); // invalid
    ```

    This could have meant 1 January 00:30.00 but the M will grab two digits.

    Incorrectly specified fields of the *string* will cause an invalid QDateTime to be returned. Only datetimes between the local time start of year 100 and end of year 9999 are supported. Note that datetimes near the ends of this range in other time-zones, notably including UTC, may fall outside the range (and thus be treated as invalid) depending on local time zone.

    **Note:** Day and month names as well as AM/PM indicators must be given in English (C locale). If localized month and day names or localized forms of AM/PM are to be recognized, use [system()](qlocale.html#system).toDateTime().

    **Note:** If a format character is repeated more times than the longest expression in the table above using it, this part of the format will be read as several expressions with no separator between them; the longest above, possibly repeated as many times as there are copies of it, ending with a residue that may be a shorter expression. Thus `'tttttt'` would match `"Europe/BerlinEurope/Berlin"` and set the zone to Berlin time; if the datetime string contained “Europe/BerlinZ” it would “match” but produce an inconsistent result, leading to an invalid datetime.

    See also

    [toString()](#toString), [fromString()](qdate.html#fromString), [fromString()](qtime.html#fromString), [toDateTime()](qlocale.html#toDateTime).

---

\_\_ge\_\_(QDateTime|datetime.datetime) → bool
:   TODO

---

\_\_gt\_\_(QDateTime|datetime.datetime) → bool
:   TODO

---

\_\_hash\_\_() → int
:   TODO

---

isDaylightTime() → bool
:   Returns if this datetime falls in Daylight-Saving Time.

    If the [TimeSpec](qt.html#TimeSpec) is not [LocalTime](qt.html#TimeSpec-LocalTime) or [TimeZone](qt.html#TimeSpec-TimeZone) then will always return false.

    See also

    [timeSpec()](#timeSpec).

---

isNull() → bool
:   Returns `true` if both the date and the time are null; otherwise returns `false`. A null datetime is invalid.

    See also

    [isNull()](qdate.html#isNull), [isNull()](qtime.html#isNull), [isValid()](#isValid).

---

isValid() → bool
:   Returns `true` if this datetime represents a definite moment, otherwise `false`.

    A datetime is valid if both its date and its time are valid and the time representation used gives a valid meaning to their combination. When the time representation is a specific time-zone or local time, there may be times on some dates that the zone skips in its representation, as when a daylight-saving transition skips an hour (typically during a night in spring). For example, if DST ends at 2am with the clock advancing to 3am, then datetimes from 02:00:00 to 02:59:59.999 on that day are invalid.

    See also

    [YearRange](#YearRange), [isValid()](qdate.html#isValid), [isValid()](qtime.html#isValid).

---

\_\_le\_\_(QDateTime|datetime.datetime) → bool
:   TODO

---

\_\_lt\_\_(QDateTime|datetime.datetime) → bool
:   TODO

---

msecsTo(QDateTime|datetime.datetime) → int
:   Returns the number of milliseconds from this datetime to the *other* datetime. If the *other* datetime is earlier than this datetime, the value returned is negative.

    Before performing the comparison, the two datetimes are converted to [UTC](qt.html#TimeSpec-UTC) to ensure that the result is correct if daylight-saving (DST) applies to one of the two datetimes and but not the other.

    Returns 0 if either datetime is invalid.

    See also

    [addMSecs()](#addMSecs), [daysTo()](#daysTo), [msecsTo()](qtime.html#msecsTo).

---

\_\_ne\_\_(QDateTime|datetime.datetime) → bool
:   TODO

---

offsetFromUtc() → int
:   Returns this datetime’s Offset From UTC in seconds.

    The result depends on [timeSpec()](#timeSpec):

    * `Qt::UTC` The offset is 0.
    * `Qt::OffsetFromUTC` The offset is the value originally set.
    * `Qt::LocalTime` The local time’s offset from UTC is returned.
    * `Qt::TimeZone` The offset used by the time-zone is returned.

    For the last two, the offset at this date and time will be returned, taking account of Daylight-Saving Offset. The offset is the difference between the local time or time in the given time-zone and UTC time; it is positive in time-zones ahead of UTC (East of The Prime Meridian), negative for those behind UTC (West of The Prime Meridian).

    See also

    [setOffsetFromUtc()](#setOffsetFromUtc), [setTimeZone()](#setTimeZone).

---

\_\_repr\_\_() → str
:   TODO

---

secsTo(QDateTime|datetime.datetime) → int
:   Returns the number of seconds from this datetime to the *other* datetime. If the *other* datetime is earlier than this datetime, the value returned is negative.

    Before performing the comparison, the two datetimes are converted to [UTC](qt.html#TimeSpec-UTC) to ensure that the result is correct if daylight-saving (DST) applies to one of the two datetimes but not the other.

    Returns 0 if either datetime is invalid.

    Example:

    ```
    # QDateTime now = QDateTime::currentDateTime();
    # QDateTime xmas(QDate(now.date().year(), 12, 25).startOfDay());
    # qDebug("There are %d seconds to Christmas", now.secsTo(xmas));
    ```

    See also

    [addSecs()](#addSecs), [daysTo()](#daysTo), [secsTo()](qtime.html#secsTo).

---

setDate([QDate](qdate.html)|datetime.date, resolve: [TransitionResolution](#TransitionResolution) = [LegacyBehavior](#TransitionResolution-LegacyBehavior))
:   Sets the date part of this datetime to *date*.

    If no time is set yet, it is set to midnight. If *date* is invalid, this QDateTime becomes invalid.

    If *date* and [time()](#time) describe a moment close to a transition for this datetime’s time representation, *resolve* controls how that situation is resolved.

    **Note:** Prior to Qt 6.7, the version of this function lacked the *resolve* parameter so had no way to resolve the ambiguities related to transitions.

    See also

    [date()](#date), [setTime()](#setTime), [setTimeZone()](#setTimeZone).

---

setMSecsSinceEpoch(int)
:   Sets the datetime to represent a moment a given number, *msecs*, of milliseconds after the start, in UTC, of the year 1970.

    On systems that do not support time zones, this function will behave as if local time were [UTC](qt.html#TimeSpec-UTC).

    Note that passing the minimum of `qint64` (`std::numeric_limits<qint64>::min()`) to *msecs* will result in undefined behavior.

    See also

    [setSecsSinceEpoch()](#setSecsSinceEpoch), [toMSecsSinceEpoch()](#toMSecsSinceEpoch), [fromMSecsSinceEpoch()](#fromMSecsSinceEpoch).

---

setOffsetFromUtc(int)
:   Use [setTimeZone()](#setTimeZone)([fromSecondsAheadOfUtc()](qtimezone.html#fromSecondsAheadOfUtc)(offsetSeconds)) instead

    Sets the [timeSpec()](#timeSpec) to [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) and the offset to *offsetSeconds*. The datetime may refer to a different point in time.

    The maximum and minimum offset is 14 positive or negative hours. If *offsetSeconds* is larger or smaller than that, then the result is undefined.

    If *offsetSeconds* is 0 then the [timeSpec()](#timeSpec) will be set to [UTC](qt.html#TimeSpec-UTC).

    See also

    [setTimeZone()](#setTimeZone), [isValid()](#isValid), [offsetFromUtc()](#offsetFromUtc), [toOffsetFromUtc()](#toOffsetFromUtc).

---

setSecsSinceEpoch(int)
:   Sets the datetime to represent a moment a given number, *secs*, of seconds after the start, in UTC, of the year 1970.

    On systems that do not support time zones, this function will behave as if local time were [UTC](qt.html#TimeSpec-UTC).

    See also

    [setMSecsSinceEpoch()](#setMSecsSinceEpoch), [toSecsSinceEpoch()](#toSecsSinceEpoch), [fromSecsSinceEpoch()](#fromSecsSinceEpoch).

---

setTime([QTime](qtime.html)|datetime.time, resolve: [TransitionResolution](#TransitionResolution) = [LegacyBehavior](#TransitionResolution-LegacyBehavior))
:   Sets the time part of this datetime to *time*. If *time* is not valid, this function sets it to midnight. Therefore, it’s possible to clear any set time in a QDateTime by setting it to a default [QTime](qtime.html):

    ```
    QDateTime dt = QDateTime::currentDateTime();
    dt.setTime(QTime());
    ```

    If [date()](#date) and *time* describe a moment close to a transition for this datetime’s time representation, *resolve* controls how that situation is resolved.

    **Note:** Prior to Qt 6.7, the version of this function lacked the *resolve* parameter so had no way to resolve the ambiguities related to transitions.

    See also

    [time()](#time), [setDate()](#setDate), [setTimeZone()](#setTimeZone).

---

setTimeSpec([TimeSpec](qt.html#TimeSpec))
:   Use [setTimeZone()](#setTimeZone) instead

    Sets the time specification used in this datetime to *spec*. The datetime may refer to a different point in time.

    If *spec* is [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) then the [timeSpec()](#timeSpec) will be set to [UTC](qt.html#TimeSpec-UTC), i.e. an effective offset of 0.

    If *spec* is [TimeZone](qt.html#TimeSpec-TimeZone) then the spec will be set to [LocalTime](qt.html#TimeSpec-LocalTime), i.e. the current system time zone.

    Example:

    ```
    # QDateTime local(QDateTime::currentDateTime());
    # qDebug() << "Local time is:" << local;

    # QDateTime UTC(local);
    # UTC.setTimeSpec(Qt::UTC);
    # qDebug() << "UTC time is:" << UTC;

    # qDebug() << "There are" << local.secsTo(UTC) << "seconds difference between the datetimes.";
    ```

    See also

    [setTimeZone()](#setTimeZone), [timeSpec()](#timeSpec), [toTimeSpec()](#toTimeSpec), [setDate()](#setDate), [setTime()](#setTime).

---

setTimeZone([QTimeZone](qtimezone.html), resolve: [TransitionResolution](#TransitionResolution) = [LegacyBehavior](#TransitionResolution-LegacyBehavior))
:   Sets the time zone used in this datetime to *toZone*.

    The datetime may refer to a different point in time. It uses the time representation of *toZone*, which may change the meaning of its unchanged [date()](#date) and [time()](#time).

    If *toZone* is invalid then the datetime will be invalid. Otherwise, this datetime’s [timeSpec()](#timeSpec) after the call will match `toZone.timeSpec()`.

    If [date()](#date) and [time()](#time) describe a moment close to a transition for *toZone*, *resolve* controls how that situation is resolved.

    **Note:** Prior to Qt 6.7, the version of this function lacked the *resolve* parameter so had no way to resolve the ambiguities related to transitions.

    See also

    [timeRepresentation()](#timeRepresentation), [timeZone()](#timeZone), [TimeSpec](qt.html#TimeSpec).

---

swap(QDateTime)
:   Swaps this datetime with *other*. This operation is very fast and never fails.

---

time() → [QTime](qtime.html)
:   Returns the time part of the datetime.

    See also

    [setTime()](#setTime), [date()](#date), [timeRepresentation()](#timeRepresentation).

---

timeRepresentation() → [QTimeZone](qtimezone.html)
:   Returns a [QTimeZone](qtimezone.html) identifying how this datetime represents time.

    The [timeSpec()](#timeSpec) of the returned [QTimeZone](qtimezone.html) will coincide with that of this datetime; if it is not [TimeZone](qt.html#TimeSpec-TimeZone) then the returned [QTimeZone](qtimezone.html) is a time representation. When their [timeSpec()](#timeSpec) is [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC), the returned [QTimeZone](qtimezone.html)’s fixedSecondsAheadOfUtc() supplies the offset. When [timeSpec()](#timeSpec) is [TimeZone](qt.html#TimeSpec-TimeZone), the [QTimeZone](qtimezone.html) object itself is the full representation of that time zone.

    See also

    [timeZone()](#timeZone), [setTimeZone()](#setTimeZone), [asBackendZone()](qtimezone.html#asBackendZone).

---

timeSpec() → [TimeSpec](qt.html#TimeSpec)
:   Returns the time specification of the datetime.

    This classifies its time representation as local time, UTC, a fixed offset from UTC (without indicating the offset) or a time zone (without giving the details of that time zone). Equivalent to `timeRepresentation().timeSpec()`.

    See also

    [setTimeSpec()](#setTimeSpec), [setTimeZone()](#setTimeZone), [timeRepresentation()](#timeRepresentation), [date()](#date), [time()](#time).

---

timeZone() → [QTimeZone](qtimezone.html)
:   Returns the time zone of the datetime.

    The result is the same as `timeRepresentation().asBackendZone()`. In all cases, the result’s [timeSpec()](qtimezone.html#timeSpec) is [TimeZone](qt.html#TimeSpec-TimeZone).

    When [timeSpec()](#timeSpec) is [LocalTime](qt.html#TimeSpec-LocalTime), the result will describe local time at the time this method was called. It will not reflect subsequent changes to the system time zone, even when the QDateTime from which it was obtained does.

    See also

    [timeRepresentation()](#timeRepresentation), [setTimeZone()](#setTimeZone), [TimeSpec](qt.html#TimeSpec), [asBackendZone()](qtimezone.html#asBackendZone).

---

timeZoneAbbreviation() → str
:   Returns the Time Zone Abbreviation for this datetime.

    The returned string depends on [timeSpec()](#timeSpec):

    * For [UTC](qt.html#TimeSpec-UTC) it is “UTC”.
    * For [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) it will be in the format “UTC[+-]00:00”.
    * For [LocalTime](qt.html#TimeSpec-LocalTime), the host system is queried.
    * For [TimeZone](qt.html#TimeSpec-TimeZone), the associated [QTimeZone](qtimezone.html) object is queried.

    **Note:** The abbreviation is not guaranteed to be unique, i.e. different time zones may have the same abbreviation. For [LocalTime](qt.html#TimeSpec-LocalTime) and [TimeZone](qt.html#TimeSpec-TimeZone), when returned by the host system, the abbreviation may be localized.

    See also

    [timeSpec()](#timeSpec), [abbreviation()](qtimezone.html#abbreviation).

---

toLocalTime() → QDateTime
:   Returns a copy of this datetime converted to local time.

    The result represents the same moment in time as, and is equal to, this datetime.

    Example:

    ```
    # QDateTime UTC(QDateTime::currentDateTimeUtc());
    # QDateTime local(UTC.toLocalTime());
    # qDebug() << "UTC time is:" << UTC;
    # qDebug() << "Local time is:" << local;
    # qDebug() << "No difference between times:" << UTC.secsTo(local);
    ```

    See also

    [toTimeZone()](#toTimeZone), [toUTC()](#toUTC), [toOffsetFromUtc()](#toOffsetFromUtc).

---

toMSecsSinceEpoch() → int
:   Returns the datetime as a number of milliseconds after the start, in UTC, of the year 1970.

    On systems that do not support time zones, this function will behave as if local time were [UTC](qt.html#TimeSpec-UTC).

    The behavior for this function is undefined if the datetime stored in this object is not valid. However, for all valid dates, this function returns a unique value.

    See also

    [toSecsSinceEpoch()](#toSecsSinceEpoch), [setMSecsSinceEpoch()](#setMSecsSinceEpoch), [fromMSecsSinceEpoch()](#fromMSecsSinceEpoch).

---

toOffsetFromUtc(int) → QDateTime
:   Returns a copy of this datetime converted to a spec of [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) with the given *offsetSeconds*. Equivalent to `toTimeZone(QTimeZone::fromSecondsAheadOfUtc(offsetSeconds))`.

    If the *offsetSeconds* equals 0 then a UTC datetime will be returned.

    The result represents the same moment in time as, and is equal to, this datetime.

    See also

    [offsetFromUtc()](#offsetFromUtc), [toTimeZone()](#toTimeZone).

---

toPyDateTime() → datetime.datetime
:   TODO

---

toSecsSinceEpoch() → int
:   Returns the datetime as a number of seconds after the start, in UTC, of the year 1970.

    On systems that do not support time zones, this function will behave as if local time were [UTC](qt.html#TimeSpec-UTC).

    The behavior for this function is undefined if the datetime stored in this object is not valid. However, for all valid dates, this function returns a unique value.

    See also

    [toMSecsSinceEpoch()](#toMSecsSinceEpoch), [fromSecsSinceEpoch()](#fromSecsSinceEpoch), [setSecsSinceEpoch()](#setSecsSinceEpoch).

---

toString(format: [DateFormat](qt.html#DateFormat) = [TextDate](qt.html#DateFormat-TextDate)) → str
:   Returns the datetime as a string in the *format* given.

    If the *format* is [TextDate](qt.html#DateFormat-TextDate), the string is formatted in the default way. The day and month names will be in English. An example of this formatting is “Wed May 20 03:40:13 1998”. For localized formatting, see [toString()](qlocale.html#toString).

    If the *format* is [ISODate](qt.html#DateFormat-ISODate), the string format corresponds to the ISO 8601 extended specification for representations of dates and times, taking the form yyyy-MM-ddTHH:mm:ss[Z|±HH:mm], depending on the [timeSpec()](#timeSpec) of the QDateTime. If the [timeSpec()](#timeSpec) is [UTC](qt.html#TimeSpec-UTC), Z will be appended to the string; if the [timeSpec()](#timeSpec) is [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC), the offset in hours and minutes from UTC will be appended to the string. To include milliseconds in the ISO 8601 date, use the *format* [ISODateWithMs](qt.html#DateFormat-ISODateWithMs), which corresponds to yyyy-MM-ddTHH:mm:ss.zzz[Z|±HH:mm].

    If the *format* is [RFC2822Date](qt.html#DateFormat-RFC2822Date), the string is formatted following RFC 2822.

    If the datetime is invalid, an empty string will be returned.

    **Warning:** The [ISODate](qt.html#DateFormat-ISODate) format is only valid for years in the range 0 to 9999.

    See also

    [fromString()](#fromString), [toString()](qdate.html#toString), [toString()](qtime.html#toString), [toString()](qlocale.html#toString).

---

toString(str|None, cal: [QCalendar](qcalendar.html) = QCalendar()) → str
:   TODO

---

toTimeSpec([TimeSpec](qt.html#TimeSpec)) → QDateTime
:   Use [toTimeZone()](#toTimeZone) instead.

    Returns a copy of this datetime converted to the given time *spec*.

    The result represents the same moment in time as, and is equal to, this datetime.

    If *spec* is [OffsetFromUTC](qt.html#TimeSpec-OffsetFromUTC) then it is set to [UTC](qt.html#TimeSpec-UTC). To set to a fixed offset from UTC, use [toTimeZone()](#toTimeZone) or [toOffsetFromUtc()](#toOffsetFromUtc).

    If *spec* is [TimeZone](qt.html#TimeSpec-TimeZone) then it is set to [LocalTime](qt.html#TimeSpec-LocalTime), i.e. the local Time Zone. To set a specified time-zone, use [toTimeZone()](#toTimeZone).

    Example:

    ```
    # QDateTime local(QDateTime::currentDateTime());
    # QDateTime UTC(local.toTimeSpec(Qt::UTC));
    # qDebug() << "Local time is:" << local;
    # qDebug() << "UTC time is:" << UTC;
    # qDebug() << "No difference between times:" << local.secsTo(UTC);
    ```

    See also

    [setTimeSpec()](#setTimeSpec), [timeSpec()](#timeSpec), [toTimeZone()](#toTimeZone).

---

toTimeZone([QTimeZone](qtimezone.html)) → QDateTime
:   Returns a copy of this datetime converted to the given *timeZone*.

    The result represents the same moment in time as, and is equal to, this datetime.

    The result describes the moment in time in terms of *timeZone*’s time representation. For example:

    ```
    # This code needs porting to Python.

    # /****************************************************************************
    # **
    # ** Copyright (C) 2016 The Qt Company Ltd.
    # ** Contact: https://www.qt.io/licensing/
    # **
    # ** This file is part of the documentation of the Qt Toolkit.
    # **
    # ** $QT_BEGIN_LICENSE:BSD$
    # ** Commercial License Usage
    # ** Licensees holding valid commercial Qt licenses may use this file in
    # ** accordance with the commercial license agreement provided with the
    # ** Software or, alternatively, in accordance with the terms contained in
    # ** a written agreement between you and The Qt Company. For licensing terms
    # ** and conditions see https://www.qt.io/terms-conditions. For further
    # ** information use the contact form at https://www.qt.io/contact-us.
    # **
    # ** BSD License Usage
    # ** Alternatively, you may use this file under the terms of the BSD license
    # ** as follows:
    # **
    # ** "Redistribution and use in source and binary forms, with or without
    # ** modification, are permitted provided that the following conditions are
    # ** met:
    # **   * Redistributions of source code must retain the above copyright
    # **     notice, this list of conditions and the following disclaimer.
    # **   * Redistributions in binary form must reproduce the above copyright
    # **     notice, this list of conditions and the following disclaimer in
    # **     the documentation and/or other materials provided with the
    # **     distribution.
    # **   * Neither the name of The Qt Company Ltd nor the names of its
    # **     contributors may be used to endorse or promote products derived
    # **     from this software without specific prior written permission.
    # **
    # **
    # ** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    # ** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    # ** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    # ** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    # ** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    # ** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    # ** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    # ** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    # ** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    # ** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    # ** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
    # **
    # ** $QT_END_LICENSE$
    # **
    # ****************************************************************************/

    # #! [0]
    # QDate d1(1995, 5, 17);  // May 17, 1995
    # QDate d2(1995, 5, 20);  // May 20, 1995
    # d1.daysTo(d2);          // returns 3
    # d2.daysTo(d1);          // returns -3
    # #! [0]

    # #! [1]
    # QDate date = QDate::fromString("1MM12car2003", "d'MM'MMcaryyyy");
    # // date is 1 December 2003
    # #! [1]

    # #! [2]
    # QDate date = QDate::fromString("130", "Md"); // invalid
    # #! [2]

    # #! [3]
    # QDate::fromString("1.30", "M.d");           // January 30 1900
    # QDate::fromString("20000110", "yyyyMMdd");  // January 10, 2000
    # QDate::fromString("20000110", "yyyyMd");    // January 10, 2000
    # #! [3]

    # #! [4]
    # QDate::isValid(2002, 5, 17);  // true
    # QDate::isValid(2002, 2, 30);  // false (Feb 30 does not exist)
    # QDate::isValid(2004, 2, 29);  // true (2004 is a leap year)
    # QDate::isValid(2000, 2, 29);  // true (2000 is a leap year)
    # QDate::isValid(2006, 2, 29);  // false (2006 is not a leap year)
    # QDate::isValid(2100, 2, 29);  // false (2100 is not a leap year)
    # QDate::isValid(1202, 6, 6);   // true (even though 1202 is pre-Gregorian)
    # #! [4]

    # #! [5]
    # QTime n(14, 0, 0);                // n == 14:00:00
    # QTime t;
    # t = n.addSecs(70);                // t == 14:01:10
    # t = n.addSecs(-70);               // t == 13:58:50
    # t = n.addSecs(10 * 60 * 60 + 5);  // t == 00:00:05
    # t = n.addSecs(-15 * 60 * 60);     // t == 23:00:00
    # #! [5]

    # #! [6]
    # QTime time = QTime::fromString("1mm12car00", "m'mm'hcarss");
    # // time is 12:01.00
    # #! [6]

    # #! [7]
    # QTime time = QTime::fromString("00:710", "hh:ms"); // invalid
    # #! [7]

    # #! [8]
    # QTime time = QTime::fromString("1.30", "m.s");
    # // time is 00:01:30.000
    # #! [8]

    # #! [9]
    # QTime::isValid(21, 10, 30); // returns true
    # QTime::isValid(22, 5,  62); // returns false
    # #! [9]

    # #! [10]
    # QTime t;
    # t.start();
    # some_lengthy_task();
    # qDebug("Time elapsed: %d ms", t.elapsed());
    # #! [10]

    # #! [11]
    # QDateTime now = QDateTime::currentDateTime();
    # QDateTime xmas(QDate(now.date().year(), 12, 25).startOfDay());
    # qDebug("There are %d seconds to Christmas", now.secsTo(xmas));
    # #! [11]

    # #! [12]
    # QTime time1 = QTime::fromString("131", "HHh");
    # // time1 is 13:00:00
    # QTime time1 = QTime::fromString("1apA", "1amAM");
    # // time1 is 01:00:00

    # QDateTime dateTime2 = QDateTime::fromString("M1d1y9800:01:02",
    #                                             "'M'M'd'd'y'yyhh:mm:ss");
    # // dateTime is 1 January 1998 00:01:02
    # #! [12]

    # #! [13]
    # QDateTime dateTime = QDateTime::fromString("130", "Mm"); // invalid
    # #! [13]

    # #! [14]
    # QDateTime dateTime = QDateTime::fromString("1.30.1", "M.d.s");
    # // dateTime is January 30 in 1900 at 00:00:01.
    # dateTime = QDateTime::fromString("12", "yy");
    # // dateTime is January 1 in 1912 at 00:00:00.
    # #! [14]

    # #! [15]
    # QDateTime startDate(QDate(2012, 7, 6), QTime(8, 30, 0));
    # QDateTime endDate(QDate(2012, 7, 7), QTime(16, 30, 0));
    # qDebug() << "Days from startDate to endDate: " << startDate.daysTo(endDate);

    # startDate = QDateTime(QDate(2012, 7, 6), QTime(23, 55, 0));
    # endDate = QDateTime(QDate(2012, 7, 7), QTime(0, 5, 0));
    # qDebug() << "Days from startDate to endDate: " << startDate.daysTo(endDate);

    # qSwap(startDate, endDate); // Make endDate before startDate.
    # qDebug() << "Days from startDate to endDate: " << startDate.daysTo(endDate);
    # #! [15]

    # #! [16]
    # QDateTime local(QDateTime::currentDateTime());
    # QDateTime UTC(local.toTimeSpec(Qt::UTC));
    # qDebug() << "Local time is:" << local;
    # qDebug() << "UTC time is:" << UTC;
    # qDebug() << "No difference between times:" << local.secsTo(UTC);
    # #! [16]

    # #! [17]
    # QDateTime UTC(QDateTime::currentDateTimeUtc());
    # QDateTime local(UTC.toLocalTime());
    # qDebug() << "UTC time is:" << UTC;
    # qDebug() << "Local time is:" << local;
    # qDebug() << "No difference between times:" << UTC.secsTo(local);
    # #! [17]

    # #! [18]
    # QDateTime local(QDateTime::currentDateTime());
    # QDateTime UTC(local.toUTC());
    # qDebug() << "Local time is:" << local;
    # qDebug() << "UTC time is:" << UTC;
    # qDebug() << "No difference between times:" << local.secsTo(UTC);
    # #! [18]

    # #! [19]
    # QDateTime local(QDateTime::currentDateTime());
    # qDebug() << "Local time is:" << local;

    # QDateTime UTC(local);
    # UTC.setTimeSpec(Qt::UTC);
    # qDebug() << "UTC time is:" << UTC;

    # qDebug() << "There are" << local.secsTo(UTC) << "seconds difference between the datetimes.";
    # #! [19]

    # #! [20]
    # QString string = "Monday, 23 April 12 22:51:41";
    # QString format = "dddd, d MMMM yy hh:mm:ss";
    # QDateTime invalid = QDateTime::fromString(string, format);
    # #! [20]

    # #! [21]
    # QString string = "Tuesday, 23 April 12 22:51:41";
    # QString format = "dddd, d MMMM yy hh:mm:ss";
    # QDateTime valid = QDateTime::fromString(string, format);
    # #! [21]
    ```

    If *timeZone* is invalid then the datetime will be invalid. Otherwise the returned datetime’s [timeSpec()](#timeSpec) will match `timeZone.timeSpec()`.

    See also

    [timeRepresentation()](#timeRepresentation), [toLocalTime()](#toLocalTime), [toUTC()](#toUTC), [toOffsetFromUtc()](#toOffsetFromUtc).

---

toUTC() → QDateTime
:   Returns a copy of this datetime converted to UTC.

    The result represents the same moment in time as, and is equal to, this datetime.

    Example:

    ```
    # QDateTime local(QDateTime::currentDateTime());
    # QDateTime UTC(local.toUTC());
    # qDebug() << "Local time is:" << local;
    # qDebug() << "UTC time is:" << UTC;
    # qDebug() << "No difference between times:" << local.secsTo(UTC);
    ```

    See also

    [toTimeZone()](#toTimeZone), [toLocalTime()](#toLocalTime), [toOffsetFromUtc()](#toOffsetFromUtc).

### [Table of Contents](../../index.html)

* QDateTime
  + [Description](#description)
    - [Remarks](#remarks)
      * [Range of Valid Dates](#range-of-valid-dates)
      * [Use of Timezones](#use-of-timezones)
      * [Timezone transitions](#timezone-transitions)
        + [Whole day transitions](#whole-day-transitions)
      * [Offsets From UTC](#offsets-from-utc)
  + [Enums](#enums)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QDateTime

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QKeySequence {#qkeysequence}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QKeySequence

# QKeySequence[¶](#qkeysequence "Link to this heading")

[PyQt6.QtGui](qtgui-module.html).QKeySequence

## Description[¶](#description "Link to this heading")

The QKeySequence class encapsulates a key sequence as used by shortcuts.

In its most common form, a key sequence describes a combination of keys that must be used together to perform some action. Key sequences are used with [QAction](qaction.html) objects to specify which keyboard shortcuts can be used to trigger actions.

Key sequences can be constructed for use as keyboard shortcuts in three different ways:

* For standard shortcuts, a [StandardKey](#StandardKey) can be used to request the platform-specific key sequence associated with each shortcut.
* For custom shortcuts, human-readable strings such as “Ctrl+X” can be used, and these can be translated into the appropriate shortcuts for users of different languages. Translations are made in the “[QShortcut](qshortcut.html)” context.
* For hard-coded shortcuts, integer key codes can be specified with a combination of values defined by the [Key](../qtcore/qt.html#Key) and [KeyboardModifier](../qtcore/qt.html#KeyboardModifier) enum values. Each key code consists of a single [Key](../qtcore/qt.html#Key) value and zero or more modifiers, such as [ShiftModifier](../qtcore/qt.html#KeyboardModifier-ShiftModifier), [ControlModifier](../qtcore/qt.html#KeyboardModifier-ControlModifier), [AltModifier](../qtcore/qt.html#KeyboardModifier-AltModifier) and [MetaModifier](../qtcore/qt.html#KeyboardModifier-MetaModifier).

For example, Ctrl P might be a sequence used as a shortcut for printing a document, and can be specified in any of the following ways:

```
# QKeySequence(QKeySequence::Print);
# QKeySequence(tr("Ctrl+P"));
# QKeySequence(tr("Ctrl+p"));
# QKeySequence(Qt::CTRL | Qt::Key_P);
# QKeySequence(Qt::CTRL + Qt::Key_P); // deprecated
```

Note that, for letters, the case used in the specification string does not matter. In the above examples, the user does not need to hold down the Shift key to activate a shortcut specified with “Ctrl+P”. However, for other keys, the use of Shift as an unspecified extra modifier key can lead to confusion for users of an application whose keyboards have different layouts to those used by the developers. See the [Keyboard Layout Issues](#qkeysequence-keyboard-layout-issues) section below for more details.

It is preferable to use standard shortcuts where possible. When creating key sequences for non-standard shortcuts, you should use human-readable strings in preference to hard-coded integer values.

QKeySequence object can be serialized to human-readable strings with the [toString()](#toString) function.

An alternative way to specify hard-coded key codes is to use the Unicode code point of the character; for example, ‘A’ gives the same key sequence as [Key\_A](../qtcore/qt.html#Key-Key_A).

**Note:** On Apple platforms, references to “Ctrl”, [CTRL](../qtcore/qt.html#Modifier-CTRL), [Key\_Control](../qtcore/qt.html#Key-Key_Control) and [ControlModifier](../qtcore/qt.html#KeyboardModifier-ControlModifier) correspond to the Command keys on the Macintosh keyboard, and references to “Meta”, [META](../qtcore/qt.html#Modifier-META), [Key\_Meta](../qtcore/qt.html#Key-Key_Meta) and [MetaModifier](../qtcore/qt.html#KeyboardModifier-MetaModifier) correspond to the Control keys. In effect, developers can use the same shortcut descriptions across all platforms, and their applications will automatically work as expected on Apple platforms.

### Standard Shortcuts[¶](#standard-shortcuts "Link to this heading")

QKeySequence defines many [StandardKey](#StandardKey) to reduce the amount of effort required when setting up actions in a typical application. The table below shows some common key sequences that are often used for these standard shortcuts by applications on four widely-used platforms. Note that on Apple platforms, the Ctrl value corresponds to the Command keys on the Macintosh keyboard, and the Meta value corresponds to the Control keys.

| StandardKey | Windows | Apple platforms | KDE Plasma | GNOME |
| --- | --- | --- | --- | --- |
| [HelpContents](#StandardKey-HelpContents) | F1 | Ctrl+? | F1 | F1 |
| [WhatsThis](#StandardKey-WhatsThis) | Shift+F1 | Shift+F1 | Shift+F1 | Shift+F1 |
| Open | Ctrl+O | Ctrl+O | Ctrl+O | Ctrl+O |
| Close | Ctrl+F4, Ctrl+W | Ctrl+W, Ctrl+F4 | Ctrl+W | Ctrl+W |
| Save | Ctrl+S | Ctrl+S | Ctrl+S | Ctrl+S |
| Quit |  | Ctrl+Q | Ctrl+Q | Ctrl+Q |
| [SaveAs](#StandardKey-SaveAs) | Ctrl+Shift+S | Ctrl+Shift+S | Ctrl+Shift+S | Ctrl+Shift+S |
| New | Ctrl+N | Ctrl+N | Ctrl+N | Ctrl+N |
| Delete | Del | Forward Delete, Meta+D | Del, Ctrl+D | Del, Ctrl+D |
| Cut | Ctrl+X, Shift+Del | Ctrl+X, Meta+K | Ctrl+X, F20, Shift+Del | Ctrl+X, F20, Shift+Del |
| Copy | Ctrl+C, Ctrl+Ins | Ctrl+C | Ctrl+C, F16, Ctrl+Ins | Ctrl+C, F16, Ctrl+Ins |
| Paste | Ctrl+V, Shift+Ins | Ctrl+V, Meta+Y | Ctrl+V, F18, Shift+Ins | Ctrl+V, F18, Shift+Ins |
| Preferences |  | Ctrl+, | Ctrl+Shift+, |  |
| Undo | Ctrl+Z, Alt+Backspace | Ctrl+Z | Ctrl+Z, F14 | Ctrl+Z, F14 |
| Redo | Ctrl+Y, Shift+Ctrl+Z, Alt+Shift+Backspace | Ctrl+Shift+Z | Ctrl+Shift+Z | Ctrl+Shift+Z |
| Back | Alt+Left, Backspace | Ctrl+[ | Alt+Left | Alt+Left |
| Forward | Alt+Right, Shift+Backspace | Ctrl+] | Alt+Right | Alt+Right |
| Refresh | F5 | F5 | F5 | Ctrl+R, F5 |
| [ZoomIn](#StandardKey-ZoomIn) | Ctrl+Plus | Ctrl+Plus | Ctrl+Plus | Ctrl+Plus |
| [ZoomOut](#StandardKey-ZoomOut) | Ctrl+Minus | Ctrl+Minus | Ctrl+Minus | Ctrl+Minus |
| [FullScreen](#StandardKey-FullScreen) | F11, Alt+Enter | Ctrl+Meta+F | F11, Ctrl+Shift+F | Ctrl+F11 |
| Print | Ctrl+P | Ctrl+P | Ctrl+P | Ctrl+P |
| [AddTab](#StandardKey-AddTab) | Ctrl+T | Ctrl+T | Ctrl+Shift+N, Ctrl+T | Ctrl+T |
| [NextChild](#StandardKey-NextChild) | Ctrl+Tab, Forward, Ctrl+F6 | Ctrl+}, Forward, Ctrl+Tab | Ctrl+Tab, Forward, Ctrl+Comma | Ctrl+Tab, Forward |
| [PreviousChild](#StandardKey-PreviousChild) | Ctrl+Shift+Tab, Back, Ctrl+Shift+F6 | Ctrl+{, Back, Ctrl+Shift+Tab | Ctrl+Shift+Tab, Back, Ctrl+Period | Ctrl+Shift+Tab, Back |
| Find | Ctrl+F | Ctrl+F | Ctrl+F | Ctrl+F |
| [FindNext](#StandardKey-FindNext) | F3, Ctrl+G | Ctrl+G | F3 | Ctrl+G, F3 |
| [FindPrevious](#StandardKey-FindPrevious) | Shift+F3, Ctrl+Shift+G | Ctrl+Shift+G | Shift+F3 | Ctrl+Shift+G, Shift+F3 |
| Replace | Ctrl+H | (none) | Ctrl+R | Ctrl+H |
| [SelectAll](#StandardKey-SelectAll) | Ctrl+A | Ctrl+A | Ctrl+A | Ctrl+A |
| Deselect |  |  | Ctrl+Shift+A | Ctrl+Shift+A |
| Bold | Ctrl+B | Ctrl+B | Ctrl+B | Ctrl+B |
| Italic | Ctrl+I | Ctrl+I | Ctrl+I | Ctrl+I |
| Underline | Ctrl+U | Ctrl+U | Ctrl+U | Ctrl+U |
| [MoveToNextChar](#StandardKey-MoveToNextChar) | Right | Right, Meta+F | Right | Right |
| [MoveToPreviousChar](#StandardKey-MoveToPreviousChar) | Left | Left, Meta+B | Left | Left |
| [MoveToNextWord](#StandardKey-MoveToNextWord) | Ctrl+Right | Alt+Right | Ctrl+Right | Ctrl+Right |
| [MoveToPreviousWord](#StandardKey-MoveToPreviousWord) | Ctrl+Left | Alt+Left | Ctrl+Left | Ctrl+Left |
| [MoveToNextLine](#StandardKey-MoveToNextLine) | Down | Down, Meta+N | Down | Down |
| [MoveToPreviousLine](#StandardKey-MoveToPreviousLine) | Up | Up, Meta+P | Up | Up |
| [MoveToNextPage](#StandardKey-MoveToNextPage) | PgDown | PgDown, Alt+PgDown, Meta+Down, Meta+PgDown, Meta+V | PgDown | PgDown |
| [MoveToPreviousPage](#StandardKey-MoveToPreviousPage) | PgUp | PgUp, Alt+PgUp, Meta+Up, Meta+PgUp | PgUp | PgUp |
| [MoveToStartOfLine](#StandardKey-MoveToStartOfLine) | Home | Ctrl+Left, Meta+Left | Home | Home |
| [MoveToEndOfLine](#StandardKey-MoveToEndOfLine) | End | Ctrl+Right, Meta+Right | End, Ctrl+E | End, Ctrl+E |
| [MoveToStartOfBlock](#StandardKey-MoveToStartOfBlock) | (none) | Alt+Up, Meta+A | (none) | (none) |
| [MoveToEndOfBlock](#StandardKey-MoveToEndOfBlock) | (none) | Alt+Down, Meta+E | (none) | (none) |
| [MoveToStartOfDocument](#StandardKey-MoveToStartOfDocument) | Ctrl+Home | Ctrl+Up, Home | Ctrl+Home | Ctrl+Home |
| [MoveToEndOfDocument](#StandardKey-MoveToEndOfDocument) | Ctrl+End | Ctrl+Down, End | Ctrl+End | Ctrl+End |
| [SelectNextChar](#StandardKey-SelectNextChar) | Shift+Right | Shift+Right | Shift+Right | Shift+Right |
| [SelectPreviousChar](#StandardKey-SelectPreviousChar) | Shift+Left | Shift+Left | Shift+Left | Shift+Left |
| [SelectNextWord](#StandardKey-SelectNextWord) | Ctrl+Shift+Right | Alt+Shift+Right | Ctrl+Shift+Right | Ctrl+Shift+Right |
| [SelectPreviousWord](#StandardKey-SelectPreviousWord) | Ctrl+Shift+Left | Alt+Shift+Left | Ctrl+Shift+Left | Ctrl+Shift+Left |
| [SelectNextLine](#StandardKey-SelectNextLine) | Shift+Down | Shift+Down | Shift+Down | Shift+Down |
| [SelectPreviousLine](#StandardKey-SelectPreviousLine) | Shift+Up | Shift+Up | Shift+Up | Shift+Up |
| [SelectNextPage](#StandardKey-SelectNextPage) | Shift+PgDown | Shift+PgDown | Shift+PgDown | Shift+PgDown |
| [SelectPreviousPage](#StandardKey-SelectPreviousPage) | Shift+PgUp | Shift+PgUp | Shift+PgUp | Shift+PgUp |
| [SelectStartOfLine](#StandardKey-SelectStartOfLine) | Shift+Home | Ctrl+Shift+Left | Shift+Home | Shift+Home |
| [SelectEndOfLine](#StandardKey-SelectEndOfLine) | Shift+End | Ctrl+Shift+Right | Shift+End | Shift+End |
| [SelectStartOfBlock](#StandardKey-SelectStartOfBlock) | (none) | Alt+Shift+Up, Meta+Shift+A | (none) | (none) |
| [SelectEndOfBlock](#StandardKey-SelectEndOfBlock) | (none) | Alt+Shift+Down, Meta+Shift+E | (none) | (none) |
| [SelectStartOfDocument](#StandardKey-SelectStartOfDocument) | Ctrl+Shift+Home | Ctrl+Shift+Up, Shift+Home | Ctrl+Shift+Home | Ctrl+Shift+Home |
| [SelectEndOfDocument](#StandardKey-SelectEndOfDocument) | Ctrl+Shift+End | Ctrl+Shift+Down, Shift+End | Ctrl+Shift+End | Ctrl+Shift+End |
| [DeleteStartOfWord](#StandardKey-DeleteStartOfWord) | Ctrl+Backspace | Alt+Backspace | Ctrl+Backspace | Ctrl+Backspace |
| [DeleteEndOfWord](#StandardKey-DeleteEndOfWord) | Ctrl+Del | (none) | Ctrl+Del | Ctrl+Del |
| [DeleteEndOfLine](#StandardKey-DeleteEndOfLine) | (none) | (none) | Ctrl+K | Ctrl+K |
| [DeleteCompleteLine](#StandardKey-DeleteCompleteLine) | (none) | (none) | Ctrl+U | Ctrl+U |
| [InsertParagraphSeparator](#StandardKey-InsertParagraphSeparator) | Enter | Enter | Enter | Enter |
| [InsertLineSeparator](#StandardKey-InsertLineSeparator) | Shift+Enter | Meta+Enter, Meta+O | Shift+Enter | Shift+Enter |
| Backspace | (none) | Delete, Meta+H | (none) | (none) |
| Cancel | Escape | Escape, Ctrl+. | Escape | Escape |

Note that, since the key sequences used for the standard shortcuts differ between platforms, you still need to test your shortcuts on each platform to ensure that you do not unintentionally assign the same key sequence to many actions.

### Keyboard Layout Issues[¶](#keyboard-layout-issues "Link to this heading")

Many key sequence specifications are chosen by developers based on the layout of certain types of keyboard, rather than choosing keys that represent the first letter of an action’s name, such as Ctrl S (“Ctrl+S”) or Ctrl C (“Ctrl+C”). Additionally, because certain symbols can only be entered with the help of modifier keys on certain keyboard layouts, key sequences intended for use with one keyboard layout may map to a different key, map to no keys at all, or require an additional modifier key to be used on different keyboard layouts.

For example, the shortcuts, Ctrl plus and Ctrl minus, are often used as shortcuts for zoom operations in graphics applications, and these may be specified as “Ctrl++” and “Ctrl+-” respectively. However, the way these shortcuts are specified and interpreted depends on the keyboard layout. Users of Norwegian keyboards will note that the + and - keys are not adjacent on the keyboard, but will still be able to activate both shortcuts without needing to press the Shift key. However, users with British keyboards will need to hold down the Shift key to enter the + symbol, making the shortcut effectively the same as “Ctrl+Shift+=”.

Although some developers might resort to fully specifying all the modifiers they use on their keyboards to activate a shortcut, this will also result in unexpected behavior for users of different keyboard layouts.

For example, a developer using a British keyboard may decide to specify “Ctrl+Shift+=” as the key sequence in order to create a shortcut that coincidentally behaves in the same way as Ctrl plus. However, the = key needs to be accessed using the Shift key on Norwegian keyboard, making the required shortcut effectively Ctrl Shift Shift = (an impossible key combination).

As a result, both human-readable strings and hard-coded key codes can both be problematic to use when specifying a key sequence that can be used on a variety of different keyboard layouts. Only the use of [StandardKey](#StandardKey) guarantees that the user will be able to use the shortcuts that the developer intended.

Despite this, we can address this issue by ensuring that human-readable strings are used, making it possible for translations of key sequences to be made for users of different languages. This approach will be successful for users whose keyboards have the most typical layout for the language they are using.

### GNU Emacs Style Key Sequences[¶](#gnu-emacs-style-key-sequences "Link to this heading")

Key sequences similar to those used in [GNU Emacs](http://www.gnu.org/software/emacs/), allowing up to four key codes, can be created by using the multiple argument constructor, or by passing a human-readable string of comma-separated key sequences.

For example, the key sequence, Ctrl X followed by Ctrl C, can be specified using either of the following ways:

```
# QKeySequence(tr("Ctrl+X, Ctrl+C"));
# QKeySequence(Qt::CTRL | Qt::Key_X, Qt::CTRL | Qt::Key_C);
# QKeySequence(Qt::CTRL + Qt::Key_X, Qt::CTRL + Qt::Key_C); // deprecated
```

**Warning:** A [QApplication](../qtwidgets/qapplication.html) instance must have been constructed before a QKeySequence is created; otherwise, your application may crash.

See also

[QShortcut](qshortcut.html).

## Enums[¶](#enums "Link to this heading")

SequenceFormat
:   | Member | Value | Description |
    | --- | --- | --- |
    | NativeText | 0 | The key sequence as a platform specific string. This means that it will be shown translated and on Apple platforms it will resemble a key sequence from the menu bar. This enum is best used when you want to display the string to the user. |
    | PortableText | 1 | The key sequence is given in a “portable” format, suitable for reading and writing to a file. In many cases, it will look similar to the native text on Windows and X11. |

---

SequenceMatch
:   | Member | Value | Description |
    | --- | --- | --- |
    | ExactMatch | 2 | The key sequences are the same. |
    | NoMatch | 0 | The key sequences are different; not even partially matching. |
    | PartialMatch | 1 | The key sequences match partially, but are not the same. |

---

StandardKey
:   This enum represent standard key bindings. They can be used to assign platform dependent keyboard shortcuts to a [QAction](qaction.html).

    Note that the key bindings are platform dependent. The currently bound shortcuts can be queried using [keyBindings()](#keyBindings).

    | Member | Value | Description |
    | --- | --- | --- |
    | AddTab | 19 | Add new tab. |
    | Back | 13 | Navigate back. |
    | Backspace | 69 | Delete previous character. |
    | Bold | 27 | Bold text. |
    | Cancel | 70 | Cancel the current operation. |
    | Close | 4 | Close document/tab. |
    | Copy | 9 | Copy. |
    | Cut | 8 | Cut. |
    | Delete | 7 | Delete. |
    | DeleteCompleteLine | 68 | Delete the entire line. |
    | DeleteEndOfLine | 60 | Delete end of line. |
    | DeleteEndOfWord | 59 | Delete word from the end of the cursor. |
    | DeleteStartOfWord | 58 | Delete the beginning of a word up to the cursor. |
    | Deselect | 67 | Deselect text. Since 5.1 |
    | Find | 22 | Find in document. |
    | FindNext | 23 | Find next result. |
    | FindPrevious | 24 | Find previous result. |
    | Forward | 14 | Navigate forward. |
    | FullScreen | 66 | Toggle the window state to/from full screen. |
    | HelpContents | 1 | Open help contents. |
    | InsertLineSeparator | 62 | Insert a new line. |
    | InsertParagraphSeparator | 61 | Insert a new paragraph. |
    | Italic | 28 | Italic text. |
    | MoveToEndOfBlock | 41 | Move cursor to end of block. This shortcut is only used on Apple platforms. |
    | MoveToEndOfDocument | 43 | Move cursor to end of document. |
    | MoveToEndOfLine | 39 | Move cursor to end of line. |
    | MoveToNextChar | 30 | Move cursor to next character. |
    | MoveToNextLine | 34 | Move cursor to next line. |
    | MoveToNextPage | 36 | Move cursor to next page. |
    | MoveToNextWord | 32 | Move cursor to next word. |
    | MoveToPreviousChar | 31 | Move cursor to previous character. |
    | MoveToPreviousLine | 35 | Move cursor to previous line. |
    | MoveToPreviousPage | 37 | Move cursor to previous page. |
    | MoveToPreviousWord | 33 | Move cursor to previous word. |
    | MoveToStartOfBlock | 40 | Move cursor to start of a block. This shortcut is only used on Apple platforms. |
    | MoveToStartOfDocument | 42 | Move cursor to start of document. |
    | MoveToStartOfLine | 38 | Move cursor to start of line. |
    | New | 6 | Create new document. |
    | NextChild | 20 | Navigate to next tab or child window. |
    | Open | 3 | Open document. |
    | Paste | 10 | Paste. |
    | Preferences | 64 | Open the preferences dialog. |
    | PreviousChild | 21 | Navigate to previous tab or child window. |
    | Print | 18 | Print document. |
    | Quit | 65 | Quit the application. |
    | Redo | 12 | Redo. |
    | Refresh | 15 | Refresh or reload current document. |
    | Replace | 25 | Find and replace. |
    | Save | 5 | Save document. |
    | SaveAs | 63 | Save document after prompting the user for a file name. |
    | SelectAll | 26 | Select all text. |
    | SelectEndOfBlock | 55 | Extend selection to the end of a text block. This shortcut is only used on Apple platforms. |
    | SelectEndOfDocument | 57 | Extend selection to end of document. |
    | SelectEndOfLine | 53 | Extend selection to end of line. |
    | SelectNextChar | 44 | Extend selection to next character. |
    | SelectNextLine | 48 | Extend selection to next line. |
    | SelectNextPage | 50 | Extend selection to next page. |
    | SelectNextWord | 46 | Extend selection to next word. |
    | SelectPreviousChar | 45 | Extend selection to previous character. |
    | SelectPreviousLine | 49 | Extend selection to previous line. |
    | SelectPreviousPage | 51 | Extend selection to previous page. |
    | SelectPreviousWord | 47 | Extend selection to previous word. |
    | SelectStartOfBlock | 54 | Extend selection to the start of a text block. This shortcut is only used on Apple platforms. |
    | SelectStartOfDocument | 56 | Extend selection to start of document. |
    | SelectStartOfLine | 52 | Extend selection to start of line. |
    | Underline | 29 | Underline text. |
    | Undo | 11 | Undo. |
    | UnknownKey | 0 | Unbound key. |
    | WhatsThis | 2 | Activate “what’s this”. |
    | ZoomIn | 16 | Zoom in. |
    | ZoomOut | 17 | Zoom out. |

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs an empty key sequence.

---

\_\_init\_\_(QKeySequence)
:   Copy constructor. Makes a copy of *keysequence*.

---

\_\_init\_\_([StandardKey](#StandardKey))
:   Constructs a QKeySequence object for the given *key*. The result will depend on the currently running platform.

    The resulting object will be based on the first element in the list of key bindings for the *key*.

---

\_\_init\_\_(Any)
:   TODO

---

\_\_init\_\_(str|None, format: [SequenceFormat](#SequenceFormat) = [NativeText](#SequenceFormat-NativeText))
:   Creates a key sequence from the *key* string, based on *format*.

    For example “Ctrl+O” gives CTRL+’O’. The strings “Ctrl”, “Shift”, “Alt” and “Meta” are recognized, as well as their translated equivalents in the “[QShortcut](qshortcut.html)” context (using [tr()](../qtcore/qobject.html#tr)).

    Up to four key codes may be entered by separating them with commas, e.g. “Alt+X,Ctrl+S,Q”.

    This constructor is typically used with [tr()](../qtcore/qobject.html#tr)(), so that shortcut keys can be replaced in translations:

    ```
    # QMenu *file = new QMenu(this);
    # file->addAction(tr("&Open..."), this, SLOT(open()),
    #                   QKeySequence(tr("Ctrl+O", "File|Open")));
    ```

    Note the “File|Open” translator comment. It is by no means necessary, but it provides some context for the human translator.

---

\_\_init\_\_(int, key2: int = 0, key3: int = 0, key4: int = 0)
:   Constructs a key sequence with up to 4 keys *k1*, *k2*, *k3* and *k4*.

    The key codes are listed in [Key](../qtcore/qt.html#Key) and can be combined with modifiers (see [KeyboardModifier](../qtcore/qt.html#KeyboardModifier)) such as [ShiftModifier](../qtcore/qt.html#KeyboardModifier-ShiftModifier), [ControlModifier](../qtcore/qt.html#KeyboardModifier-ControlModifier), [AltModifier](../qtcore/qt.html#KeyboardModifier-AltModifier), or [MetaModifier](../qtcore/qt.html#KeyboardModifier-MetaModifier).

---

\_\_init\_\_([QKeyCombination](../qtcore/qkeycombination.html), key2: [QKeyCombination](../qtcore/qkeycombination.html) = QKeyCombination.fromCombined(0), key3: [QKeyCombination](../qtcore/qkeycombination.html) = QKeyCombination.fromCombined(0), key4: [QKeyCombination](../qtcore/qkeycombination.html) = QKeyCombination.fromCombined(0))
:   Constructs a key sequence with up to 4 keys *k1*, *k2*, *k3* and *k4*.

    See also

    [QKeyCombination](https://doc.qt.io/qt-6/gui-changes-qt6.html#qkeycombination).

---

count() → int
:   Returns the number of keys in the key sequence. The maximum is 4.

---

\_\_eq\_\_(QKeySequence|[StandardKey](#StandardKey)|str|None|int) → bool
:   TODO

---

@staticmethod fromString(str|None, format: [SequenceFormat](#SequenceFormat) = [PortableText](#SequenceFormat-PortableText)) → QKeySequence
:   Return a QKeySequence from the string *str* based on *format*.

    See also

    [toString()](#toString).

---

\_\_ge\_\_(QKeySequence|[StandardKey](#StandardKey)|str|None|int) → bool
:   TODO

---

\_\_getitem\_\_(int) → [QKeyCombination](../qtcore/qkeycombination.html)
:   TODO

---

\_\_gt\_\_(QKeySequence|[StandardKey](#StandardKey)|str|None|int) → bool
:   TODO

---

\_\_hash\_\_() → int
:   TODO

---

isDetached() → bool
:   TODO

---

isEmpty() → bool
:   Returns `true` if the key sequence is empty; otherwise returns false.

---

@staticmethod keyBindings([StandardKey](#StandardKey)) → list[QKeySequence]
:   Returns a list of key bindings for the given *key*. The result of calling this function will vary based on the target platform. The first element of the list indicates the primary shortcut for the given platform. If the result contains more than one result, these can be considered alternative shortcuts on the same platform for the given *key*.

---

\_\_le\_\_(QKeySequence|[StandardKey](#StandardKey)|str|None|int) → bool
:   TODO

---

\_\_len\_\_() → int
:   TODO

---

@staticmethod listFromString(str|None, format: [SequenceFormat](#SequenceFormat) = [PortableText](#SequenceFormat-PortableText)) → list[QKeySequence]
:   Return a list of QKeySequence from the string *str* based on *format*.

    See also

    [fromString()](#fromString), [listToString()](#listToString).

---

@staticmethod listToString(Iterable[QKeySequence|[StandardKey](#StandardKey)|str|None|int], format: [SequenceFormat](#SequenceFormat) = [PortableText](#SequenceFormat-PortableText)) → str
:   Return a string representation of *list* based on *format*.

    See also

    [toString()](#toString), [listFromString()](#listFromString).

---

\_\_lt\_\_(QKeySequence|[StandardKey](#StandardKey)|str|None|int) → bool
:   TODO

---

matches(QKeySequence|[StandardKey](#StandardKey)|str|None|int) → [SequenceMatch](#SequenceMatch)
:   Matches the sequence with *seq*. Returns [ExactMatch](#SequenceMatch-ExactMatch) if successful, [PartialMatch](#SequenceMatch-PartialMatch) if *seq* matches incompletely, and [NoMatch](#SequenceMatch-NoMatch) if the sequences have nothing in common. Returns [NoMatch](#SequenceMatch-NoMatch) if *seq* is shorter.

---

@staticmethod mnemonic(str|None) → QKeySequence
:   Returns the shortcut key sequence for the mnemonic in *text*, or an empty key sequence if no mnemonics are found.

    For example, mnemonic(“E&xit”) returns `Qt::ALT+Qt::Key_X`, mnemonic(”&Quit”) returns `ALT+Key_Q`, and mnemonic(“Quit”) returns an empty QKeySequence.

---

\_\_ne\_\_(QKeySequence|[StandardKey](#StandardKey)|str|None|int) → bool
:   TODO

---

swap(QKeySequence)
:   Swaps this key sequence with *other*. This operation is very fast and never fails.

---

toString(format: [SequenceFormat](#SequenceFormat) = [PortableText](#SequenceFormat-PortableText)) → str
:   Return a string representation of the key sequence, based on *format*.

    For example, the value Key\_O results in “Ctrl+O”. If the key sequence has multiple key codes, each is separated by commas in the string returned, such as “Alt+X, Ctrl+Y, Z”. The strings, “Ctrl”, “Shift”, etc. are translated using [tr()](../qtcore/qobject.html#tr) in the “[QShortcut](qshortcut.html)” context.

    If the key sequence has no keys, an empty string is returned.

    On Apple platforms, the string returned resembles the sequence that is shown in the menu bar if *format* is [NativeText](#SequenceFormat-NativeText); otherwise, the string uses the “portable” format, suitable for writing to a file.

    See also

    [fromString()](#fromString).

### [Table of Contents](../../index.html)

* QKeySequence
  + [Description](#description)
    - [Standard Shortcuts](#standard-shortcuts)
    - [Keyboard Layout Issues](#keyboard-layout-issues)
    - [GNU Emacs Style Key Sequences](#gnu-emacs-style-key-sequences)
  + [Enums](#enums)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QKeySequence

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QLine {#qline}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QLine

# QLine[¶](#qline "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QLine

## Description[¶](#description "Link to this heading")

The QLine class provides a two-dimensional vector using integer precision.

A QLine describes a finite length line (or a line segment) on a two-dimensional surface. The start and end points of the line are specified using integer point accuracy for coordinates. Use the [QLineF](qlinef.html) constructor to retrieve a floating point copy.

|  |  |
| --- | --- |
| ![image-qline-point-png](../../_images/qline-point.png) | ![image-qline-coordinates-png](../../_images/qline-coordinates.png) |

The positions of the line’s start and end points can be retrieved using the [p1()](#p1), [x1()](#x1), [y1()](#y1), [p2()](#p2), [x2()](#x2), and [y2()](#y2) functions. The [dx()](#dx) and [dy()](#dy) functions return the horizontal and vertical components of the line. Use [isNull()](#isNull) to determine whether the QLine represents a valid line or a null line.

Finally, the line can be translated a given offset using the [translate()](#translate) function.

See also

[QLineF](qlinef.html), [QPolygon](../qtgui/qpolygon.html), [QRect](qrect.html).

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs a null line.

---

\_\_init\_\_(QLine)
:   TODO

---

\_\_init\_\_([QPoint](qpoint.html), [QPoint](qpoint.html))
:   Constructs a line object that represents the line between *p1* and *p2*.

---

\_\_init\_\_(int, int, int, int)
:   Constructs a line object that represents the line between (*x1*, *y1*) and (*x2*, *y2*).

---

\_\_bool\_\_() → int
:   TODO

---

center() → [QPoint](qpoint.html)
:   Returns the center point of this line. This is equivalent to ([p1()](#p1) + [p2()](#p2)) / 2, except it will never overflow.

---

dx() → int
:   Returns the horizontal component of the line’s vector.

    See also

    [dy()](#dy).

---

dy() → int
:   Returns the vertical component of the line’s vector.

    See also

    [dx()](#dx).

---

\_\_eq\_\_([QLineF](qlinef.html)) → bool
:   TODO

---

\_\_eq\_\_(QLine) → bool
:   TODO

---

isNull() → bool
:   Returns `true` if the line does not have distinct start and end points; otherwise returns `false`.

---

\_\_ne\_\_([QLineF](qlinef.html)) → bool
:   TODO

---

\_\_ne\_\_(QLine) → bool
:   TODO

---

p1() → [QPoint](qpoint.html)
:   Returns the line’s start point.

    See also

    [setP1()](#setP1), [x1()](#x1), [y1()](#y1), [p2()](#p2).

---

p2() → [QPoint](qpoint.html)
:   Returns the line’s end point.

    See also

    [setP2()](#setP2), [x2()](#x2), [y2()](#y2), [p1()](#p1).

---

\_\_repr\_\_() → str
:   TODO

---

setLine(int, int, int, int)
:   Sets this line to the start in *x1*, *y1* and end in *x2*, *y2*.

    See also

    [setP1()](#setP1), [setP2()](#setP2), [p1()](#p1), [p2()](#p2).

---

setP1([QPoint](qpoint.html))
:   Sets the starting point of this line to *p1*.

    See also

    [setP2()](#setP2), [p1()](#p1).

---

setP2([QPoint](qpoint.html))
:   Sets the end point of this line to *p2*.

    See also

    [setP1()](#setP1), [p2()](#p2).

---

setPoints([QPoint](qpoint.html), [QPoint](qpoint.html))
:   Sets the start point of this line to *p1* and the end point of this line to *p2*.

    See also

    [setP1()](#setP1), [setP2()](#setP2), [p1()](#p1), [p2()](#p2).

---

toLineF() → [QLineF](qlinef.html)
:   Returns this line as a line with floating point accuracy.

    See also

    [toLine()](qlinef.html#toLine).

---

translate([QPoint](qpoint.html))
:   Translates this line by the given *offset*.

---

translate(int, int)
:   Translates this line the distance specified by *dx* and *dy*.

---

translated([QPoint](qpoint.html)) → QLine
:   Returns this line translated by the given *offset*.

---

translated(int, int) → QLine
:   Returns this line translated the distance specified by *dx* and *dy*.

---

x1() → int
:   Returns the x-coordinate of the line’s start point.

    See also

    [p1()](#p1).

---

x2() → int
:   Returns the x-coordinate of the line’s end point.

    See also

    [p2()](#p2).

---

y1() → int
:   Returns the y-coordinate of the line’s start point.

    See also

    [p1()](#p1).

---

y2() → int
:   Returns the y-coordinate of the line’s end point.

    See also

    [p2()](#p2).

### [Table of Contents](../../index.html)

* QLine
  + [Description](#description)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QLine

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QLineF {#qlinef}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QLineF

# QLineF[¶](#qlinef "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QLineF

## Description[¶](#description "Link to this heading")

The QLineF class provides a two-dimensional vector using floating point precision.

A QLineF describes a finite length line (or line segment) on a two-dimensional surface. QLineF defines the start and end points of the line using floating point accuracy for coordinates. Use the [toLine()](#toLine) function to retrieve an integer based copy of this line.

|  |  |
| --- | --- |
| ![image-qline-point-png](../../_images/qline-point.png) | ![image-qline-coordinates-png](../../_images/qline-coordinates.png) |

The positions of the line’s start and end points can be retrieved using the [p1()](#p1), [x1()](#x1), [y1()](#y1), [p2()](#p2), [x2()](#x2), and [y2()](#y2) functions. The [dx()](#dx) and [dy()](#dy) functions return the horizontal and vertical components of the line, respectively.

The line’s length can be retrieved using the [length()](#length) function, and altered using the [setLength()](#setLength) function. Similarly, [angle()](#angle) and [setAngle()](#setAngle) are respectively used for retrieving and altering the angle of the line. Use the [isNull()](#isNull) function to determine whether the QLineF represents a valid line or a null line.

The [intersects()](#intersects) function determines the IntersectionType for this line and a given line, while the [angleTo()](#angleTo) function returns the angle between the lines. In addition, the [unitVector()](#unitVector) function returns a line that has the same starting point as this line, but with a length of only 1, while the [normalVector()](#normalVector) function returns a line that is perpendicular to this line with the same starting point and length.

Finally, the line can be translated a given offset using the [translate()](#translate) function, and can be traversed using the [pointAt()](#pointAt) function.

### Constraints[¶](#constraints "Link to this heading")

[QLine](qline.html) is limited to the minimum and maximum values for the `int` type. Operations on a [QLine](qline.html) that could potentially result in values outside this range will result in undefined behavior.

See also

[QLine](qline.html), [QPolygonF](../qtgui/qpolygonf.html), [QRectF](qrectf.html).

## Enums[¶](#enums "Link to this heading")

IntersectionType
:   Describes the intersection between two lines.

    |  |  |
    | --- | --- |
    | ![image-qlinef-unbounded-png](../../_images/qlinef-unbounded.png) | ![image-qlinef-bounded-png](../../_images/qlinef-bounded.png) |
    | QLineF::UnboundedIntersection | QLineF::BoundedIntersection |

    See also

    [intersects()](#intersects).

    | Member | Value | Description |
    | --- | --- | --- |
    | BoundedIntersection | 1 | The two lines intersect with each other within the start and end points of each line. |
    | NoIntersection | 0 | Indicates that the lines do not intersect; i.e. they are parallel. |
    | UnboundedIntersection | 2 | The two lines intersect, but not within the range defined by their lengths. This will be the case if the lines are not parallel. intersect() will also return this value if the intersect point is within the start and end point of only one of the lines. |

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs a null line.

---

\_\_init\_\_([QLine](qline.html))
:   Construct a QLineF object from the given integer-based *line*.

    See also

    [toLine()](#toLine), [toLineF()](qline.html#toLineF).

---

\_\_init\_\_(QLineF)
:   TODO

---

\_\_init\_\_([QPointF](qpointf.html), [QPointF](qpointf.html))
:   Constructs a line object that represents the line between *p1* and *p2*.

---

\_\_init\_\_(float, float, float, float)
:   Constructs a line object that represents the line between (*x1*, *y1*) and (*x2*, *y2*).

---

angle() → float
:   Returns the angle of the line in degrees.

    The return value will be in the range of values from 0.0 up to but not including 360.0. The angles are measured counter-clockwise from a point on the x-axis to the right of the origin (x > 0).

    See also

    [setAngle()](#setAngle).

---

angleTo(QLineF) → float
:   Returns the angle (in degrees) from this line to the given *line*, taking the direction of the lines into account. If the lines do not [intersects()](#intersects) within their range, it is the intersection point of the extended lines that serves as origin (see [UnboundedIntersection](#IntersectionType-UnboundedIntersection)).

    The returned value represents the number of degrees you need to add to this line to make it have the same angle as the given *line*, going counter-clockwise.

    See also

    [intersects()](#intersects).

---

\_\_bool\_\_() → int
:   TODO

---

center() → [QPointF](qpointf.html)
:   Returns the center point of this line. This is equivalent to 0.5 \* [p1()](#p1) + 0.5 \* [p2()](#p2).

---

dx() → float
:   Returns the horizontal component of the line’s vector.

    See also

    [dy()](#dy), [pointAt()](#pointAt).

---

dy() → float
:   Returns the vertical component of the line’s vector.

    See also

    [dx()](#dx), [pointAt()](#pointAt).

---

\_\_eq\_\_([QLine](qline.html)) → bool
:   TODO

---

\_\_eq\_\_(QLineF) → bool
:   TODO

---

@staticmethod fromPolar(float, float) → QLineF
:   Returns a QLineF with the given *length* and *angle*.

    The first point of the line will be on the origin.

    Positive values for the angles mean counter-clockwise while negative values mean the clockwise direction. Zero degrees is at the 3 o’clock position.

---

intersects(QLineF) → ([IntersectionType](#IntersectionType), [QPointF](qpointf.html))
:   Returns a value indicating whether or not *this* line intersects with the given *line*.

    The actual intersection point is extracted to *intersectionPoint* (if the pointer is valid). If the lines are parallel, the intersection point is undefined.

---

isNull() → bool
:   Returns `true` if the line does not have distinct start and end points; otherwise returns `false`. The start and end points are considered distinct if [qFuzzyCompare()](qtcore-module.html#qFuzzyCompare) can distinguish them in at least one coordinate.

    **Note:** Due to the use of fuzzy comparison, may return `true` for lines whose [length()](#length) is not zero.

    See also

    [qFuzzyCompare()](qtcore-module.html#qFuzzyCompare), [length()](#length).

---

length() → float
:   Returns the length of the line.

    See also

    [setLength()](#setLength), [isNull()](#isNull).

---

\_\_ne\_\_([QLine](qline.html)) → bool
:   TODO

---

\_\_ne\_\_(QLineF) → bool
:   TODO

---

normalVector() → QLineF
:   Returns a line that is perpendicular to this line with the same starting point and length.

    ![../../_images/qlinef-normalvector.png](../../_images/qlinef-normalvector.png)

    See also

    [unitVector()](#unitVector).

---

p1() → [QPointF](qpointf.html)
:   Returns the line’s start point.

    See also

    [setP1()](#setP1), [x1()](#x1), [y1()](#y1), [p2()](#p2).

---

p2() → [QPointF](qpointf.html)
:   Returns the line’s end point.

    See also

    [setP2()](#setP2), [x2()](#x2), [y2()](#y2), [p1()](#p1).

---

pointAt(float) → [QPointF](qpointf.html)
:   Returns the point at the position specified by finite parameter *t*. The function returns the line’s start point if t = 0, and its end point if t = 1.

    See also

    [dx()](#dx), [dy()](#dy).

---

\_\_repr\_\_() → str
:   TODO

---

setAngle(float)
:   Sets the angle of the line to the given *angle* (in degrees). This will change the position of the second point of the line such that the line has the given angle.

    Positive values for the angles mean counter-clockwise while negative values mean the clockwise direction. Zero degrees is at the 3 o’clock position.

    See also

    [angle()](#angle).

---

setLength(float)
:   Sets the length of the line to the given finite *length*. QLineF will move the end point - [p2()](#p2) - of the line to give the line its new length, unless [length()](#length) was previously zero, in which case no scaling is attempted.

    See also

    [length()](#length), [unitVector()](#unitVector).

---

setLine(float, float, float, float)
:   Sets this line to the start in *x1*, *y1* and end in *x2*, *y2*.

    See also

    [setP1()](#setP1), [setP2()](#setP2), [p1()](#p1), [p2()](#p2).

---

setP1([QPointF](qpointf.html))
:   Sets the starting point of this line to *p1*.

    See also

    [setP2()](#setP2), [p1()](#p1).

---

setP2([QPointF](qpointf.html))
:   Sets the end point of this line to *p2*.

    See also

    [setP1()](#setP1), [p2()](#p2).

---

setPoints([QPointF](qpointf.html), [QPointF](qpointf.html))
:   Sets the start point of this line to *p1* and the end point of this line to *p2*.

    See also

    [setP1()](#setP1), [setP2()](#setP2), [p1()](#p1), [p2()](#p2).

---

toLine() → [QLine](qline.html)
:   Returns an integer-based copy of this line.

    Note that the returned line’s start and end points are rounded to the nearest integer.

    See also

    QLineF, [toLineF()](qline.html#toLineF).

---

translate([QPointF](qpointf.html))
:   Translates this line by the given *offset*.

---

translate(float, float)
:   Translates this line the distance specified by *dx* and *dy*.

---

translated([QPointF](qpointf.html)) → QLineF
:   Returns this line translated by the given *offset*.

---

translated(float, float) → QLineF
:   Returns this line translated the distance specified by *dx* and *dy*.

---

unitVector() → QLineF
:   Returns the unit vector for this line, i.e a line starting at the same point as *this* line with a length of 1.0, provided the line is non-null.

    See also

    [normalVector()](#normalVector), [setLength()](#setLength).

---

x1() → float
:   Returns the x-coordinate of the line’s start point.

    See also

    [p1()](#p1).

---

x2() → float
:   Returns the x-coordinate of the line’s end point.

    See also

    [p2()](#p2).

---

y1() → float
:   Returns the y-coordinate of the line’s start point.

    See also

    [p1()](#p1).

---

y2() → float
:   Returns the y-coordinate of the line’s end point.

    See also

    [p2()](#p2).

### [Table of Contents](../../index.html)

* QLineF
  + [Description](#description)
    - [Constraints](#constraints)
  + [Enums](#enums)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QLineF

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QPoint {#qpoint}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QPoint

# QPoint[¶](#qpoint "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QPoint

## Description[¶](#description "Link to this heading")

The QPoint class defines a point in the plane using integer precision.

A point is specified by a x coordinate and an y coordinate which can be accessed using the [x()](#x) and [y()](#y) functions. The [isNull()](#isNull) function returns `true` if both x and y are set to 0. The coordinates can be set (or altered) using the [setX()](#setX) and [setY()](#setY) functions, or alternatively the rx() and ry() functions which return references to the coordinates (allowing direct manipulation).

Given a point *p*, the following statements are all equivalent:

```
# QPoint p;

# p.setX(p.x() + 1);
# p += QPoint(1, 0);
# p.rx()++;
```

A QPoint object can also be used as a vector: Addition and subtraction are defined as for vectors (each component is added separately). A QPoint object can also be divided or multiplied by an `int` or a `qreal`.

In addition, the QPoint class provides the [manhattanLength()](#manhattanLength) function which gives an inexpensive approximation of the length of the QPoint object interpreted as a vector. Finally, QPoint objects can be streamed as well as compared.

See also

[QPointF](qpointf.html), [QPolygon](../qtgui/qpolygon.html).

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs a null point, i.e. with coordinates (0, 0)

    See also

    [isNull()](#isNull).

---

\_\_init\_\_(QPoint)
:   TODO

---

\_\_init\_\_(int, int)
:   Constructs a point with the given coordinates (*xpos*, *ypos*).

    See also

    [setX()](#setX), [setY()](#setY).

---

\_\_add\_\_(QPoint) → QPoint
:   TODO

---

\_\_bool\_\_() → int
:   TODO

---

@staticmethod dotProduct(QPoint, QPoint) → int
:   ```
    # QPoint p( 3, 7);
    # QPoint q(-1, 4);
    # int lengthSquared = QPoint::dotProduct(p, q);   // lengthSquared becomes 25
    ```

    Returns the dot product of *p1* and *p2*.

---

\_\_eq\_\_([QPointF](qpointf.html)) → bool
:   TODO

---

\_\_eq\_\_(QPoint) → bool
:   TODO

---

\_\_hash\_\_() → int
:   TODO

---

\_\_iadd\_\_(QPoint) → QPoint
:   TODO

---

\_\_imul\_\_(int) → QPoint
:   TODO

---

\_\_imul\_\_(float) → QPoint
:   TODO

---

isNull() → bool
:   Returns `true` if both the x and y coordinates are set to 0, otherwise returns `false`.

---

\_\_isub\_\_(QPoint) → QPoint
:   TODO

---

\_\_itruediv\_\_(float) → QPoint
:   TODO

---

manhattanLength() → int
:   Returns the sum of the absolute values of [x()](#x) and [y()](#y), traditionally known as the “Manhattan length” of the vector from the origin to the point. For example:

    ```
    # QPoint oldPosition;

    # MyWidget::mouseMoveEvent(QMouseEvent *event)
    # {
    #     QPoint point = event->pos() - oldPosition;
    #     if (point.manhattanLength() > 3)
    #         // the mouse has moved more than 3 pixels since the oldPosition
    # }
    ```

    This is a useful, and quick to calculate, approximation to the true length:

    ```
    # double trueLength = std::sqrt(std::pow(x(), 2) + std::pow(y(), 2));
    ```

    The tradition of “Manhattan length” arises because such distances apply to travelers who can only travel on a rectangular grid, like the streets of Manhattan.

---

\_\_mul\_\_(int) → QPoint
:   TODO

---

\_\_mul\_\_(float) → QPoint
:   TODO

---

\_\_ne\_\_([QPointF](qpointf.html)) → bool
:   TODO

---

\_\_ne\_\_(QPoint) → bool
:   TODO

---

\_\_neg\_\_() → QPoint
:   TODO

---

\_\_pos\_\_() → QPoint
:   TODO

---

\_\_repr\_\_() → str
:   TODO

---

\_\_rmul\_\_(int) → QPoint
:   TODO

---

\_\_rmul\_\_(float) → QPoint
:   TODO

---

setX(int)
:   Sets the x coordinate of this point to the given *x* coordinate.

    See also

    [x()](#x), [setY()](#setY).

---

setY(int)
:   Sets the y coordinate of this point to the given *y* coordinate.

    See also

    [y()](#y), [setX()](#setX).

---

\_\_sub\_\_(QPoint) → QPoint
:   TODO

---

toPointF() → [QPointF](qpointf.html)
:   Returns this point as a point with floating point accuracy.

    See also

    [toPoint()](qpointf.html#toPoint).

---

transposed() → QPoint
:   Returns a point with x and y coordinates exchanged:

    ```
    QPoint{1, 2}.transposed() // {2, 1}
    ```

    See also

    [x()](#x), [y()](#y), [setX()](#setX), [setY()](#setY).

---

\_\_truediv\_\_(float) → QPoint
:   TODO

---

x() → int
:   Returns the x coordinate of this point.

    See also

    [setX()](#setX), rx().

---

y() → int
:   Returns the y coordinate of this point.

    See also

    [setY()](#setY), ry().

### [Table of Contents](../../index.html)

* QPoint
  + [Description](#description)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QPoint

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QPointF {#qpointf}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QPointF

# QPointF[¶](#qpointf "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QPointF

## Description[¶](#description "Link to this heading")

The QPointF class defines a point in the plane using floating point precision.

A point is specified by a x coordinate and an y coordinate which can be accessed using the [x()](#x) and [y()](#y) functions. The coordinates of the point are specified using floating point numbers for accuracy. The [isNull()](#isNull) function returns `true` if both x and y are set to 0.0. The coordinates can be set (or altered) using the [setX()](#setX) and [setY()](#setY) functions, or alternatively the rx() and ry() functions which return references to the coordinates (allowing direct manipulation).

Given a point *p*, the following statements are all equivalent:

```
# QPointF p;

# p.setX(p.x() + 1.0);
# p += QPointF(1.0, 0.0);
# p.rx()++;
```

A QPointF object can also be used as a vector: Addition and subtraction are defined as for vectors (each component is added separately). A QPointF object can also be divided or multiplied by an `int` or a `qreal`.

In addition, the QPointF class provides a constructor converting a [QPoint](qpoint.html) object into a QPointF object, and a corresponding [toPoint()](#toPoint) function which returns a [QPoint](qpoint.html) copy of *this* point. Finally, QPointF objects can be streamed as well as compared.

See also

[QPoint](qpoint.html), [QPolygonF](../qtgui/qpolygonf.html).

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs a null point, i.e. with coordinates (0.0, 0.0)

    See also

    [isNull()](#isNull).

---

\_\_init\_\_([QPoint](qpoint.html))
:   Constructs a copy of the given *point*.

    See also

    [toPoint()](#toPoint), [toPointF()](qpoint.html#toPointF).

---

\_\_init\_\_(QPointF)
:   TODO

---

\_\_init\_\_(float, float)
:   Constructs a point with the given coordinates (*xpos*, *ypos*).

    See also

    [setX()](#setX), [setY()](#setY).

---

\_\_add\_\_(QPointF) → QPointF
:   TODO

---

\_\_bool\_\_() → int
:   TODO

---

@staticmethod dotProduct(QPointF, QPointF) → float
:   ```
    # QPointF p( 3.1, 7.1);
    # QPointF q(-1.0, 4.1);
    # int lengthSquared = QPointF::dotProduct(p, q);   // lengthSquared becomes 26.01
    ```

    Returns the dot product of *p1* and *p2*.

---

\_\_eq\_\_([QPoint](qpoint.html)) → bool
:   TODO

---

\_\_eq\_\_(QPointF) → bool
:   TODO

---

\_\_iadd\_\_(QPointF) → QPointF
:   TODO

---

\_\_imul\_\_(float) → QPointF
:   TODO

---

isNull() → bool
:   Returns `true` if both the x and y coordinates are set to 0.0 (ignoring the sign); otherwise returns `false`.

---

\_\_isub\_\_(QPointF) → QPointF
:   TODO

---

\_\_itruediv\_\_(float) → QPointF
:   TODO

---

manhattanLength() → float
:   Returns the sum of the absolute values of [x()](#x) and [y()](#y), traditionally known as the “Manhattan length” of the vector from the origin to the point.

    See also

    [manhattanLength()](qpoint.html#manhattanLength).

---

\_\_mul\_\_(float) → QPointF
:   TODO

---

\_\_ne\_\_([QPoint](qpoint.html)) → bool
:   TODO

---

\_\_ne\_\_(QPointF) → bool
:   TODO

---

\_\_neg\_\_() → QPointF
:   TODO

---

\_\_pos\_\_() → QPointF
:   TODO

---

\_\_repr\_\_() → str
:   TODO

---

\_\_rmul\_\_(float) → QPointF
:   TODO

---

setX(float)
:   Sets the x coordinate of this point to the given finite *x* coordinate.

    See also

    [x()](#x), [setY()](#setY).

---

setY(float)
:   Sets the y coordinate of this point to the given finite *y* coordinate.

    See also

    [y()](#y), [setX()](#setX).

---

\_\_sub\_\_(QPointF) → QPointF
:   TODO

---

toPoint() → [QPoint](qpoint.html)
:   Rounds the coordinates of this point to the nearest integer, and returns a [QPoint](qpoint.html) object with the rounded coordinates.

    See also

    QPointF, [toPointF()](qpoint.html#toPointF).

---

transposed() → QPointF
:   Returns a point with x and y coordinates exchanged:

    ```
    QPointF{1.0, 2.0}.transposed() // {2.0, 1.0}
    ```

    See also

    [x()](#x), [y()](#y), [setX()](#setX), [setY()](#setY).

---

\_\_truediv\_\_(float) → QPointF
:   TODO

---

x() → float
:   Returns the x coordinate of this point.

    See also

    [setX()](#setX), rx().

---

y() → float
:   Returns the y coordinate of this point.

    See also

    [setY()](#setY), ry().

### [Table of Contents](../../index.html)

* QPointF
  + [Description](#description)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QPointF

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QPolygon {#qpolygon}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QPolygon

# QPolygon[¶](#qpolygon "Link to this heading")

[PyQt6.QtGui](qtgui-module.html).QPolygon

## Description[¶](#description "Link to this heading")

The QPolygon class provides a list of points using integer precision.

A QPolygon object is a QList<[QPoint](../qtcore/qpoint.html)>. The easiest way to add points to a QPolygon is to use QList’s streaming operator, as illustrated below:

```
# QPolygon polygon;
# polygon << QPoint(10, 20) << QPoint(20, 30);
```

In addition to the functions provided by QList, QPolygon provides some point-specific functions.

Each point in a polygon can be retrieved by passing its index to the [point()](#point) function. To populate the polygon, QPolygon provides the [setPoint()](#setPoint) function to set the point at a given index, the [setPoints()](#setPoints) function to set all the points in the polygon (resizing it to the given number of points), and the [putPoints()](#putPoints) function which copies a number of given points into the polygon from a specified index (resizing the polygon if necessary).

QPolygon provides the [boundingRect()](#boundingRect) and [translate()](#translate) functions for geometry functions. Use the [map()](qtransform.html#map) function for more general transformations of QPolygons.

The QPolygon class is [implicitly shared](https://doc.qt.io/qt-6/implicit-sharing.html).

See also

QList, [QPolygonF](qpolygonf.html), [QLine](../qtcore/qline.html).

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs a polygon with no points.

    See also

    QList::isEmpty().

---

\_\_init\_\_(Iterable[[QPoint](../qtcore/qpoint.html)])
:   Constructs a polygon containing the specified *points*.

    See also

    [setPoints()](#setPoints).

---

\_\_init\_\_(Any)
:   TODO

---

\_\_init\_\_(QPolygon)
:   TODO

---

\_\_init\_\_([QRect](../qtcore/qrect.html), closed: bool = False)
:   Constructs a polygon from the given *rectangle*. If *closed* is false, the polygon just contains the four points of the rectangle ordered clockwise, otherwise the polygon’s fifth point is set to *rectangle*.topLeft().

    Note that the bottom-right corner of the rectangle is located at (rectangle.x() + rectangle.width(), rectangle.y() + rectangle.height()).

    See also

    [setPoints()](#setPoints).

---

\_\_add\_\_(QPolygon) → QPolygon
:   TODO

---

append([QPoint](../qtcore/qpoint.html))
:   TODO

---

at(int) → [QPoint](../qtcore/qpoint.html)
:   TODO

---

boundingRect() → [QRect](../qtcore/qrect.html)
:   Returns the bounding rectangle of the polygon, or [QRect](../qtcore/qrect.html)(0, 0, 0, 0) if the polygon is empty.

    See also

    QList::isEmpty().

---

clear()
:   TODO

---

\_\_contains\_\_([QPoint](../qtcore/qpoint.html)) → int
:   TODO

---

contains([QPoint](../qtcore/qpoint.html)) → bool
:   TODO

---

containsPoint([QPoint](../qtcore/qpoint.html), [FillRule](../qtcore/qt.html#FillRule)) → bool
:   Returns `true` if the given *point* is inside the polygon according to the specified *fillRule*; otherwise returns `false`.

---

count() → int
:   TODO

---

count([QPoint](../qtcore/qpoint.html)) → int
:   TODO

---

data() → [voidptr](../sip/sip-module.html#PyQt6.sip.voidptr "PyQt6.sip.voidptr")
:   TODO

---

\_\_delitem\_\_(int)
:   TODO

---

\_\_delitem\_\_(slice)
:   TODO

---

\_\_eq\_\_(QPolygon) → bool
:   TODO

---

fill([QPoint](../qtcore/qpoint.html), size: int = -1)
:   TODO

---

first() → [QPoint](../qtcore/qpoint.html)
:   TODO

---

\_\_getitem\_\_(int) → [QPoint](../qtcore/qpoint.html)
:   TODO

---

\_\_getitem\_\_(slice) → QPolygon
:   TODO

---

\_\_iadd\_\_(QPolygon) → QPolygon
:   TODO

---

\_\_iadd\_\_([QPoint](../qtcore/qpoint.html)) → QPolygon
:   TODO

---

indexOf([QPoint](../qtcore/qpoint.html), from: int = 0) → int
:   TODO

---

insert(int, [QPoint](../qtcore/qpoint.html))
:   TODO

---

intersected(QPolygon) → QPolygon
:   Returns a polygon which is the intersection of this polygon and *r*.

    Set operations on polygons will treat the polygons as areas. Non-closed polygons will be treated as implicitly closed.

    See also

    [intersects()](#intersects).

---

intersects(QPolygon) → bool
:   Returns `true` if the current polygon intersects at any point the given polygon *p*. Also returns `true` if the current polygon contains or is contained by any part of *p*.

    Set operations on polygons will treat the polygons as areas. Non-closed polygons will be treated as implicitly closed.

    See also

    [intersected()](#intersected).

---

isEmpty() → bool
:   TODO

---

last() → [QPoint](../qtcore/qpoint.html)
:   TODO

---

lastIndexOf([QPoint](../qtcore/qpoint.html), from: int = -1) → int
:   TODO

---

\_\_len\_\_() → int
:   TODO

---

\_\_lshift\_\_([QPoint](../qtcore/qpoint.html)) → Any
:   TODO

---

mid(int, length: int = -1) → QPolygon
:   TODO

---

\_\_mul\_\_([QTransform](qtransform.html)) → QPolygon
:   TODO

---

\_\_ne\_\_(QPolygon) → bool
:   TODO

---

point(int) → [QPoint](../qtcore/qpoint.html)
:   Returns the point at the given *index*.

---

prepend([QPoint](../qtcore/qpoint.html))
:   TODO

---

putPoints(int, int, int, int)
:   TODO

---

putPoints(int, int, QPolygon, from: int = 0)
:   Copies *nPoints* points from the given *fromIndex* ( 0 by default) in *fromPolygon* into this polygon, starting at the specified *index*. For example:

    ```
    # QPolygon polygon1;
    # polygon1.putPoints(0, 3, 1,2, 0,0, 5,6);
    # // polygon1 is now the three-point polygon(1,2, 0,0, 5,6);

    # QPolygon polygon2;
    # polygon2.putPoints(0, 3, 4,4, 5,5, 6,6);
    # // polygon2 is now (4,4, 5,5, 6,6);

    # polygon1.putPoints(2, 3, polygon2);
    # // polygon1 is now the five-point polygon(1,2, 0,0, 4,4, 5,5, 6,6);
    ```

---

remove(int)
:   TODO

---

remove(int, int)
:   TODO

---

replace(int, [QPoint](../qtcore/qpoint.html))
:   TODO

---

resize(int)
:   TODO

---

\_\_setitem\_\_(int, [QPoint](../qtcore/qpoint.html))
:   TODO

---

\_\_setitem\_\_(slice, QPolygon)
:   TODO

---

setPoint(int, [QPoint](../qtcore/qpoint.html))
:   Sets the point at the given *index* to the given *point*.

---

setPoint(int, int, int)
:   Sets the point at the given *index* to the point specified by (*x*, *y*).

    See also

    [point()](#point), [putPoints()](#putPoints), [setPoints()](#setPoints).

---

setPoints(int, int, int)
:   TODO

---

size() → int
:   TODO

---

subtracted(QPolygon) → QPolygon
:   Returns a polygon which is *r* subtracted from this polygon.

    Set operations on polygons will treat the polygons as areas. Non-closed polygons will be treated as implicitly closed.

---

swap(QPolygon)
:   Swaps this polygon with *other*. This operation is very fast and never fails.

---

toPolygonF() → [QPolygonF](qpolygonf.html)
:   Returns this polygon as a polygon with floating point accuracy.

    See also

    [toPolygon()](qpolygonf.html#toPolygon).

---

translate([QPoint](../qtcore/qpoint.html))
:   Translates all points in the polygon by the given *offset*.

    See also

    [translated()](#translated).

---

translate(int, int)
:   Translates all points in the polygon by (*dx*, *dy*).

    See also

    [translated()](#translated).

---

translated([QPoint](../qtcore/qpoint.html)) → QPolygon
:   Returns a copy of the polygon that is translated by the given *offset*.

    See also

    [translate()](#translate).

---

translated(int, int) → QPolygon
:   Returns a copy of the polygon that is translated by (*dx*, *dy*).

    See also

    [translate()](#translate).

---

united(QPolygon) → QPolygon
:   Returns a polygon which is the union of this polygon and *r*.

    Set operations on polygons, will treat the polygons as areas, and implicitly close the polygon.

    See also

    [intersected()](#intersected), [subtracted()](#subtracted).

---

value(int) → [QPoint](../qtcore/qpoint.html)
:   TODO

---

value(int, [QPoint](../qtcore/qpoint.html)) → [QPoint](../qtcore/qpoint.html)
:   TODO

### [Table of Contents](../../index.html)

* QPolygon
  + [Description](#description)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QPolygon

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QRect {#qrect}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QRect

# QRect[¶](#qrect "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QRect

## Description[¶](#description "Link to this heading")

The QRect class defines a rectangle in the plane using integer precision.

A rectangle is normally expressed as a top-left corner and a size. The size (width and height) of a QRect is always equivalent to the mathematical rectangle that forms the basis for its rendering.

A QRect can be constructed with a set of left, top, width and height integers, or from a [QPoint](qpoint.html) and a [QSize](qsize.html). The following code creates two identical rectangles.

```
# QRect r1(100, 200, 11, 16);
# QRect r2(QPoint(100, 200), QSize(11, 16));
```

There is a third constructor that creates a QRect using the top-left and bottom-right coordinates, but we recommend that you avoid using it. The rationale is that for historical reasons the values returned by the [bottom()](#bottom) and [right()](#right) functions deviate from the true bottom-right corner of the rectangle.

The QRect class provides a collection of functions that return the various rectangle coordinates, and enable manipulation of these. QRect also provides functions to move the rectangle relative to the various coordinates. In addition there is a [moveTo()](#moveTo) function that moves the rectangle, leaving its top left corner at the given coordinates. Alternatively, the [translate()](#translate) function moves the rectangle the given offset relative to the current position, and the [translated()](#translated) function returns a translated copy of this rectangle.

The [size()](#size) function returns the rectangle’s dimensions as a [QSize](qsize.html). The dimensions can also be retrieved separately using the [width()](#width) and [height()](#height) functions. To manipulate the dimensions use the [setSize()](#setSize), [setWidth()](#setWidth) or [setHeight()](#setHeight) functions. Alternatively, the size can be changed by applying either of the functions setting the rectangle coordinates, for example, [setBottom()](#setBottom) or [setRight()](#setRight).

The [contains()](#contains) function tells whether a given point is inside the rectangle or not, and the [intersects()](#intersects) function returns `true` if this rectangle intersects with a given rectangle. The QRect class also provides the [intersected()](#intersected) function which returns the intersection rectangle, and the [united()](#united) function which returns the rectangle that encloses the given rectangle and this:

|  |  |
| --- | --- |
| ![image-qrect-intersect-png](../../_images/qrect-intersect.png) | ![image-qrect-unite-png](../../_images/qrect-unite.png) |
| [intersected()](#intersected) | [united()](#united) |

The [isEmpty()](#isEmpty) function returns `true` if [left()](#left) > [right()](#right) or [top()](#top) > [bottom()](#bottom). Note that an empty rectangle is not valid: The [isValid()](#isValid) function returns `true` if [left()](#left) <= [right()](#right) *and* [top()](#top) <= [bottom()](#bottom). A null rectangle ([isNull()](#isNull) == true) on the other hand, has both width and height set to 0.

Note that due to the way QRect and [QRectF](qrectf.html) are defined, an empty QRect is defined in essentially the same way as [QRectF](qrectf.html).

Finally, QRect objects can be streamed as well as compared.

### Rendering[¶](#rendering "Link to this heading")

When using an Antialiasing painter, the boundary line of a QRect will be rendered symmetrically on both sides of the mathematical rectangle’s boundary line. But when using an aliased painter (the default) other rules apply.

Then, when rendering with a one pixel wide pen the QRect’s boundary line will be rendered to the right and below the mathematical rectangle’s boundary line.

When rendering with a two pixels wide pen the boundary line will be split in the middle by the mathematical rectangle. This will be the case whenever the pen is set to an even number of pixels, while rendering with a pen with an odd number of pixels, the spare pixel will be rendered to the right and below the mathematical rectangle as in the one pixel case.

|  |  |
| --- | --- |
| ![image-qrect-diagram-zero-png](../../_images/qrect-diagram-zero.png) | ![image-qrect-diagram-one-png](../../_images/qrect-diagram-one.png) |
| Logical representation | One pixel wide pen |
| ![image-qrect-diagram-two-png](../../_images/qrect-diagram-two.png) | ![image-qrect-diagram-three-png](../../_images/qrect-diagram-three.png) |
| Two pixel wide pen | Three pixel wide pen |

### Coordinates[¶](#coordinates "Link to this heading")

The QRect class provides a collection of functions that return the various rectangle coordinates, and enable manipulation of these. QRect also provides functions to move the rectangle relative to the various coordinates.

For example the [left()](#left), [setLeft()](#setLeft) and [moveLeft()](#moveLeft) functions as an example: [left()](#left) returns the x-coordinate of the rectangle’s left edge, [setLeft()](#setLeft) sets the left edge of the rectangle to the given x coordinate (it may change the width, but will never change the rectangle’s right edge) and [moveLeft()](#moveLeft) moves the entire rectangle horizontally, leaving the rectangle’s left edge at the given x coordinate and its size unchanged.

![../../_images/qrect-coordinates.png](../../_images/qrect-coordinates.png)

Note that for historical reasons the values returned by the [bottom()](#bottom) and [right()](#right) functions deviate from the true bottom-right corner of the rectangle: The [right()](#right) function returns \* [left()](#left) + [width()](#width) - 1\* and the [bottom()](#bottom) function returns *:sip:ref:`~PyQt6.QtCore.QRect.top` + :sip:ref:`~PyQt6.QtCore.QRect.height` - 1*. The same is the case for the point returned by the [bottomRight()](#bottomRight) convenience function. In addition, the x and y coordinate of the [topRight()](#topRight) and [bottomLeft()](#bottomLeft) functions, respectively, contain the same deviation from the true right and bottom edges.

We recommend that you use [x()](#x) + [width()](#width) and [y()](#y) + [height()](#height) to find the true bottom-right corner, and avoid [right()](#right) and [bottom()](#bottom). Another solution is to use [QRectF](qrectf.html): The [QRectF](qrectf.html) class defines a rectangle in the plane using floating point accuracy for coordinates, and the [right()](qrectf.html#right) and [bottom()](qrectf.html#bottom) functions *do* return the right and bottom coordinates.

It is also possible to add offsets to this rectangle’s coordinates using the [adjust()](#adjust) function, as well as retrieve a new rectangle based on adjustments of the original one using the [adjusted()](#adjusted) function. If either of the width and height is negative, use the [normalized()](#normalized) function to retrieve a rectangle where the corners are swapped.

In addition, QRect provides the [getCoords()](#getCoords) function which extracts the position of the rectangle’s top-left and bottom-right corner, and the [getRect()](#getRect) function which extracts the rectangle’s top-left corner, width and height. Use the [setCoords()](#setCoords) and [setRect()](#setRect) function to manipulate the rectangle’s coordinates and dimensions in one go.

### Constraints[¶](#constraints "Link to this heading")

QRect is limited to the minimum and maximum values for the `int` type. Operations on a QRect that could potentially result in values outside this range will result in undefined behavior.

See also

[QRectF](qrectf.html), [QRegion](../qtgui/qregion.html).

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs a null rectangle.

    See also

    [isNull()](#isNull).

---

\_\_init\_\_(QRect)
:   TODO

---

\_\_init\_\_([QPoint](qpoint.html), [QPoint](qpoint.html))
:   Constructs a rectangle with the given *topLeft* and *bottomRight* corners, both included.

    If *bottomRight* is to higher and to the left of *topLeft*, the rectangle defined is instead non-inclusive of the corners.

    **Note:** To ensure both points are included regardless of relative order, use [span()](#span).

    See also

    [setTopLeft()](#setTopLeft), [setBottomRight()](#setBottomRight), [span()](#span).

---

\_\_init\_\_([QPoint](qpoint.html), [QSize](qsize.html))
:   Constructs a rectangle with the given *topLeft* corner and the given *size*.

    See also

    [setTopLeft()](#setTopLeft), [setSize()](#setSize).

---

\_\_init\_\_(int, int, int, int)
:   Constructs a rectangle with (*x*, *y*) as its top-left corner and the given *width* and *height*.

    See also

    [setRect()](#setRect).

---

\_\_add\_\_([QMargins](qmargins.html)) → QRect
:   TODO

---

adjust(int, int, int, int)
:   Adds *dx1*, *dy1*, *dx2* and *dy2* respectively to the existing coordinates of the rectangle.

    See also

    [adjusted()](#adjusted), [setRect()](#setRect).

---

adjusted(int, int, int, int) → QRect
:   Returns a new rectangle with *dx1*, *dy1*, *dx2* and *dy2* added respectively to the existing coordinates of this rectangle.

    See also

    [adjust()](#adjust).

---

\_\_and\_\_(QRect) → QRect
:   TODO

---

\_\_bool\_\_() → int
:   TODO

---

bottom() → int
:   Returns the y-coordinate of the rectangle’s bottom edge.

    Note that for historical reasons this function returns [top()](#top) + [height()](#height) - 1; use [y()](#y) + [height()](#height) to retrieve the true y-coordinate.

    See also

    [setBottom()](#setBottom), [bottomLeft()](#bottomLeft), [bottomRight()](#bottomRight).

---

bottomLeft() → [QPoint](qpoint.html)
:   Returns the position of the rectangle’s bottom-left corner. Note that for historical reasons this function returns [QPoint](qpoint.html)([left()](#left), [top()](#top) + [height()](#height) - 1).

    See also

    [setBottomLeft()](#setBottomLeft), [bottom()](#bottom), [left()](#left).

---

bottomRight() → [QPoint](qpoint.html)
:   Returns the position of the rectangle’s bottom-right corner.

    Note that for historical reasons this function returns [QPoint](qpoint.html)([left()](#left) + [width()](#width) -1, [top()](#top) + [height()](#height) - 1).

    See also

    [setBottomRight()](#setBottomRight), [bottom()](#bottom), [right()](#right).

---

center() → [QPoint](qpoint.html)
:   Returns the center point of the rectangle.

    See also

    [moveCenter()](#moveCenter).

---

\_\_contains\_\_([QPoint](qpoint.html)) → int
:   TODO

---

\_\_contains\_\_(QRect) → int
:   TODO

---

contains([QPoint](qpoint.html), proper: bool = False) → bool
:   Returns `true` if the given *point* is inside or on the edge of the rectangle, otherwise returns `false`. If *proper* is true, this function only returns `true` if the given *point* is *inside* the rectangle (i.e., not on the edge).

    See also

    [intersects()](#intersects).

---

contains(QRect, proper: bool = False) → bool
:   Returns `true` if the given *rectangle* is inside this rectangle. otherwise returns `false`. If *proper* is true, this function only returns `true` if the *rectangle* is entirely inside this rectangle (not on the edge).

---

contains(int, int) → bool
:   Returns `true` if the point (*x*, *y*) is inside this rectangle, otherwise returns `false`.

---

contains(int, int, bool) → bool
:   Returns `true` if the point (*x*, *y*) is inside or on the edge of the rectangle, otherwise returns `false`. If *proper* is true, this function only returns `true` if the point is entirely inside the rectangle(not on the edge).

---

\_\_eq\_\_([QRectF](qrectf.html)) → bool
:   TODO

---

\_\_eq\_\_(QRect) → bool
:   TODO

---

getCoords() → (int, int, int, int)
:   Extracts the position of the rectangle’s top-left corner to \**x1* and \**y1*, and the position of the bottom-right corner to \**x2* and \**y2*.

    See also

    [setCoords()](#setCoords), [getRect()](#getRect).

---

getRect() → (int, int, int, int)
:   Extracts the position of the rectangle’s top-left corner to \**x* and \**y*, and its dimensions to \**width* and \**height*.

    See also

    [setRect()](#setRect), [getCoords()](#getCoords).

---

\_\_hash\_\_() → int
:   TODO

---

height() → int
:   Returns the height of the rectangle.

    See also

    [setHeight()](#setHeight), [width()](#width), [size()](#size).

---

\_\_iadd\_\_([QMargins](qmargins.html)) → QRect
:   TODO

---

\_\_iand\_\_(QRect) → QRect
:   TODO

---

intersected(QRect) → QRect
:   Returns the intersection of this rectangle and the given *rectangle*. Note that `r.intersected(s)` is equivalent to `r & s`.

    ![../../_images/qrect-intersect.png](../../_images/qrect-intersect.png)

    See also

    [intersects()](#intersects), [united()](#united), operator&=().

---

intersects(QRect) → bool
:   Returns `true` if this rectangle intersects with the given *rectangle* (i.e., there is at least one pixel that is within both rectangles), otherwise returns `false`.

    The intersection rectangle can be retrieved using the [intersected()](#intersected) function.

    See also

    [contains()](#contains).

---

\_\_ior\_\_(QRect) → QRect
:   TODO

---

isEmpty() → bool
:   Returns `true` if the rectangle is empty, otherwise returns `false`.

    An empty rectangle has a [left()](#left) > [right()](#right) or [top()](#top) > [bottom()](#bottom). An empty rectangle is not valid (i.e., == ![isValid()](#isValid)).

    Use the [normalized()](#normalized) function to retrieve a rectangle where the corners are swapped.

    See also

    [isNull()](#isNull), [isValid()](#isValid), [normalized()](#normalized).

---

isNull() → bool
:   Returns `true` if the rectangle is a null rectangle, otherwise returns `false`.

    A null rectangle has both the width and the height set to 0 (i.e., [right()](#right) == [left()](#left) - 1 and [bottom()](#bottom) == [top()](#top) - 1). A null rectangle is also empty, and hence is not valid.

    See also

    [isEmpty()](#isEmpty), [isValid()](#isValid).

---

\_\_isub\_\_([QMargins](qmargins.html)) → QRect
:   TODO

---

isValid() → bool
:   Returns `true` if the rectangle is valid, otherwise returns `false`.

    A valid rectangle has a [left()](#left) <= [right()](#right) and [top()](#top) <= [bottom()](#bottom). Note that non-trivial operations like intersections are not defined for invalid rectangles. A valid rectangle is not empty (i.e., == ![isEmpty()](#isEmpty)).

    See also

    [isNull()](#isNull), [isEmpty()](#isEmpty), [normalized()](#normalized).

---

left() → int
:   Returns the x-coordinate of the rectangle’s left edge. Equivalent to [x()](#x).

    See also

    [setLeft()](#setLeft), [topLeft()](#topLeft), [bottomLeft()](#bottomLeft).

---

marginsAdded([QMargins](qmargins.html)) → QRect
:   Returns a rectangle grown by the *margins*.

    See also

    operator+=(), [marginsRemoved()](#marginsRemoved), operator-=().

---

marginsRemoved([QMargins](qmargins.html)) → QRect
:   Removes the *margins* from the rectangle, shrinking it.

    See also

    [marginsAdded()](#marginsAdded), operator+=(), operator-=().

---

moveBottom(int)
:   Moves the rectangle vertically, leaving the rectangle’s bottom edge at the given *y* coordinate. The rectangle’s size is unchanged.

    See also

    [bottom()](#bottom), [setBottom()](#setBottom), [moveTop()](#moveTop).

---

moveBottomLeft([QPoint](qpoint.html))
:   Moves the rectangle, leaving the bottom-left corner at the given *position*. The rectangle’s size is unchanged.

    See also

    [setBottomLeft()](#setBottomLeft), [moveBottom()](#moveBottom), [moveLeft()](#moveLeft).

---

moveBottomRight([QPoint](qpoint.html))
:   Moves the rectangle, leaving the bottom-right corner at the given *position*. The rectangle’s size is unchanged.

    See also

    [setBottomRight()](#setBottomRight), [moveRight()](#moveRight), [moveBottom()](#moveBottom).

---

moveCenter([QPoint](qpoint.html))
:   Moves the rectangle, leaving the center point at the given *position*. The rectangle’s size is unchanged.

    See also

    [center()](#center).

---

moveLeft(int)
:   Moves the rectangle horizontally, leaving the rectangle’s left edge at the given *x* coordinate. The rectangle’s size is unchanged.

    See also

    [left()](#left), [setLeft()](#setLeft), [moveRight()](#moveRight).

---

moveRight(int)
:   Moves the rectangle horizontally, leaving the rectangle’s right edge at the given *x* coordinate. The rectangle’s size is unchanged.

    See also

    [right()](#right), [setRight()](#setRight), [moveLeft()](#moveLeft).

---

moveTo([QPoint](qpoint.html))
:   Moves the rectangle, leaving the top-left corner at the given *position*.

---

moveTo(int, int)
:   Moves the rectangle, leaving the top-left corner at the given position (*x*, *y*). The rectangle’s size is unchanged.

    See also

    [translate()](#translate), [moveTopLeft()](#moveTopLeft).

---

moveTop(int)
:   Moves the rectangle vertically, leaving the rectangle’s top edge at the given *y* coordinate. The rectangle’s size is unchanged.

    See also

    [top()](#top), [setTop()](#setTop), [moveBottom()](#moveBottom).

---

moveTopLeft([QPoint](qpoint.html))
:   Moves the rectangle, leaving the top-left corner at the given *position*. The rectangle’s size is unchanged.

    See also

    [setTopLeft()](#setTopLeft), [moveTop()](#moveTop), [moveLeft()](#moveLeft).

---

moveTopRight([QPoint](qpoint.html))
:   Moves the rectangle, leaving the top-right corner at the given *position*. The rectangle’s size is unchanged.

    See also

    [setTopRight()](#setTopRight), [moveTop()](#moveTop), [moveRight()](#moveRight).

---

\_\_ne\_\_([QRectF](qrectf.html)) → bool
:   TODO

---

\_\_ne\_\_(QRect) → bool
:   TODO

---

normalized() → QRect
:   Returns a normalized rectangle; i.e., a rectangle that has a non-negative width and height.

    If [width()](#width) < 0 the function swaps the left and right corners, and it swaps the top and bottom corners if [height()](#height) < 0. The corners are at the same time changed from being non-inclusive to inclusive.

    See also

    [isValid()](#isValid), [isEmpty()](#isEmpty).

---

\_\_or\_\_(QRect) → QRect
:   TODO

---

\_\_repr\_\_() → str
:   TODO

---

right() → int
:   Returns the x-coordinate of the rectangle’s right edge.

    Note that for historical reasons this function returns [left()](#left) + [width()](#width) - 1; use [x()](#x) + [width()](#width) to retrieve the true x-coordinate.

    See also

    [setRight()](#setRight), [topRight()](#topRight), [bottomRight()](#bottomRight).

---

setBottom(int)
:   Sets the bottom edge of the rectangle to the given *y* coordinate. May change the height, but will never change the top edge of the rectangle.

    See also

    [bottom()](#bottom), [moveBottom()](#moveBottom).

---

setBottomLeft([QPoint](qpoint.html))
:   Set the bottom-left corner of the rectangle to the given *position*. May change the size, but will never change the top-right corner of the rectangle.

    See also

    [bottomLeft()](#bottomLeft), [moveBottomLeft()](#moveBottomLeft).

---

setBottomRight([QPoint](qpoint.html))
:   Set the bottom-right corner of the rectangle to the given *position*. May change the size, but will never change the top-left corner of the rectangle.

    See also

    [bottomRight()](#bottomRight), [moveBottomRight()](#moveBottomRight).

---

setCoords(int, int, int, int)
:   Sets the coordinates of the rectangle’s top-left corner to (*x1*, *y1*), and the coordinates of its bottom-right corner to (*x2*, *y2*).

    See also

    [getCoords()](#getCoords), [setRect()](#setRect).

---

setHeight(int)
:   Sets the height of the rectangle to the given *height*. The bottom edge is changed, but not the top one.

    See also

    [height()](#height), [setSize()](#setSize).

---

setLeft(int)
:   Sets the left edge of the rectangle to the given *x* coordinate. May change the width, but will never change the right edge of the rectangle.

    Equivalent to [setX()](#setX).

    See also

    [left()](#left), [moveLeft()](#moveLeft).

---

setRect(int, int, int, int)
:   Sets the coordinates of the rectangle’s top-left corner to (*x*, *y*), and its size to the given *width* and *height*.

    See also

    [getRect()](#getRect), [setCoords()](#setCoords).

---

setRight(int)
:   Sets the right edge of the rectangle to the given *x* coordinate. May change the width, but will never change the left edge of the rectangle.

    See also

    [right()](#right), [moveRight()](#moveRight).

---

setSize([QSize](qsize.html))
:   Sets the size of the rectangle to the given *size*. The top-left corner is not moved.

    See also

    [size()](#size), [setWidth()](#setWidth), [setHeight()](#setHeight).

---

setTop(int)
:   Sets the top edge of the rectangle to the given *y* coordinate. May change the height, but will never change the bottom edge of the rectangle.

    Equivalent to [setY()](#setY).

    See also

    [top()](#top), [moveTop()](#moveTop).

---

setTopLeft([QPoint](qpoint.html))
:   Set the top-left corner of the rectangle to the given *position*. May change the size, but will never change the bottom-right corner of the rectangle.

    See also

    [topLeft()](#topLeft), [moveTopLeft()](#moveTopLeft).

---

setTopRight([QPoint](qpoint.html))
:   Set the top-right corner of the rectangle to the given *position*. May change the size, but will never change the bottom-left corner of the rectangle.

    See also

    [topRight()](#topRight), [moveTopRight()](#moveTopRight).

---

setWidth(int)
:   Sets the width of the rectangle to the given *width*. The right edge is changed, but not the left one.

    See also

    [width()](#width), [setSize()](#setSize).

---

setX(int)
:   Sets the left edge of the rectangle to the given *x* coordinate. May change the width, but will never change the right edge of the rectangle.

    Equivalent to [setLeft()](#setLeft).

    See also

    [x()](#x), [setY()](#setY), [setTopLeft()](#setTopLeft).

---

setY(int)
:   Sets the top edge of the rectangle to the given *y* coordinate. May change the height, but will never change the bottom edge of the rectangle.

    Equivalent to [setTop()](#setTop).

    See also

    [y()](#y), [setX()](#setX), [setTopLeft()](#setTopLeft).

---

size() → [QSize](qsize.html)
:   Returns the size of the rectangle.

    See also

    [setSize()](#setSize), [width()](#width), [height()](#height).

---

@staticmethod span([QPoint](qpoint.html), [QPoint](qpoint.html)) → QRect
:   Returns a rectangle spanning the two points *p1* and *p2*, including both and everything in between.

---

\_\_sub\_\_([QMargins](qmargins.html)) → QRect
:   TODO

---

top() → int
:   Returns the y-coordinate of the rectangle’s top edge. Equivalent to [y()](#y).

    See also

    [setTop()](#setTop), [topLeft()](#topLeft), [topRight()](#topRight).

---

topLeft() → [QPoint](qpoint.html)
:   Returns the position of the rectangle’s top-left corner.

    See also

    [setTopLeft()](#setTopLeft), [top()](#top), [left()](#left).

---

topRight() → [QPoint](qpoint.html)
:   Returns the position of the rectangle’s top-right corner.

    Note that for historical reasons this function returns [QPoint](qpoint.html)([left()](#left) + [width()](#width) -1, [top()](#top)).

    See also

    [setTopRight()](#setTopRight), [top()](#top), [right()](#right).

---

toRectF() → [QRectF](qrectf.html)
:   Returns this rectangle as a rectangle with floating point accuracy.

    **Note:** This function, like the [QRectF](qrectf.html)(QRect) constructor, preserves the [size()](#size) of the rectangle, not its [bottomRight()](#bottomRight) corner.

    See also

    [toRect()](qrectf.html#toRect).

---

translate([QPoint](qpoint.html))
:   Moves the rectangle *offset*.[x()](qpoint.html#x) along the x axis and *offset*.[y()](qpoint.html#y) along the y axis, relative to the current position.

---

translate(int, int)
:   Moves the rectangle *dx* along the x axis and *dy* along the y axis, relative to the current position. Positive values move the rectangle to the right and down.

    See also

    [moveTopLeft()](#moveTopLeft), [moveTo()](#moveTo), [translated()](#translated).

---

translated([QPoint](qpoint.html)) → QRect
:   Returns a copy of the rectangle that is translated *offset*.[x()](qpoint.html#x) along the x axis and *offset*.[y()](qpoint.html#y) along the y axis, relative to the current position.

---

translated(int, int) → QRect
:   Returns a copy of the rectangle that is translated *dx* along the x axis and *dy* along the y axis, relative to the current position. Positive values move the rectangle to the right and down.

    See also

    [translate()](#translate).

---

transposed() → QRect
:   Returns a copy of the rectangle that has its width and height exchanged:

    ```
    # QRect r = {15, 51, 42, 24};
    # r = r.transposed(); // r == {15, 51, 24, 42}
    ```

    See also

    [transposed()](qsize.html#transposed).

---

united(QRect) → QRect
:   Returns the bounding rectangle of this rectangle and the given *rectangle*.

    ![../../_images/qrect-unite.png](../../_images/qrect-unite.png)

    See also

    [intersected()](#intersected).

---

width() → int
:   Returns the width of the rectangle.

    See also

    [setWidth()](#setWidth), [height()](#height), [size()](#size).

---

x() → int
:   Returns the x-coordinate of the rectangle’s left edge. Equivalent to [left()](#left).

    See also

    [setX()](#setX), [y()](#y), [topLeft()](#topLeft).

---

y() → int
:   Returns the y-coordinate of the rectangle’s top edge. Equivalent to [top()](#top).

    See also

    [setY()](#setY), [x()](#x), [topLeft()](#topLeft).

### [Table of Contents](../../index.html)

* QRect
  + [Description](#description)
    - [Rendering](#rendering)
    - [Coordinates](#coordinates)
    - [Constraints](#constraints)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QRect

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QRectF {#qrectf}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QRectF

# QRectF[¶](#qrectf "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QRectF

## Description[¶](#description "Link to this heading")

The QRectF class defines a finite rectangle in the plane using floating point precision.

A rectangle is normally expressed as a top-left corner and a size. The size (width and height) of a QRectF is always equivalent to the mathematical rectangle that forms the basis for its rendering.

A QRectF can be constructed with a set of left, top, width and height coordinates, or from a [QPointF](qpointf.html) and a [QSizeF](qsizef.html). The following code creates two identical rectangles.

```
# QRectF r1(100.0, 200.1, 11.2, 16.3);
# QRectF r2(QPointF(100.0, 200.1), QSizeF(11.2, 16.3));
```

There is also a third constructor creating a QRectF from a [QRect](qrect.html), and a corresponding [toRect()](#toRect) function that returns a [QRect](qrect.html) object based on the values of this rectangle (note that the coordinates in the returned rectangle are rounded to the nearest integer).

The QRectF class provides a collection of functions that return the various rectangle coordinates, and enable manipulation of these. QRectF also provides functions to move the rectangle relative to the various coordinates. In addition there is a [moveTo()](#moveTo) function that moves the rectangle, leaving its top left corner at the given coordinates. Alternatively, the [translate()](#translate) function moves the rectangle the given offset relative to the current position, and the [translated()](#translated) function returns a translated copy of this rectangle.

The [size()](#size) function returns the rectangle’s dimensions as a [QSizeF](qsizef.html). The dimensions can also be retrieved separately using the [width()](#width) and [height()](#height) functions. To manipulate the dimensions use the [setSize()](#setSize), [setWidth()](#setWidth) or [setHeight()](#setHeight) functions. Alternatively, the size can be changed by applying either of the functions setting the rectangle coordinates, for example, [setBottom()](#setBottom) or [setRight()](#setRight).

The [contains()](#contains) function tells whether a given point is inside the rectangle or not, and the [intersects()](#intersects) function returns `true` if this rectangle intersects with a given rectangle (otherwise false). The QRectF class also provides the [intersected()](#intersected) function which returns the intersection rectangle, and the [united()](#united) function which returns the rectangle that encloses the given rectangle and this:

|  |  |
| --- | --- |
| ![image-qrect-intersect-png](../../_images/qrect-intersect.png) | ![image-qrect-unite-png](../../_images/qrect-unite.png) |
| [intersected()](#intersected) | [united()](#united) |

The [isEmpty()](#isEmpty) function returns `true` if the rectangle’s width or height is less than, or equal to, 0. Note that an empty rectangle is not valid: The [isValid()](#isValid) function returns `true` if both width and height is larger than 0. A null rectangle ([isNull()](#isNull) == true) on the other hand, has both width and height set to 0.

Note that due to the way [QRect](qrect.html) and QRectF are defined, an empty QRectF is defined in essentially the same way as [QRect](qrect.html).

Finally, QRectF objects can be streamed as well as compared.

### Rendering[¶](#rendering "Link to this heading")

When using an [Antialiasing](../qtgui/qpainter.html#RenderHint-Antialiasing) painter, the boundary line of a QRectF will be rendered symmetrically on both sides of the mathematical rectangle’s boundary line. But when using an aliased painter (the default) other rules apply.

Then, when rendering with a one pixel wide pen the QRectF’s boundary line will be rendered to the right and below the mathematical rectangle’s boundary line.

When rendering with a two pixels wide pen the boundary line will be split in the middle by the mathematical rectangle. This will be the case whenever the pen is set to an even number of pixels, while rendering with a pen with an odd number of pixels, the spare pixel will be rendered to the right and below the mathematical rectangle as in the one pixel case.

|  |  |
| --- | --- |
| ![image-qrect-diagram-zero-png](../../_images/qrect-diagram-zero.png) | ![image-qrectf-diagram-one-png](../../_images/qrectf-diagram-one.png) |
| Logical representation | One pixel wide pen |
| ![image-qrectf-diagram-two-png](../../_images/qrectf-diagram-two.png) | ![image-qrectf-diagram-three-png](../../_images/qrectf-diagram-three.png) |
| Two pixel wide pen | Three pixel wide pen |

### Coordinates[¶](#coordinates "Link to this heading")

The QRectF class provides a collection of functions that return the various rectangle coordinates, and enable manipulation of these. QRectF also provides functions to move the rectangle relative to the various coordinates.

For example: the [bottom()](#bottom), [setBottom()](#setBottom) and [moveBottom()](#moveBottom) functions: [bottom()](#bottom) returns the y-coordinate of the rectangle’s bottom edge, [setBottom()](#setBottom) sets the bottom edge of the rectangle to the given y coordinate (it may change the height, but will never change the rectangle’s top edge) and [moveBottom()](#moveBottom) moves the entire rectangle vertically, leaving the rectangle’s bottom edge at the given y coordinate and its size unchanged.

![../../_images/qrectf-coordinates.png](../../_images/qrectf-coordinates.png)

It is also possible to add offsets to this rectangle’s coordinates using the [adjust()](#adjust) function, as well as retrieve a new rectangle based on adjustments of the original one using the [adjusted()](#adjusted) function. If either of the width and height is negative, use the [normalized()](#normalized) function to retrieve a rectangle where the corners are swapped.

In addition, QRectF provides the [getCoords()](#getCoords) function which extracts the position of the rectangle’s top-left and bottom-right corner, and the [getRect()](#getRect) function which extracts the rectangle’s top-left corner, width and height. Use the [setCoords()](#setCoords) and [setRect()](#setRect) function to manipulate the rectangle’s coordinates and dimensions in one go.

See also

[QRect](qrect.html), [QRegion](../qtgui/qregion.html).

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs a null rectangle.

    See also

    [isNull()](#isNull).

---

\_\_init\_\_([QRect](qrect.html))
:   Constructs a QRectF rectangle from the given [QRect](qrect.html) *rectangle*.

    **Note:** This function, like [toRectF()](qrect.html#toRectF), preserves the [size()](#size) of *rectangle*, not its [bottomRight()](#bottomRight) corner.

    See also

    [toRect()](#toRect), [toRectF()](qrect.html#toRectF).

---

\_\_init\_\_(QRectF)
:   TODO

---

\_\_init\_\_([QPointF](qpointf.html), [QSizeF](qsizef.html))
:   Constructs a rectangle with the given *topLeft* corner and the given *size*.

    See also

    [setTopLeft()](#setTopLeft), [setSize()](#setSize).

---

\_\_init\_\_([QPointF](qpointf.html), [QPointF](qpointf.html))
:   Constructs a rectangle with the given *topLeft* and *bottomRight* corners.

    See also

    [setTopLeft()](#setTopLeft), [setBottomRight()](#setBottomRight).

---

\_\_init\_\_(float, float, float, float)
:   Constructs a rectangle with (*x*, *y*) as its top-left corner and the given *width* and *height*.

    See also

    [setRect()](#setRect).

---

\_\_add\_\_([QMarginsF](qmarginsf.html)) → QRectF
:   TODO

---

adjust(float, float, float, float)
:   Adds *dx1*, *dy1*, *dx2* and *dy2* respectively to the existing coordinates of the rectangle.

    See also

    [adjusted()](#adjusted), [setRect()](#setRect).

---

adjusted(float, float, float, float) → QRectF
:   Returns a new rectangle with *dx1*, *dy1*, *dx2* and *dy2* added respectively to the existing coordinates of this rectangle.

    See also

    [adjust()](#adjust).

---

\_\_and\_\_(QRectF) → QRectF
:   TODO

---

\_\_bool\_\_() → int
:   TODO

---

bottom() → float
:   Returns the y-coordinate of the rectangle’s bottom edge.

    See also

    [setBottom()](#setBottom), [bottomLeft()](#bottomLeft), [bottomRight()](#bottomRight).

---

bottomLeft() → [QPointF](qpointf.html)
:   Returns the position of the rectangle’s bottom-left corner.

    See also

    [setBottomLeft()](#setBottomLeft), [bottom()](#bottom), [left()](#left).

---

bottomRight() → [QPointF](qpointf.html)
:   Returns the position of the rectangle’s bottom-right corner.

    See also

    [setBottomRight()](#setBottomRight), [bottom()](#bottom), [right()](#right).

---

center() → [QPointF](qpointf.html)
:   Returns the center point of the rectangle.

    See also

    [moveCenter()](#moveCenter).

---

\_\_contains\_\_([QPointF](qpointf.html)) → int
:   TODO

---

\_\_contains\_\_(QRectF) → int
:   TODO

---

contains([QPointF](qpointf.html)) → bool
:   Returns `true` if the given *point* is inside or on the edge of the rectangle; otherwise returns `false`.

    See also

    [intersects()](#intersects).

---

contains(QRectF) → bool
:   Returns `true` if the given *rectangle* is inside this rectangle; otherwise returns `false`.

---

contains(float, float) → bool
:   Returns `true` if the point (*x*, *y*) is inside or on the edge of the rectangle; otherwise returns `false`.

---

\_\_eq\_\_([QRect](qrect.html)) → bool
:   TODO

---

\_\_eq\_\_(QRectF) → bool
:   TODO

---

getCoords() → (float, float, float, float)
:   Extracts the position of the rectangle’s top-left corner to \**x1* and \**y1*, and the position of the bottom-right corner to \**x2* and \**y2*.

    See also

    [setCoords()](#setCoords), [getRect()](#getRect).

---

getRect() → (float, float, float, float)
:   Extracts the position of the rectangle’s top-left corner to \**x* and \**y*, and its dimensions to \**width* and \**height*.

    See also

    [setRect()](#setRect), [getCoords()](#getCoords).

---

height() → float
:   Returns the height of the rectangle.

    See also

    [setHeight()](#setHeight), [width()](#width), [size()](#size).

---

\_\_iadd\_\_([QMarginsF](qmarginsf.html)) → QRectF
:   TODO

---

\_\_iand\_\_(QRectF) → QRectF
:   TODO

---

intersected(QRectF) → QRectF
:   Returns the intersection of this rectangle and the given *rectangle*. Note that `r.intersected(s)` is equivalent to `r & s`.

    ![../../_images/qrect-intersect.png](../../_images/qrect-intersect.png)

    See also

    [intersects()](#intersects), [united()](#united), operator&=().

---

intersects(QRectF) → bool
:   Returns `true` if this rectangle intersects with the given *rectangle* (i.e. there is a non-empty area of overlap between them), otherwise returns `false`.

    The intersection rectangle can be retrieved using the [intersected()](#intersected) function.

    See also

    [contains()](#contains).

---

\_\_ior\_\_(QRectF) → QRectF
:   TODO

---

isEmpty() → bool
:   Returns `true` if the rectangle is empty, otherwise returns `false`.

    An empty rectangle has [width()](#width) <= 0 or [height()](#height) <= 0. An empty rectangle is not valid (i.e., == ![isValid()](#isValid)).

    Use the [normalized()](#normalized) function to retrieve a rectangle where the corners are swapped.

    See also

    [isNull()](#isNull), [isValid()](#isValid), [normalized()](#normalized).

---

isNull() → bool
:   Returns `true` if the rectangle is a null rectangle, otherwise returns `false`.

    A null rectangle has both the width and the height set to 0. A null rectangle is also empty, and hence not valid.

    See also

    [isEmpty()](#isEmpty), [isValid()](#isValid).

---

\_\_isub\_\_([QMarginsF](qmarginsf.html)) → QRectF
:   TODO

---

isValid() → bool
:   Returns `true` if the rectangle is valid, otherwise returns `false`.

    A valid rectangle has a [width()](#width) > 0 and [height()](#height) > 0. Note that non-trivial operations like intersections are not defined for invalid rectangles. A valid rectangle is not empty (i.e., == ![isEmpty()](#isEmpty)).

    See also

    [isNull()](#isNull), [isEmpty()](#isEmpty), [normalized()](#normalized).

---

left() → float
:   Returns the x-coordinate of the rectangle’s left edge. Equivalent to [x()](#x).

    See also

    [setLeft()](#setLeft), [topLeft()](#topLeft), [bottomLeft()](#bottomLeft).

---

marginsAdded([QMarginsF](qmarginsf.html)) → QRectF
:   Returns a rectangle grown by the *margins*.

    See also

    operator+=(), [marginsRemoved()](#marginsRemoved), operator-=().

---

marginsRemoved([QMarginsF](qmarginsf.html)) → QRectF
:   Removes the *margins* from the rectangle, shrinking it.

    See also

    [marginsAdded()](#marginsAdded), operator+=(), operator-=().

---

moveBottom(float)
:   Moves the rectangle vertically, leaving the rectangle’s bottom edge at the given finite *y* coordinate. The rectangle’s size is unchanged.

    See also

    [bottom()](#bottom), [setBottom()](#setBottom), [moveTop()](#moveTop).

---

moveBottomLeft([QPointF](qpointf.html))
:   Moves the rectangle, leaving the bottom-left corner at the given *position*. The rectangle’s size is unchanged.

    See also

    [setBottomLeft()](#setBottomLeft), [moveBottom()](#moveBottom), [moveLeft()](#moveLeft).

---

moveBottomRight([QPointF](qpointf.html))
:   Moves the rectangle, leaving the bottom-right corner at the given *position*. The rectangle’s size is unchanged.

    See also

    [setBottomRight()](#setBottomRight), [moveBottom()](#moveBottom), [moveRight()](#moveRight).

---

moveCenter([QPointF](qpointf.html))
:   Moves the rectangle, leaving the center point at the given *position*. The rectangle’s size is unchanged.

    See also

    [center()](#center).

---

moveLeft(float)
:   Moves the rectangle horizontally, leaving the rectangle’s left edge at the given finite *x* coordinate. The rectangle’s size is unchanged.

    See also

    [left()](#left), [setLeft()](#setLeft), [moveRight()](#moveRight).

---

moveRight(float)
:   Moves the rectangle horizontally, leaving the rectangle’s right edge at the given finite *x* coordinate. The rectangle’s size is unchanged.

    See also

    [right()](#right), [setRight()](#setRight), [moveLeft()](#moveLeft).

---

moveTo([QPointF](qpointf.html))
:   Moves the rectangle, leaving the top-left corner at the given *position*.

---

moveTo(float, float)
:   Moves the rectangle, leaving the top-left corner at the given position (*x*, *y*). The rectangle’s size is unchanged.

    See also

    [translate()](#translate), [moveTopLeft()](#moveTopLeft).

---

moveTop(float)
:   Moves the rectangle vertically, leaving the rectangle’s top line at the given finite *y* coordinate. The rectangle’s size is unchanged.

    See also

    [top()](#top), [setTop()](#setTop), [moveBottom()](#moveBottom).

---

moveTopLeft([QPointF](qpointf.html))
:   Moves the rectangle, leaving the top-left corner at the given *position*. The rectangle’s size is unchanged.

    See also

    [setTopLeft()](#setTopLeft), [moveTop()](#moveTop), [moveLeft()](#moveLeft).

---

moveTopRight([QPointF](qpointf.html))
:   Moves the rectangle, leaving the top-right corner at the given *position*. The rectangle’s size is unchanged.

    See also

    [setTopRight()](#setTopRight), [moveTop()](#moveTop), [moveRight()](#moveRight).

---

\_\_ne\_\_([QRect](qrect.html)) → bool
:   TODO

---

\_\_ne\_\_(QRectF) → bool
:   TODO

---

normalized() → QRectF
:   Returns a normalized rectangle; i.e., a rectangle that has a non-negative width and height.

    If [width()](#width) < 0 the function swaps the left and right corners, and it swaps the top and bottom corners if [height()](#height) < 0.

    See also

    [isValid()](#isValid), [isEmpty()](#isEmpty).

---

\_\_or\_\_(QRectF) → QRectF
:   TODO

---

\_\_repr\_\_() → str
:   TODO

---

right() → float
:   Returns the x-coordinate of the rectangle’s right edge.

    See also

    [setRight()](#setRight), [topRight()](#topRight), [bottomRight()](#bottomRight).

---

setBottom(float)
:   Sets the bottom edge of the rectangle to the given finite *y* coordinate. May change the height, but will never change the top edge of the rectangle.

    See also

    [bottom()](#bottom), [moveBottom()](#moveBottom).

---

setBottomLeft([QPointF](qpointf.html))
:   Set the bottom-left corner of the rectangle to the given *position*. May change the size, but will never change the top-right corner of the rectangle.

    See also

    [bottomLeft()](#bottomLeft), [moveBottomLeft()](#moveBottomLeft).

---

setBottomRight([QPointF](qpointf.html))
:   Set the bottom-right corner of the rectangle to the given *position*. May change the size, but will never change the top-left corner of the rectangle.

    See also

    [bottomRight()](#bottomRight), [moveBottomRight()](#moveBottomRight).

---

setCoords(float, float, float, float)
:   Sets the coordinates of the rectangle’s top-left corner to (*x1*, *y1*), and the coordinates of its bottom-right corner to (*x2*, *y2*).

    See also

    [getCoords()](#getCoords), [setRect()](#setRect).

---

setHeight(float)
:   Sets the height of the rectangle to the given finite *height*. The bottom edge is changed, but not the top one.

    See also

    [height()](#height), [setSize()](#setSize).

---

setLeft(float)
:   Sets the left edge of the rectangle to the given finite *x* coordinate. May change the width, but will never change the right edge of the rectangle.

    Equivalent to [setX()](#setX).

    See also

    [left()](#left), [moveLeft()](#moveLeft).

---

setRect(float, float, float, float)
:   Sets the coordinates of the rectangle’s top-left corner to (*x*, *y*), and its size to the given *width* and *height*.

    See also

    [getRect()](#getRect), [setCoords()](#setCoords).

---

setRight(float)
:   Sets the right edge of the rectangle to the given finite *x* coordinate. May change the width, but will never change the left edge of the rectangle.

    See also

    [right()](#right), [moveRight()](#moveRight).

---

setSize([QSizeF](qsizef.html))
:   Sets the size of the rectangle to the given finite *size*. The top-left corner is not moved.

    See also

    [size()](#size), [setWidth()](#setWidth), [setHeight()](#setHeight).

---

setTop(float)
:   Sets the top edge of the rectangle to the given finite *y* coordinate. May change the height, but will never change the bottom edge of the rectangle.

    Equivalent to [setY()](#setY).

    See also

    [top()](#top), [moveTop()](#moveTop).

---

setTopLeft([QPointF](qpointf.html))
:   Set the top-left corner of the rectangle to the given *position*. May change the size, but will never change the bottom-right corner of the rectangle.

    See also

    [topLeft()](#topLeft), [moveTopLeft()](#moveTopLeft).

---

setTopRight([QPointF](qpointf.html))
:   Set the top-right corner of the rectangle to the given *position*. May change the size, but will never change the bottom-left corner of the rectangle.

    See also

    [topRight()](#topRight), [moveTopRight()](#moveTopRight).

---

setWidth(float)
:   Sets the width of the rectangle to the given finite *width*. The right edge is changed, but not the left one.

    See also

    [width()](#width), [setSize()](#setSize).

---

setX(float)
:   Sets the left edge of the rectangle to the given finite *x* coordinate. May change the width, but will never change the right edge of the rectangle.

    Equivalent to [setLeft()](#setLeft).

    See also

    [x()](#x), [setY()](#setY), [setTopLeft()](#setTopLeft).

---

setY(float)
:   Sets the top edge of the rectangle to the given finite *y* coordinate. May change the height, but will never change the bottom edge of the rectangle.

    Equivalent to [setTop()](#setTop).

    See also

    [y()](#y), [setX()](#setX), [setTopLeft()](#setTopLeft).

---

size() → [QSizeF](qsizef.html)
:   Returns the size of the rectangle.

    See also

    [setSize()](#setSize), [width()](#width), [height()](#height).

---

\_\_sub\_\_([QMarginsF](qmarginsf.html)) → QRectF
:   TODO

---

toAlignedRect() → [QRect](qrect.html)
:   Returns a [QRect](qrect.html) based on the values of this rectangle that is the smallest possible integer rectangle that completely contains this rectangle.

    See also

    [toRect()](#toRect).

---

top() → float
:   Returns the y-coordinate of the rectangle’s top edge. Equivalent to [y()](#y).

    See also

    [setTop()](#setTop), [topLeft()](#topLeft), [topRight()](#topRight).

---

topLeft() → [QPointF](qpointf.html)
:   Returns the position of the rectangle’s top-left corner.

    See also

    [setTopLeft()](#setTopLeft), [top()](#top), [left()](#left).

---

topRight() → [QPointF](qpointf.html)
:   Returns the position of the rectangle’s top-right corner.

    See also

    [setTopRight()](#setTopRight), [top()](#top), [right()](#right).

---

toRect() → [QRect](qrect.html)
:   Returns a [QRect](qrect.html) based on the values of this rectangle. Note that the coordinates in the returned rectangle are rounded to the nearest integer.

    See also

    QRectF, [toAlignedRect()](#toAlignedRect), [toRectF()](qrect.html#toRectF).

---

translate([QPointF](qpointf.html))
:   Moves the rectangle *offset*.[x()](qpointf.html#x) along the x axis and *offset*.[y()](qpointf.html#y) along the y axis, relative to the current position.

---

translate(float, float)
:   Moves the rectangle *dx* along the x-axis and *dy* along the y-axis, relative to the current position. Positive values move the rectangle to the right and downwards.

    See also

    [moveTopLeft()](#moveTopLeft), [moveTo()](#moveTo), [translated()](#translated).

---

translated([QPointF](qpointf.html)) → QRectF
:   Returns a copy of the rectangle that is translated *offset*.[x()](qpointf.html#x) along the x axis and *offset*.[y()](qpointf.html#y) along the y axis, relative to the current position.

---

translated(float, float) → QRectF
:   Returns a copy of the rectangle that is translated *dx* along the x axis and *dy* along the y axis, relative to the current position. Positive values move the rectangle to the right and down.

    See also

    [translate()](#translate).

---

transposed() → QRectF
:   Returns a copy of the rectangle that has its width and height exchanged:

    ```
    # QRectF r = {1.5, 5.1, 4.2, 2.4};
    # r = r.transposed(); // r == {1.5, 5.1, 2.4, 4.2}
    ```

    See also

    [transposed()](qsizef.html#transposed).

---

united(QRectF) → QRectF
:   Returns the bounding rectangle of this rectangle and the given *rectangle*.

    ![../../_images/qrect-unite.png](../../_images/qrect-unite.png)

    See also

    [intersected()](#intersected).

---

width() → float
:   Returns the width of the rectangle.

    See also

    [setWidth()](#setWidth), [height()](#height), [size()](#size).

---

x() → float
:   Returns the x-coordinate of the rectangle’s left edge. Equivalent to [left()](#left).

    See also

    [setX()](#setX), [y()](#y), [topLeft()](#topLeft).

---

y() → float
:   Returns the y-coordinate of the rectangle’s top edge. Equivalent to [top()](#top).

    See also

    [setY()](#setY), [x()](#x), [topLeft()](#topLeft).

### [Table of Contents](../../index.html)

* QRectF
  + [Description](#description)
    - [Rendering](#rendering)
    - [Coordinates](#coordinates)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QRectF

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QSize {#qsize}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QSize

# QSize[¶](#qsize "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QSize

## Description[¶](#description "Link to this heading")

The QSize class defines the size of a two-dimensional object using integer point precision.

A size is specified by a [width()](#width) and a [height()](#height). It can be set in the constructor and changed using the [setWidth()](#setWidth), [setHeight()](#setHeight), or [scale()](#scale) functions, or using arithmetic operators. A size can also be manipulated directly by retrieving references to the width and height using the rwidth() and rheight() functions. Finally, the width and height can be swapped using the [transpose()](#transpose) function.

The [isValid()](#isValid) function determines if a size is valid (a valid size has both width and height greater than or equal to zero). The [isEmpty()](#isEmpty) function returns `true` if either of the width and height is less than, or equal to, zero, while the [isNull()](#isNull) function returns `true` only if both the width and the height is zero.

Use the [expandedTo()](#expandedTo) function to retrieve a size which holds the maximum height and width of *this* size and a given size. Similarly, the [boundedTo()](#boundedTo) function returns a size which holds the minimum height and width of *this* size and a given size.

QSize objects can be streamed as well as compared.

See also

[QSizeF](qsizef.html), [QPoint](qpoint.html), [QRect](qrect.html).

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs a size with an invalid width and height (i.e., [isValid()](#isValid) returns `false`).

    See also

    [isValid()](#isValid).

---

\_\_init\_\_(QSize)
:   TODO

---

\_\_init\_\_(int, int)
:   Constructs a size with the given *width* and *height*.

    See also

    [setWidth()](#setWidth), [setHeight()](#setHeight).

---

\_\_add\_\_(QSize) → QSize
:   TODO

---

\_\_bool\_\_() → int
:   TODO

---

boundedTo(QSize) → QSize
:   Returns a size holding the minimum width and height of this size and the given *otherSize*.

    See also

    [expandedTo()](#expandedTo), [scale()](#scale).

---

\_\_eq\_\_([QSizeF](qsizef.html)) → bool
:   TODO

---

\_\_eq\_\_(QSize) → bool
:   TODO

---

expandedTo(QSize) → QSize
:   Returns a size holding the maximum width and height of this size and the given *otherSize*.

    See also

    [boundedTo()](#boundedTo), [scale()](#scale).

---

grownBy([QMargins](qmargins.html)) → QSize
:   TODO

---

\_\_hash\_\_() → int
:   TODO

---

height() → int
:   Returns the height.

    See also

    [width()](#width), [setHeight()](#setHeight).

---

\_\_iadd\_\_(QSize) → QSize
:   TODO

---

\_\_imul\_\_(float) → QSize
:   TODO

---

isEmpty() → bool
:   Returns `true` if either of the width and height is less than or equal to 0; otherwise returns `false`.

    See also

    [isNull()](#isNull), [isValid()](#isValid).

---

isNull() → bool
:   Returns `true` if both the width and height is 0; otherwise returns false.

    See also

    [isValid()](#isValid), [isEmpty()](#isEmpty).

---

\_\_isub\_\_(QSize) → QSize
:   TODO

---

isValid() → bool
:   Returns `true` if both the width and height is equal to or greater than 0; otherwise returns `false`.

    See also

    [isNull()](#isNull), [isEmpty()](#isEmpty).

---

\_\_itruediv\_\_(float) → QSize
:   TODO

---

\_\_mul\_\_(float) → QSize
:   TODO

---

\_\_ne\_\_([QSizeF](qsizef.html)) → bool
:   TODO

---

\_\_ne\_\_(QSize) → bool
:   TODO

---

\_\_repr\_\_() → str
:   TODO

---

\_\_rmul\_\_(float) → QSize
:   TODO

---

scale(QSize, [AspectRatioMode](qt.html#AspectRatioMode))
:   Scales the size to a rectangle with the given *size*, according to the specified *mode*.

---

scale(int, int, [AspectRatioMode](qt.html#AspectRatioMode))
:   Scales the size to a rectangle with the given *width* and *height*, according to the specified *mode*:

    * If *mode* is [IgnoreAspectRatio](qt.html#AspectRatioMode-IgnoreAspectRatio), the size is set to (*width*, *height*).
    * If *mode* is [KeepAspectRatio](qt.html#AspectRatioMode-KeepAspectRatio), the current size is scaled to a rectangle as large as possible inside (*width*, *height*), preserving the aspect ratio.
    * If *mode* is [KeepAspectRatioByExpanding](qt.html#AspectRatioMode-KeepAspectRatioByExpanding), the current size is scaled to a rectangle as small as possible outside (*width*, *height*), preserving the aspect ratio.

    Example:

    ```
    # QSize t1(10, 12);
    # t1.scale(60, 60, Qt::IgnoreAspectRatio);
    # // t1 is (60, 60)

    # QSize t2(10, 12);
    # t2.scale(60, 60, Qt::KeepAspectRatio);
    # // t2 is (50, 60)

    # QSize t3(10, 12);
    # t3.scale(60, 60, Qt::KeepAspectRatioByExpanding);
    # // t3 is (60, 72)
    ```

    See also

    [setWidth()](#setWidth), [setHeight()](#setHeight), [scaled()](#scaled).

---

scaled(QSize, [AspectRatioMode](qt.html#AspectRatioMode)) → QSize
:   Return a size scaled to a rectangle with the given size *s*, according to the specified *mode*.

---

scaled(int, int, [AspectRatioMode](qt.html#AspectRatioMode)) → QSize
:   Return a size scaled to a rectangle with the given *width* and *height*, according to the specified *mode*.

    See also

    [scale()](#scale).

---

setHeight(int)
:   Sets the height to the given *height*.

    See also

    rheight(), [height()](#height), [setWidth()](#setWidth).

---

setWidth(int)
:   Sets the width to the given *width*.

    See also

    rwidth(), [width()](#width), [setHeight()](#setHeight).

---

shrunkBy([QMargins](qmargins.html)) → QSize
:   TODO

---

\_\_sub\_\_(QSize) → QSize
:   TODO

---

toSizeF() → [QSizeF](qsizef.html)
:   Returns this size as a size with floating point accuracy.

    See also

    [toSize()](qsizef.html#toSize).

---

transpose()
:   Swaps the width and height values.

    See also

    [setWidth()](#setWidth), [setHeight()](#setHeight), [transposed()](#transposed).

---

transposed() → QSize
:   Returns a QSize with width and height swapped.

    See also

    [transpose()](#transpose).

---

\_\_truediv\_\_(float) → QSize
:   TODO

---

width() → int
:   Returns the width.

    See also

    [height()](#height), [setWidth()](#setWidth).

### [Table of Contents](../../index.html)

* QSize
  + [Description](#description)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QSize

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QSizeF {#qsizef}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QSizeF

# QSizeF[¶](#qsizef "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QSizeF

## Description[¶](#description "Link to this heading")

The QSizeF class defines the size of a two-dimensional object using floating point precision.

A size is specified by a [width()](#width) and a [height()](#height). It can be set in the constructor and changed using the [setWidth()](#setWidth), [setHeight()](#setHeight), or [scale()](#scale) functions, or using arithmetic operators. A size can also be manipulated directly by retrieving references to the width and height using the rwidth() and rheight() functions. Finally, the width and height can be swapped using the [transpose()](#transpose) function.

The [isValid()](#isValid) function determines if a size is valid. A valid size has both width and height greater than or equal to zero. The [isEmpty()](#isEmpty) function returns `true` if either of the width and height is *less* than (or equal to) zero, while the [isNull()](#isNull) function returns `true` only if both the width and the height is zero.

Use the [expandedTo()](#expandedTo) function to retrieve a size which holds the maximum height and width of this size and a given size. Similarly, the [boundedTo()](#boundedTo) function returns a size which holds the minimum height and width of this size and a given size.

The QSizeF class also provides the [toSize()](#toSize) function returning a [QSize](qsize.html) copy of this size, constructed by rounding the width and height to the nearest integers.

QSizeF objects can be streamed as well as compared.

See also

[QSize](qsize.html), [QPointF](qpointf.html), [QRectF](qrectf.html).

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs an invalid size.

    See also

    [isValid()](#isValid).

---

\_\_init\_\_([QSize](qsize.html))
:   Constructs a size with floating point accuracy from the given *size*.

    See also

    [toSize()](#toSize), [toSizeF()](qsize.html#toSizeF).

---

\_\_init\_\_(QSizeF)
:   TODO

---

\_\_init\_\_(float, float)
:   Constructs a size with the given finite *width* and *height*.

---

\_\_add\_\_(QSizeF) → QSizeF
:   TODO

---

\_\_bool\_\_() → int
:   TODO

---

boundedTo(QSizeF) → QSizeF
:   Returns a size holding the minimum width and height of this size and the given *otherSize*.

    See also

    [expandedTo()](#expandedTo), [scale()](#scale).

---

\_\_eq\_\_([QSize](qsize.html)) → bool
:   TODO

---

\_\_eq\_\_(QSizeF) → bool
:   TODO

---

expandedTo(QSizeF) → QSizeF
:   Returns a size holding the maximum width and height of this size and the given *otherSize*.

    See also

    [boundedTo()](#boundedTo), [scale()](#scale).

---

grownBy([QMarginsF](qmarginsf.html)) → QSizeF
:   TODO

---

height() → float
:   Returns the height.

    See also

    [width()](#width), [setHeight()](#setHeight).

---

\_\_iadd\_\_(QSizeF) → QSizeF
:   TODO

---

\_\_imul\_\_(float) → QSizeF
:   TODO

---

isEmpty() → bool
:   Returns `true` if either of the width and height is less than or equal to 0; otherwise returns `false`.

    See also

    [isNull()](#isNull), [isValid()](#isValid).

---

isNull() → bool
:   Returns `true` if both the width and height are 0.0 (ignoring the sign); otherwise returns `false`.

    See also

    [isValid()](#isValid), [isEmpty()](#isEmpty).

---

\_\_isub\_\_(QSizeF) → QSizeF
:   TODO

---

isValid() → bool
:   Returns `true` if both the width and height is equal to or greater than 0; otherwise returns `false`.

    See also

    [isNull()](#isNull), [isEmpty()](#isEmpty).

---

\_\_itruediv\_\_(float) → QSizeF
:   TODO

---

\_\_mul\_\_(float) → QSizeF
:   TODO

---

\_\_ne\_\_([QSize](qsize.html)) → bool
:   TODO

---

\_\_ne\_\_(QSizeF) → bool
:   TODO

---

\_\_repr\_\_() → str
:   TODO

---

\_\_rmul\_\_(float) → QSizeF
:   TODO

---

scale(QSizeF, [AspectRatioMode](qt.html#AspectRatioMode))
:   Scales the size to a rectangle with the given *size*, according to the specified *mode*.

---

scale(float, float, [AspectRatioMode](qt.html#AspectRatioMode))
:   Scales the size to a rectangle with the given *width* and *height*, according to the specified *mode*.

    * If *mode* is [IgnoreAspectRatio](qt.html#AspectRatioMode-IgnoreAspectRatio), the size is set to (*width*, *height*).
    * If *mode* is [KeepAspectRatio](qt.html#AspectRatioMode-KeepAspectRatio), the current size is scaled to a rectangle as large as possible inside (*width*, *height*), preserving the aspect ratio.
    * If *mode* is [KeepAspectRatioByExpanding](qt.html#AspectRatioMode-KeepAspectRatioByExpanding), the current size is scaled to a rectangle as small as possible outside (*width*, *height*), preserving the aspect ratio.

    Example:

    ```
    # QSizeF t1(10, 12);
    # t1.scale(60, 60, Qt::IgnoreAspectRatio);
    # // t1 is (60, 60)

    # QSizeF t2(10, 12);
    # t2.scale(60, 60, Qt::KeepAspectRatio);
    # // t2 is (50, 60)

    # QSizeF t3(10, 12);
    # t3.scale(60, 60, Qt::KeepAspectRatioByExpanding);
    # // t3 is (60, 72)
    ```

    See also

    [setWidth()](#setWidth), [setHeight()](#setHeight), [scaled()](#scaled).

---

scaled(QSizeF, [AspectRatioMode](qt.html#AspectRatioMode)) → QSizeF
:   Returns a size scaled to a rectangle with the given size *s*, according to the specified *mode*.

---

scaled(float, float, [AspectRatioMode](qt.html#AspectRatioMode)) → QSizeF
:   Returns a size scaled to a rectangle with the given *width* and *height*, according to the specified *mode*.

    See also

    [scale()](#scale).

---

setHeight(float)
:   Sets the height to the given finite *height*.

    See also

    [height()](#height), rheight(), [setWidth()](#setWidth).

---

setWidth(float)
:   Sets the width to the given finite *width*.

    See also

    [width()](#width), rwidth(), [setHeight()](#setHeight).

---

shrunkBy([QMarginsF](qmarginsf.html)) → QSizeF
:   TODO

---

\_\_sub\_\_(QSizeF) → QSizeF
:   TODO

---

toSize() → [QSize](qsize.html)
:   Returns an integer based copy of this size.

    Note that the coordinates in the returned size will be rounded to the nearest integer.

    See also

    QSizeF, [toSizeF()](qsize.html#toSizeF).

---

transpose()
:   Swaps the width and height values.

    See also

    [setWidth()](#setWidth), [setHeight()](#setHeight), [transposed()](#transposed).

---

transposed() → QSizeF
:   Returns the size with width and height values swapped.

    See also

    [transpose()](#transpose).

---

\_\_truediv\_\_(float) → QSizeF
:   TODO

---

width() → float
:   Returns the width.

    See also

    [height()](#height), [setWidth()](#setWidth).

### [Table of Contents](../../index.html)

* QSizeF
  + [Description](#description)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QSizeF

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

## QTime {#qtime}

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QTime

# QTime[¶](#qtime "Link to this heading")

[PyQt6.QtCore](qtcore-module.html).QTime

## Description[¶](#description "Link to this heading")

The QTime class provides clock time functions.

A QTime object contains a clock time, which it can express as the numbers of hours, minutes, seconds, and milliseconds since midnight. It provides functions for comparing times and for manipulating a time by adding a number of milliseconds. QTime objects should be passed by value rather than by reference to const; they simply package `int`.

QTime uses the 24-hour clock format; it has no concept of AM/PM. Unlike [QDateTime](qdatetime.html), QTime knows nothing about time zones or daylight-saving time (DST).

A QTime object is typically created either by giving the number of hours, minutes, seconds, and milliseconds explicitly, or by using the static function [currentTime()](#currentTime), which creates a QTime object that represents the system’s local time.

The [hour()](#hour), [minute()](#minute), [second()](#second), and [msec()](#msec) functions provide access to the number of hours, minutes, seconds, and milliseconds of the time. The same information is provided in textual format by the [toString()](#toString) function.

The [addSecs()](#addSecs) and [addMSecs()](#addMSecs) functions provide the time a given number of seconds or milliseconds later than a given time. Correspondingly, the number of seconds or milliseconds between two times can be found using [secsTo()](#secsTo) or [msecsTo()](#msecsTo).

QTime provides a full set of operators to compare two QTime objects; an earlier time is considered smaller than a later one; if A.[msecsTo()](#msecsTo)(B) is positive, then A < B.

QTime objects can also be created from a text representation using [fromString()](#fromString) and converted to a string representation using [toString()](#toString). All conversion to and from string formats is done using the C locale. For localized conversions, see [QLocale](qlocale.html).

See also

[QDate](qdate.html), [QDateTime](qdatetime.html).

## Methods[¶](#methods "Link to this heading")

\_\_init\_\_()
:   Constructs a null time object. For a null time, [isNull()](#isNull) returns `true` and [isValid()](#isValid) returns `false`. If you need a zero time, use QTime(0, 0). For the start of a day, see [startOfDay()](qdate.html#startOfDay).

    See also

    [isNull()](#isNull), [isValid()](#isValid).

---

\_\_init\_\_(QTime)
:   TODO

---

\_\_init\_\_(int, int, second: int = 0, msec: int = 0)
:   Constructs a time with hour *h*, minute *m*, seconds *s* and milliseconds *ms*.

    *h* must be in the range 0 to 23, *m* and *s* must be in the range 0 to 59, and *ms* must be in the range 0 to 999.

    See also

    [isValid()](#isValid).

---

addMSecs(int) → QTime
:   Returns a QTime object containing a time *ms* milliseconds later than the time of this object (or earlier if *ms* is negative).

    Note that the time will wrap if it passes midnight. See [addSecs()](#addSecs) for an example.

    Returns a null time if this time is invalid.

    See also

    [addSecs()](#addSecs), [msecsTo()](#msecsTo), [addMSecs()](qdatetime.html#addMSecs).

---

addSecs(int) → QTime
:   Returns a QTime object containing a time *s* seconds later than the time of this object (or earlier if *s* is negative).

    Note that the time will wrap if it passes midnight.

    Returns a null time if this time is invalid.

    Example:

    ```
    # QTime n(14, 0, 0);                // n == 14:00:00
    # QTime t;
    # t = n.addSecs(70);                // t == 14:01:10
    # t = n.addSecs(-70);               // t == 13:58:50
    # t = n.addSecs(10 * 60 * 60 + 5);  // t == 00:00:05
    # t = n.addSecs(-15 * 60 * 60);     // t == 23:00:00
    ```

    See also

    [addMSecs()](#addMSecs), [secsTo()](#secsTo), [addSecs()](qdatetime.html#addSecs).

---

\_\_bool\_\_() → int
:   TODO

---

@staticmethod currentTime() → QTime
:   Returns the current time as reported by the system clock.

    Note that the accuracy depends on the accuracy of the underlying operating system; not all systems provide 1-millisecond accuracy.

    Furthermore, currentTime() only increases within each day; it shall drop by 24 hours each time midnight passes; and, beside this, changes in it may not correspond to elapsed time, if a daylight-saving transition intervenes.

    See also

    [currentDateTime()](qdatetime.html#currentDateTime), [currentDateTimeUtc()](qdatetime.html#currentDateTimeUtc).

---

\_\_eq\_\_(QTime|datetime.time) → bool
:   TODO

---

@staticmethod fromMSecsSinceStartOfDay(int) → QTime
:   Returns a new QTime instance with the time set to the number of *msecs* since the start of the day, i.e. since 00:00:00.

    If *msecs* falls outside the valid range an invalid QTime will be returned.

    See also

    [msecsSinceStartOfDay()](#msecsSinceStartOfDay).

---

@staticmethod fromString(str|None, format: [DateFormat](qt.html#DateFormat) = [TextDate](qt.html#DateFormat-TextDate)) → QTime
:   Returns the time represented in the *string* as a QTime using the *format* given, or an invalid time if this is not possible.

    See also

    [toString()](#toString), [toTime()](qlocale.html#toTime).

---

@staticmethod fromString(str|None, str|None) → QTime
:   Returns the QTime represented by the *string*, using the *format* given, or an invalid time if the string cannot be parsed.

    These expressions may be used for the format:

    | Expression | Output |
    | --- | --- |
    | h | The hour without a leading zero (0 to 23 or 1 to 12 if AM/PM display) |
    | hh | The hour with a leading zero (00 to 23 or 01 to 12 if AM/PM display) |
    | H | The hour without a leading zero (0 to 23, even with AM/PM display) |
    | HH | The hour with a leading zero (00 to 23, even with AM/PM display) |
    | m | The minute without a leading zero (0 to 59) |
    | mm | The minute with a leading zero (00 to 59) |
    | s | The whole second, without any leading zero (0 to 59) |
    | ss | The whole second, with a leading zero where applicable (00 to 59) |
    | z or zz | The fractional part of the second, as would usually follow a decimal point, without requiring trailing zeroes (0 to 999). Thus `"s.z"` matches the seconds with up to three digits of fractional part supplying millisecond precision, without needing trailing zeroes. For example, `"s.z"` would recognize either `"00.250"` or `"0.25"` as representing a time a quarter second into its minute. |
    | zzz | Three digit fractional part of the second, to millisecond precision, including trailing zeroes where applicable (000 to 999). For example, `"ss.zzz"` would reject `"0.25"` but recognize `"00.250"` as representing a time a quarter second into its minute. |
    | AP, A, ap, a, aP or Ap | Either ‘AM’ indicating a time before 12:00 or ‘PM’ for later times, matched case-insensitively. |

    All other input characters will be treated as text. Any non-empty sequence of characters enclosed in single quotes will also be treated (stripped of the quotes) as text and not be interpreted as expressions.

    ```
    # QTime time = QTime::fromString("1mm12car00", "m'mm'hcarss");
    # // time is 12:01.00
    ```

    If the format is not satisfied, an invalid QTime is returned. Expressions that do not expect leading zeroes to be given (h, m, s and z) are greedy. This means that they will use two digits (or three, for z) even if this puts them outside the range of accepted values and leaves too few digits for other sections. For example, the following string could have meant 00:07:10, but the m will grab two digits, resulting in an invalid time:

    ```
    # QTime time = QTime::fromString("00:710", "hh:ms"); // invalid
    ```

    Any field that is not represented in the format will be set to zero. For example:

    ```
    # QTime time = QTime::fromString("1.30", "m.s");
    # // time is 00:01:30.000
    ```

    **Note:** If localized forms of am or pm (the AP, ap, Ap, aP, A or a formats) are to be recognized, use [system()](qlocale.html#system).toTime().

    **Note:** If a format character is repeated more times than the longest expression in the table above using it, this part of the format will be read as several expressions with no separator between them; the longest above, possibly repeated as many times as there are copies of it, ending with a residue that may be a shorter expression. Thus `'HHHHH'` would match `"08088"` or `"080808"` and set the hour to 8; if the time string contained “070809” it would “match” but produce an inconsistent result, leading to an invalid time.

    See also

    [toString()](#toString), [fromString()](qdatetime.html#fromString), [fromString()](qdate.html#fromString), [toTime()](qlocale.html#toTime), [toDateTime()](qlocale.html#toDateTime).

---

\_\_ge\_\_(QTime|datetime.time) → bool
:   TODO

---

\_\_gt\_\_(QTime|datetime.time) → bool
:   TODO

---

\_\_hash\_\_() → int
:   TODO

---

hour() → int
:   Returns the hour part (0 to 23) of the time.

    Returns -1 if the time is invalid.

    See also

    [minute()](#minute), [second()](#second), [msec()](#msec).

---

isNull() → bool
:   Returns `true` if the time is null (i.e., the QTime object was constructed using the default constructor); otherwise returns false. A null time is also an invalid time.

    See also

    [isValid()](#isValid).

---

isValid() → bool
:   Returns `true` if the time is valid; otherwise returns `false`. For example, the time 23:30:55.746 is valid, but 24:12:30 is invalid.

    See also

    [isNull()](#isNull).

---

@staticmethod isValid(int, int, int, msec: int = 0) → bool
:   Returns `true` if the specified time is valid; otherwise returns false.

    The time is valid if *h* is in the range 0 to 23, *m* and *s* are in the range 0 to 59, and *ms* is in the range 0 to 999.

    Example:

    ```
    # QTime::isValid(21, 10, 30); // returns true
    # QTime::isValid(22, 5,  62); // returns false
    ```

---

\_\_le\_\_(QTime|datetime.time) → bool
:   TODO

---

\_\_lt\_\_(QTime|datetime.time) → bool
:   TODO

---

minute() → int
:   Returns the minute part (0 to 59) of the time.

    Returns -1 if the time is invalid.

    See also

    [hour()](#hour), [second()](#second), [msec()](#msec).

---

msec() → int
:   Returns the millisecond part (0 to 999) of the time.

    Returns -1 if the time is invalid.

    See also

    [hour()](#hour), [minute()](#minute), [second()](#second).

---

msecsSinceStartOfDay() → int
:   Returns the number of msecs since the start of the day, i.e. since 00:00:00.

    See also

    [fromMSecsSinceStartOfDay()](#fromMSecsSinceStartOfDay).

---

msecsTo(QTime|datetime.time) → int
:   Returns the number of milliseconds from this time to *t*. If *t* is earlier than this time, the number of milliseconds returned is negative.

    Because QTime measures time within a day and there are 86400 seconds in a day, the result is always between -86400000 and 86400000 ms.

    Returns 0 if either time is invalid.

    See also

    [secsTo()](#secsTo), [addMSecs()](#addMSecs), [msecsTo()](qdatetime.html#msecsTo).

---

\_\_ne\_\_(QTime|datetime.time) → bool
:   TODO

---

\_\_repr\_\_() → str
:   TODO

---

second() → int
:   Returns the second part (0 to 59) of the time.

    Returns -1 if the time is invalid.

    See also

    [hour()](#hour), [minute()](#minute), [msec()](#msec).

---

secsTo(QTime|datetime.time) → int
:   Returns the number of seconds from this time to *t*. If *t* is earlier than this time, the number of seconds returned is negative.

    Because QTime measures time within a day and there are 86400 seconds in a day, the result is always between -86400 and 86400.

    secsTo() does not take into account any milliseconds.

    Returns 0 if either time is invalid.

    See also

    [addSecs()](#addSecs), [secsTo()](qdatetime.html#secsTo).

---

setHMS(int, int, int, msec: int = 0) → bool
:   Sets the time to hour *h*, minute *m*, seconds *s* and milliseconds *ms*.

    *h* must be in the range 0 to 23, *m* and *s* must be in the range 0 to 59, and *ms* must be in the range 0 to 999. Returns `true` if the set time is valid; otherwise returns `false`.

    See also

    [isValid()](#isValid).

---

toPyTime() → datetime.time
:   TODO

---

toString(format: [DateFormat](qt.html#DateFormat) = [TextDate](qt.html#DateFormat-TextDate)) → str
:   Returns the time as a string. The *format* parameter determines the format of the string.

    If *format* is [TextDate](qt.html#DateFormat-TextDate), the string format is HH:mm:ss; e.g. 1 second before midnight would be “23:59:59”.

    If *format* is [ISODate](qt.html#DateFormat-ISODate), the string format corresponds to the ISO 8601 extended specification for representations of dates, represented by HH:mm:ss. To include milliseconds in the ISO 8601 date, use the *format* [ISODateWithMs](qt.html#DateFormat-ISODateWithMs), which corresponds to HH:mm:ss.zzz.

    If the *format* is [RFC2822Date](qt.html#DateFormat-RFC2822Date), the string is formatted in an RFC 2822 compatible way. An example of this formatting is “23:59:20”.

    If the time is invalid, an empty string will be returned.

    See also

    [fromString()](#fromString), [toString()](qdate.html#toString), [toString()](qdatetime.html#toString), [toString()](qlocale.html#toString).

---

toString(str|None) → str
:   TODO

### [Table of Contents](../../index.html)

* QTime
  + [Description](#description)
  + [Methods](#methods)

### Quick search

### Navigation

* [Index](../../genindex.html "General index")
* [Classes](../../sip-classes.html "Index of all classes") |
* [Modules](../../module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](../../index.html) »
* QTime

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Using PyQt6 from the Python Shell {#using-pyqt6-from-the-python-shell}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Using PyQt6 from the Python Shell

# Using PyQt6 from the Python Shell[¶](#using-pyqt6-from-the-python-shell "Link to this heading")

PyQt6 installs an input hook (using `PyOS_InputHook()`) that processes
events when an interactive interpreter is waiting for user input. This means
that you can, for example, create widgets from the Python shell prompt,
interact with them, and still being able to enter other Python commands.

For example, if you enter the following in the Python shell:

```
>>> from PyQt6.QtWidgets import QApplication, QWidget
>>> a = QApplication([])
>>> w = QWidget()
>>> w.show()
>>> w.hide()
>>>
```

The widget would be displayed when `w.show()` was entered and hidden as soon
as `w.hide()` was entered.

The installation of an input hook can cause problems for certain applications
(particularly those that implement a similar feature using different means).
The [QtCore](api/qtcore/qtcore-module.html) module contains the
[pyqtRemoveInputHook()](api/qtcore/qtcore-module.html#pyqtRemoveInputHook) and
[pyqtRestoreInputHook()](api/qtcore/qtcore-module.html#pyqtRestoreInputHook) functions that remove and restore
the input hook respectively.

#### Previous topic

[Support for Pickling](pickle.html "previous chapter")

#### Next topic

[Internationalisation of PyQt6 Applications](i18n.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Using PyQt6 from the Python Shell

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# Internationalisation of PyQt6 Applications {#internationalisation-of-pyqt6-applications}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Internationalisation of PyQt6 Applications

# Internationalisation of PyQt6 Applications[¶](#internationalisation-of-pyqt6-applications "Link to this heading")

PyQt6 and Qt include a comprehensive set of tools for translating applications
into local languages. For a full description, see the Qt Linguist Manual in
the Qt documentation.

The process of internationalising an application comprises the following
steps.

* The programmer uses **pylupdate6** to create or update a `.ts`
  translation file for each human language that the application is to be
  translated into. A `.ts` file is an XML file that contains the
  messages to be translated and the corresponding translations that have
  already been made. **pylupdate6** can be run any number of times
  during development to update the `.ts` files with the latest messages
  for translation.
* The translator uses Qt Linguist to update the `.ts` files with
  translations of the messages.
* The release manager then uses Qt’s **lrelease** utility to convert the
  `.ts` files to `.qm` files which are compact binary equivalents
  used by the application. If an application cannot find an appropriate
  `.qm` file, or a particular message hasn’t been translated, then the
  messages used in the original source code are used instead.

## **pylupdate6**[¶](#pylupdate6 "Link to this heading")

The **pylupdate6** utility is a command line interface to the
[lupdate](api/lupdate/lupdate-module.html) module. The command has the following syntax:

```
pylupdate6 [options] --ts .ts-file [--ts .ts-file ...] file [file ...]
```

The full set of command line options is:

-h, --help[¶](#cmdoption-pylupdate6-h "Link to this definition")
:   A help message is written to `stdout`.

-V, --version[¶](#cmdoption-pylupdate6-V "Link to this definition")
:   The version number is written to `stdout`.

--exclude PATTERN[¶](#cmdoption-pylupdate6-exclude "Link to this definition")
:   a UNIX shell-style pattern that is matched against the source files found
    when recursively searching a directory. If a source file matches then it
    is excluded. This option may be specified any number of times.

--no-obsolete[¶](#cmdoption-pylupdate6-no-obsolete "Link to this definition")
:   All obsolete messages from the translation files will be discarded. An
    obsolete message is one that was found by a previous invocation of
    **pylupdate6** but has not been found by this invocation. By
    default obsolete messages are retained and marked as such in the
    translation file.

--no-summary[¶](#cmdoption-pylupdate6-no-summary "Link to this definition")
:   A summary of updates to the translation files will not be displayed on
    `stdout`.

--ts FILE[¶](#cmdoption-pylupdate6-ts "Link to this definition")
:   The name of a translation file that is created or updated with the
    translatable messages extracted from the source files. This option may be
    specified any number of times.

--verbose[¶](#cmdoption-pylupdate6-verbose "Link to this definition")
:   Progress messages will be displayed to `stdout`.

The rest of the command line are the names of the `.py` Python source
files and `.ui` Designer files from which **pylupdate6** extracts
messages from.

Note

Each time you invoke **pylupdate6** you should be careful to specify
all the `.py` and `.ui` files that make up your application and
not just the ones that have changed. Otherwise any messages that appear in
files that you don’t specify will be marked as obsolete.

## Differences Between PyQt6 and Qt[¶](#differences-between-pyqt6-and-qt "Link to this heading")

Qt implements internationalisation support through the
[QTranslator](api/qtcore/qtranslator.html) class, and the
[QT\_TRANSLATE\_NOOP()](api/qtcore/qtcore-module.html#QT_TRANSLATE_NOOP),
[translate()](api/qtcore/qcoreapplication.html#translate),
[QT\_TR\_NOOP()](api/qtcore/qtcore-module.html#QT_TR_NOOP) and [tr()](api/qtcore/qobject.html#tr)
methods. Usually [tr()](api/qtcore/qobject.html#tr) is used to obtain the
correct translation of a message. The translation process uses a message
context to allow the same message to be translated differently. In Qt
[tr()](api/qtcore/qobject.html#tr) is actually generated by **moc** and
uses the hardcoded class name as the context. On the other hand,
translate allows the context to be
specified explicitly.

Unfortunately, because of the way Qt implements
[tr()](api/qtcore/qobject.html#tr) it is not possible for PyQt6 to exactly
reproduce its behaviour. The PyQt6 implementation of
[tr()](api/qtcore/qobject.html#tr) uses the class name of the instance as the
context. The key difference, and the source of potential problems, is that the
context is determined dynamically in PyQt6, but is hardcoded in Qt. In other
words, the context of a translation may change depending on an instance’s class
hierarchy. For example:

```
class A(QObject):
    def hello(self):
        return self.tr("Hello")

class B(A):
    pass

a = A()
a.hello()

b = B()
b.hello()
```

In the above the message is translated by `a.hello()` using a context of
`A`, and by `b.hello()` using a context of `B`. In the equivalent C++
version the context would be `A` in both cases.

The PyQt6 behaviour is unsatisfactory and may be changed in the future. It is
recommended that [translate()](api/qtcore/qcoreapplication.html#translate) be used in
preference to [tr()](api/qtcore/qobject.html#tr). This is guaranteed to work
with current and future versions of PyQt6 and makes it much easier to share
message files between Python and C++ code. Below is the alternative
implementation of `A` that uses
[translate()](api/qtcore/qcoreapplication.html#translate):

```
class A(QObject):
    def hello(self):
        return QCoreApplication.translate('A', "Hello")
```

## Support for Translator Comments[¶](#support-for-translator-comments "Link to this heading")

In the same way that Qt’s **lupdate** can extract C++ comments aimed at
the translator, **pylupdate6** can extract similarly formatted Python
comments. Specifically:

> **#:** introduces a general comment for the translator
>
> **#=** introduces a unique identifier attached to the message
>
> **#~** introduces a field name and field contents attached to the message.

### [Table of Contents](index.html)

* Internationalisation of PyQt6 Applications
  + [**pylupdate6**](#pylupdate6)
  + [Differences Between PyQt6 and Qt](#differences-between-pyqt6-and-qt)
  + [Support for Translator Comments](#support-for-translator-comments)

#### Previous topic

[Using PyQt6 from the Python Shell](python_shell.html "previous chapter")

#### Next topic

[DBus Support](dbus.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* Internationalisation of PyQt6 Applications

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# DBus Support {#dbus-support}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* DBus Support

# DBus Support[¶](#dbus-support "Link to this heading")

PyQt6 provides two different modules that implement support for DBus. The
[QtDBus](api/qtdbus/qtdbus-module.html) module provides wrappers for the standard Qt DBus
classes. The `dbus.mainloop.pyqt6` module adds support for the Qt event loop
to the standard `dbus-python` Python module.

## [QtDBus](api/qtdbus/qtdbus-module.html)[¶](#qtdbus "Link to this heading")

The [QtDBus](api/qtdbus/qtdbus-module.html) module is used in a similar way to the C++ library
it wraps. The main difference is in the way it supports the demarshalling of
DBus structures. C++ relies on the template-based registration of types using
`qDBusRegisterMetaType()` which isn’t possible from Python. Instead a slot
that accepts a DBus structure in an argument should specify a slot with a
single [QDBusMessage](api/qtdbus/qdbusmessage.html) argument. The implementation of
the slot should then extract the arguments from the message using its
`arguments()` method.

For example, say we have a DBus method called `setColors()` that has a single
argument that is an array of structures of three integers (red, green and
blue). The DBus signature of the argument would then be `a(iii)`. In C++
you would typically define a class to hold the red, green and blue values and
so your code would include the following (incomplete) fragments:

```
struct Color
{
    int red;
    int green;
    int blue;
};
Q_DECLARE_METATYPE(Color)

qDBusRegisterMetaType<Color>();

class ServerAdaptor : public QDBusAbstractAdaptor
{
    Q_OBJECT

public slots:
    void setColors(QList<const Color &> colors);
};
```

The Python version is, of course, much simpler:

```
class ServerAdaptor(QDBusAbstractAdaptor):

    @pyqtSlot(QDBusMessage)
    def setColors(self, message):
        # Get the single argument.
        colors = message.arguments()[0]

        # The argument will be a list of 3-tuples of ints.
        for red, green, blue in colors:
            print("RGB:", red, green, blue)
```

Note that this technique can be used for arguments of any type, it is only
require if DBus structures are involved.

## dbus.mainloop.pyqt6[¶](#dbus-mainloop-pyqt6 "Link to this heading")

The `dbus.mainloop.pyqt6` module provides support for the Qt event loop to
`dbus-python`. The module’s API is almost identical to that of the
`dbus.mainloop.glib` modules that provides support for the GLib event loop.

The `dbus.mainloop.pyqt6` module contains the following function.

DBusQtMainLoop(*set\_as\_default=False*)[¶](#DBusQtMainLoop "Link to this definition")
:   Create a `dbus.mainloop.NativeMainLoop` object that uses the the Qt event
    loop.

    Parameters:
    :   **set\_as\_default** – is optionally set to make the main loop instance the default for all
        new Connection and Bus instances. It may only be specified as a
        keyword argument, and not as a positional argument.

The following code fragment is all that is normally needed to set up the
standard `dbus-python` language bindings package to be used with PyQt6:

```
from dbus.mainloop.pyqt6 import DBusQtMainLoop

DBusQtMainLoop(set_as_default=True)
```

### [Table of Contents](index.html)

* DBus Support
  + [QtDBus](#qtdbus)
  + [dbus.mainloop.pyqt6](#dbus-mainloop-pyqt6)
    - [`DBusQtMainLoop()`](#DBusQtMainLoop)

#### Previous topic

[Internationalisation of PyQt6 Applications](i18n.html "previous chapter")

#### Next topic

[The PyQt6 Extension API](extension_api.html "next chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* DBus Support

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.



---

# The PyQt6 Extension API {#the-pyqt6-extension-api}

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* The PyQt6 Extension API

# The PyQt6 Extension API[¶](#the-pyqt6-extension-api "Link to this heading")

An important feature of PyQt6 (and SIP generated modules in general) is the
ability for other extension modules to build on top of it.
[QScintilla](https://www.riverbankcomputing.com/software/qscintilla/) is
such an example.

PyQt6 provides a C++ extension API that can be used by other modules. This has
the advantage of sharing code and also enforcing consistent behaviour.

## C++ API[¶](#c-api "Link to this heading")

The C++ API is a set of functions. The addresses of each function is obtained
by calling SIP’s `sipImportSymbol()` function with the name of the
function required.

The functions exported by PyQt6 are as follows:

void pyqt6\_cleanup\_qobjects()[¶](#_CPPv422pyqt6_cleanup_qobjectsv "Link to this definition")
:   Call the C++ destructor of any [QObject](api/qtcore/qobject.html) instance
    that is owned by Python (with the exception of any
    [QCoreApplication](api/qtcore/qcoreapplication.html) instance).

void pyqt6\_err\_print()[¶](#_CPPv415pyqt6_err_printv "Link to this definition")
:   A replacement for [`PyErr_Print()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Print "(in Python v3.14)") that passes the text of the
    exception and traceback to `qFatal()`.

char \*\*pyqt6\_from\_argv\_list(PyObject \*argv\_list, int &argc)[¶](#_CPPv420pyqt6_from_argv_listP8PyObjectRi "Link to this definition")
:   Convert a Python list to a standard C array of command line arguments and
    an argument count.

    Parameters:
    :   * **argv\_list** – is the Python list of arguments.
        * **argc** – is updated with the number of arguments in the list.

    Returns:
    :   an array of pointers to the arguments on the heap.

PyObject \*pyqt6\_from\_qvariant\_by\_type(QVariant &value, PyObject \*type)[¶](#_CPPv427pyqt6_from_qvariant_by_typeR8QVariantP8PyObject "Link to this definition")
:   Convert a [QVariant](api/qtcore/qvariant.html) to a Python object according
    to an optional Python type.

    Parameters:
    :   * **value** – is the value to convert.
        * **type** – is the Python type.

    Returns:
    :   the converted value. If it is `0` then a Python exception will have
        been raised.

sipErrorState pyqt6\_get\_connection\_parts(PyObject \*slot, QObject \*transmitter, const char \*signal\_signature, bool single\_shot, QObject \*\*receiver, QByteArray &slot\_signature)[¶](#_CPPv426pyqt6_get_connection_partsP8PyObjectP7QObjectPKcbPP7QObjectR10QByteArray "Link to this definition")
:   Get the receiver object and slot signature to allow a signal to be
    connected to an optional transmitter.

    Parameters:
    :   * **slot** – is the slot and should be a callable or a bound signal.
        * **transmitter** – is the optional [QObject](api/qtcore/qobject.html) transmitter.
        * **signal\_signature** – is the signature of the signal to be connected.
        * **single\_shot** – is `true` if the signal will only ever be emitted once.
        * **receiver** – is updated with the [QObject](api/qtcore/qobject.html) receiver. This
          may be a proxy if the slot requires it.
        * **slot\_signature** – is updated with the signature of the slot.

    Returns:
    :   the error state. If this is `sipErrorFail` then a Python
        exception will have been raised.

const QMetaObject \*pyqt6\_get\_qmetaobject(PyTypeObject \*type)[¶](#_CPPv421pyqt6_get_qmetaobjectP12PyTypeObject "Link to this definition")
:   Get the QMetaObject instance for a Python type. The Python type must be a
    sub-type of [QObject](api/qtcore/qobject.html)’s Python type.

    Parameters:
    :   **type** – is the Python type object.

    Returns:
    :   the [QMetaObject](api/qtcore/qmetaobject.html).

sipErrorState pyqt6\_get\_pyqtsignal\_parts(PyObject \*signal, QObject \*\*transmitter, QByteArray &signal\_signature)[¶](#_CPPv426pyqt6_get_pyqtsignal_partsP8PyObjectPP7QObjectR10QByteArray "Link to this definition")
:   Get the transmitter object and signal signature from a bound signal.

    Parameters:
    :   * **signal** – is the bound signal.
        * **transmitter** – is updated with the [QObject](api/qtcore/qobject.html) transmitter.
        * **signal\_signature** – is updated with the signature of the signal.

    Returns:
    :   the error state. If this is `sipErrorFail` then a Python
        exception will have been raised.

sipErrorState pyqt6\_get\_pyqtslot\_parts(PyObject \*slot, QObject \*\*receiver, QByteArray &slot\_signature)[¶](#_CPPv424pyqt6_get_pyqtslot_partsP8PyObjectPP7QObjectR10QByteArray "Link to this definition")
:   Get the receiver object and slot signature from a callable decorated with
    [pyqtSlot()](api/qtcore/qtcore-module.html#pyqtSlot).

    Parameters:
    :   * **slot** – is the callable slot.
        * **receiver** – is updated with the [QObject](api/qtcore/qobject.html) receiver.
        * **slot\_signature** – is updated with the signature of the slot.

    Returns:
    :   the error state. If this is `sipErrorFail` then a Python
        exception will have been raised.

sipErrorState pyqt6\_get\_signal\_signature(PyObject \*signal, const QObject \*transmitter, QByteArray &signal\_signature)[¶](#_CPPv426pyqt6_get_signal_signatureP8PyObjectPK7QObjectR10QByteArray "Link to this definition")
:   Get the signature string for a bound or unbound signal. If the signal is
    bound, and the given transmitter is specified, then it must be bound to the
    transmitter.

    Parameters:
    :   * **signal** – is the signal.
        * **transmitter** – is the optional [QObject](api/qtcore/qobject.html) transmitter.
        * **signal\_signature** – is updated with the signature of the signal.

    Returns:
    :   the error state. If this is `sipErrorFail` then a Python
        exception will have been raised.

void pyqt6\_register\_from\_qvariant\_convertor(bool (\*convertor)(const QVariant&, PyObject\*\*))[¶](#_CPPv438pyqt6_register_from_qvariant_convertorPFbRK8QVariantPP8PyObjectE "Link to this definition")
:   Register a convertor function that converts a
    [QVariant](api/qtcore/qvariant.html) value to a Python object.

    Parameters:
    :   **convertor** – is the convertor function. This takes two arguments. The first
        argument is the [QVariant](api/qtcore/qvariant.html) value to be
        converted. The second argument is updated with a reference to the
        result of the conversion and it will be `0`, and a Python exception
        raised, if there was an error. The convertor will return `true` if
        the value was handled so that no other convertor will be tried.

void pyqt6\_register\_to\_qvariant\_convertor(bool (\*convertor)(PyObject\*, QVariant&, bool\*))[¶](#_CPPv436pyqt6_register_to_qvariant_convertorPFbP8PyObjectR8QVariantPbE "Link to this definition")
:   Register a convertor function that converts a Python object to a
    [QVariant](api/qtcore/qvariant.html) value.

    Parameters:
    :   **convertor** – is the convertor function. This takes three arguments. The first
        argument is the Python object to be converted. The second argument is a
        pointer to [QVariant](api/qtcore/qvariant.html) value that is updated
        with the result of the conversion. The third argument is updated with
        an error flag which will be `false`, and a Python exception raised,
        if there was an error. The convertor will return `true` if the value
        was handled so that no other convertor will be tried.

void pyqt6\_register\_to\_qvariant\_data\_convertor(bool (\*convertor)(PyObject\*, void\*, int, bool\*))[¶](#_CPPv441pyqt6_register_to_qvariant_data_convertorPFbP8PyObjectPviPbE "Link to this definition")
:   Register a convertor function that converts a Python object to the
    pre-allocated data of a [QVariant](api/qtcore/qvariant.html) value.

    Parameters:
    :   **convertor** – is the convertor function. This takes four arguments. The first
        argument is the Python object to be converted. The second argument is a
        pointer to the pre-allocated data of a
        [QVariant](api/qtcore/qvariant.html) value that is updated with the
        result of the conversion. The third argument is the meta-type of the
        value. The fourth argument is updated with an error flag which will be
        `false`, and a Python exception raised, if there was an error. The
        convertor will return `true` if the value was handled so that no
        other convertor will be tried.

void pyqt6\_update\_argv\_list(PyObject \*argv\_list, int argc, char \*\*argv)[¶](#_CPPv422pyqt6_update_argv_listP8PyObjectiPPc "Link to this definition")
:   Update a Python list from a standard C array of command line arguments and
    an argument count. This is used in conjunction with
    [`pyqt6_from_argv_list()`](#_CPPv420pyqt6_from_argv_listP8PyObjectRi "pyqt6_from_argv_list") to handle the updating of argument lists
    after calling constructors of classes such as
    [QCoreApplication](api/qtcore/qcoreapplication.html).

    Parameters:
    :   * **argv\_list** – is the Python list of arguments that will be updated.
        * **argc** – is the number of command line arguments.
        * **argv** – is the array of pointers to the arguments on the heap.

### [Table of Contents](index.html)

* The PyQt6 Extension API
  + [C++ API](#c-api)
    - [`pyqt6_cleanup_qobjects()`](#_CPPv422pyqt6_cleanup_qobjectsv)
    - [`pyqt6_err_print()`](#_CPPv415pyqt6_err_printv)
    - [`pyqt6_from_argv_list()`](#_CPPv420pyqt6_from_argv_listP8PyObjectRi)
    - [`pyqt6_from_qvariant_by_type()`](#_CPPv427pyqt6_from_qvariant_by_typeR8QVariantP8PyObject)
    - [`pyqt6_get_connection_parts()`](#_CPPv426pyqt6_get_connection_partsP8PyObjectP7QObjectPKcbPP7QObjectR10QByteArray)
    - [`pyqt6_get_qmetaobject()`](#_CPPv421pyqt6_get_qmetaobjectP12PyTypeObject)
    - [`pyqt6_get_pyqtsignal_parts()`](#_CPPv426pyqt6_get_pyqtsignal_partsP8PyObjectPP7QObjectR10QByteArray)
    - [`pyqt6_get_pyqtslot_parts()`](#_CPPv424pyqt6_get_pyqtslot_partsP8PyObjectPP7QObjectR10QByteArray)
    - [`pyqt6_get_signal_signature()`](#_CPPv426pyqt6_get_signal_signatureP8PyObjectPK7QObjectR10QByteArray)
    - [`pyqt6_register_from_qvariant_convertor()`](#_CPPv438pyqt6_register_from_qvariant_convertorPFbRK8QVariantPP8PyObjectE)
    - [`pyqt6_register_to_qvariant_convertor()`](#_CPPv436pyqt6_register_to_qvariant_convertorPFbP8PyObjectR8QVariantPbE)
    - [`pyqt6_register_to_qvariant_data_convertor()`](#_CPPv441pyqt6_register_to_qvariant_data_convertorPFbP8PyObjectPviPbE)
    - [`pyqt6_update_argv_list()`](#_CPPv422pyqt6_update_argv_listP8PyObjectiPPc)

#### Previous topic

[DBus Support](dbus.html "previous chapter")

### Quick search

### Navigation

* [Index](genindex.html "General index")
* [Classes](sip-classes.html "Index of all classes") |
* [Modules](module_index.html "Index of all modules") |
* [PyQt Documentation v6.11.0](index.html) »
* The PyQt6 Extension API

© Copyright 2026, Riverbank Computing Limited, The Qt Company.
Created using [Sphinx](https://www.sphinx-doc.org/) 8.2.3.

---

*本文档由 EverythingCanBeMarkdown (ECBM) 自动生成*
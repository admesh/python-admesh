CentOS 5 admesh RPMs
====================

Those are created from the `Fedora package <src.fedoraproject.org/rpms/admesh>`_.

Some adjustments have to be made to the specfile:

.. code:: diff

   diff --git a/admesh.spec b/admesh.spec
   index 547ad14..9b0d2bb 100644
   --- a/admesh.spec
   +++ b/admesh.spec
   @@ -7,6 +7,7 @@ Group:          Applications/Engineering
    URL:            http://github.com/admesh/admesh/
    Source0:        http://github.com/admesh/admesh/releases/download/v%{version}/admesh-%{version}.tar.gz
    Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
   +BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
    
    %description
    ADMesh is a program for diagnosing and/or repairing commonly encountered
   @@ -42,10 +43,10 @@ This package contains the %{name} runtime library.
    %build
    %configure
    # Pass the -v option to libtool so we can better see what's going on
   -make %{?_smp_mflags} CFLAGS="%{optflags}" LIBTOOLFLAGS="-v"
   +make %{?_smp_mflags} CFLAGS="%{optflags} -lm" LIBTOOLFLAGS="-v"
    
    %install
   -%{make_install}
   +make install DESTDIR=%{buildroot}
    # Remove the documentation installed by "make install" (rpm will handle that)
    rm -rf %{buildroot}%{_defaultdocdir}/%{name}
    # Remove the libtool archive installed by "make install"

Also, some changes need to be made in ``/etc/mock/epel-5-{x86_64,i386}.cfg``:

.. code:: python

   config_opts['use_nspawn'] = False
   config_opts['package_manager'] = 'yum'

Then, this is built by:

.. code:: console

   $ fedpkg --release el5 mockbuild
   $ fedpkg --release el5 mockbuild --mock-config epel-5-i386

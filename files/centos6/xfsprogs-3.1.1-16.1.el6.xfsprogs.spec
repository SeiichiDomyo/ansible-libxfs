Summary:	Utilities for managing the XFS filesystem
Name:		xfsprogs
Version:	3.1.1
Release:	16.1%{?dist}
# Licensing based on generic "GNU GENERAL PUBLIC LICENSE"
# in source, with no mention of version.
# doc/COPYING file specifies what is GPL and what is LGPL
# but no mention of versions in the source.
License:	GPL+ and LGPLv2+
Group:		System Environment/Base
URL:		http://oss.sgi.com/projects/xfs/
Source0:	ftp://oss.sgi.com/projects/xfs/cmd_tars/%{name}-%{version}.tar.gz
Source1:	xfsprogs-wrapper.h
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libtool, gettext, libuuid-devel
BuildRequires:	readline-devel, libblkid-devel >= 2.17-0.1.git5e51568
Provides:	xfs-cmds
Obsoletes:	xfs-cmds <= %{version}
Conflicts:	xfsdump < 3.0.1

Patch0:		xfsprogs-3.1.0-glibc-fixes.patch
Patch1:		xfsprogs-3.1.1-fd-test-fix.patch
Patch2:		xfsprogs-3.1.1-empty-blkid-fix.patch
Patch3:		xfsprogs-3.1.1-btree-locking.patch
Patch4:		xfsprogs-3.1.2-fsr-attr-v2.patch
Patch5:		xfsprogs-3.1.2-admin-lazy_count-fix.patch
Patch6:		xfsprogs-3.1.2-xfs_quota-ESRCH.patch
Patch7:		xfsprogs-3.1.5-xfs_repair-check-if-agno-is-inside-the-filesystem.patch
Patch8:		xfsprogs-3.1.5-xfs_metadump-fixes.patch
Patch9:		xfsprogs-3.1.6-agblock-count-fix.patch
Patch10:	xfsprogs-3.1.6-double-pquota-values.patch
Patch11:	xfsprogs-3.1.6-ignore-fs_table_errors.patch
Patch12:	xfsprogs-3.1.1-mkfs-misaligned.patch
Patch13:	xfsprogs-3.1.1-mkfs-physsect.patch
Patch14:	xfsprogs-3.1.1-agsize-warn.patch
Patch15:	xfsprogs-3.1.1-projid32bit.patch
Patch16:	xfsprogs-3.1.1-projid32flag.patch
Patch17:	xfsprogs-3.1.1-validatestring.patch
Patch18:	xfsprogs-3.1.11-multidisk-mode.patch
Patch19:	xfsprogs-3.1.11-logprint-multilog.patch
Patch20:	xfsprogs-3.1.11-io-remove-setfl.patch
Patch21:	xfsprogs-3.1.11-io-manpage.patch
Patch22:	xfsprogs-3.1.9-repair-frag-dir2-leaf.patch
Patch23:	xfsprogs-3.1.9-repair-frag-dir2-blkmap.patch
Patch24:	xfsprogs-3.1.8-repair-thread-local-data.patch
Patch25:	xfsprogs-3.1.11-mkfs-manpage.patch
Patch26:	xfsprogs-3.1.18-repair-unlinked-walk.patch
Patch27:	xfsprogs-3.1.1-logprint-continuation.patch
Patch28:	xfsprogs-3.1.1-logprint-fix-continuation.patch
Patch29:	xfsprogs-3.1.1-logprint-fix-wrapped-log.patch
Patch30:	xfsprogs-3.2.0-platform_test_xfs_fd-regular-files.patch
Patch31:	xfsprogs-3.2.0-repair-early-progress-segfault.patch
Patch32:	xfsprogs-3.2.0-xfs_fsr-selinux.patch
Patch33:	xfsprogs-3.2.1-xfs_copy-exit-not-killall.patch
Patch34:	xfsprogs-3.2.1-xfs_copy_fix_corruption.patch
Patch35:	xfsprogs-3.1.1-install-libxfs.patch

%description
A set of commands to use the XFS filesystem, including mkfs.xfs.

XFS is a high performance journaling filesystem which originated
on the SGI IRIX platform.  It is completely multi-threaded, can
support large files and large filesystems, extended attributes,
variable block sizes, is extent based, and makes extensive use of
Btrees (directories, extents, free space) to aid both performance
and scalability.

Refer to the documentation at http://oss.sgi.com/projects/xfs/
for complete details.  This implementation is on-disk compatible
with the IRIX version of XFS.

%package devel
Summary: XFS filesystem-specific static libraries and headers
Group: Development/Libraries
Requires: xfsprogs = %{version}-%{release}

%description devel
xfsprogs-devel contains the libraries and header files needed to
develop XFS filesystem-specific programs.

You should install xfsprogs-devel if you want to develop XFS
filesystem-specific programs,  If you install xfsprogs-devel, you'll
also want to install xfsprogs.

%package qa-devel
Summary: XFS QA filesystem-specific static libraries and headers
Group: Development/Libraries
Requires: xfsprogs = %{version}-%{release}
Requires: xfsprogs-devel = %{version}-%{release}

%description qa-devel
xfsprogs-qa-devel contains headers and libraries needed to build
the xfstests QA suite.

You should install xfsprogs-qa-devel only if you are interested
in building or running the xfstests QA suite.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1

%build
export tagname=CC DEBUG=-DNDEBUG
%configure \
        --enable-readline=yes	\
	--enable-blkid=yes

# Kill rpaths
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make V=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DIST_ROOT=$RPM_BUILD_ROOT install install-dev install-qa

# nuke .la files, etc
rm -f $RPM_BUILD_ROOT/{%{_lib}/*.{la,a,so},%{_libdir}/*.la}
# fix up symlink to be correct
rm -f $RPM_BUILD_ROOT/%{_libdir}/libhandle.so
ln -s ../../%{_lib}/libhandle.so.1 $RPM_BUILD_ROOT/%{_libdir}/libhandle.so
chmod 0755 $RPM_BUILD_ROOT/%{_lib}/libhandle.so.*.*.*

# remove non-versioned docs location
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/xfsprogs/

# ugly hack to allow parallel install of 32-bit and 64-bit -devel packages:
%define multilib_arches %{ix86} x86_64 ppc ppc64 s390 s390x %{sparc}

%ifarch %{multilib_arches}
mv -f $RPM_BUILD_ROOT%{_includedir}/xfs/platform_defs.h \
      $RPM_BUILD_ROOT%{_includedir}/xfs/platform_defs-%{_arch}.h
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/xfs/platform_defs.h
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc doc/CHANGES doc/COPYING doc/CREDITS README
/sbin/fsck.xfs
/sbin/mkfs.xfs
/sbin/xfs_repair
/%{_lib}/*.so.*
%{_mandir}/man8/*
%{_mandir}/man5/*
%{_sbindir}/*

%files devel
%defattr(-,root,root)
%{_mandir}/man3/*
%dir %{_includedir}/xfs
%{_includedir}/xfs/handle.h
%{_includedir}/xfs/jdm.h
%{_includedir}/xfs/linux.h
%ifarch %{multilib_arches}
%{_includedir}/xfs/platform_defs-%{_arch}.h
%endif
%{_includedir}/xfs/platform_defs.h
%{_includedir}/xfs/xfs.h
%{_includedir}/xfs/xfs_fs.h
%{_includedir}/xfs/xqm.h
%{_libdir}/*.a
%{_libdir}/*.so

%files qa-devel
%defattr(-,root,root)
%{_includedir}/xfs/bitops.h
%{_includedir}/xfs/cache.h
%{_includedir}/xfs/kmem.h
%{_includedir}/xfs/libxfs.h
%{_includedir}/xfs/libxlog.h
%{_includedir}/xfs/list.h
%{_includedir}/xfs/parent.h
%{_includedir}/xfs/swab.h
%{_includedir}/xfs/xfs_ag.h
%{_includedir}/xfs/xfs_alloc.h
%{_includedir}/xfs/xfs_alloc_btree.h
%{_includedir}/xfs/xfs_arch.h
%{_includedir}/xfs/xfs_attr_leaf.h
%{_includedir}/xfs/xfs_attr_sf.h
%{_includedir}/xfs/xfs_bit.h
%{_includedir}/xfs/xfs_bmap.h
%{_includedir}/xfs/xfs_bmap_btree.h
%{_includedir}/xfs/xfs_btree.h
%{_includedir}/xfs/xfs_btree_trace.h
%{_includedir}/xfs/xfs_buf_item.h
%{_includedir}/xfs/xfs_da_btree.h
%{_includedir}/xfs/xfs_dfrag.h
%{_includedir}/xfs/xfs_dinode.h
%{_includedir}/xfs/xfs_dir2.h
%{_includedir}/xfs/xfs_dir2_block.h
%{_includedir}/xfs/xfs_dir2_data.h
%{_includedir}/xfs/xfs_dir2_leaf.h
%{_includedir}/xfs/xfs_dir2_node.h
%{_includedir}/xfs/xfs_dir2_sf.h
%{_includedir}/xfs/xfs_dir_leaf.h
%{_includedir}/xfs/xfs_dir_sf.h
%{_includedir}/xfs/xfs_extfree_item.h
%{_includedir}/xfs/xfs_ialloc.h
%{_includedir}/xfs/xfs_ialloc_btree.h
%{_includedir}/xfs/xfs_imap.h
%{_includedir}/xfs/xfs_inode.h
%{_includedir}/xfs/xfs_inode_item.h
%{_includedir}/xfs/xfs_inum.h
%{_includedir}/xfs/xfs_log.h
%{_includedir}/xfs/xfs_log_priv.h
%{_includedir}/xfs/xfs_log_recover.h
%{_includedir}/xfs/xfs_metadump.h
%{_includedir}/xfs/xfs_mount.h
%{_includedir}/xfs/xfs_quota.h
%{_includedir}/xfs/xfs_rtalloc.h
%{_includedir}/xfs/xfs_sb.h
%{_includedir}/xfs/xfs_trans.h
%{_includedir}/xfs/xfs_trans_space.h
%{_includedir}/xfs/xfs_types.h

%changelog
* Mon Jun 16 2014 Eric Sandeen <sandeen@redhat.com> 3.1.1-16
- xfs_copy: do not exit with error code if we succeed (#1100107)
- xfs_copy: fix corruption when source fs sector size is > 512 bytes (#1104956)

* Mon May 05 2014 Eric Sandeen <sandeen@redhat.com> 3.1.1-15
- libxfs: restrict platform_test_xfs_fd to regular files (#1018751)
- xfs_repair: avoid segfault if reporting progress early in repair (#1020438)
- xfs_fsr: fix SWAPEXT failures under selinux (#1024702)

* Fri Aug 30 2013 Eric Sandeen <sandeen@redhat.com> 3.1.1-14
- xfs_logprint: More fixes for continuations & log wraps  (#1002908)

* Wed Jul 24 2013 Eric Sandeen <sandeen@redhat.com> 3.1.1-13
- xfs_repair: do not walk the unlinked inode list (#950691)

* Wed Jul 24 2013 Eric Sandeen <sandeen@redhat.com> 3.1.1-12
- mkfs.xfs: Document "noalign" option in mkfs.xfs manpage (#987538)

* Fri May 17 2013 Eric Sandeen <sandeen@redhat.com> 3.1.1-11
- mkfs.xfs: Use multidisk mode when geometry is on cmdline (#961501)
- xfs_io: Update  man page to include chproj, lsproj (#962394)
- xfs_io: Remove broken setfl command (#962394)
- xfs_logprint: Handle multiply-logged fields (#962397)
- xfs_repair: Handle fragmented multiblock dir2 directories (#964216)
- xfs_repair: avoid segfault with ag_stride (#93904)

* Wed Nov 28 2012 Eric Sandeen <sandeen@redhat.com> 3.1.1-10
- Validate string -> number conversion (#878859)

* Mon Oct 15 2012 Eric Sandeen <sandeen@redhat.com> 3.1.1-9
- Add 32-bit project ID support (#827186)

* Tue Sep 25 2012 Eric Sandeen <sandeen@redhat.com> 3.1.1-8
- mkfs.xfs: better handle misaligned 4k devices (#836433)
- mkfs.xfs: default to physical sectorsize (#836433)
- mkfs.xfs: clarify errors when specified AG size is too large (#730433)

* Wed Feb 15 2012 Eric Sandeen <sandeen@redhat.com> 3.1.1-7
- Fix xfs_metadump hang (#730886)
- mkfs.xfs: don't increase agblocks past maximum (#738279)
- Fix double reporting of quota values (#749435)
- xfs_quota: handle malformed entries in mtab (749434)

* Mon Jul 25 2011 Lukas Czerner <lczerner@redhat.com> 3.1.1-6
- Check if agno is inside the filesystem (#694706)

* Fri Jun 03 2011 Eric Sandeen <sandeen@redhat.com> 3.1.1-5
- Don't try to report quotas which aren't there (#679154)
 
* Mon May 10 2010 Eric Sandeen <sandeen@redhat.com> 3.1.1-4
- Two important fixes from 3.1.2 release (#590773)
- Fix up attribute handling in xfs_fsr
- Make sure xfs_admin writes both sb fields when changing lazy_count

* Mon Mar 15 2010 Eric Sandeen <sandeen@redhat.com> 3.1.1-3
- Fix missing locking for btree manipulation in xfs_repair (#573831)

* Mon Feb 01 2010 Eric Sandeen <sandeen@redhat.com> 3.1.1-2
- Fix mkfs of target with nothing blkid can recognize (#561870)
 
* Mon Feb 01 2010 Eric Sandeen <sandeen@redhat.com> 3.1.1-1
- New upstream release (#555847)
- Fix fd validity test for device-less mkfs invocation
 
* Sun Jan 17 2010 Eric Sandeen <sandeen@redhat.com> 3.1.0-2
- Post-release mkfs fixes (#555847)
- Minor fixups for new glibc headers

* Wed Jan 13 2010 Eric Sandeen <sandeen@redhat.com> 3.1.0-1
- New upstream release
- Fixes default mkfs.xfs on 4k sector device (#539553)

* Tue Dec 08 2009 Eric Sandeen <sandeen@redhat.com> 3.0.3-5
- And finally, BuildRequire libblkid-devel

* Mon Dec 07 2009 Eric Sandeen <sandeen@redhat.com> 3.0.3-4
- Actually patch & run configure script w/ blkid bits...
- Kill rpath in xfs_fsr

* Fri Nov 20 2009 Eric Sandeen <sandeen@redhat.com> 3.0.3-3
- Fix up build issues w.r.t. off64_t

* Tue Nov 10 2009 Eric Sandeen <sandeen@redhat.com> 3.0.3-2
- Add trim/discard & libblkid support

* Tue Sep 01 2009 Eric Sandeen <sandeen@redhat.com> 3.0.3-1
- New upstream release

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-9
- Fix block overflows in xfs_repair and xfs_metadump

* Tue Jun 30 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-8
- Fix up build-requires after e2fsprogs splitup

* Thu Jun 18 2009 Dennis Gilmore <dennis@ausil.us> 3.0.1-7
- update sparc multilib handling

* Mon Jun 15 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-6
- Make lazy superblock counters the default

* Mon Jun 15 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-5
- Add fallocate command to config script & fix for 32-bit

* Mon Jun 15 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-4
- Add fallocate command to xfs_io

* Fri May 15 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-3
- Fix and re-enable readline

* Tue May 05 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-2
- Conflict with xfsdump < 3.0.1 since files moved between them

* Tue May 05 2009 Eric Sandeen <sandeen@redhat.com> 3.0.1-1
- New upstream release

* Sat Apr 18 2009 Eric Sandeen <sandeen@redhat.com> 3.0.0-4
- Fix build for non-multilib arches, oops.

* Sat Apr 18 2009 Eric Sandeen <sandeen@redhat.com> 3.0.0-3
- Create new xfsprogs-qa-devel subpackage

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Eric Sandeen <sandeen@redhat.com> 3.0.0-1
- New upstream release

* Thu Jan 08 2009 Eric Sandeen <sandeen@redhat.com> 2.10.2-3
- Fix perms of libhandle.so in specfile, not makefile

* Wed Jan 07 2009 Eric Sandeen <sandeen@redhat.com> 2.10.2-2
- Fix perms of libhandle.so so that it's properly stripped

* Sun Dec 07 2008 Eric Sandeen <sandeen@redhat.com> 2.10.2-1
- New upstream release, bugfix only.

* Wed Nov 26 2008 Eric Sandeen <sandeen@redhat.com> 2.10.1-4
- Add protection from borken sys_ustat
- Add final upstream versions of gfs2 & parallel build patches

* Wed Nov 12 2008 Eric Sandeen <sandeen@redhat.com> 2.10.1-2
- Recognize gfs/gfs2 in libdisk
- Enable parallel builds

* Fri Sep 05 2008 Eric Sandeen <sandeen@redhat.com> 2.10.1-1
- Update to xfsprogs 2.10.1
- Add ASCII case-insensitive support to xfsprogs.
- xfs_repair fixes

* Wed Jun 04 2008 Dennis Gilmore <dennis@ausil.us> 2.9.8-3
- sparc32 is built using the sparcv9 variant 

* Wed Jun 04 2008 Eric Sandeen <sandeen@redhat.com> 2.9.8-2
- Tidy up multilib hack for non-multilib arches & add sparc (#448452)

* Wed Apr 23 2008 Eric Sandeen <sandeen@redhat.com> 2.9.8-1
- Update to xfsprogs 2.9.8
- Add support for sb_features2 in wrong location
- Add -c option to xfs_admin to turn lazy-counters on/off
- Added support for mdp in libdisk/mkfs.xfs

* Sun Mar 02 2008 Eric Sandeen <sandeen@redhat.com> 2.9.7-1
- Update to xfsprogs 2.9.7
- Lazy sb counters back off by default; other misc fixes

* Wed Feb 06 2008 Eric Sandeen <sandeen@redhat.com> 2.9.6-1
- Update to xfsprogs 2.9.6 - fixes mkfs sizing problem.
- Trim down BuildRequires to what's actually required now

* Mon Jan 21 2008 Eric Sandeen <sandeen@redhat.com> 2.9.5-1
- Update to xfsprogs 2.9.5
- Contains more optimal mkfs defaults
- specfile cleanup, & don't restate config defaults

* Tue Oct 23 2007 Eric Sandeen <sandeen@redhat.com> 2.9.4-4
- Add arm to multilib header wrapper

* Tue Oct 02 2007 Eric Sandeen <sandeen@redhat.com> 2.9.4-3
- mkfs.xfs: Fix wiping old AG headers and purge whack buffers

* Mon Oct 01 2007 Eric Sandeen <sandeen@redhat.com> 2.9.4-2
- Add alpha to the multilib wrapper (#310411)

* Mon Sep 10 2007 Eric Sandeen <sandeen@redhat.com> 2.9.4-1
- Update to xfsprogs 2.9.4

* Fri Aug 24 2007 Eric Sandeen <sandeen@redhat.com> 2.9.3-3
- Add gawk to buildrequires

* Thu Aug 16 2007 Eric Sandeen <sandeen@redhat.com> 2.9.3-2
- Update license tag

* Thu Jul 26 2007 Eric Sandeen <sandeen@redhat.com> 2.9.3-1
- Upgrade to xfsprogs 2.9.2, quota, xfs_repair, and filestreams changes

* Thu Jul  6 2007 Eric Sandeen <sandeen@redhat.com> 2.8.21-1
- Upgrade to xfsprogs 2.8.21, lazy sb counters enabled,
  xfs_quota fix (#236746)

* Thu May 31 2007 Eric Sandeen <sandeen@redhat.com> 2.8.20-2
- Fix ppc64 build... again

* Fri May 25 2007 Eric Sandeen <sandeen@redhat.com> 2.8.20-1
- Upgrade to xfsprogs 2.8.20, several xfs_repair fixes

* Tue Mar 06 2007 Miroslav Lichvar <mlichvar@redhat.com> 2.8.18-3
- Remove libtermcap-devel from BuildRequires

* Wed Feb 14 2007 Miroslav Lichvar <mlichvar@redhat.com> 2.8.18-2
- Disable readline support for now (#223781)

* Sun Feb 04 2007 Jarod Wilson <jwilson@redhat.com> 2.8.18-1
- Post-facto changelog addition to note bump to 2.8.18

* Wed Sep 27 2006 Russell Cattelan <cattelan@thebarn.com> 2.8.11-3
- bump build version to 3 for a new brew build

* Tue Sep 26 2006 Russell Cattelan <cattelan@thebarn.com> 2.8.11-2
- add ppc64 build patch

* Thu Sep 21 2006 Russell Cattelan <cattelan@redhat.com> 2.8.11-1
- Upgrade to xfsprogs 2.8.11 Need to pick up important repair fixes

* Tue Jul 18 2006 Jeremy Katz <katzj@redhat.com> - 2.8.4-3
- exclude arch ppc64 for now (#199315)

* Mon Jul 17 2006 Jesse Keating <jkeating@redhat.com> - 2.8.4-2
- rebuild

* Tue Jul 04 2006 Robert Scheck <redhat@linuxnetz.de> 2.8.4-1
- Upgrade to 2.8.4 (#196599 #c2)

* Sun Jun 25 2006 Robert Scheck <redhat@linuxnetz.de> 2.8.3-1
- Upgrade to 2.8.3 (#196599)
- Applied Russell Coker's suggested patch to improve the
  performance for SELinux machines significantly (#120622)

* Sun Jun 25 2006 Robert Scheck <redhat@linuxnetz.de> 2.7.11-2
- Fixed multilib conflict of xfs/platform_defs.h (#192755)

* Sun Mar 12 2006 Robert Scheck <redhat@linuxnetz.de> 2.7.11-1
- Upgrade to 2.7.11 and spec file cleanup (#185234)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.7.3-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.7.3-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Oct 31 2005 Robert Scheck <redhat@linuxnetz.de> 2.7.3-1
- Upgrade to 2.7.3 and enabled termcap support (#154323)

* Wed Sep 28 2005 Florian La Roche <laroche@redhat.com>
- fixup building with current rpm

* Wed Apr 20 2005 Dave Jones <davej@redhat.com>
- Disable debug. (#151438)
- Rebuild with gcc4

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> - 2.6.13-3
- Rebuilt for new readline.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May  5 2004 Jeremy Katz <katzj@redhat.com> - 2.6.13-1
- update to 2.6.13 per request of upstream
- fixes mount by label of xfs on former raid partition (#122043)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan  8 2004 Jeremy Katz <katzj@redhat.com> 2.6.0-2
- add defattr (reported by Matthias)

* Tue Dec 23 2003 Elliot Lee <sopwith@redhat.com> 2.6.0-3
- Fix tyops in dependencies

* Mon Dec 22 2003 Jeremy Katz <katzj@redhat.com> 2.6.0-1
- build for Fedora Core
- switch to more explicit file lists, nuke .la files

* Tue Dec 16 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 2.6.0
- Update to 2.6.0.

* Sat Sep 13 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Sync with XFS 1.3.0.
- Update to 2.5.6.

* Thu Apr 10 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 2.3.9-0_2.90at
- Rebuilt for Red Hat 9.

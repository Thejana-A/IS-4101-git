# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build

# Include any dependencies generated for this target.
include CMakeFiles/gecodesupport.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/gecodesupport.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/gecodesupport.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/gecodesupport.dir/flags.make

CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.o: CMakeFiles/gecodesupport.dir/flags.make
CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.o: ../gecode/support/exception.cpp
CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.o: CMakeFiles/gecodesupport.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.o -MF CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.o.d -o CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.o -c /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/exception.cpp

CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/exception.cpp > CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.i

CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/exception.cpp -o CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.s

CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.o: CMakeFiles/gecodesupport.dir/flags.make
CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.o: ../gecode/support/allocator.cpp
CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.o: CMakeFiles/gecodesupport.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.o -MF CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.o.d -o CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.o -c /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/allocator.cpp

CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/allocator.cpp > CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.i

CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/allocator.cpp -o CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.s

CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.o: CMakeFiles/gecodesupport.dir/flags.make
CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.o: ../gecode/support/heap.cpp
CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.o: CMakeFiles/gecodesupport.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.o -MF CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.o.d -o CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.o -c /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/heap.cpp

CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/heap.cpp > CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.i

CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/heap.cpp -o CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.s

CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.o: CMakeFiles/gecodesupport.dir/flags.make
CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.o: ../gecode/support/thread/thread.cpp
CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.o: CMakeFiles/gecodesupport.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.o -MF CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.o.d -o CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.o -c /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/thread/thread.cpp

CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/thread/thread.cpp > CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.i

CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/thread/thread.cpp -o CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.s

CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.o: CMakeFiles/gecodesupport.dir/flags.make
CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.o: ../gecode/support/thread/windows.cpp
CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.o: CMakeFiles/gecodesupport.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.o -MF CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.o.d -o CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.o -c /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/thread/windows.cpp

CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/thread/windows.cpp > CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.i

CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/thread/windows.cpp -o CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.s

CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.o: CMakeFiles/gecodesupport.dir/flags.make
CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.o: ../gecode/support/thread/pthreads.cpp
CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.o: CMakeFiles/gecodesupport.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.o -MF CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.o.d -o CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.o -c /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/thread/pthreads.cpp

CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/thread/pthreads.cpp > CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.i

CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/thread/pthreads.cpp -o CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.s

CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.o: CMakeFiles/gecodesupport.dir/flags.make
CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.o: ../gecode/support/hw-rnd.cpp
CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.o: CMakeFiles/gecodesupport.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building CXX object CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.o -MF CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.o.d -o CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.o -c /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/hw-rnd.cpp

CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/hw-rnd.cpp > CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.i

CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/gecode/support/hw-rnd.cpp -o CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.s

# Object files for target gecodesupport
gecodesupport_OBJECTS = \
"CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.o" \
"CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.o" \
"CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.o" \
"CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.o" \
"CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.o" \
"CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.o" \
"CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.o"

# External object files for target gecodesupport
gecodesupport_EXTERNAL_OBJECTS =

libgecodesupport.a: CMakeFiles/gecodesupport.dir/gecode/support/exception.cpp.o
libgecodesupport.a: CMakeFiles/gecodesupport.dir/gecode/support/allocator.cpp.o
libgecodesupport.a: CMakeFiles/gecodesupport.dir/gecode/support/heap.cpp.o
libgecodesupport.a: CMakeFiles/gecodesupport.dir/gecode/support/thread/thread.cpp.o
libgecodesupport.a: CMakeFiles/gecodesupport.dir/gecode/support/thread/windows.cpp.o
libgecodesupport.a: CMakeFiles/gecodesupport.dir/gecode/support/thread/pthreads.cpp.o
libgecodesupport.a: CMakeFiles/gecodesupport.dir/gecode/support/hw-rnd.cpp.o
libgecodesupport.a: CMakeFiles/gecodesupport.dir/build.make
libgecodesupport.a: CMakeFiles/gecodesupport.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Linking CXX static library libgecodesupport.a"
	$(CMAKE_COMMAND) -P CMakeFiles/gecodesupport.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gecodesupport.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/gecodesupport.dir/build: libgecodesupport.a
.PHONY : CMakeFiles/gecodesupport.dir/build

CMakeFiles/gecodesupport.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/gecodesupport.dir/cmake_clean.cmake
.PHONY : CMakeFiles/gecodesupport.dir/clean

CMakeFiles/gecodesupport.dir/depend:
	cd /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0 /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0 /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles/gecodesupport.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/gecodesupport.dir/depend

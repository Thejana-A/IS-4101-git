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
include CMakeFiles/fzn-gecode.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/fzn-gecode.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/fzn-gecode.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/fzn-gecode.dir/flags.make

CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.o: CMakeFiles/fzn-gecode.dir/flags.make
CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.o: ../tools/flatzinc/fzn-gecode.cpp
CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.o: CMakeFiles/fzn-gecode.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.o -MF CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.o.d -o CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.o -c /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/tools/flatzinc/fzn-gecode.cpp

CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/tools/flatzinc/fzn-gecode.cpp > CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.i

CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/tools/flatzinc/fzn-gecode.cpp -o CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.s

# Object files for target fzn-gecode
fzn__gecode_OBJECTS = \
"CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.o"

# External object files for target fzn-gecode
fzn__gecode_EXTERNAL_OBJECTS =

bin/fzn-gecode: CMakeFiles/fzn-gecode.dir/tools/flatzinc/fzn-gecode.cpp.o
bin/fzn-gecode: CMakeFiles/fzn-gecode.dir/build.make
bin/fzn-gecode: libgecodeflatzinc.a
bin/fzn-gecode: libgecodeminimodel.a
bin/fzn-gecode: libgecodedriver.a
bin/fzn-gecode: libgecodeset.a
bin/fzn-gecode: libgecodesearch.a
bin/fzn-gecode: libgecodefloat.a
bin/fzn-gecode: libgecodeint.a
bin/fzn-gecode: libgecodekernel.a
bin/fzn-gecode: libgecodesupport.a
bin/fzn-gecode: CMakeFiles/fzn-gecode.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable bin/fzn-gecode"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/fzn-gecode.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/fzn-gecode.dir/build: bin/fzn-gecode
.PHONY : CMakeFiles/fzn-gecode.dir/build

CMakeFiles/fzn-gecode.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/fzn-gecode.dir/cmake_clean.cmake
.PHONY : CMakeFiles/fzn-gecode.dir/clean

CMakeFiles/fzn-gecode.dir/depend:
	cd /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0 /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0 /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build/CMakeFiles/fzn-gecode.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/fzn-gecode.dir/depend


# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
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
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/xsm/control/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/xsm/control/build

# Include any dependencies generated for this target.
include learning_communication/CMakeFiles/server.dir/depend.make

# Include the progress variables for this target.
include learning_communication/CMakeFiles/server.dir/progress.make

# Include the compile flags for this target's objects.
include learning_communication/CMakeFiles/server.dir/flags.make

learning_communication/CMakeFiles/server.dir/src/server.cpp.o: learning_communication/CMakeFiles/server.dir/flags.make
learning_communication/CMakeFiles/server.dir/src/server.cpp.o: /home/xsm/control/src/learning_communication/src/server.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xsm/control/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object learning_communication/CMakeFiles/server.dir/src/server.cpp.o"
	cd /home/xsm/control/build/learning_communication && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/server.dir/src/server.cpp.o -c /home/xsm/control/src/learning_communication/src/server.cpp

learning_communication/CMakeFiles/server.dir/src/server.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/server.dir/src/server.cpp.i"
	cd /home/xsm/control/build/learning_communication && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/xsm/control/src/learning_communication/src/server.cpp > CMakeFiles/server.dir/src/server.cpp.i

learning_communication/CMakeFiles/server.dir/src/server.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/server.dir/src/server.cpp.s"
	cd /home/xsm/control/build/learning_communication && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/xsm/control/src/learning_communication/src/server.cpp -o CMakeFiles/server.dir/src/server.cpp.s

learning_communication/CMakeFiles/server.dir/src/server.cpp.o.requires:

.PHONY : learning_communication/CMakeFiles/server.dir/src/server.cpp.o.requires

learning_communication/CMakeFiles/server.dir/src/server.cpp.o.provides: learning_communication/CMakeFiles/server.dir/src/server.cpp.o.requires
	$(MAKE) -f learning_communication/CMakeFiles/server.dir/build.make learning_communication/CMakeFiles/server.dir/src/server.cpp.o.provides.build
.PHONY : learning_communication/CMakeFiles/server.dir/src/server.cpp.o.provides

learning_communication/CMakeFiles/server.dir/src/server.cpp.o.provides.build: learning_communication/CMakeFiles/server.dir/src/server.cpp.o


# Object files for target server
server_OBJECTS = \
"CMakeFiles/server.dir/src/server.cpp.o"

# External object files for target server
server_EXTERNAL_OBJECTS =

/home/xsm/control/devel/lib/learning_communication/server: learning_communication/CMakeFiles/server.dir/src/server.cpp.o
/home/xsm/control/devel/lib/learning_communication/server: learning_communication/CMakeFiles/server.dir/build.make
/home/xsm/control/devel/lib/learning_communication/server: /opt/ros/kinetic/lib/libroscpp.so
/home/xsm/control/devel/lib/learning_communication/server: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/xsm/control/devel/lib/learning_communication/server: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/xsm/control/devel/lib/learning_communication/server: /opt/ros/kinetic/lib/librosconsole.so
/home/xsm/control/devel/lib/learning_communication/server: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/xsm/control/devel/lib/learning_communication/server: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/xsm/control/devel/lib/learning_communication/server: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/xsm/control/devel/lib/learning_communication/server: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/xsm/control/devel/lib/learning_communication/server: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/xsm/control/devel/lib/learning_communication/server: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/xsm/control/devel/lib/learning_communication/server: /opt/ros/kinetic/lib/librostime.so
/home/xsm/control/devel/lib/learning_communication/server: /opt/ros/kinetic/lib/libcpp_common.so
/home/xsm/control/devel/lib/learning_communication/server: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/xsm/control/devel/lib/learning_communication/server: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/xsm/control/devel/lib/learning_communication/server: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/xsm/control/devel/lib/learning_communication/server: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/xsm/control/devel/lib/learning_communication/server: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/xsm/control/devel/lib/learning_communication/server: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/xsm/control/devel/lib/learning_communication/server: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/xsm/control/devel/lib/learning_communication/server: learning_communication/CMakeFiles/server.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xsm/control/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/xsm/control/devel/lib/learning_communication/server"
	cd /home/xsm/control/build/learning_communication && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/server.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
learning_communication/CMakeFiles/server.dir/build: /home/xsm/control/devel/lib/learning_communication/server

.PHONY : learning_communication/CMakeFiles/server.dir/build

learning_communication/CMakeFiles/server.dir/requires: learning_communication/CMakeFiles/server.dir/src/server.cpp.o.requires

.PHONY : learning_communication/CMakeFiles/server.dir/requires

learning_communication/CMakeFiles/server.dir/clean:
	cd /home/xsm/control/build/learning_communication && $(CMAKE_COMMAND) -P CMakeFiles/server.dir/cmake_clean.cmake
.PHONY : learning_communication/CMakeFiles/server.dir/clean

learning_communication/CMakeFiles/server.dir/depend:
	cd /home/xsm/control/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xsm/control/src /home/xsm/control/src/learning_communication /home/xsm/control/build /home/xsm/control/build/learning_communication /home/xsm/control/build/learning_communication/CMakeFiles/server.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : learning_communication/CMakeFiles/server.dir/depend


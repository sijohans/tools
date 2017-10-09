# - Try to find CppUTest
# Once done this will define
#
#  CPPUTEST_ROOT_DIR - Set this variable to the root installation of CppUTest
#
# Read-Only variables:
#  CPPUTEST_FOUND - system has CppUTest
#  CPPUTEST_INCLUDE_DIR - the CppUTest include directory
#  CPPUTEST_LIBRARIES - Link these to use CppUTest
#  CPPUTEST_DEFINITIONS - Compiler switches required for using CppUTest
#

set(_CPPUTEST_ROOT_HINTS
)

set(_CPPUTEST_ROOT_PATHS
    "$ENV{PROGRAMFILES}/CppUTest"
)

find_path(CPPUTEST_ROOT_DIR
    NAMES
        include/CppUTest/*.h
    HINTS
        ${_CPPUTEST_ROOT_HINTS}
    PATHS
        ${_CPPUTEST_ROOT_PATHS}
)
mark_as_advanced(CPPUTEST_ROOT_DIR)

find_path(CPPUTEST_INCLUDE_DIR
    NAMES
        CppUTest/*.h
    PATHS
        ${CPPUTEST_ROOT_DIR}/include
)

find_library(CPPUTEST_LIBRARY
    NAMES
        CppUTest
    PATHS
        ${CPPUTEST_ROOT_DIR}/lib
)

if (CPPUTEST_LIBRARY)
  set(CPPUTEST_LIBRARIES
      ${CPPUTEST_LIBRARIES}
      ${CPPUTEST_LIBRARY}
  )
endif (CPPUTEST_LIBRARY)

include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(CppUTest DEFAULT_MSG CPPUTEST_LIBRARIES CPPUTEST_INCLUDE_DIR)

# show the CPPUTEST_INCLUDE_DIR and CPPUTEST_LIBRARIES variables only in the advanced view
mark_as_advanced(CPPUTEST_INCLUDE_DIR CPPUTEST_LIBRARIES)

# CMake generated Testfile for 
# Source directory: /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0
# Build directory: /home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/build
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test "gecode-test" "-iter" "2" "-test" "Branch::Int::Dense::3" "-test" "Int::Linear::Int::Int::Eq::Bnd::12::4" "-test" "Int::Distinct::Random" "-test" "Int::Arithmetic::Mult::XYZ::Bnd::C" "-test" "Int::Arithmetic::Mult::XYZ::Dom::A" "-test" "Search::BAB::Sol::BalGr::Binary::Binary::Binary::1::1")
set_tests_properties(test PROPERTIES  _BACKTRACE_TRIPLES "/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/CMakeLists.txt;471;add_test;/home/thejana/Documents/assignments/year_04/is4101/maxsat_solvers/gecode/gecode-release-6.2.0/CMakeLists.txt;0;")

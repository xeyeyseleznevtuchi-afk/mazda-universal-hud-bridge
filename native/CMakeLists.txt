cmake_minimum_required(VERSION 3.10)
project(mazda_hud_native LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_library(mazda_hud_core STATIC
    src/hud_bridge.cpp
)

target_include_directories(mazda_hud_core
    PUBLIC include
)

add_executable(mazda_hud_tests
    tests/test_bridge.cpp
)

target_link_libraries(mazda_hud_tests
    PRIVATE mazda_hud_core
)

enable_testing()
add_test(NAME native_guidance COMMAND mazda_hud_tests)

add_executable(mazda_vbs_tests tests/test_vbs.cpp)
target_link_libraries(mazda_vbs_tests PRIVATE mazda_hud_core)
add_test(NAME vbs_staging COMMAND mazda_vbs_tests)

add_executable(mazda_vbs_sender_tests tests/test_vbs_sender.cpp)
target_link_libraries(mazda_vbs_sender_tests PRIVATE mazda_hud_core)
add_test(NAME vbs_sender_guard COMMAND mazda_vbs_sender_tests)

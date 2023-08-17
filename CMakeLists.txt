cmake_minimum_required(VERSION 3.5.0)
project(ControlSystem VERSION 0.1.0 LANGUAGES C CXX)

# include(CTest)
#enable_testing()
add_library(
    ControlSys
    control-system.hh
    control-system.cpp
)
add_executable(ControlSystem main.cpp   control-system.cpp)

target_link_libraries(ControlSystem PRIVATE ControlSys)
#set(CPACK_PROJECT_NAME ${PROJECT_NAME})
#set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
#include(CPack)
add_custom_target(run
    COMMAND ${PROJECT_NAME}
    DEPENDS ${PROJECT_NAME}
    WORKING_DIRECTORY ${CMAKE_PROJECT_DIR}
)
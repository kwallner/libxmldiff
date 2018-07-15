add_library(xmldiff STATIC errors.cpp lx2_diff.cpp lx2_ops.cpp lx2_parse.cpp lx2_util.cpp)
target_link_libraries(xmldiff xml2)
set_target_properties(xmldiff
        PROPERTIES
            INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_CURRENT_SOURCE_DIR}"
        )
set_target_properties(xmldiff PROPERTIES FOLDER 3rdParty/libxmldiff)
ADD_EXECUTABLE(xmldiffer xmldiff.cpp)
target_link_libraries(xmldiffer xmldiff)

set_target_properties(xmldiffer PROPERTIES FOLDER 3rdParty/libxmldiff)

add_library(xmldiff errors.cpp lx2_diff.cpp lx2_ops.cpp lx2_parse.cpp lx2_util.cpp)
target_link_libraries(xmldiff PUBLIC xml2) 
target_link_libraries(xmldiff PUBLIC iconv) # FIXME: This should not be needed ... but it is!
target_include_directories(xmldiff
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
        $<INSTALL_INTERFACE:include>
    )

ADD_EXECUTABLE(xmldiffer xmldiff.cpp)
target_link_libraries(xmldiffer xmldiff)



# Install
install(FILES 
	${CMAKE_CURRENT_SOURCE_DIR}/errors.h
	${CMAKE_CURRENT_SOURCE_DIR}/libxmldiff.h
	${CMAKE_CURRENT_SOURCE_DIR}/lx2_diff.h
	${CMAKE_CURRENT_SOURCE_DIR}/lx2_ops.h
	${CMAKE_CURRENT_SOURCE_DIR}/lx2_parse.h
	${CMAKE_CURRENT_SOURCE_DIR}/lx2_str.h
	${CMAKE_CURRENT_SOURCE_DIR}/lx2_util.h
	${CMAKE_CURRENT_SOURCE_DIR}/xmldiff.h
	DESTINATION include
	)

install(TARGETS xmldiff
    EXPORT Targets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
    )
    

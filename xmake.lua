add_requires("opencv", {system = true}) -- 系统OpenCV，实验用的OpenCV为4.5.5-r1
-- 打开的编译选项(Portage USE)：为了读取视频，必须加上ffmpeg (with -DFFMPEG_SUPPORT)

target("background_substraction")
    set_kind("binary")
    add_files("src/background_substraction/*.cpp")
    add_packages("opencv")
    add_includedirs("src/include")

target("meanshift")
    set_kind("binary")
    add_files("src/meanshift/*.cpp")
    add_packages("opencv")
    add_includedirs("src/include")

target("camshift")
    set_kind("binary")
    add_files("src/camshift/*.cpp")
    add_packages("opencv")
    add_includedirs("src/include")

target("optical_flow")
    set_kind("binary")
    add_files("src/optical_flow/*.cpp")
    add_packages("opencv")
    add_includedirs("src/include")
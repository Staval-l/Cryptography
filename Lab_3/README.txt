Чтобы установить boost, нужно выполнить mingw-19.0.exe (лежит в этой же директории).

Затем нужно зайти в созданную директорию и выполнить 2 батника: open_distro_window.bat и set_distro_paths.bat

После этого в вашем CLion открываете настройки, затем выбираете пункт Toolchains и добавляете новый (жмете плюсик). Затем в настройках CMake выбираете добавленный MinGW. Подробнее в этом видео: https://youtu.be/lOt3Nei4vLk

После этого настраиваете CMakeLists.txt
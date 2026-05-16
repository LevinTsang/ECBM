@echo off
setlocal enabledelayedexpansion

:: 获取日期并转换为 YYYY-MM-DD 格式
set "date_str=%date:~0,4%-%date:~5,2%-%date:~8,2%"

:: 获取时间并转换为 HH:MM 格式（处理小时小于10时的空格问题）
set "time_str=%time:~0,5%"
set "time_str=!time_str: =0!"

:: 输出最终格式的时间
echo %date_str% %time_str%

endlocal
@echo off
svn update
svn add * --force
echo 开始向资源库提交更新...
echo 请输入更新的描述信息:
set /p comment=
svn commit -m %comment%
echo 更新已完成.
pause
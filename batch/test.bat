
@REM variable, it can be either double quate or without it
set class_cat=ClassB
set seq_name=BasketballDrive
set class_id=0
set flag=false

@REM https://stackoverflow.com/questions/25384358/batch-if-elseif-else
@REM IF /i %flag%==true goto block1
@REM IF /i %flag%==false goto block2

if %flag%==true (goto block1) else (goto block2)

:block1
echo Class category: %class_cat%, Sequence name: %seq_name%, class ID selected: %class_id%
goto end

:block2
echo %class_cat%_%seq_name%_%class_id%
goto end

:end




# not working by bash run.sh

#time bash test.sh & time bash test.sh & time bash test.sh &

# time bash test.sh &\
# time bash test.sh &\
# time bash test.sh &

# print_val()

arr=(0 32 56 "all" )

for el in ${arr[@]}
do
    if [ ${el} == "all" ]
    then
        echo ${arr[@]::${#arr[@]}-1}
    else
        echo ${el[@]}
    fi
done

flag=true
if ${flag} == true
then
    echo "flag is true"
else
    echo "flag is not true"
fi

## declare an array variable
declare -a category_arr=("ClassB" "ClassC" "ClassD")
declare -a seq_arr=("seq_1" "seq_2" "seq_3")

## nested loop
for category in ${category_arr[@]}
do
    for seq_name in ${seq_arr[@]}
    do
        echo ${category}
        echo ${seq_name}
    done
done

declare -a val_arr=(1 2 3 4 5 6 7)
declare -a val_arr2=($(seq 200 10 1000)) #https://stackoverflow.com/questions/39267836/create-an-array-with-a-sequence-of-numbers-in-bash
for value in ${val_arr[@]}
do
    echo "value is ${value}"
done

# declare -a conf_thres=($(seq 0.1 0.05 0.9))
# declare -a iou_thres=($(seq 0.1 0.05 0.9))
# #declare -a img_size=($(seq 200 20 900))
# declare -a img_size=(640)

declare -a conf_thres=($(seq 1 1 5))
declare -a iou_thres=($(seq 1 1 5))
declare -a img_size=($(seq 0.1 0.05 0.9))

counter=0
for conf in ${conf_thres[@]}
do
    for iou in ${iou_thres[@]}
    do
        for img_s in ${img_size[@]}
        do
            echo "iter = ${counter}, ${conf}, ${iou}, ${img_s}"
            counter=$(($counter + 1))
        done
    done
done

x=2
y=3
echo "(${x},${y})"

uuid=$(uuidgen)
echo one_iter_${uuid}.txt
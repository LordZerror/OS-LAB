read -p "Enter the number till the factorial should continue : " n
prod=1
num=1
i=0
while [ $i -lt $n ]
do 
prod=$((prod*num))
num=$((num+1))
i=$((i+1))
done
echo "$prod is the factorial of $n numbers."

read -p "Enter the number till the summation should continue : " n
sum=0
num=1
i=0
while [ $i -lt $n ]
do 
sum=$((sum+num))
num=$((num+1))
i=$((i+1))
done
echo "$sum is the sum of $n numbers from 1 to $n."

read -p "Enter the age of the voter : " n
if [ $n -ge 18 ]
then
echo "The person is eligible to vote and has a chance to be a good citizen."
else
echo "The person is not eligible to vote and be a good citizen."
fi

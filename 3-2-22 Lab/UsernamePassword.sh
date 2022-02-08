function data()
{
read -p "Enter the username of your : " username
read -p "Enter the password of the website : " password
}
data
if [[ $username == "kaushal16" && $password == "passKsp" ]]
then 
echo "Successful Login"
else
echo "Invalid credentials"
fi

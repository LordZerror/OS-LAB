function data()
{
read -p "Enter your username : " username
read -p "Enter your password : " password
}
data
if [[ $username == "kaushal16" && $password == "passKsp" ]]
then 
echo "Successful Login"
else
echo "Invalid credentials"
fi

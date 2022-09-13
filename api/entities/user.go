package entities

type User struct {
	ID			string		`json:"id"`
	First		string		`json:"firstname"`
	Last		string		`json:"lastname"`
	Email		string		`json:"emai"`
	Password	string		`json:"password"`
	Prefix		string		`json:"prefix"`
	LastLogin	string		`json:"lastlogin"`
}
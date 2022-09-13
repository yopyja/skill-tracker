package controllers

import (
	"encoding/json"
	"net/http"
	"rest-api/database"
	"rest-api/entities"
)

func CreateUser(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	var user entities.User
	json.NewDecoder(r.Body).Decode(&user)
	database.Instance.Create(&user)
	json.NewEncoder(w).Encode(user)
}



func checkIfUserExist(userID string) bool {
	var user entities.User
	database.Instance.First(&user, userID)
	if user.ID == "" {
		return false
	}
	return true
}
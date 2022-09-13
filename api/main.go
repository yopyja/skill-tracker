package main

import (
	"fmt"
	"log"
	"net/http"
	"rest-api/database"
	"rest-api/controllers"

	"github.com/gorilla/mux"
	"github.com/spf13/viper"
)

type Config struct {
	Port             string `mapstructure:"port"`
	ConnectionString string `mapstructure:"connection_string"`
}


func main() {
	// Load Configurations from config.json using Viper
	LoadAppConfig()
	// Initialize Database
	database.Connect(AppConfig.ConnectionString)
	database.Migrate()
	
	// Initialize the router
	router := mux.NewRouter().StrictSlash(true)
	// Register Routes
	RegisterProductRoutes(router)
	// Start the server
	log.Println(fmt.Sprintf("Starting Server on port %s", AppConfig.Port))
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%v", AppConfig.Port), router))
}


var AppConfig *Config
func LoadAppConfig(){
	log.Println("Loading Server Configurations...")
	viper.AddConfigPath(".")
	viper.SetConfigName("config")
	viper.SetConfigType("json")
	err := viper.ReadInConfig()
	if err != nil {
		log.Fatal(err)
	}
	err = viper.Unmarshal(&AppConfig)
	if err != nil {
		log.Fatal(err)
	}
}


func RegisterProductRoutes(router *mux.Router) {
	//router.HandleFunc("/api/user", controllers.GetProducts).Methods("GET")
	//router.HandleFunc("/api/user/{id}", controllers.GetProductById).Methods("GET")
	router.HandleFunc("/api/user", controllers.CreateUser).Methods("POST")
	//router.HandleFunc("/api/user/{id}", controllers.UpdateProduct).Methods("PUT")
	//router.HandleFunc("/api/user/{id}", controllers.DeleteProduct).Methods("DELETE")
}
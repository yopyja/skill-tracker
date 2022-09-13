# GoLang Rest API

```
go get -u github.com/gorilla/mux
```


- Gorilla/mux will be what we be using to route the incoming HTTP request to the correct method that handles the specific operation. For instance when a client send a POST request to /api/products endpoints, routing helps the application understand where the request should be routed to, and in this case it gets routed to a method that is responsibe for Creating Product.


```
go get -u gorm.io/gorm
go get -u gorm.io/driver/postgres
```


 - Gorm is an ORM that helps access the defined database. It provides easy to understand helper functions that can query or execute commands over a specific database. No more writing boring old SQL Queries to work with the data! In this article we will be just using the basic functionalities of GORM to achieve CRUD operations. We’ll talk about GORM in detail in a seperate article.


```
go get -u github.com/spf13/viper
```


 - Viper is a configurations manager that helps us to load file and environment defined values into the application’s runtime. There will be seperate article about Viper too!



https://codevoweb.com/setup-golang-gorm-restful-api-project-with-postgres/

https://github.com/cosmtrek/air




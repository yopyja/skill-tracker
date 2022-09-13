package models

import (
	"time"

	"github.com/google/uuid"
)

type User struct {
	ID 			  uuid.UUID `gorm:"type:uuid;default:uuid_generate_v4();primary_key"`
	// ID     uint   `gorm:"primary_key"`
	First     	  string    `gorm:"type:varchar(255);not null"`
	Last      	  string    `gorm:"type:varchar(255);not null"`
	Email  		  string    `gorm:"uniqueIndex;not null"`
	Password      string    `gorm:"type:varchar(255);not null"`
	Role     	  string    `gorm:"type:varchar(255);not null"`
    Photo     	  string    `gorm:"not null"`
    Verified  	  bool      `gorm:"not null"`
	CreatedAt 	  time.Time
	UpdatedAt 	  time.Time
	LastLogin 	  time.Time
}
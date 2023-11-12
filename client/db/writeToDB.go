package db

import (
	"database/sql"
	"log"
	_ "github.com/lib/pq"
)

func WriteDataToDB(video_name,result string) {
	db, err := sql.Open("postgres", connectionStr)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	
	
	s :="insert into results (video_name,result,date) values ('"+video_name+"','"+result+"',LOCALTIMESTAMP);"


	res,err :=db.Exec(s)
	if err != nil {
		panic(err)
	}
	log.Println(res.RowsAffected())
    //defer rows.Close(s)
}
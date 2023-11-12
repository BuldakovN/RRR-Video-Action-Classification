package db

import (
	"database/sql"
	"hack/Client/entity"
	"log"
	_ "github.com/lib/pq"
)

func GetFromDB() []entity.Results{
	db, err := sql.Open("postgres", connectionStr)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	rows, err := db.Query("select id,video_name,result,date from results order by date desc;")
    if err != nil {
        panic(err)
    }
    defer rows.Close()

	results := []entity.Results{}

	for rows.Next(){
        p := entity.Results{}
        err := rows.Scan(&p.Id, &p.Video_name, &p.Result, &p.Date)
        if err != nil{
            log.Println(err)
            continue
        }
        results = append(results, p)
    }
	log.Println(results[0].Result+results[0].Date)
	return results
}
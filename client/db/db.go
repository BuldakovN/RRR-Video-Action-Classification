package db

import (
	"database/sql"
	"log"

	_ "github.com/lib/pq"
)



var(
	connectionStr = "host="+Co().Host+"  user="+Co().User+" password="+Co().Password+" dbname="+Co().DBname+" port="+Co().Port+" sslmode="+Co().Sslmode
	//connectionStr = "host=  user=root password=root dbname=test_db port=5432 sslmode=disable"
)

/*func fillTableClasses(db *sql.DB){
	res, err := db.Exec("insert into classes (id,name) values (0,'cartwheel'),(1,'catch'),(2,'clap'),(3,'climb'),(4,'dive'),(5,'draw_sword'),(6,'dribble'),(7,'fencing'),(8,'flic_flac'),(9,'golf'),(10,'handstand'),(11,'hit'),(12,'jump'),(13,'pick'),(14,'pour'),(15,'pullup'),(16,'push'),(17,'pushup'),(18,'shoot_ball'),(19,'sit'),(20,'situp'),(21,'swing_baseball'),(22,'sword_exercise'),(23,'throw');")
	if err != nil {
		panic(err)
	}
	log.Println(res.RowsAffected())
}*/

func InitDataBase(){
	
	db, err := sql.Open("postgres", connectionStr)
   	if err != nil {
    	log.Fatal(err)
   	}
	defer db.Close()
	

	/*res, err:=db.Exec("CREATE TABLE IF NOT EXISTS classes (id int PRIMARY KEY, name varchar(30));")
	if err != nil {
        panic(err)
    }
	log.Println(res.RowsAffected())

	var tableClassesSize int
	db.QueryRow("select count(*) from classes;").Scan(&tableClassesSize)
	if(tableClassesSize == 0){
		fillTableClasses(db)
	}*/

	res, err:=db.Exec("CREATE TABLE IF NOT EXISTS results (id SERIAL PRIMARY KEY,video_name text, result text,date timestamp); ")
	if err != nil {
        panic(err)
    }
	log.Println(res.RowsAffected())
	
}

func SetDataBaseTestData(){
	db, err := sql.Open("postgres", connectionStr)
   	if err != nil {
    	log.Fatal(err)
   	}
	defer db.Close()
	var idEmployee int
	db.QueryRow("insert into employees (name, email) values ('testName', 'testEmail') returning id").Scan(&idEmployee)
	var idWork int
	db.QueryRow("insert into works (type, description) values ('testType', 'testEmail@mail.com') returning id").Scan(&idWork)
	db.QueryRow("insert into works_employees (employee_id, work_id) values ($1, $2) returning id",idEmployee,idWork).Scan(&idEmployee)
}
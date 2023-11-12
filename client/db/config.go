package db

type ConfigDB struct{
	Host string
	Port string
	DBname string
	User string
	Password string
	Sslmode string

}

func Co() ConfigDB{
	c := ConfigDB{
		Host: "db",
		//Host: "localhost",
		Port: "5432",
		DBname: "test_db",
		User: "root",
		Password: "root",
		Sslmode: "disable",
	}
	return c
}
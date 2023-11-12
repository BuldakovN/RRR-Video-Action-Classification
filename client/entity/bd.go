package entity


//структуры для работы с бд
type Classes struct{
	Id int `json:"id"`
    Name string `json:"name"`
}

type Results struct{
	Id int `json:"id"`
	Video_name string `json:"video_name"`
	Result string `json:"result"`
	Date string `json:"date"`
}
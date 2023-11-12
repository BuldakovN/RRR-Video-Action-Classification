package main

import (
	"bytes"
	"encoding/json"
	"hack/Client/db"
	"hack/Client/entity"
	"log"
	"net/http"
	//"strconv"

	"github.com/gin-gonic/gin"
)

var router *gin.Engine

//var host = "localhost"
var host = "model"

func main() {

	db.InitDataBase()

	router = gin.Default()
	//подгрузка статических файлов
	router.LoadHTMLGlob("templates/*.html")
	//router.LoadHTMLGlob("templates/indexVideo.html")
	router.Static("/js", "./js")
	router.Static("/css", "./css")
	router.StaticFile("/favicon.ico", "./resources/favicon.ico")
	router.StaticFile("/load.gif", "./css/images/load.gif")

	router.GET("/", func(c *gin.Context) {

		// Call the HTML method of the Context to render a template
		c.HTML(
			// Set the HTTP status to 200 (OK)
			http.StatusOK,
			// Use the index.html template
			"index.html",
			// Pass the data that the page uses (in this case, 'title')
			gin.H{
				"title": "Home Page",
			},
		)
	})
	router.GET("/stream",func(c*gin.Context){
		c.HTML(
			// Set the HTTP status to 200 (OK)
			http.StatusOK,
			// Use the index.html template
			"index2.html",
			// Pass the data that the page uses (in this case, 'title')
			gin.H{
				"title": "Home Page",
			},
		)
	})

	router.GET("/data",func(c *gin.Context) {
		results := db.GetFromDB()
		var finalResult string
		//finalResult = "["
		for _, result := range results {
			
			//finalResult += "{\"id\":"+strconv.Itoa(result.Id)+",\"name\":\""+result.Video_name+"\",\"result\":\""+result.Result+"\",\"date\":\""+result.Date+"\"}"
			finalResult += "Название видео:"+result.Video_name+"$"+result.Result+"|"
			
			//if (i+1<len(results)){
				//finalResult +=","
			//}
		}
		//finalResult +="]"

		//m:= make(map[string]string)

		//m["data"]=finalResult
		
		c.String(200,finalResult)

	})

	router.POST("/sendVideo", func(c *gin.Context) {
		//запись в структуру go для промежуточной обработки данных
		var data entity.FormBase64
		c.ShouldBindJSON(&data)
		bytesRepresentation, err := json.Marshal(data)
		if err != nil {
			log.Fatalln(err)
		}
		
		//пост запрос на сервер с нейронкой
		log.Println("Запрос на py сервер")
		log.Println(host)
		resp, err := http.Post("http://"+host+":5000/upload", "application/json", bytes.NewBuffer(bytesRepresentation)) 
    	if err != nil { 
        	log.Println(err) 
    	}
		log.Println("Ответ с py сервера")
		//defer resp.Body.Close()
		var res map[string]interface{}
		
		//json
    	json.NewDecoder(resp.Body).Decode(&res)
		log.Println(res["class"])
		log.Println(res["videoName"])

		db.WriteDataToDB(res["videoName"].(string),res["class"].(string))
		log.Println("Ответ на js")
		//entity.Base64ToFile(res["b64"].(string))
		c.JSON(200,res)
    	//log.Println(res["b64"])
		resp.Body.Close()
	})


	router.Run(":8080")
}